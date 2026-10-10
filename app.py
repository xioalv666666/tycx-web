# -*- coding: utf-8 -*-
"""
统壹出行 · 网页版
直接复用桌面版引擎(统壹出行最后代码.py), 注册参数/指纹/流程 100% 一致。
网页功能: 邀请码----数量 批量提交 + 任务选择(仅注册/注册签到) + 代理API + 实时进度(成功/失败/剩余/总计)。
本地运行: python app.py → 浏览器打开 http://127.0.0.1:5000
云端部署: 整个文件夹上传 Hugging Face Spaces(Docker) 或 Render, 无需电脑开机。
"""
import os
import sys
import re
import json
import time
import types
import shutil
import base64
import threading
import queue
import importlib.util
import urllib.request
import urllib.error
from collections import deque

BASE = os.path.dirname(os.path.abspath(__file__))
ENGINE_FILE = os.path.join(BASE, "统壹出行最后代码.py")
CACHE_FILE = os.path.join(BASE, "_phone_cache.pkl")

# 首次运行自动从上级目录复制引擎文件(本地使用; 云端部署时整个文件夹直接上传, 无需此步)
def _ensure_engine_files():
    parent = os.path.dirname(BASE)
    if not os.path.exists(ENGINE_FILE):
        src = os.path.join(parent, "统壹出行最后代码.py")
        if os.path.exists(src):
            shutil.copy2(src, ENGINE_FILE)
    if not os.path.exists(CACHE_FILE):
        src = os.path.join(parent, "_phone_cache.pkl")
        if os.path.exists(src):
            shutil.copy2(src, CACHE_FILE)
_ensure_engine_files()

# ============ PyQt5 桩模块: 无界面环境让引擎完成导入(只用到 QThread/pyqtSignal) ============
class _SignalDesc:
    """pyqtSignal 桩: 类属性描述符, 实例访问时返回可 emit 的发射器"""
    def __init__(self, *a, **k):
        self._name = None
    def __set_name__(self, owner, name):
        self._name = name
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        d = obj.__dict__.setdefault("_sig_emitters", {})
        if self._name not in d:
            d[self._name] = _Emitter(self._name, obj)
        return d[self._name]

class _Emitter:
    def __init__(self, name, obj):
        self._name, self._obj = name, obj
    def emit(self, *args):
        cb = getattr(_pyqt_dispatch, "hook", None)
        if cb:
            try:
                cb(self._obj, self._name, args)
            except Exception:
                pass
    def connect(self, *a, **k):
        pass

class _QThreadStub:
    def __init__(self, parent=None):
        pass
    def start(self, *a, **k): pass
    def wait(self, *a, **k): pass
    def terminate(self, *a, **k): pass
    def isRunning(self, *a, **k): return False
    def currentThread(self, *a, **k): return None
    def msleep(self, *a, **k): pass
    def exec_(self, *a, **k): return 0

def _pyqt_dispatch(obj, name, args):
    pass  # app 层通过 _pyqt_dispatch.hook 覆盖

class _StubModule(types.ModuleType):
    def __getattr__(self, k):
        if k.startswith("__"):
            raise AttributeError(k)
        cls = type(k, (), {"__init__": lambda self, *a, **kw: None})
        setattr(self, k, cls)
        return cls

_pyqt5 = _StubModule("PyQt5")
_qtcore = _StubModule("PyQt5.QtCore")
_qtwidgets = _StubModule("PyQt5.QtWidgets")
_qtgui = _StubModule("PyQt5.QtGui")
_qtcore.QThread = _QThreadStub
_qtcore.pyqtSignal = _SignalDesc
_qtcore.Qt = types.SimpleNamespace(AA_EnableHighDpiScaling=0, AA_UseHighDpiPixmaps=1,
                                   AlignCenter=0, ISODate=1)
sys.modules["PyQt5"] = _pyqt5
sys.modules["PyQt5.QtCore"] = _qtcore
sys.modules["PyQt5.QtWidgets"] = _qtwidgets
sys.modules["PyQt5.QtGui"] = _qtgui

# ============ 导入引擎(参数与桌面版完全一致) ============
_spec = importlib.util.spec_from_file_location("tycx_engine", ENGINE_FILE)
engine = importlib.util.module_from_spec(_spec)
sys.modules["tycx_engine"] = engine
_spec.loader.exec_module(engine)

# ============ 数据目录 → 桌面「统一出行数据」(引擎注册/登录逻辑零改动, 仅改保存位置) ============
DATA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(BASE))), "统一出行数据")
os.makedirs(DATA_ROOT, exist_ok=True)
engine.BASE_FOLDER = DATA_ROOT
engine.REG_SUCCESS_FOLDER = os.path.join(DATA_ROOT, "统一出行注册成功")
engine.REG_FAIL_FOLDER = os.path.join(DATA_ROOT, "统一出行注册失败")
engine.REG_SIGN_FOLDER = os.path.join(DATA_ROOT, "统一出行注册成功签到专用")
engine.SIGN_LOG_FOLDER = os.path.join(DATA_ROOT, "统一出行签到日志")
engine.CONFIG_FILE = os.path.join(DATA_ROOT, "config.json")
engine.CRASH_LOG = os.path.join(DATA_ROOT, "崩溃日志.txt")
engine._IDCARD_CACHE_FILE = os.path.join(DATA_ROOT, "_idcard_cache.pkl")
for _f in (engine.REG_SUCCESS_FOLDER, engine.REG_FAIL_FOLDER, engine.REG_SIGN_FOLDER, engine.SIGN_LOG_FOLDER):
    os.makedirs(_f, exist_ok=True)

from flask import Flask, request, jsonify, Response, render_template_string, make_response, redirect, url_for

app = Flask(__name__)

# ============ 访问密码(部署到公网必须设置, 防止陌生人使用) ============
ACCESS_PASS = "179300"   # 打开网页需输入此密码, 可自行修改
DEFAULT_API = "http://api.dmdaili.com/dmgetip.asp?apikey=adb9670e&pwd=04b3de1e2744a06660f84db3b92116ea&getnum=1&httptype=1&geshi=1&fenge=1&fengefu=&operate=all"   # 默认代理API, 网页自动填入可改

# ============ 任务状态(多任务池: 每个提交=一个独立任务, 可并行, 点选查看) ============
STATE_LOCK = threading.Lock()
TASKS = {}        # tid -> task dict
WT2TID = {}       # id(WorkThread) -> tid (信号路由)
TID_SEQ = [0]
SUBS = set()
SUBS_LOCK = threading.Lock()
MAX_KEEP = 30     # 列表最多保留任务数(超出清理最旧的已完成任务)

def publish(evt):
    with SUBS_LOCK:
        dead = []
        for q in SUBS:
            try:
                q.put_nowait(evt)
            except Exception:
                dead.append(q)
        for q in dead:
            SUBS.discard(q)

def add_log(task, msg):
    ts = time.strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    task["logs"].append(line)
    publish({"t": "log", "tid": task["tid"], "m": line})

def _gc_tasks():
    # 超上限时清理最旧的已完成任务
    if len(TASKS) <= MAX_KEEP:
        return
    dones = sorted([t["tid"] for t in TASKS.values() if not t["running"]])
    while len(TASKS) > MAX_KEEP and dones:
        old = dones.pop(0)
        t = TASKS.pop(old, None)
        if t:
            WT2TID.pop(id(t["wt"]), None)

# ============ 引擎信号 → 网页事件(按任务路由) ============
def _hook(obj, name, args):
    try:
        tid = WT2TID.get(id(obj))
        if tid is None:
            return
        with STATE_LOCK:
            task = TASKS.get(tid)
        if task is None:
            return
        if name == "log_signal":
            add_log(task, str(args[0]))
        elif name == "batch_progress_signal":
            _on_batch_snapshot(task, str(args[0]))
        elif name == "stats_signal":
            with STATE_LOCK:
                task["success"], task["fail"], task["total"] = int(args[0]), int(args[1]), int(args[2])
            publish({"t": "stats", "tid": tid})
        elif name == "progress_signal":
            with STATE_LOCK:
                task["completed"] = int(args[0])
            publish({"t": "stats", "tid": tid})
        elif name == "update_reg_signal":
            tel, ip, st = str(args[0]), str(args[1]), str(args[2])
            task["feed"].append(f"{tel}  {ip}  {st}")
            publish({"t": "row", "tid": tid, "m": f"{tel}  {ip}  {st}"})
        elif name == "pre_reg_signal":
            tel, pwd, nm, inv, ip, card = [str(a) for a in args]
            add_log(task, f"▶ 开始注册 {tel} 邀请码[{inv}] IP:{ip} 姓名:{nm}")
        elif name == "update_card_signal":
            tel, nm, card = [str(a) for a in args]
            add_log(task, f"♻ {tel} 更新资料 姓名:{nm} 身份证:{card}")
        elif name == "update_tel_signal":
            old, new, nm, card = [str(a) for a in args]
            add_log(task, f"♻ 号码已注册, 换新号 {old} → {new}")
        elif name == "task_break_signal":
            msg = str(args[0])
            with STATE_LOCK:
                task["break_msg"] = msg
            add_log(task, f"⛔ {msg}")
        elif name == "notify_signal":
            add_log(task, f"ℹ {args[0]}")
        elif name == "finish_signal":
            _finish_task(task)
    except Exception:
        pass

_pyqt_dispatch.hook = _hook

def _on_batch_snapshot(task, text):
    # 解析引擎快照: "批量进度 已完成 X / Y" + 每行 "    code: 成功a/n 失败b 剩余c"
    with STATE_LOCK:
        m = re.search(r"已完成\s*(\d+)\s*/\s*(\d+)", text)
        if m:
            task["done_target"] = int(m.group(2))
        rows = []
        for mm in re.finditer(r"(\S+):\s*成功(\d+)/(\d+)\s*失败(\d+)\s*剩余(\d+)", text):
            code, ok, n, fail, left = mm.group(1), int(mm.group(2)), int(mm.group(3)), int(mm.group(4)), int(mm.group(5))
            state = "已完成" if (ok + fail >= n) else "进行中"
            rows.append({"code": code, "n": n, "ok": ok, "fail": fail, "left": left, "state": state})
        if rows:
            task["rows"] = rows
        total_done = sum(r["ok"] for r in task["rows"])
        total_target = sum(r["n"] for r in task["rows"])
        snap = {"t": "batch", "tid": task["tid"], "rows": task["rows"],
                "total_done": total_done, "total_target": total_target,
                "success": task["success"], "fail": task["fail"]}
    publish(snap)

def _finish_task(task):
    with STATE_LOCK:
        if task["running"]:
            task["running"] = False
            task["end_at"] = time.strftime("%H:%M:%S")
            total_done = sum(r["ok"] for r in task["rows"])
            total_target = sum(r["n"] for r in task["rows"])
            add_log(task, f"======= 任务结束 ======= 邀请码总计完成 {total_done} / {total_target} 成功:{task['success']} 失败:{task['fail']}")
            publish({"t": "batch", "tid": task["tid"], "rows": task["rows"],
                     "total_done": total_done, "total_target": total_target,
                     "success": task["success"], "fail": task["fail"], "finished": True})
        publish({"t": "done", "tid": task["tid"]})

# ============ 批量文本解析: 邀请码----数量 ============
_BATCH_RE = re.compile(r"^\s*(\d{1,15})\s*(?:-{2,}|—|——|×|\*|\s)\s*(\d{1,6})\s*$")

def parse_batch(text):
    entries, bad = [], []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        m = _BATCH_RE.match(line)
        if not m:
            bad.append(line)
            continue
        code, n = m.group(1), int(m.group(2))
        if n <= 0:
            bad.append(line)
            continue
        entries.append((code, n))
    return entries, bad

# ============ 启动/停止任务(多任务并行) ============
RUN_LIMIT = 10   # 同时运行的任务上限(防止代理API被限流)

_DELAY_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*[-—~]\s*(\d+(?:\.\d+)?)\s*$")

def _safe_delay(v, default="0-0.2"):
    m = _DELAY_RE.match(str(v or ""))
    if not m:
        return default
    lo, hi = float(m.group(1)), float(m.group(2))
    if lo < 0 or hi < lo:
        return default
    return f"{lo}-{hi}"

def start_job(task_kind, entries, api, pwd, threads, delay=""):
    with STATE_LOCK:
        running_cnt = sum(1 for t in TASKS.values() if t["running"])
        if running_cnt >= RUN_LIMIT:
            return False, f"同时运行的任务已达上限({RUN_LIMIT}个), 请先停止部分任务"
        TID_SEQ[0] += 1
        tid = TID_SEQ[0]
        wt = engine.WorkThread()
        wt.task_type = engine.TASK_REGISTER_ONLY if task_kind == "register_only" else engine.TASK_REGISTER
        wt.config = {
            "batch_invites": entries,
            "invite": entries[0][0] if entries else "",
            "reg_pwd": pwd or "123456",
            "use_proxy": bool(api.strip()),
            "proxy_api": api.strip(),
            "thread_count": max(1, min(int(threads or 5), 99)),
            "thread_delay_range": _safe_delay(delay),
            "delay_range": _safe_delay(delay),
        }
        wt.account_list = []
        label = "仅注册" if task_kind == "register_only" else "注册签到"
        name = "+".join(f"{c}×{n}" for c, n in entries)
        if len(name) > 40:
            name = name[:37] + "..."
        task = {
            "tid": tid, "name": name, "task_label": label, "running": True,
            "total": sum(n for _, n in entries), "success": 0, "fail": 0, "completed": 0,
            "rows": [{"code": c, "n": n, "ok": 0, "fail": 0, "left": n, "state": "进行中"} for c, n in entries],
            "done_target": 0, "start_at": time.strftime("%H:%M:%S"), "end_at": "", "break_msg": "",
            "logs": deque(maxlen=800), "feed": deque(maxlen=60), "wt": wt,
        }
        TASKS[tid] = task
        WT2TID[id(wt)] = tid
        _gc_tasks()
        add_log(task, "🟢 网页批量任务已开启(复用桌面版引擎, 参数100%一致)")
        for c, n in entries:
            t = engine.detect_invite_type(c)
            add_log(task, f"📋 邀请码[{c}] 类型={'手机号' if t == 'phone' else 'ID'} 注册{n}个")
        add_log(task, f"任务: {label} | 合计: {task['total']}个 | 线程: {wt.config['thread_count']} | 代理API: {'已填' if api.strip() else '未填'}")

    def _run():
        try:
            wt.run()
        finally:
            _finish_task(task)

    threading.Thread(target=_run, daemon=True).start()
    return True, tid

def stop_task(tid):
    with STATE_LOCK:
        task = TASKS.get(tid)
        if task is None:
            return False, "任务不存在"
        if not task["running"]:
            return False, "该任务已结束"
        wt = task["wt"]
    wt.is_running = False
    try:
        if wt.stop_event is not None:
            wt.stop_event.set()
    except Exception:
        pass
    add_log(task, "⏹ 收到停止指令, 正在停止(已启动的账号会完成当前步骤)...")
    return True, "停止指令已发出"

# ============ 图片识别邀请码: 二维码 scene=pid_纯数字 + OCR 推荐人尾号 (仅识别, 不参与注册) ============
_SCAN_LOCK = threading.Lock()
_OCR_MODEL = {"m": None, "tried": False}

def _get_ocr():
    """懒加载 OCR(首次用图才加载, 失败不影响二维码识别)"""
    if _OCR_MODEL["tried"]:
        return _OCR_MODEL["m"]
    _OCR_MODEL["tried"] = True
    try:
        from rapidocr_onnxruntime import RapidOCR
        _OCR_MODEL["m"] = RapidOCR()
    except Exception:
        _OCR_MODEL["m"] = None
    return _OCR_MODEL["m"]

_PID_RE = re.compile(r"scene\s*=\s*pid[_=:]?\s*(\d{3,20})", re.I)
_PURE_DIGITS_RE = re.compile(r"^\d{3,20}$")
_TAIL_RES = (
    re.compile(r"1[3-9]\d\*{2,6}(\d{3,4})"),   # 151****1919
    re.compile(r"(\d{3,4})\s*(?:推荐|邀請|邀请)"),  # 1919 推荐您加入
    re.compile(r"\*{2,}\s*(\d{4})"),
)

def _decode_qr(img):
    """多策略二维码解码: zxing 优先(最稳), 失败再用 opencv 多轮预处理"""
    texts = []
    try:
        import zxingcpp
        for res in zxingcpp.read_barcodes(img):
            t = str(res.text).strip()
            if t:
                texts.append(t)
    except Exception:
        pass
    if texts:
        return texts
    try:
        import cv2
        det = cv2.QRCodeDetector()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if img.ndim == 3 else img
        variants = [img, gray]
        for scale in (2, 3):
            h, w = gray.shape[:2]
            if max(h, w) * scale <= 4000:
                variants.append(cv2.resize(gray, (w * scale, h * scale), interpolation=cv2.INTER_CUBIC))
        try:
            _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            variants.append(bw)
            variants.append(cv2.bitwise_not(bw))
        except Exception:
            pass
        for v in variants:
            try:
                data, _, _ = det.detectAndDecode(v)
                if data and data.strip():
                    texts.append(data.strip())
                    break
            except Exception:
                continue
    except Exception:
        pass
    return texts

def _extract_invite(texts):
    """只认 scene=pid_纯数字 或 整串纯数字, 避免误填"""
    for t in texts:
        m = _PID_RE.search(t or "")
        if m:
            return m.group(1), t
    for t in texts:
        t2 = (t or "").strip()
        if _PURE_DIGITS_RE.match(t2):
            return t2, t
    return "", (texts[0] if texts else "")

def _ocr_tail(img):
    """识别推荐人手机尾号(尽力而为, 失败不影响邀请码)"""
    model = _get_ocr()
    if model is None:
        return ""
    try:
        with _SCAN_LOCK:
            result, _ = model(img)
        lines = []
        for item in (result or []):
            try:
                lines.append(str(item[1]))
            except Exception:
                pass
        text = " ".join(lines)
        for rx in _TAIL_RES:
            m = rx.search(text)
            if m:
                return m.group(1)
    except Exception:
        pass
    return ""

@app.route("/scan", methods=["POST"])
def scan():
    if not _authed():
        return jsonify({"ok": False, "msg": "未授权"}), 401
    f = request.files.get("file")
    if not f:
        return jsonify({"ok": False, "msg": "没有收到图片"})
    data = f.read()
    if not data:
        return jsonify({"ok": False, "msg": "图片为空"})
    try:
        import cv2
        import numpy as np
    except Exception:
        return jsonify({"ok": False, "msg": "服务器缺图片库: pip install opencv-python-headless numpy zxing-cpp rapidocr-onnxruntime"})
    try:
        img = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
    except Exception:
        img = None
    if img is None:
        return jsonify({"ok": False, "msg": "图片格式无法解析"})
    texts = _decode_qr(img)
    code, raw = _extract_invite(texts)
    if code:
        return jsonify({"ok": True, "code": code, "tail": _ocr_tail(img), "raw": str(raw)[:120]})
    if texts:
        return jsonify({"ok": False, "msg": "发现二维码但不是邀请码(需 scene=pid_纯数字)", "raw": str(texts[0])[:120]})
    return jsonify({"ok": False, "msg": "未发现二维码, 请用清晰完整的海报截图"})

# ============ 路由 ============
PAGE = """<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>统壹出行 · 网页版</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,"PingFang SC","Microsoft YaHei",sans-serif;
background:#0b1020;color:#e2e8f0;min-height:100vh;padding:14px}
.wrap{max-width:860px;margin:0 auto}
h1{font-size:20px;margin:6px 0 14px;color:#7dd3fc}
.card{background:#131a30;border:1px solid #1e2a4a;border-radius:12px;padding:14px;margin-bottom:12px}
label{display:block;font-size:13px;color:#94a3b8;margin:8px 0 4px}
textarea,input,select{width:100%;background:#0d1428;border:1px solid #25335c;color:#e2e8f0;
border-radius:8px;padding:9px 11px;font-size:14px;outline:none}
textarea{min-height:110px;resize:vertical;font-family:monospace}
input:focus,textarea:focus,select:focus{border-color:#38bdf8}
.row{display:flex;gap:10px;flex-wrap:wrap}
.row>div{flex:1;min-width:140px}
.btns{display:flex;gap:10px;margin-top:12px}
button{flex:1;padding:11px;border:0;border-radius:9px;font-size:15px;font-weight:600;cursor:pointer}
#btnGo{background:#059669;color:#fff}
#btnStop{background:#b91c1c;color:#fff;flex:0 0 34%}
button:disabled{opacity:.45;cursor:not-allowed}
.total{font-size:16px;font-weight:700;color:#7dd3fc;margin-bottom:10px}
.total b{color:#34d399}
.total .f{color:#f87171}
.invline{display:flex;justify-content:space-between;align-items:center;background:#0d1428;
border:1px solid #223055;border-radius:8px;padding:8px 10px;margin:6px 0;font-size:13px;flex-wrap:wrap;gap:4px}
.invline .code{color:#fbbf24;font-weight:700;font-size:14px}
.invline .st{padding:2px 8px;border-radius:6px;font-size:12px}
.st.run{background:#1e3a8a;color:#93c5fd}
.st.fin{background:#064e3b;color:#6ee7b7}
.tag{font-size:12px;color:#64748b}
#feed{background:#0d1428;border-radius:8px;padding:8px;max-height:150px;overflow-y:auto;font-size:12px;color:#94a3b8}
#logs{background:#0d1428;border-radius:8px;padding:8px;max-height:260px;overflow-y:auto;
font-family:Consolas,monospace;font-size:12px;white-space:pre-wrap;color:#a5b4fc}
h2{font-size:15px;color:#c4b5fd;margin-bottom:8px}
.ok{color:#34d399}.bad{color:#f87171}.warn{color:#fbbf24}
.tcard{background:#0d1428;border:1px solid #223055;border-radius:9px;padding:10px 12px;margin:8px 0;cursor:pointer}
.tcard.sel{border-color:#38bdf8;background:#101a35}
.tcard.on{border-left:3px solid #34d399}
.trow1{display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap}
.trow2{display:flex;gap:14px;flex-wrap:wrap;font-size:13px;color:#94a3b8;margin-top:6px}
.trow3{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:#64748b;margin-top:6px}
.bar{height:6px;background:#1a2440;border-radius:3px;margin-top:7px;overflow:hidden}
.bar i{display:block;height:100%;background:linear-gradient(90deg,#059669,#34d399);border-radius:3px;transition:width .5s}
.mini{padding:3px 12px;font-size:12px;border-radius:6px;background:#b91c1c;color:#fff;border:0;cursor:pointer;flex:none}
</style></head><body>
<div class="wrap">
<h1>🚗 统壹出行 · 网页版</h1>

<div class="card">
  <label>任务选择</label>
  <select id="kind">
    <option value="register_only">仅注册</option>
    <option value="register">注册签到</option>
  </select>
  <label>批量任务（每行一条：邀请码----数量）</label>
  <textarea id="batch" placeholder="7237919----100&#10;18815798989----50"></textarea>
  <div class="row">
    <div><label>代理API</label><input id="api" value="__DEFAULT_API__" placeholder="代理API提取链接"></div>
    <div><label>注册密码</label><input id="pwd" value="123456"></div>
    <div><label>并发线程</label><input id="th" type="number" value="5" min="1" max="99"></div>
    <div><label>线程延迟(秒, 如0-0.2)</label><input id="delay" value="0-0.2" placeholder="0-0.2"></div>
  </div>
  <div class="btns">
    <button id="btnGo" onclick="go()">提交任务</button>
    <button id="btnStop" onclick="stopJob()">停止</button>
  </div>
</div>

<div class="card">
  <h2>📷 图片识别邀请码 <span class="tag">仅识别, 不参与注册</span></h2>
  <label>上传海报/截图(可多选), 二维码自动提取邀请码 + 识别推荐人尾号</label>
  <input id="imgs" type="file" accept="image/*" multiple>
  <div class="btns"><button id="btnScan" style="background:#2563eb;color:#fff" onclick="scanImgs()">开始识别</button></div>
  <div id="scanOut"><div class="tag">还没有识别结果</div></div>
</div>

<div class="card">
  <h2>任务列表 <span style="float:right">
    <button class="mini" style="background:#334155" onclick="clearDone()">清空已结束</button>
    <a href="/download" style="font-size:13px;color:#38bdf8;text-decoration:none;
     background:#0d1428;border:1px solid #25335c;border-radius:7px;padding:4px 10px">⬇ 下载数据</a></span></h2>
  <div id="tasklist"><div class="tag">还没有任务, 在上方提交后显示</div></div>
</div>

<div class="card">
  <h2 id="dtitle">任务详情</h2>
  <div class="total" id="total">点击上方任务查看详情</div>
  <div id="inv"></div>
  <label>账号实时状态</label>
  <div id="feed"></div>
</div>

<div class="card">
  <h2>运行日志</h2>
  <div id="logs"></div>
</div>
</div>

<script>
let curTid=0;
const $=id=>document.getElementById(id);
function esc(s){return String(s).replace(/[<>&]/g,c=>({"<":"&lt;",">":"&gt;","&":"&amp;"}[c]))}

function renderTasks(tasks){
  const el=$("tasklist");
  if(!tasks.length){el.innerHTML='<div class="tag">还没有任务, 在上方提交后显示</div>';return}
  el.innerHTML="";
  tasks.forEach(t=>{
    const card=document.createElement("div");
    card.className="tcard"+(t.tid===curTid?" sel":"")+(t.running?" on":"");
    const pct=t.target?Math.round(t.done/t.target*100):0;
    card.innerHTML=`<div class="trow1"><span class="code">#${t.tid} ${esc(t.name)}</span>
      <span class="st ${t.running?'run':'fin'}">${t.running?'● 运行中':'✓ 已结束'}</span></div>
      <div class="trow2">
        <span>${esc(t.task_label)}</span>
        <span>成功 <b class="ok">${t.success}</b> 失败 <b class="${t.fail?'bad':'ok'}">${t.fail}</b></span>
        <span>${t.done}/${t.target} (${pct}%)</span>
      </div>
      <div class="bar"><i style="width:${pct}%"></i></div>
      <div class="trow3"><span>${t.running?('开始 '+t.start_at):('结束 '+t.end_at)}</span>
      ${t.running?`<button class="mini" onclick="stopTask(${t.tid});event.stopPropagation()">停止</button>`:''}</div>`;
    card.onclick=()=>selectTask(t.tid);
    el.appendChild(card);
  });
}

function renderDetail(d){
  if(!d){$("dtitle").textContent="任务详情";$("total").textContent="点击上方任务查看详情";
    $("inv").innerHTML="";$("feed").innerHTML="";$("logs").textContent="";return}
  $("dtitle").textContent=`任务详情 · #${d.tid} ${d.name}`;
  const done=(d.rows||[]).reduce((a,b)=>a+b.ok,0),tt=(d.rows||[]).reduce((a,b)=>a+b.n,0);
  $("total").innerHTML=d.running?
    `批量进度 已完成 <b>${done}</b> / ${tt} &nbsp;·&nbsp; 成功 <b>${(d.success||0)}</b> &nbsp;·&nbsp; 失败 <b class="f">${(d.fail||0)}</b>`:
    `已结束 · 完成 <b>${done}</b> / ${tt} &nbsp;·&nbsp; 成功 <b>${(d.success||0)}</b> &nbsp;·&nbsp; 失败 <b class="f">${(d.fail||0)}</b>${d.break_msg?' &nbsp;·&nbsp; <span class="warn">⛔'+esc(d.break_msg)+'</span>':''}`;
  const el=$("inv");el.innerHTML="";
  (d.rows||[]).forEach(r=>{
    const div=document.createElement("div");div.className="invline";
    div.innerHTML=`<span class="code">邀请码 ${esc(r.code)}</span>
      <span>成功 <b class="ok">${r.ok}</b>/${r.n} &nbsp;失败 <b class="${r.fail?'bad':'ok'}">${r.fail}</b> &nbsp;剩余 ${r.left}</span>
      <span class="st ${r.state==='已完成'?'fin':'run'}">${r.state==='已完成'?'✓ 完成':'进行中'}</span>`;
    el.appendChild(div);
  });
  $("feed").innerHTML=(d.feed||[]).map(x=>`<div>${esc(x)}</div>`).join("")||"<div>—</div>";
  const lg=$("logs");
  if(lg.dataset.tid!==String(d.tid)){lg.textContent=(d.logs||[]).join("\\n");lg.dataset.tid=d.tid}
  lg.scrollTop=1e9;
}

async function refresh(){
  try{
    const r=await fetch("/state?tid="+curTid);
    const s=await r.json();
    renderTasks(s.tasks||[]);
    renderDetail(s.detail);
    if(!curTid&&(s.tasks||[]).length){curTid=s.tasks[0].tid;refresh()}
  }catch(e){}
}
function selectTask(tid){curTid=tid;refresh()}
async function go(){
  const body={kind:$("kind").value,batch:$("batch").value,api:$("api").value,pwd:$("pwd").value,threads:$("th").value,delay:$("delay").value};
  $("btnGo").disabled=true;
  try{
    const r=await fetch("/start",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
    const j=await r.json();
    if(!j.ok){alert(j.msg||"提交失败");return}
    curTid=j.tid;
    $("total").textContent="任务启动中…";$("inv").innerHTML="";$("feed").innerHTML="";
  }catch(e){
    alert("提交失败: "+e+"（请刷新页面重试）");
  }finally{
    $("btnGo").disabled=false;
    refresh();
  }
}
async function stopTask(tid){
  if(!tid)tid=curTid;
  if(!tid)return;
  try{await fetch("/stop",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({tid:tid})})}catch(e){}
  setTimeout(refresh,800);
}
async function clearDone(){
  try{await fetch("/clear",{method:"POST"})}catch(e){}
  refresh();
}
let scanRows=[];
function _copyTxt(t){
  try{
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).catch(()=>prompt("请手动复制:",t))}
    else{prompt("请手动复制:",t)}
  }catch(e){prompt("请手动复制:",t)}
}
async function scanImgs(){
  const inp=$("imgs");
  if(!inp.files||!inp.files.length){alert("请先选择海报/截图图片");return}
  const btn=$("btnScan");btn.disabled=true;btn.textContent="识别中…";
  const out=$("scanOut");out.innerHTML='<div class="tag">正在识别…</div>';
  scanRows=[];
  for(const f of inp.files){
    const fd=new FormData();fd.append("file",f);
    let j;
    try{const r=await fetch("/scan",{method:"POST",body:fd});j=await r.json()}
    catch(e){j={ok:false,msg:"请求失败:"+e}}
    scanRows.push({ok:!!j.ok,code:j.code||"",tail:j.tail||"",msg:j.msg||"",raw:j.raw||""});
  }
  btn.disabled=false;btn.textContent="开始识别";
  renderScan();
}
function scanCodes(){return scanRows.filter(r=>r.ok).map(r=>r.code)}
function importToBatch(){
  const codes=scanCodes();
  if(!codes.length){alert("还没有识别成功的邀请码");return}
  const ta=$("batch");
  const have=new Set(ta.value.split(/\\n/).map(s=>s.split(/-{2,}|—|——|×|\\*|\\s/)[0].trim()).filter(Boolean));
  let added=0,skipped=0;
  const lines=[];
  codes.forEach(c=>{
    if(have.has(c)){skipped++;return}
    have.add(c);added++;lines.push(c+"----");
  });
  if(!lines.length){alert("识别的邀请码都已在批量任务里");return}
  const cur=ta.value.trim();
  ta.value=(cur?cur.replace(/\\n+$/,"")+"\\n":"")+lines.join("\\n")+"\\n";
  ta.scrollTop=ta.scrollHeight;
  alert(`已导入 ${added} 个邀请码到批量任务(已带----, 补数量即可)`+(skipped?`, 跳过重复 ${skipped} 个`:""));
}
function renderScan(){
  const out=$("scanOut");
  if(!scanRows.length){out.innerHTML='<div class="tag">还没有识别结果</div>';return}
  let html="",summary=[];
  scanRows.forEach((r,i)=>{
    if(r.ok){
      summary.push(`图片${i+1}`+(r.tail?`尾号${r.tail}`:"")+`邀请码${r.code}`);
      html+=`<div class="invline"><span>图片${i+1}${r.tail?` <span class="tag">尾号${esc(r.tail)}</span>`:""} 邀请码 <b class="code">${esc(r.code)}</b></span><button class="mini" style="background:#334155" onclick="_copyTxt('${esc(r.code)}')">复制</button></div>`;
    }else{
      summary.push(`图片${i+1}识别失败`);
      html+=`<div class="invline"><span>图片${i+1} <span class="bad">✗ ${esc(r.msg||"识别失败")}</span>${r.raw?` <span class="tag">${esc(r.raw)}</span>`:""}</span></div>`;
    }
  });
  html+=`<label>识别汇总(可直接编辑)</label><textarea id="scanSummary" style="min-height:84px">${esc(summary.join("\\n"))}</textarea>`;
  html+=`<div class="btns">`
    +(scanCodes().length?`<button style="background:#059669;color:#fff" onclick="importToBatch()">📥 一键导入到批量任务(${scanCodes().length})</button>`:"")
    +(scanCodes().length?`<button style="background:#334155;color:#fff" onclick="_copyTxt(scanCodes().join('\\n'))">复制全部邀请码</button>`:"")
    +`</div>`;
  out.innerHTML=html;
}
const es=new EventSource("/stream");
es.onmessage=e=>{
  const d=JSON.parse(e.data);
  if(d.tid&&d.tid!==curTid){
    if(d.t==="done"||d.t==="batch")refresh();
    return;
  }
  if(d.t==="log"){const el=$("logs");el.textContent+=d.m+"\\n";el.scrollTop=1e9;}
  else if(d.t==="batch"||d.t==="stats"){refresh();}
  else if(d.t==="row"){const el=$("feed");const div=document.createElement("div");div.textContent=d.m;el.prepend(div);
    while(el.children.length>60)el.lastChild.remove();}
  else if(d.t==="done"){refresh();}
};
es.onerror=()=>{};
refresh();
setInterval(refresh,5000);
</script>
</body></html>"""

PAGE = PAGE.replace("__DEFAULT_API__", DEFAULT_API)

LOGIN_PAGE = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>访问验证</title></head>
<body style="font-family:sans-serif;background:#0b1020;color:#e2e8f0;display:flex;justify-content:center;padding-top:15vh">
<form method="post" action="/login" style="background:#131a30;padding:24px;border-radius:12px">
<h3>访问验证</h3><input name="key" type="password" placeholder="访问密码" style="display:block;margin:12px 0;padding:9px;border-radius:8px;border:1px solid #25335c;background:#0d1428;color:#e2e8f0">
<button style="padding:9px 20px;border:0;border-radius:8px;background:#059669;color:#fff">进入</button>
</form></body></html>"""

def _authed():
    if not ACCESS_PASS:
        return True
    return request.cookies.get("k") == ACCESS_PASS

@app.route("/login", methods=["POST"])
def login():
    if request.form.get("key", "") == ACCESS_PASS:
        resp = make_response(redirect("/"))
        resp.set_cookie("k", ACCESS_PASS, max_age=30 * 86400)
        return resp
    return LOGIN_PAGE

@app.route("/")
def index():
    if not _authed():
        resp = make_response(LOGIN_PAGE)
        resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        return resp
    resp = make_response(render_template_string(PAGE))
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return resp

@app.route("/state")
def state():
    if not _authed():
        return jsonify({"tasks": [], "detail": None})
    try:
        sel = int(request.args.get("tid", "0"))
    except ValueError:
        sel = 0
    with STATE_LOCK:
        tasks = []
        for t in sorted(TASKS.values(), key=lambda x: -x["tid"]):
            done = sum(r["ok"] for r in t["rows"])
            target = sum(r["n"] for r in t["rows"])
            tasks.append({
                "tid": t["tid"], "name": t["name"], "task_label": t["task_label"],
                "running": t["running"], "success": t["success"], "fail": t["fail"],
                "total": t["total"], "done": done, "target": target,
                "start_at": t["start_at"], "end_at": t["end_at"], "break_msg": t["break_msg"],
            })
        detail = None
        task = TASKS.get(sel)
        if task:
            detail = {
                "tid": task["tid"], "name": task["name"], "task_label": task["task_label"],
                "running": task["running"], "success": task["success"], "fail": task["fail"],
                "rows": list(task["rows"]),
                "logs": list(task["logs"])[-300:],
                "feed": list(task["feed"])[-40:],
                "break_msg": task["break_msg"],
            }
    return jsonify({"tasks": tasks, "detail": detail, "sel": sel})

@app.route("/start", methods=["POST"])
def start():
    if not _authed():
        return jsonify({"ok": False, "msg": "未授权"}), 401
    d = request.get_json(force=True, silent=True) or {}
    entries, bad = parse_batch(d.get("batch", ""))
    if not entries:
        return jsonify({"ok": False, "msg": "没有有效的「邀请码----数量」行, 请检查格式"}), 400
    ok, msg = start_job(d.get("kind", "register_only"), entries, d.get("api", ""), d.get("pwd", ""), d.get("threads", 5), d.get("delay", ""))
    if ok and bad:
        with STATE_LOCK:
            task = TASKS.get(msg)
            if task:
                add_log(task, f"⚠️ {len(bad)}行格式错误已跳过: {bad[:5]}")
    return jsonify({"ok": ok, "tid": msg if ok else 0, "msg": str(msg)})

@app.route("/stop", methods=["POST"])
def stop():
    if not _authed():
        return jsonify({"ok": False}), 401
    d = request.get_json(force=True, silent=True) or {}
    try:
        tid = int(d.get("tid", "0"))
    except (TypeError, ValueError):
        tid = 0
    ok, msg = stop_task(tid)
    return jsonify({"ok": ok, "msg": msg})

@app.route("/clear", methods=["POST"])
def clear():
    if not _authed():
        return jsonify({"ok": False}), 401
    with STATE_LOCK:
        dones = [tid for tid, t in TASKS.items() if not t["running"]]
        for tid in dones:
            t = TASKS.pop(tid, None)
            if t:
                WT2TID.pop(id(t["wt"]), None)
    return jsonify({"ok": True, "msg": f"已清空 {len(dones)} 个已结束任务"})

@app.route("/download")
def download():
    """打包下载全部结果数据(手机浏览器可直接下载zip)"""
    if not _authed():
        return jsonify({"ok": False}), 401
    import io
    import zipfile
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        root = DATA_ROOT
        if os.path.exists(root):
            for dp, _, fns in os.walk(root):
                for fn in fns:
                    if fn.endswith(".lock"):
                        continue
                    p = os.path.join(dp, fn)
                    zf.write(p, os.path.relpath(p, root))
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="application/zip",
                    headers={"Content-Disposition": f"attachment; filename=results_{time.strftime('%m%d_%H%M')}.zip"})

@app.route("/stream")
def stream():
    if not _authed():
        return Response("unauthorized", status=401)
    q = queue.Queue(maxsize=400)
    with SUBS_LOCK:
        SUBS.add(q)
    def gen():
        try:
            while True:
                try:
                    evt = q.get(timeout=20)
                    yield f"data: {json.dumps(evt, ensure_ascii=False)}\n\n"
                except queue.Empty:
                    yield ": keepalive\n\n"
        finally:
            with SUBS_LOCK:
                SUBS.discard(q)
    return Response(gen(), mimetype="text/event-stream",
                    headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    from werkzeug.serving import make_server
    srv = make_server("0.0.0.0", port, app, threaded=True)
    print(f"✅ 统壹出行网页版已启动: http://127.0.0.1:{port}")
    srv.serve_forever()
