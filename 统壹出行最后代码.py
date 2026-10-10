

# 省份代码 -> 中文名称
PROVINCE_CN_MAP = {
    "BJ": "北京", "SH": "上海", "GD": "广东", "JS": "江苏", "ZJ": "浙江",
    "SD": "山东", "HA": "河南", "SC": "四川", "HB": "湖北", "HN": "湖南",
    "FJ": "福建", "AH": "安徽", "HE": "河北", "SN": "陕西", "LN": "辽宁",
    "JL": "吉林", "HL": "黑龙江", "JX": "江西", "GX": "广西", "YN": "云南",
    "GZ": "贵州", "SX": "山西", "GS": "甘肃", "HI": "海南", "NM": "内蒙古",
    "XJ": "新疆", "NX": "宁夏", "QH": "青海", "XZ": "西藏", "TJ": "天津", "CQ": "重庆",
}

# 运营商代码 -> 中文名称
CARRIER_CN_MAP = {
    "CMCC": "移动", "CUCC": "联通", "CTCC": "电信", "CBN": "广电",
}

# 省份 -> 专属IP网段 (每省每运营商独立IP段, 无重叠)
# CMCC=中国移动, CUCC=中国联通, CTCC=中国电信
PROVINCE_IP_RANGES = {
    "BJ": [
        ("CMCC", [(112,65,0,16),(141,72,0,16)]),
        ("CUCC", [(123,125,100,16),(202,106,0,14)]),
        ("CTCC", [(36,64,100,16),(42,56,100,16)]),
    ],
    "SH": [
        ("CMCC", [(117,136,0,16),(139,0,100,16)]),
        ("CUCC", [(218,75,0,14),(123,125,101,16)]),
        ("CTCC", [(36,64,101,16),(42,56,101,16)]),
    ],
    "GD": [
        ("CMCC", [(117,114,0,16),(183,232,0,16)]),
        ("CUCC", [(202,105,0,14),(218,75,100,16)]),
        ("CTCC", [(59,48,0,14),(115,164,0,14)]),
    ],
    "JS": [
        ("CMCC", [(112,4,0,14),(120,192,0,15)]),
        ("CUCC", [(202,106,100,16),(123,125,102,16)]),
        ("CTCC", [(61,165,100,16),(36,64,102,16)]),
    ],
    "ZJ": [
        ("CMCC", [(112,64,0,14),(117,109,0,16)]),
        ("CUCC", [(218,76,0,14),(202,106,101,16)]),
        ("CTCC", [(222,176,0,14),(222,177,0,14)]),
    ],
    "SD": [
        ("CMCC", [(123,125,0,14),(218,200,100,16)]),
        ("CUCC", [(202,106,102,16),(123,125,103,16)]),
        ("CTCC", [(36,64,103,16),(42,56,102,16)]),
    ],
    "HA": [
        ("CMCC", [(117,139,0,16),(218,200,101,16)]),
        ("CUCC", [(202,102,0,14),(123,125,104,16)]),
        ("CTCC", [(222,172,0,14),(36,64,104,16)]),
    ],
    "SC": [
        ("CMCC", [(183,233,0,16),(218,200,102,16)]),
        ("CUCC", [(202,98,0,14),(123,125,105,16)]),
        ("CTCC", [(61,165,101,16),(42,56,103,16)]),
    ],
    "HB": [
        ("CMCC", [(117,140,0,16),(218,200,103,16)]),
        ("CUCC", [(202,106,103,16),(123,125,106,16)]),
        ("CTCC", [(36,64,105,16),(42,56,104,16)]),
    ],
    "HN": [
        ("CMCC", [(117,141,0,16),(218,200,104,16)]),
        ("CUCC", [(202,103,0,14),(123,125,107,16)]),
        ("CTCC", [(61,165,102,16),(42,56,105,16)]),
    ],
    "FJ": [
        ("CMCC", [(117,142,0,16),(218,200,105,16)]),
        ("CUCC", [(218,75,101,16),(123,125,108,16)]),
        ("CTCC", [(36,64,106,16),(42,56,106,16)]),
    ],
    "AH": [
        ("CMCC", [(112,64,100,16),(218,200,106,16)]),
        ("CUCC", [(202,106,104,16),(123,125,109,16)]),
        ("CTCC", [(61,164,0,14),(42,56,107,16)]),
    ],
    "HE": [
        ("CMCC", [(112,64,101,16),(218,200,107,16)]),
        ("CUCC", [(202,99,0,14),(123,125,110,16)]),
        ("CTCC", [(36,64,107,16),(42,56,108,16)]),
    ],
    "SN": [
        ("CMCC", [(117,143,0,16),(218,200,108,16)]),
        ("CUCC", [(202,106,105,16),(123,125,111,16)]),
        ("CTCC", [(36,64,108,16),(42,56,109,16)]),
    ],
    "LN": [
        ("CMCC", [(117,144,0,16),(218,200,109,16)]),
        ("CUCC", [(218,75,102,16),(123,125,112,16)]),
        ("CTCC", [(222,176,100,16),(36,64,109,16)]),
    ],
    "JL": [
        ("CMCC", [(117,145,0,16),(218,200,110,16)]),
        ("CUCC", [(202,98,100,16),(123,125,113,16)]),
        ("CTCC", [(222,176,101,16),(42,56,110,16)]),
    ],
    "HL": [
        ("CMCC", [(117,146,0,16),(218,200,111,16)]),
        ("CUCC", [(202,97,0,14),(123,125,114,16)]),
        ("CTCC", [(222,176,102,16),(42,56,111,16)]),
    ],
    "JX": [
        ("CMCC", [(117,147,0,16),(218,200,112,16)]),
        ("CUCC", [(202,106,106,16),(123,125,115,16)]),
        ("CTCC", [(61,165,103,16),(42,56,112,16)]),
    ],
    "GX": [
        ("CMCC", [(117,148,0,16),(218,200,113,16)]),
        ("CUCC", [(202,103,100,16),(123,125,116,16)]),
        ("CTCC", [(36,64,110,16),(42,56,113,16)]),
    ],
    "YN": [
        ("CMCC", [(117,149,0,16),(218,200,114,16)]),
        ("CUCC", [(202,98,101,16),(123,125,117,16)]),
        ("CTCC", [(36,64,111,16),(42,56,114,16)]),
    ],
    "GZ": [
        ("CMCC", [(117,150,0,16),(218,200,115,16)]),
        ("CUCC", [(202,98,102,16),(123,125,118,16)]),
        ("CTCC", [(61,165,104,16),(42,56,115,16)]),
    ],
    "SX": [
        ("CMCC", [(117,151,0,16),(218,200,116,16)]),
        ("CUCC", [(202,99,100,16),(123,125,119,16)]),
        ("CTCC", [(36,64,112,16),(42,56,116,16)]),
    ],
    "GS": [
        ("CMCC", [(117,152,0,16),(218,200,117,16)]),
        ("CUCC", [(202,106,107,16),(123,125,120,16)]),
        ("CTCC", [(61,165,105,16),(42,56,117,16)]),
    ],
    "HI": [
        ("CMCC", [(117,153,0,16),(218,200,118,16)]),
        ("CUCC", [(202,103,101,16),(123,125,121,16)]),
        ("CTCC", [(36,64,113,16),(42,56,118,16)]),
    ],
    "NM": [
        ("CMCC", [(117,154,0,16),(218,200,119,16)]),
        ("CUCC", [(202,106,108,16),(123,125,122,16)]),
        ("CTCC", [(36,64,114,16),(42,56,119,16)]),
    ],
    "XJ": [
        ("CMCC", [(117,155,0,16),(218,200,120,16)]),
        ("CUCC", [(202,106,109,16),(123,125,123,16)]),
        ("CTCC", [(36,64,115,16),(42,56,120,16)]),
    ],
    "NX": [
        ("CMCC", [(117,156,0,16),(218,200,121,16)]),
        ("CUCC", [(202,106,110,16),(123,125,124,16)]),
        ("CTCC", [(36,64,116,16),(42,56,121,16)]),
    ],
    "QH": [
        ("CMCC", [(117,157,0,16),(218,200,122,16)]),
        ("CUCC", [(202,106,111,16),(123,125,125,16)]),
        ("CTCC", [(36,64,117,16),(42,56,122,16)]),
    ],
    "XZ": [
        ("CMCC", [(117,158,0,16),(218,200,123,16)]),
        ("CUCC", [(202,98,103,16),(123,125,126,16)]),
        ("CTCC", [(36,64,118,16),(42,56,123,16)]),
    ],
    "TJ": [
        ("CMCC", [(166,1,0,16),(218,200,124,16)]),
        ("CUCC", [(218,75,103,16),(123,125,127,16)]),
        ("CTCC", [(36,64,119,16),(42,56,124,16)]),
    ],
    "CQ": [
        ("CMCC", [(183,234,0,16),(218,200,125,16)]),
        ("CUCC", [(202,98,104,16),(123,125,128,16)]),
        ("CTCC", [(61,165,106,16),(42,56,125,16)]),
    ],
}
# -*- coding: utf-8 -*-
import sys
import random
import time
import os
import json
import re
import ast
import calendar
import string
import asyncio
import threading
import pickle

# PyInstaller 打包后用 _internal 目录, 开发环境用脚本所在目录
if getattr(sys, 'frozen', False):
    # 打包后 EXE 在根目录, 数据文件在 _internal 目录
    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(sys.executable)), '_internal')
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 软件所在文件夹: 打包后为 EXE 根目录(用户可见), 开发环境为脚本目录; 重复IP黑名单等用户文件跟随此目录
APP_DIR = os.path.dirname(os.path.abspath(sys.executable)) if getattr(sys, 'frozen', False) else BASE_DIR
import hashlib
import requests
from typing import Optional, Tuple, List
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# 核心库检查与导入
try:
    from curl_cffi.requests import AsyncSession, RequestsError
except ImportError:
    print("错误: 未安装 curl_cffi。请运行: pip install curl_cffi")
    sys.exit(1)

try:
    from faker import Faker
except ImportError:
    print("错误: 未安装 Faker。请运行: pip install Faker")
    sys.exit(1)

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
                                 QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView,
                                 QLineEdit, QPushButton, QComboBox, QCheckBox, QGroupBox,
                                 QFormLayout, QTextEdit, QFileDialog, QMessageBox, QLabel, QMenu, QAction, QProgressBar,
                                 QSlider, QSpinBox, QSizePolicy, QStyleFactory, QFrame, QScrollArea)
    from PyQt5.QtCore import Qt, QDateTime, QThread, pyqtSignal
    from PyQt5.QtGui import QFont, QColor, QPalette
    # 画布缩放所需(整个界面跟随窗口等比缩放)
    from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
    from PyQt5.QtGui import QPainter
    from PyQt5.QtCore import QTimer
except ImportError:
    print("错误: 未安装 PyQt5。请运行: pip install PyQt5")
    sys.exit(1)

# 初始化 Faker
fake = Faker('zh_CN')
random.seed()

# ===================== 跨进程文件锁(防多软件并发写同一文件丢数据) =====================
try:
    import msvcrt  # Windows
    _IS_WINDOWS = True
except ImportError:
    try:
        import fcntl  # Linux/Mac
        _IS_WINDOWS = False
    except ImportError:
        _IS_WINDOWS = None  # 无锁支持, 退化为无锁写入

def _file_lock(file_obj):
    """获取排他锁(阻塞等待), 保护跨进程并发写入"""
    if _IS_WINDOWS is True:
        # Windows: msvcrt.locking 锁定从当前指针起的 1 字节, LK_LOCK 阻塞等待
        try:
            msvcrt.locking(file_obj.fileno(), msvcrt.LK_LOCK, 1)
            return True
        except OSError:
            return False
    elif _IS_WINDOWS is False:
        # Linux/Mac: fcntl.flock 全文件排他锁, 阻塞等待
        try:
            fcntl.flock(file_obj.fileno(), fcntl.LOCK_EX)
            return True
        except OSError:
            return False
    return False

def _file_unlock(file_obj):
    """释放排他锁"""
    if _IS_WINDOWS is True:
        try:
            msvcrt.locking(file_obj.fileno(), msvcrt.LK_UNLCK, 1)
        except OSError:
            pass
    elif _IS_WINDOWS is False:
        try:
            fcntl.flock(file_obj.fileno(), fcntl.LOCK_UN)
        except OSError:
            pass

# =====================【中文姓名生成器】=====================
_SURNAMES = [
    "王", "李", "张", "刘", "陈", "杨", "黄", "赵", "吴", "周",
    "徐", "孙", "胡", "朱", "高", "林", "何", "郭", "马", "罗",
    "梁", "宋", "郑", "谢", "韩", "唐", "冯", "于", "董", "萧",
    "程", "曹", "袁", "邓", "许", "傅", "沈", "曾", "彭", "吕",
    "苏", "卢", "蒋", "蔡", "贾", "丁", "魏", "薛", "叶", "阎",
    "余", "潘", "杜", "戴", "夏", "钟", "汪", "田", "任", "姜",
    "范", "方", "石", "姚", "谭", "廖", "邹", "熊", "金", "陆",
    "郝", "孔", "白", "崔", "康", "毛", "邱", "秦", "江", "史",
    "顾", "侯", "邵", "孟", "龙", "万", "段", "雷", "钱", "汤"
]

_GIVEN_2CHAR = [
    "秀英", "秀兰", "桂英", "志强", "建华", "晓东", "晓明", "志伟", "丽娟", "艳华",
    "静怡", "敏华", "伟杰", "海涛", "春晓", "秋霞", "冬冬", "春花", "夏雨", "秋月",
    "雪莲", "雪峰", "云鹏", "云飞", "金龙", "金凤", "小龙", "小凤", "大鹏", "小燕",
    "志远", "志刚", "志华", "俊杰", "俊华", "俊峰", "文博", "文涛", "文杰", "文辉",
    "文婷", "文静", "文丽", "文艳", "文轩", "思远", "思涵", "思琪", "思思", "思敏",
    "思静", "思彤", "思颖", "思雨", "梓豪", "梓轩", "梓涵", "梓琪", "梓萱", "梓妍",
    "梓晴", "梓婷", "梓悦", "梓欣", "宇轩", "宇豪", "宇涵", "宇彤", "宇泽", "宇飞",
    "宇辰", "宇航", "宇翔", "浩然", "浩宇", "浩轩", "浩涵", "浩峰", "浩天", "浩哲",
    "浩浩", "子轩", "子涵", "子琪", "子豪", "子墨", "子谦", "子航", "子健", "子俊",
    "子杰", "睿杰", "睿轩", "睿涵", "睿琪", "睿哲", "睿涛", "睿锋", "睿彬", "睿华",
    "欣怡", "欣妍", "欣悦", "欣如", "欣彤", "欣雅", "欣慧", "怡然", "沐然", "沐辰",
    "沐阳", "沐宸", "沐浩", "沐宇", "沐轩", "沐哲", "雨轩", "雨涵", "雨桐", "雨泽",
    "雨辰", "雨欣", "雨婷", "雨薇", "诗琪", "诗涵", "诗妍", "诗雨", "诗琳", "诗韵",
    "诗雅", "诗悦", "雅琪", "雅静", "雅雯", "雅婷", "雅琳", "雅欣", "雅妍", "雅晴",
    "雅茹", "雅琴", "天佑", "天翊", "天乐", "天骄", "天悦", "天宇", "天翔", "天昊",
    "天磊", "天阳", "一鸣", "一凡", "一诺", "一轩", "一涵", "一航", "一辰", "一然",
    "一川", "一舟", "博文", "博雅", "博宇", "博浩", "博轩", "博涵", "博远", "博涛",
    "博飞", "奕辰", "奕轩", "奕涵", "奕奕", "奕泽", "奕豪", "奕杰", "奕涛", "奕锋",
    "奕然", "俊熙", "俊轩", "俊涵", "俊豪", "俊才", "俊涛", "俊哲", "俊彬", "晨曦",
    "晨光", "辰逸", "辰宇", "辰皓", "辰轩", "辰霖", "辰阳", "佳豪", "佳琪", "佳欣",
    "佳怡", "佳涵", "佳轩", "佳宁", "佳悦", "佳慧", "建宇", "建国", "建军", "建明",
    "建辉", "建峰", "建涛", "建龙", "建伟", "志明", "志鹏", "志斌", "志豪", "志轩",
    "雪梅", "雪琴", "雪娟", "雪丽", "雪婷", "雪茹", "雪琳", "雪妍", "雪晴", "雪莹",
    "桂芳", "桂华", "桂兰", "桂珍", "桂妹", "桂秀", "桂菊", "桂梅", "桂萍", "丽红",
    "丽华", "丽敏", "丽静", "丽莉", "丽玲", "丽霞", "丽菲", "晓峰", "晓雯", "晓婷",
    "晓梅", "晓娟", "晓芳", "晓燕", "晓琳", "建飞", "春燕", "春梅", "春芳", "春娣",
    "春兰", "春霞", "春阳", "春生", "春明", "秋萍", "秋芳", "秋燕", "秋阳", "秋生",
    "秋明", "秋华", "秋红", "秋敏", "冬梅", "冬雪", "冬阳", "冬生", "冬琳", "冬燕",
    "冬晴", "海峰", "海华", "海鹏", "海飞", "海龙", "海燕", "海霞", "海琳", "海宁",
    "金鹏", "金花", "金华", "金明", "金辉", "金海", "金刚", "金鑫", "银柱", "银山",
    "银凤", "银花", "银杏", "银辉", "银海", "银涛", "银燕", "银玲", "玉峰", "玉华",
    "玉兰", "玉梅", "玉琴", "玉珍", "玉珠", "玉琳", "玉婷", "玉蓉", "宝峰", "宝龙",
    "宝华", "宝珍", "宝玉", "宝娟", "宝霞", "宝燕", "宝琳", "宝茹", "彩凤", "彩霞",
    "彩琴", "彩娟", "彩云", "彩红", "彩华", "彩玲", "彩英", "彩莲", "凤凰", "凤仪",
    "凤英", "凤霞", "凤娟", "凤玲", "凤梅", "凤兰", "凤春", "凤飞", "龙腾", "龙飞",
    "龙华", "青龙", "云龙", "腾龙", "飞龙", "云峰", "云海", "云华", "云燕", "云梅",
    "云波", "云翔", "云舒", "天明", "天云", "天辉", "天华", "天鸣", "天助", "天成",
    "志浩", "俊辉", "文涵", "文昊", "文彬", "文彦", "文浩", "思成", "思明", "雨萱",
]

_GIVEN_1CHAR = [
    "伟", "芳", "娜", "敏", "静", "丽", "强", "磊", "军", "洋",
    "勇", "艳", "杰", "娟", "涛", "明", "超", "霞", "平", "刚",
    "华", "东", "英", "俊", "豪", "文", "武", "斌", "峰", "鹏",
    "飞", "龙", "凤", "玲", "琳", "梅", "兰", "竹", "松", "雪",
    "霜", "露", "云", "风", "雨", "雷", "电", "星", "月", "日",
    "天", "地", "山", "河", "海", "川", "湖", "江", "溪", "泉",
    "潭", "渊", "源", "林", "森", "树", "木", "花", "草", "叶",
    "禾", "苗", "蕊", "金", "银", "铜", "铁", "锡", "铅", "铝",
    "锌", "镍", "铬", "玉", "珠", "宝", "贝", "玑", "珊", "瑚",
    "玛", "瑙", "琉", "红", "橙", "黄", "绿", "青", "蓝", "紫",
    "白", "黑", "灰", "春", "夏", "秋", "冬", "南", "西", "北",
    "中", "外", "左", "右", "前", "后", "上", "下", "里", "间",
    "内", "旁", "大", "小", "多", "少", "高", "低", "长", "短",
    "宽", "窄", "远", "近", "深", "浅", "厚", "薄", "重", "轻",
    "快", "慢", "新", "旧", "老", "壮", "弱", "盛", "衰", "美",
    "丑", "善", "恶", "真", "假", "虚", "实", "暗", "智", "愚",
    "怯", "仁", "义", "礼", "信", "忠", "孝", "悌", "廉", "耻",
    "荣", "辱", "福", "祸", "吉", "凶", "富", "贫", "贵", "贱",
    "兴", "成", "败", "得", "失", "安", "危", "存", "亡", "进",
    "退", "升", "降", "开", "关", "来", "去", "归", "离", "合",
    "分", "聚", "散", "出", "爱", "恨", "恩", "怨", "情", "仇",
    "亲", "疏", "生", "死", "活", "有", "无", "是", "否", "对",
    "错", "好", "坏", "优", "劣", "胖", "瘦", "粗", "细", "干",
    "湿", "暖", "冷", "热", "凉", "温", "寒", "暑", "燥", "润",
    "鲜", "亮", "淡", "浓", "香", "臭", "味", "甜", "酸", "苦",
    "辣", "咸", "直", "曲", "弯", "折", "尖", "钝", "圆", "方",
    "正", "斜", "立", "卧", "坐", "行", "走", "跑", "跳", "游",
    "翔", "说", "笑", "哭", "喊", "唱", "叫", "吟", "诵", "读",
    "写", "看", "听", "闻", "尝", "摸", "触", "感", "想", "思",
    "念", "心", "肝", "肺", "脾", "肾", "脑", "血", "肉", "骨",
    "筋", "雾", "水", "田", "园", "村", "镇", "城", "市", "省",
    "国", "张", "王", "李", "赵", "钱", "孙", "周", "吴", "郑",
    "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦",
    "尤", "许", "何", "吕", "施", "孔", "曹", "严", "魏", "陶",
    "姜", "戚", "谢", "邹", "喻", "柏", "窦", "章", "苏", "潘",
    "葛", "奚", "范", "彭", "郎", "鲁", "韦", "昌", "马", "俞",
    "任", "袁", "柳", "唐", "罗", "薛", "伍", "余", "米", "臧",
    "计", "戴", "宋", "茅", "庞", "熊", "纪", "舒", "屈", "项",
    "祝", "董", "梁", "杜", "阮", "闵", "席", "季", "麻", "贾",
    "路", "娄", "童", "颜", "郭", "刁", "钟", "徐", "邱", "骆",
]

# 姓氏权重: 按真实人口频率排序, 越靠前的姓氏占比越高
_SURNAME_WEIGHTS = [max(1, int(100 - i * 1.0)) for i in range(len(_SURNAMES))]

# 名字尾字性别倾向(用于从通用名库划分男女名, 保证姓名与身份证性别一致)
_MALE_NAME_TAIL = set(
    "强伟杰涛峰鹏飞龙刚勇军明超华东斌洋磊志远博轩豪宇泽辰航浩哲海川波天"
    "成国金鑫彬毅皓宏民胜祥生贵义荣凯泉山林河源光庆元安顺昌德平文武云奕舟"
    "昊阳坤旭睿晨坚卓铭弘谦麟焕滔鸣佑凡才逸霖熙墨健锋腾翔"
)
_FEMALE_NAME_TAIL = set(
    "英兰娟婷静丽艳芳霞玲琳梅雪欣妍悦慧琪萱萌瑶露燕凤花香丹秀淑蕊茜莹玉萍"
    "红珍琴珠蓉妮媛倩婧嫣紫梦馨爱芝芸洁惠月思晓然曦骄娣娥苹蕾薇荷菊竹舒伊"
    "璐璇蓓菱冬雨莲茹晴妹莉菲雯宁杏虹凰仪春彤如韵诺珂娅妤汐"
)

# 按性别划分后的名字池(模块加载时计算一次)
_MALE_GIVEN_2CHAR = [n for n in _GIVEN_2CHAR if n[-1] in _MALE_NAME_TAIL] or _GIVEN_2CHAR
_FEMALE_GIVEN_2CHAR = [n for n in _GIVEN_2CHAR if n[-1] in _FEMALE_NAME_TAIL] or _GIVEN_2CHAR
_MALE_GIVEN_1CHAR = [n for n in _GIVEN_1CHAR if n in _MALE_NAME_TAIL] or _GIVEN_1CHAR
_FEMALE_GIVEN_1CHAR = [n for n in _GIVEN_1CHAR if n in _FEMALE_NAME_TAIL] or _GIVEN_1CHAR

# 最近一次生成姓名的性别(供身份证生成保持性别一致)
_LAST_GENDER = "M"


def gen_chinese_name():
    """生成真实感中文名: 姓氏按频率加权, 名字按性别划分, 2字名约75%"""
    global _LAST_GENDER
    gender = "M" if random.random() < 0.51 else "F"
    _LAST_GENDER = gender

    surname = random.choices(_SURNAMES, weights=_SURNAME_WEIGHTS)[0]
    if random.random() < 0.75:
        pool = _MALE_GIVEN_2CHAR if gender == "M" else _FEMALE_GIVEN_2CHAR
    else:
        pool = _MALE_GIVEN_1CHAR if gender == "M" else _FEMALE_GIVEN_1CHAR
    return surname + random.choice(pool)

# 省份中文名称 -> 省份代码映射 (本地数据库查询归属地用)
PROVINCE_NAME_TO_CODE = {
    "北京": "BJ", "上海": "SH", "天津": "TJ", "重庆": "CQ",
    "广东": "GD", "江苏": "JS", "浙江": "ZJ", "山东": "SD",
    "河南": "HA", "四川": "SC", "湖北": "HB", "湖南": "HN",
    "福建": "FJ", "安徽": "AH", "河北": "HE", "陕西": "SN",
    "辽宁": "LN", "吉林": "JL", "黑龙江": "HL", "江西": "JX",
    "广西": "GX", "云南": "YN", "贵州": "GZ", "山西": "SX",
    "甘肃": "GS", "海南": "HI", "内蒙古": "NM", "新疆": "XJ",
    "宁夏": "NX", "青海": "QH", "西藏": "XZ",
}

# ===================== 手机号号段数据库(内联自 查询归属地.py, 单文件运行) =====================
# 基于 phonenumbers (Google libphonenumber) 真实数据: 7位号段 -> (省份代码, 运营商代码, 城市核心名)
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier
    _PHONE_DB_AVAILABLE = True
except Exception:
    phonenumbers = None
    _PHONE_DB_AVAILABLE = False

_PROVINCE_NAME_TO_CODE = {
    "北京市": "BJ", "天津市": "TJ", "上海市": "SH", "重庆市": "CQ",
    "河北省": "HE", "山西省": "SX", "辽宁省": "LN", "吉林省": "JL", "黑龙江省": "HL",
    "江苏省": "JS", "浙江省": "ZJ", "安徽省": "AH", "福建省": "FJ", "江西省": "JX", "山东省": "SD",
    "河南省": "HA", "湖北省": "HB", "湖南省": "HN", "广东省": "GD", "海南省": "HI",
    "四川省": "SC", "贵州省": "GZ", "云南省": "YN", "陕西省": "SN", "甘肃省": "GS", "青海省": "QH",
    "台湾省": "TW", "内蒙古自治区": "NM", "广西壮族自治区": "GX", "西藏自治区": "XZ",
    "宁夏回族自治区": "NX", "新疆维吾尔自治区": "XJ",
    "香港特别行政区": "HK", "澳门特别行政区": "MO",
    "新疆": "XJ", "内蒙古": "NM", "广西": "GX", "西藏": "XZ",
    "宁夏": "NX", "香港": "HK", "澳门": "MO", "台湾": "TW",
    "河北": "HE", "山西": "SX", "辽宁": "LN", "吉林": "JL", "黑龙江": "HL",
    "江苏": "JS", "浙江": "ZJ", "安徽": "AH", "福建": "FJ", "江西": "JX", "山东": "SD",
    "河南": "HA", "湖北": "HB", "湖南": "HN", "广东": "GD", "海南": "HI",
    "四川": "SC", "贵州": "GZ", "云南": "YN", "陕西": "SN", "甘肃": "GS", "青海": "QH",
    "北京": "BJ", "天津": "TJ", "上海": "SH", "重庆": "CQ",
}

_CARRIER_NAME_TO_CODE = {
    "中国移动": "CMCC",
    "中国联通": "CUCC",
    "中国电信": "CTCC",
}

_MOBILE_3_PREFIXES = {
    "CMCC": ["134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "157", "158", "159", "172", "178", "182", "183", "184", "187", "188", "195", "198"],
    "CUCC": ["130", "131", "132", "145", "155", "156", "166", "171", "175", "176", "185", "186"],
    "CTCC": ["133", "149", "153", "173", "177", "180", "181", "189", "190", "191", "199"],
}

_PREFIX_CACHE = {}
_PROVINCE_PREFIXES = {}

if getattr(sys, 'frozen', False):
    # 打包环境: 预置缓存随包放在 _internal 目录, 优先从那里读取; 新建缓存写到exe同目录
    _CACHE_DIR = os.path.dirname(sys.executable)
    _READ_CACHE_FILE = os.path.join(getattr(sys, '_MEIPASS', ''), "_phone_cache.pkl")
else:
    _CACHE_DIR = os.path.dirname(os.path.abspath(__file__))
    _READ_CACHE_FILE = ""
_CACHE_FILE = os.path.join(_CACHE_DIR, "_phone_cache.pkl")
_CACHE_VERSION = 2


def _norm_city(name):
    """城市名规范化: 去掉"市/地区/自治州/盟"等后缀, 如"唐山市"->"唐山"、"大兴安岭地区"->"大兴安岭" """
    if not name:
        return ""
    for suf in ("特别行政区", "自治州", "自治区", "地区", "盟", "新区", "市", "省"):
        name = name.replace(suf, "")
    return name


def _parse_geo(geo_str):
    if not geo_str:
        return None
    for name, code in _PROVINCE_NAME_TO_CODE.items():
        if name in geo_str:
            return code
    return None


def _parse_city(geo_str, prov_code):
    """从geo字符串解析市名核心(如"河北省唐山市"->"唐山"), 直辖市返回省名本身(如"北京")"""
    if not geo_str or not prov_code:
        return ""
    for name, code in sorted(_PROVINCE_NAME_TO_CODE.items(), key=lambda x: len(x[0]), reverse=True):
        if code == prov_code and name in geo_str:
            rest = geo_str[len(name):]
            if not rest:
                # 直辖市(如"北京市"), 市=省本身
                return _norm_city(name)
            return _norm_city(rest)
    return ""


def _lookup_prefix(p7):
    if p7 in _PREFIX_CACHE:
        return _PREFIX_CACHE[p7]
    try:
        phone = p7 + "0000"
        x = phonenumbers.parse("+86" + phone, "CN")
        geo = geocoder.description_for_number(x, "zh")
        carr = carrier.name_for_number(x, "zh")
        prov = _parse_geo(geo)
        city = _parse_city(geo, prov)
        cc = _CARRIER_NAME_TO_CODE.get(carr)
        if prov and cc:
            _PREFIX_CACHE[p7] = (prov, city, cc)
            return prov, city, cc
    except Exception:
        pass
    _PREFIX_CACHE[p7] = (None, None, None)
    return None, None, None


def _build_cache():
    global _PROVINCE_PREFIXES, _PREFIX_CACHE
    if not _PHONE_DB_AVAILABLE:
        return
    total = sum(len(v) for v in _MOBILE_3_PREFIXES.values()) * 10000
    done = 0
    for cc, prefixes in _MOBILE_3_PREFIXES.items():
        for p3 in prefixes:
            for i in range(10000):
                p7 = f"{p3}{i:04d}"
                prov, city, carr = _lookup_prefix(p7)
                if prov and carr:
                    if prov not in _PROVINCE_PREFIXES:
                        _PROVINCE_PREFIXES[prov] = []
                    _PROVINCE_PREFIXES[prov].append((p7, carr, city))
                done += 1
    try:
        with open(_CACHE_FILE, "wb") as f:
            pickle.dump((_CACHE_VERSION, _PROVINCE_PREFIXES, _PREFIX_CACHE), f)
    except Exception:
        pass


def _load_cache():
    global _PROVINCE_PREFIXES, _PREFIX_CACHE
    # 优先读随包预置缓存(_internal), 其次读exe同目录
    _paths = []
    if _READ_CACHE_FILE and os.path.exists(_READ_CACHE_FILE):
        _paths.append(_READ_CACHE_FILE)
    if os.path.exists(_CACHE_FILE):
        _paths.append(_CACHE_FILE)
    for _p in _paths:
        try:
            with open(_p, "rb") as f:
                data = pickle.load(f)
            if isinstance(data, tuple) and len(data) == 3 and data[0] == _CACHE_VERSION:
                _PROVINCE_PREFIXES, _PREFIX_CACHE = data[1], data[2]
            else:
                _PROVINCE_PREFIXES = {}
                _PREFIX_CACHE = {}
                return False
            if _PROVINCE_PREFIXES:
                return True
        except Exception:
            pass
    return False


_CACHE_LOCK = threading.Lock()

def _ensure_cache():
    if _PROVINCE_PREFIXES:
        return
    with _CACHE_LOCK:
        if _PROVINCE_PREFIXES:
            return
        if not _load_cache():
            _build_cache()


def lookup_phone_local(phone):
    """查询手机号归属地, 使用 phonenumbers 真实数据, 返回(省份代码, 运营商代码)"""
    if not phone or len(phone) != 11:
        return None, None
    prov, _, carr = _lookup_prefix(phone[:7])
    return prov, carr


def _gen_phone_from(pool):
    """从号段池随机生成一个手机号, 返回(手机号, 运营商代码, 城市核心名)"""
    p7, carrier, city = random.choice(pool)
    suffix4 = ''.join(str(random.randint(0, 9)) for _ in range(4))
    return p7 + suffix4, carrier, city


def gen_phone_by_province(prov_code):
    """根据省份代码生成手机号, 返回(手机号, 运营商代码, 城市核心名)或(None,None,None)"""
    _ensure_cache()
    candidates = _PROVINCE_PREFIXES.get(prov_code, [])
    if not candidates:
        return None, None, None
    return _gen_phone_from(candidates)


def gen_phone_by_city(prov_code, city_core):
    """根据省份+城市生成手机号, 返回(手机号, 运营商代码, 城市核心名); 城市无号段时降级到省份"""
    _ensure_cache()
    candidates = _PROVINCE_PREFIXES.get(prov_code, [])
    if not candidates:
        return None, None, None
    if city_core:
        # 精确匹配优先, 失败则包含/前缀模糊匹配(提高"市一致"命中率)
        city_list = [c for c in candidates if c[2] == city_core]
        if not city_list:
            city_list = [c for c in candidates if c[2] and (city_core in c[2] or c[2] in city_core)]
        if city_list:
            return _gen_phone_from(city_list)
    return _gen_phone_from(candidates)


def get_prefix_count():
    _ensure_cache()
    return len([v for v in _PREFIX_CACHE.values() if v[0]])


def get_all_provinces():
    _ensure_cache()
    provs = set(prov for prov, _, _ in _PREFIX_CACHE.values() if prov)
    return sorted(provs)
# ===================== 手机号号段数据库结束 =====================

_PHONE_LOCATION_CACHE = {}
_PHONE_LOCATION_LOCK = threading.Lock()

# 已生成身份证去重集合(线程安全, 持久化到文件, 跨批次/跨重启不重复)
_GENERATED_IDCARDS = set()
_GENERATED_IDCARDS_LOCK = threading.Lock()
_GENERATED_IDCARDS_MAX = 500000  # 上限放大(配合持久化, 大幅降低重复概率)
_IDCARD_CACHE_FILE = os.path.join(APP_DIR, "_idcard_cache.pkl")
_IDCARD_CACHE_SAVE_EVERY = 100  # 每新增100个身份证落盘一次(防崩溃丢太多)


def _save_idcard_cache(snapshot=None):
    """把去重集合原子落盘(跨进程文件锁保护, 多实例并发安全)"""
    try:
        if snapshot is None:
            with _GENERATED_IDCARDS_LOCK:
                snapshot = set(_GENERATED_IDCARDS)
        lock_path = _IDCARD_CACHE_FILE + ".lock"
        with open(lock_path, "a") as lock_f:
            _file_lock(lock_f)
            try:
                tmp = _IDCARD_CACHE_FILE + ".tmp"
                with open(tmp, "wb") as f:
                    pickle.dump(snapshot, f, protocol=4)
                os.replace(tmp, _IDCARD_CACHE_FILE)
            finally:
                _file_unlock(lock_f)
    except Exception:
        pass


def _load_idcard_cache():
    """启动时加载历史身份证缓存, 避免跨批次/跨重启重复"""
    global _GENERATED_IDCARDS
    try:
        if os.path.exists(_IDCARD_CACHE_FILE):
            with open(_IDCARD_CACHE_FILE, "rb") as f:
                data = pickle.load(f)
            if isinstance(data, set):
                with _GENERATED_IDCARDS_LOCK:
                    _GENERATED_IDCARDS = data
    except Exception:
        pass


def _register_idcard(card):
    """登记已生成的身份证号, 定时落盘, 防止跨重启重复"""
    global _GENERATED_IDCARDS
    should_save = False
    with _GENERATED_IDCARDS_LOCK:
        if card in _GENERATED_IDCARDS:
            return
        if len(_GENERATED_IDCARDS) >= _GENERATED_IDCARDS_MAX:
            # 容量满: 先把含当前卡号的完整历史落盘, 再清空内存继续(历史已持久化, 重启不重复)
            _GENERATED_IDCARDS.add(card)
            _save_idcard_cache(set(_GENERATED_IDCARDS))
            _GENERATED_IDCARDS = set()
            return
        _GENERATED_IDCARDS.add(card)
        if len(_GENERATED_IDCARDS) % _IDCARD_CACHE_SAVE_EVERY == 0:
            should_save = True
    if should_save:
        _save_idcard_cache()


_load_idcard_cache()

_IP_PROVINCE_CACHE = {}

_IP_API_CALLS = []
_IP_LOOKUP_FAIL_COUNT = 0
_IP_LOOKUP_FAIL_NOTIFIED = False

_EN_PROVINCE_TO_CODE = {
    "Beijing": "BJ", "Tianjin": "TJ", "Shanghai": "SH", "Chongqing": "CQ",
    "Guangdong": "GD", "Jiangsu": "JS", "Zhejiang": "ZJ", "Shandong": "SD",
    "Henan": "HA", "Sichuan": "SC", "Hubei": "HB", "Hunan": "HN",
    "Fujian": "FJ", "Anhui": "AH", "Hebei": "HE", "Shaanxi": "SN",
    "Liaoning": "LN", "Jilin": "JL", "Heilongjiang": "HL", "Jiangxi": "JX",
    "Guangxi": "GX", "Yunnan": "YN", "Guizhou": "GZ", "Shanxi": "SX",
    "Gansu": "GS", "Hainan": "HI", "Neimeng": "NM", "Inner Mongolia": "NM",
    "Xinjiang": "XJ", "Ningxia": "NX", "Qinghai": "QH", "Tibet": "XZ",
    "Xizang": "XZ", "FuJian": "FJ",
}

_CN_REGION_TO_CODE = {
    "北京市": "BJ", "上海市": "SH", "天津市": "TJ", "重庆市": "CQ",
    "广东省": "GD", "江苏省": "JS", "浙江省": "ZJ", "山东省": "SD",
    "河南省": "HA", "四川省": "SC", "湖北省": "HB", "湖南省": "HN",
    "福建省": "FJ", "安徽省": "AH", "河北省": "HE", "陕西省": "SN",
    "辽宁省": "LN", "吉林省": "JL", "黑龙江省": "HL", "江西省": "JX",
    "广西壮族自治区": "GX", "云南省": "YN", "贵州省": "GZ", "山西省": "SX",
    "甘肃省": "GS", "海南省": "HI", "内蒙古自治区": "NM", "新疆维吾尔自治区": "XJ",
    "宁夏回族自治区": "NX", "青海省": "QH", "西藏自治区": "XZ",
}

# 英文城市名 -> 中文 (ip-api 返回英文拼音, 翻译后手机号/身份证才能"市一致"; 重名城市用 省代码_英文 消歧)
_CITY_EN_TO_CN = {
    "Beijing": "北京", "Shanghai": "上海", "Tianjin": "天津", "Chongqing": "重庆",
    "Shijiazhuang": "石家庄", "Tangshan": "唐山", "Qinhuangdao": "秦皇岛", "Handan": "邯郸",
    "Xingtai": "邢台", "Baoding": "保定", "Zhangjiakou": "张家口", "Chengde": "承德",
    "Cangzhou": "沧州", "Langfang": "廊坊", "Hengshui": "衡水",
    "Taiyuan": "太原", "Datong": "大同", "Yangquan": "阳泉", "Changzhi": "长治",
    "Jincheng": "晋城", "Shuozhou": "朔州", "Jinzhong": "晋中", "Yuncheng": "运城",
    "Xinzhou": "忻州", "Linfen": "临汾", "Lvliang": "吕梁",
    "Hohhot": "呼和浩特", "Baotou": "包头", "Wuhai": "乌海", "Chifeng": "赤峰",
    "Tongliao": "通辽", "Ordos": "鄂尔多斯", "Hulunbuir": "呼伦贝尔",
    "Bayannur": "巴彦淖尔", "Ulanqab": "乌兰察布",
    "Shenyang": "沈阳", "Dalian": "大连", "Anshan": "鞍山", "Fushun": "抚顺",
    "Benxi": "本溪", "Dandong": "丹东", "Jinzhou": "锦州", "Yingkou": "营口",
    "Fuxin": "阜新", "Liaoyang": "辽阳", "Panjin": "盘锦", "Tieling": "铁岭",
    "Chaoyang": "朝阳", "Huludao": "葫芦岛",
    "Changchun": "长春", "Jilin": "吉林", "Siping": "四平", "Liaoyuan": "辽源",
    "Tonghua": "通化", "Baishan": "白山", "Songyuan": "松原", "Baicheng": "白城",
    "Yanbian": "延边",
    "Harbin": "哈尔滨", "Qiqihar": "齐齐哈尔", "Jixi": "鸡西", "Hegang": "鹤岗",
    "Shuangyashan": "双鸭山", "Daqing": "大庆", "Yichun": "伊春", "Jiamusi": "佳木斯",
    "Qitaihe": "七台河", "Mudanjiang": "牡丹江", "Heihe": "黑河", "Suihua": "绥化",
    "Nanjing": "南京", "Wuxi": "无锡", "Xuzhou": "徐州", "Changzhou": "常州",
    "Suzhou": "苏州", "Nantong": "南通", "Lianyungang": "连云港", "Huai'an": "淮安",
    "Huaian": "淮安", "Yancheng": "盐城", "Yangzhou": "扬州", "Zhenjiang": "镇江",
    "Suqian": "宿迁",
    "Hangzhou": "杭州", "Ningbo": "宁波", "Wenzhou": "温州", "Jiaxing": "嘉兴",
    "Huzhou": "湖州", "Shaoxing": "绍兴", "Jinhua": "金华", "Quzhou": "衢州",
    "Zhoushan": "舟山", "Lishui": "丽水",
    "Hefei": "合肥", "Wuhu": "芜湖", "Bengbu": "蚌埠", "Huainan": "淮南",
    "Ma'anshan": "马鞍山", "Huaibei": "淮北", "Tongling": "铜陵", "Anqing": "安庆",
    "Huangshan": "黄山", "Chuzhou": "滁州", "Fuyang": "阜阳", "Lu'an": "六安",
    "Luan": "六安", "Bozhou": "亳州", "Chizhou": "池州", "Xuancheng": "宣城",
    "Fuzhou": "福州", "Xiamen": "厦门", "Putian": "莆田", "Sanming": "三明",
    "Quanzhou": "泉州", "Zhangzhou": "漳州", "Nanping": "南平", "Longyan": "龙岩",
    "Ningde": "宁德",
    "Nanchang": "南昌", "Jingdezhen": "景德镇", "Pingxiang": "萍乡", "Jiujiang": "九江",
    "Xinyu": "新余", "Yingtan": "鹰潭", "Ganzhou": "赣州", "Ji'an": "吉安",
    "Jian": "吉安", "Yichun": "宜春", "Shangrao": "上饶",
    "Jinan": "济南", "Qingdao": "青岛", "Zibo": "淄博", "Zaozhuang": "枣庄",
    "Dongying": "东营", "Yantai": "烟台", "Weifang": "潍坊", "Jining": "济宁",
    "Tai'an": "泰安", "Tian": "泰安", "Weihai": "威海", "Rizhao": "日照",
    "Linyi": "临沂", "Dezhou": "德州", "Liaocheng": "聊城", "Binzhou": "滨州",
    "Heze": "菏泽",
    "Zhengzhou": "郑州", "Kaifeng": "开封", "Luoyang": "洛阳", "Pingdingshan": "平顶山",
    "Anyang": "安阳", "Hebi": "鹤壁", "Xinxiang": "新乡", "Jiaozuo": "焦作",
    "Puyang": "濮阳", "Xuchang": "许昌", "Luohe": "漯河", "Sanmenxia": "三门峡",
    "Nanyang": "南阳", "Shangqiu": "商丘", "Xinyang": "信阳", "Zhoukou": "周口",
    "Zhumadian": "驻马店",
    "Wuhan": "武汉", "Huangshi": "黄石", "Shiyan": "十堰", "Yichang": "宜昌",
    "Xiangyang": "襄阳", "Ezhou": "鄂州", "Jingmen": "荆门", "Xiaogan": "孝感",
    "Jingzhou": "荆州", "Huanggang": "黄冈", "Xianning": "咸宁", "Suizhou": "随州",
    "Enshi": "恩施",
    "Changsha": "长沙", "Zhuzhou": "株洲", "Xiangtan": "湘潭", "Hengyang": "衡阳",
    "Shaoyang": "邵阳", "Yueyang": "岳阳", "Changde": "常德", "Zhangjiajie": "张家界",
    "Yiyang": "益阳", "Chenzhou": "郴州", "Yongzhou": "永州", "Huaihua": "怀化",
    "Loudi": "娄底",
    "Guangzhou": "广州", "Shaoguan": "韶关", "Shenzhen": "深圳", "Zhuhai": "珠海",
    "Shantou": "汕头", "Foshan": "佛山", "Jiangmen": "江门", "Zhanjiang": "湛江",
    "Maoming": "茂名", "Zhaoqing": "肇庆", "Huizhou": "惠州", "Meizhou": "梅州",
    "Shanwei": "汕尾", "Heyuan": "河源", "Yangjiang": "阳江", "Qingyuan": "清远",
    "Dongguan": "东莞", "Zhongshan": "中山", "Chaozhou": "潮州", "Jieyang": "揭阳",
    "Yunfu": "云浮",
    "Nanning": "南宁", "Liuzhou": "柳州", "Guilin": "桂林", "Wuzhou": "梧州",
    "Beihai": "北海", "Fangchenggang": "防城港", "Qinzhou": "钦州", "Guigang": "贵港",
    "Baise": "百色", "Hezhou": "贺州", "Hechi": "河池", "Laibin": "来宾",
    "Chongzuo": "崇左",
    "Haikou": "海口", "Sanya": "三亚", "Sansha": "三沙", "Danzhou": "儋州",
    "Chengdu": "成都", "Zigong": "自贡", "Panzhihua": "攀枝花", "Luzhou": "泸州",
    "Deyang": "德阳", "Mianyang": "绵阳", "Guangyuan": "广元", "Suining": "遂宁",
    "Neijiang": "内江", "Leshan": "乐山", "Nanchong": "南充", "Meishan": "眉山",
    "Yibin": "宜宾", "Guang'an": "广安", "Dazhou": "达州", "Ya'an": "雅安",
    "Yaan": "雅安", "Bazhong": "巴中", "Ziyang": "资阳", "Aba": "阿坝",
    "Ganzi": "甘孜", "Liangshan": "凉山",
    "Guiyang": "贵阳", "Liupanshui": "六盘水", "Zunyi": "遵义", "Anshun": "安顺",
    "Bijie": "毕节", "Tongren": "铜仁",
    "Kunming": "昆明", "Qujing": "曲靖", "Yuxi": "玉溪", "Baoshan": "保山",
    "Zhaotong": "昭通", "Lijiang": "丽江", "Pu'er": "普洱", "Lincang": "临沧",
    "Chuxiong": "楚雄", "Honghe": "红河", "Wenshan": "文山",
    "Xishuangbanna": "西双版纳", "Dehong": "德宏", "Nujiang": "怒江", "Diqing": "迪庆",
    "Lhasa": "拉萨", "Shigatse": "日喀则", "Chamdo": "昌都", "Nyingchi": "林芝",
    "Shannan": "山南", "Nagqu": "那曲", "Ngari": "阿里",
    "Xi'an": "西安", "Xian": "西安", "Tongchuan": "铜川", "Baoji": "宝鸡",
    "Xianyang": "咸阳", "Weinan": "渭南", "Yan'an": "延安", "Yanan": "延安",
    "Hanzhong": "汉中", "Ankang": "安康", "Shangluo": "商洛",
    "Lanzhou": "兰州", "Jiayuguan": "嘉峪关", "Jinchang": "金昌", "Baiyin": "白银",
    "Tianshui": "天水", "Wuwei": "武威", "Zhangye": "张掖", "Pingliang": "平凉",
    "Jiuquan": "酒泉", "Qingyang": "庆阳", "Dingxi": "定西", "Longnan": "陇南",
    "Linxia": "临夏", "Gannan": "甘南",
    "Xining": "西宁", "Haidong": "海东", "Haibei": "海北", "Huangnan": "黄南",
    "Guoluo": "果洛", "Yushu": "玉树", "Haixi": "海西",
    "Yinchuan": "银川", "Shizuishan": "石嘴山", "Wuzhong": "吴忠", "Guyuan": "固原",
    "Zhongwei": "中卫",
    "Urumqi": "乌鲁木齐", "Karamay": "克拉玛依", "Turpan": "吐鲁番", "Hami": "哈密",
    "Changji": "昌吉", "Bortala": "博尔塔拉", "Bayingolin": "巴音郭楞",
    "Kizilsu": "克孜勒苏", "Kashi": "喀什", "Hotan": "和田", "Ili": "伊犁",
    "Tacheng": "塔城", "Altay": "阿勒泰",
    # 重名城市: 用 省代码_英文 消歧
    "ZJ_Taizhou": "台州", "JS_Taizhou": "泰州",
    "SN_Yulin": "榆林", "GX_Yulin": "玉林",
    "JL_Jilin": "吉林",
}


def _is_chinese(s):
    """判断字符串是否包含中文字符"""
    return any('\u4e00' <= ch <= '\u9fff' for ch in s)


def _translate_city_en(prov_code, city_en):
    """ip-api 英文城市名翻译成中文(提高手机号/身份证"市一致"命中率); 未收录返回空=明确省一致"""
    if not city_en:
        return ""
    c = _CITY_EN_TO_CN.get(f"{prov_code}_{city_en}") or _CITY_EN_TO_CN.get(city_en)
    return c or ""


# 运营商 -> 手机号段 (同一号段只归属一家运营商)
_CARRIER_PREFIX_MAP = {
    "CMCC": ["134", "135", "136", "137", "138", "139", "147", "150", "151",
             "152", "157", "158", "159", "178", "182", "183", "184", "187", "188"],
    "CUCC": ["130", "131", "132", "145", "155", "156", "166", "175", "176", "185", "186"],
    "CTCC": ["133", "149", "153", "173", "177", "180", "181", "189"],
    "CBN": ["192"],
}

# 运营商中文名 -> 代码映射
_CARRIER_NAME_TO_CODE = {
    "移动": "CMCC", "联通": "CUCC", "电信": "CTCC", "广电": "CBN",
    "中国移动": "CMCC", "中国联通": "CUCC", "中国电信": "CTCC", "中国广电": "CBN",
}

def query_phone_location(phone):
    """查询手机号归属地: 仅使用本地数据库, 返回(省份代码, 运营商代码)或None"""
    if not phone or len(phone) != 11:
        return None, None

    cache_key = phone[:7]

    with _PHONE_LOCATION_LOCK:
        if cache_key in _PHONE_LOCATION_CACHE:
            return _PHONE_LOCATION_CACHE[cache_key]

    if _PHONE_DB_AVAILABLE:
        prov_code, carrier_code = lookup_phone_local(phone)
        if prov_code:
            with _PHONE_LOCATION_LOCK:
                _PHONE_LOCATION_CACHE[cache_key] = (prov_code, carrier_code)
            return prov_code, carrier_code

    return None, None

def _is_fake_suffix(s):
    """过滤明显假号特征: 4连号、4位顺子等"""
    for i in range(5):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3]:
            return True
    for i in range(5):
        seg = s[i:i + 4]
        if seg in ("0123", "1234", "2345", "3456", "4567", "5678", "6789",
                   "9876", "8765", "7654", "6543", "5432", "4321", "3210"):
            return True
    return False


def _gen_phone_suffix():
    """生成8位手机号后段, 规避明显假号"""
    for _ in range(30):
        s = "".join(str(random.randint(0, 9)) for _ in range(8))
        if not _is_fake_suffix(s):
            return s
    return "".join(str(random.randint(0, 9)) for _ in range(8))


def gen_random_phone():
    """生成随机11位手机号 (运营商号段 + 过滤假号的后8位)"""
    carrier = random.choice(list(_CARRIER_PREFIX_MAP.keys()))
    prefix3 = random.choice(_CARRIER_PREFIX_MAP[carrier])
    return prefix3 + _gen_phone_suffix()


def _prefix_to_carrier(prefix3):
    """根据3位号段推断运营商"""
    for carrier, prefixes in _CARRIER_PREFIX_MAP.items():
        if prefix3 in prefixes:
            return carrier
    return None

def gen_phone_and_location():
    """生成手机号并查归属地, 仅使用本地数据库, 返回(手机号, 省份代码, 城市核心名, 运营商代码)"""
    if _PHONE_DB_AVAILABLE:
        for _ in range(10):
            prov_code = random.choice(list(PROVINCE_IP_RANGES.keys()))
            phone, carrier_code, city_core = gen_phone_by_province(prov_code)
            if phone and prov_code in PROVINCE_IP_RANGES:
                return phone, prov_code, city_core, carrier_code
    phone = gen_random_phone()
    prov_code = random.choice(list(PROVINCE_IP_RANGES.keys()))
    return phone, prov_code, "", _prefix_to_carrier(phone[:3])

def gen_phone_by_province_any(prov_code, city_core=""):
    """按指定省份/城市生成手机号: 优先本地数据库取号, 失败则用随机号段(省份保持不变)"""
    if _PHONE_DB_AVAILABLE:
        for _ in range(10):
            phone, carrier_code, city = gen_phone_by_city(prov_code, city_core)
            if phone:
                return phone, carrier_code, city
    phone = gen_random_phone()
    return phone, _prefix_to_carrier(phone[:3]), city_core or ""


def _same_city(a, b):
    """判断两个城市核心名是否相同(已规范化, 支持互相包含的模糊比较)"""
    if not a or not b:
        return False
    a = _norm_city(a)
    b = _norm_city(b)
    return a == b or (a in b or b in a)


def gen_phone_for_ip(prov_code, ip_city):
    """生成与IP省市匹配的手机号, 返回(phone, carrier_code, phone_city, city_matched):
    - 优先精确匹配IP所在市(市一致); 手机号库无该市号段时降级到省内随机(省一致)
    - city_matched=True 表示手机号所在市与IP所在市一致(市一致)"""
    if _PHONE_DB_AVAILABLE:
        for _ in range(8):
            phone, carrier_code, phone_city = gen_phone_by_city(prov_code, ip_city)
            if not phone:
                break
            if _same_city(phone_city, ip_city):
                return phone, carrier_code, phone_city, True
        # 全市匹配不到 → 省内随机(省一致)
        for _ in range(8):
            phone, carrier_code, phone_city = gen_phone_by_province(prov_code)
            if phone:
                return phone, carrier_code, phone_city, False
    phone, carrier_code, phone_city = gen_phone_by_province_any(prov_code, ip_city)
    return phone, carrier_code, phone_city, _same_city(phone_city, ip_city)

def _norm_city(name):
    """城市名规范化: 去掉"市/地区/自治州/盟"等后缀, 如"唐山市"->"唐山"、"大兴安岭地区"->"大兴安岭" """
    if not name:
        return ""
    for suf in ("特别行政区", "自治州", "自治区", "地区", "盟", "新区", "市", "省"):
        name = name.replace(suf, "")
    return name


def _match_province(region_str, isp_str=""):
    """从region或isp字段匹配省份代码, 支持全名/缩写/英文"""
    if not region_str:
        return None
    region_str = str(region_str)
    isp_str = str(isp_str) if isp_str else ""
    
    # 1. 精确匹配 (CN_REGION_TO_CODE 有全名)
    prov_code = _CN_REGION_TO_CODE.get(region_str)
    if prov_code:
        return prov_code
    
    # 2. 包含匹配 (region是"辽宁", 字典有"辽宁省")
    for cn_name, code in PROVINCE_NAME_TO_CODE.items():
        if cn_name in region_str or region_str in cn_name:
            return code
    
    # 3. ISP字段匹配
    if isp_str:
        for cn_name, code in PROVINCE_NAME_TO_CODE.items():
            if cn_name in isp_str:
                return code
    
    # 4. 英文匹配
    for eng, code in _EN_PROVINCE_TO_CODE.items():
        if eng.lower() in region_str.lower() or eng.lower() in isp_str.lower():
            return code
    
    return None

_IP_LOOKUP_LOCK = threading.Lock()


def _lookup_ip_baidu(ip):
    """百度opendata查询IP归属地(国内稳定源), 返回(省份代码, 城市核心名) 或 (None, "").
    百度返回形如"广东省江门市 移动", 省份+城市在同一字段; 剥离省份名提取城市;
    直辖市返回"北京市"或"北京市北京市", 城市=省本身. 不占ip-api限速配额"""
    try:
        url = f"http://opendata.baidu.com/api.php?query={ip}&co=&resource_id=6006&oe=utf8"
        r = requests.get(url, timeout=3,
                         headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
        if r.status_code != 200:
            return None, ""
        data = r.json()
        items = (data.get("data") or []) if isinstance(data, dict) else []
        if not items:
            return None, ""
        location = items[0].get("location", "") or ""
        # 形如 "广东省江门市 移动" / "北京市 联通" / "北京市北京市 联通"
        parts = [p for p in location.split() if p]
        if not parts:
            return None, ""
        full = parts[0]  # 省份+城市可能在同一字段, 不能只把parts[0]当省、parts[1]当市
        # 按最长省份名匹配, 找到省份代码及省份名
        prov_code = None
        prov_name = ""
        for name, code in sorted(PROVINCE_NAME_TO_CODE.items(), key=lambda x: len(x[0]), reverse=True):
            if name in full:
                prov_code = code
                prov_name = name
                break
        if not prov_code:
            return None, ""
        # 城市 = 省份名之后的部分; 直辖市(如"北京市"无剩余)城市取省本身
        city_raw = full[len(prov_name):] if full.startswith(prov_name) else full.replace(prov_name, "", 1)
        city = _norm_city(city_raw)
        if prov_code in ("BJ", "SH", "TJ", "CQ"):
            # 百度有时返回"北京市北京市", 去重后取"北京"
            while len(city) >= 4 and city[:2] == city[2:4]:
                city = city[:2]
            if not city:
                city = _norm_city(prov_name)
        return prov_code, city
    except Exception:
        return None, ""

def lookup_ip_province(ip):
    """查询IP归属地, 返回(省份代码, 城市核心名) 或 (None, "").
    优先百度opendata(国内稳定源, 结果与主流查询一致), 失败降级ip-api.com(单次3秒快速失败).
    双源都失败才返回None. 多线程安全: 限速计数/缓存读写加锁, 等待放锁外"""
    global _IP_LOOKUP_FAIL_COUNT, _IP_LOOKUP_FAIL_NOTIFIED

    if not ip:
        with _IP_LOOKUP_LOCK:
            _IP_LOOKUP_FAIL_COUNT += 1
        return None, ""

    wait = 0
    with _IP_LOOKUP_LOCK:
        if ip in _IP_PROVINCE_CACHE:
            _IP_LOOKUP_FAIL_COUNT = 0
            return _IP_PROVINCE_CACHE[ip]
        now = time.time()
        _IP_API_CALLS[:] = [t for t in _IP_API_CALLS if now - t < 60]
        if len(_IP_API_CALLS) >= 44:
            oldest = _IP_API_CALLS[0]
            wait = max(1, 60 - (now - oldest) + 1)

    if wait:
        time.sleep(wait)

    last_error = ""
    # ① 百度opendata(国内稳定源, 优先, 且与主流IP查询结果一致)
    try:
        prov_code, city_core = _lookup_ip_baidu(ip)
        if prov_code:
            with _IP_LOOKUP_LOCK:
                _IP_PROVINCE_CACHE[ip] = (prov_code, city_core)
                _IP_LOOKUP_FAIL_COUNT = 0
                _IP_LOOKUP_FAIL_NOTIFIED = False
            return prov_code, city_core
    except Exception as e:
        last_error = str(e)[:50]

    # ② 百度失败 → ip-api(单次3秒快速失败); 格式与官方一致: /json/{ip}?lang=zh-CN&fields=...
    try:
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url,
                       params={"lang": "zh-CN", "fields": "status,message,regionName,city,isp,country,query"},
                       timeout=3)
        if r.status_code == 200:
            data = r.json()
            with _IP_LOOKUP_LOCK:
                _IP_API_CALLS.append(time.time())

            # 官方接口: status=fail(如无效IP/超配额)时直接丢弃, 与ip-api示例脚本一致
            if data.get("status") != "success":
                last_error = "ip-api fail: " + str(data.get("message", ""))[:40]
            else:
                region = data.get("regionName", "")
                country = data.get("country", "")
                isp = data.get("isp", "")
                city_raw = data.get("city", "") or ""
                city_core = _norm_city(city_raw)

                prov_code = _match_province(region, isp)
                if prov_code:
                    # ip-api 部分城市返回英文拼音, 翻译成中文(提高手机号/身份证"市一致"命中率); 未收录置空=明确省一致
                    if city_core and not _is_chinese(city_core):
                        city_core = _translate_city_en(prov_code, city_core)
                    with _IP_LOOKUP_LOCK:
                        _IP_PROVINCE_CACHE[ip] = (prov_code, city_core)
                        _IP_LOOKUP_FAIL_COUNT = 0
                        _IP_LOOKUP_FAIL_NOTIFIED = False
                    return prov_code, city_core

    except requests.exceptions.Timeout:
        last_error = "请求超时"
    except requests.exceptions.ConnectionError:
        last_error = "连接失败"
    except Exception as e:
        last_error = str(e)[:50]

    # 双源都失败, 返回 None 由调用方决定是否降级模拟IP
    with _IP_LOOKUP_LOCK:
        _IP_LOOKUP_FAIL_COUNT += 1
    return None, ""


_MY_IP_LOCK = threading.Lock()
_MY_IP_INFO = None  # {"ip":..., "prov":..., "city":..., "carrier":...}

def query_my_ip_info():
    """获取本机真实出口IP及归属地(省/市/运营商), 全局只查一次并缓存.
    无代理模式下用于按真实IP归属地生成同省市手机号/身份证(优先市一致).
    返回 dict 或 None(查询失败/非中国IP时降级随机)"""
    global _MY_IP_INFO
    if _MY_IP_INFO:
        return _MY_IP_INFO
    with _MY_IP_LOCK:
        if _MY_IP_INFO:
            return _MY_IP_INFO
        try:
            r = requests.get("http://ip-api.com/json/",
                             params={"lang": "zh-CN",
                                     "fields": "status,query,regionName,city,isp,org,country"},
                             timeout=10)
            data = r.json()
            if data.get("status") == "success":
                ip = data.get("query", "")
                country = data.get("country", "")
                region = data.get("regionName", "")
                isp = (str(data.get("isp", "")) + " " + str(data.get("org", "")))
                prov_code = _match_province(region, isp)
                city_core = _norm_city(data.get("city", "") or "")
                carrier_code = ""
                for cn, code in (("中国移动", "CMCC"), ("中国联通", "CUCC"),
                                 ("中国电信", "CTCC"), ("广电", "CBN")):
                    if cn in isp:
                        carrier_code = code
                        break
                if ip and prov_code and country == "中国":
                    _MY_IP_INFO = {"ip": ip, "prov": prov_code,
                                   "city": city_core, "carrier": carrier_code}
        except Exception:
            pass
        return _MY_IP_INFO


def gen_verified_fake_ip(prov_code="", carrier_code="", max_try=6):
    """虚拟IP生成(IP优先, 保证手机号/IP/身份证三地一致):
    - 从真实运营商网段随机生成IP → 实时查真实省市(优先百度0.1s, 失败降级ip-api)
    - 返回 (fake_ip, prov_code, city_core, carrier_code); 省份/城市即IP的真实归属,
      手机号/身份证按该省市生成即可保证三者地区一致
    - 指定prov_code时强制IP必须属于该省(不一致继续换); 全部失败返回(fake_ip,"","",carrier)由调用方兜底"""
    for _ in range(max_try):
        pc = random.choice(list(PROVINCE_IP_RANGES.keys())) if not prov_code else prov_code
        probe = create_new_device(province_code=pc, carrier_code=carrier_code)
        ip = probe.fake_ip
        p, city = _lookup_ip_baidu(ip)
        if not p:
            p, city = lookup_ip_province(ip)
        if p:
            if prov_code and p != prov_code:
                continue
            return ip, p, city, probe.ip_carrier
    pc = random.choice(list(PROVINCE_IP_RANGES.keys())) if not prov_code else prov_code
    probe = create_new_device(province_code=pc, carrier_code=carrier_code)
    return probe.fake_ip, "", "", probe.ip_carrier

def infer_province_from_phone(phone):
    """从手机号推断省份 (使用本地数据库)"""
    if not phone or len(phone) < 7:
        return None
    prov_code, _ = query_phone_location(phone)
    return prov_code

def infer_location_from_phone(phone):
    """从手机号推断省份和运营商, 返回(prov_code, carrier_code)"""
    if not phone or len(phone) < 7:
        return None, None
    return query_phone_location(phone)

# =====================【全局常量】=====================
APP_VERSION = "6.6v"  # 当前软件版本号, 打包后便于确认运行版本
DOMAIN = "cs.cqtyzq.com"
URL_INDEX = f"https://{DOMAIN}/h5/1.html"
URL_REG_BASE = f"https://{DOMAIN}/?s=/ApiIndex/regsubnew&aid=1&platform=h5&pid=0&scene=1001"
URL_REG_WARM  = f"https://{DOMAIN}/?s=/ApiIndex/reg&aid=1&platform=h5&pid=0&scene=1001"
URL_LOGIN = f"https://{DOMAIN}/?s=/ApiIndex/loginsub&aid=1&platform=h5&pid=0&scene=1001"
URL_LOGIN_WARM = f"https://{DOMAIN}/?s=/ApiIndex/login&aid=1&platform=h5&pid=0&scene=1001"
URL_SIGN = f"https://{DOMAIN}/?s=/ApiSign/signin&aid=1&platform=h5&sid=SID_PLACEHOLDER&pid=0&scene=1001"
URL_SIGN_WARM = f"https://{DOMAIN}/?s=/ApiSign/index&aid=1&platform=h5&pid=0&scene=1001"


def _url_with_session(url, session):
    """对齐真实前端请求格式: URL query 带上 session_id(与Cookie一致), 0流量成本"""
    try:
        sid = session.cookies.get_dict().get("session_id", "")
    except Exception:
        sid = ""
    return url + ("&session_id=" + sid if sid else "")


# 路径配置 - 数据目录放到 EXE 同目录(打包后不被 _internal 覆盖, 方便查找)
BASE_FOLDER = os.path.join(APP_DIR, "统一出行数据")
REG_SUCCESS_FOLDER = os.path.join(BASE_FOLDER, "统一出行注册成功")
REG_FAIL_FOLDER = os.path.join(BASE_FOLDER, "统一出行注册失败")
REG_SIGN_FOLDER = os.path.join(BASE_FOLDER, "统一出行注册成功签到专用")
SIGN_LOG_FOLDER = os.path.join(BASE_FOLDER, "统一出行签到日志")
CONFIG_FILE = os.path.join(BASE_FOLDER, "config.json")
CRASH_LOG = os.path.join(BASE_FOLDER, "崩溃日志.txt")   # 软件异常记录, 便于排查且不影响运行

def _write_crash_log(exc_type, exc_value, exc_tb):
    """异常写崩溃日志(不弹窗不退出)"""
    try:
        import traceback
        tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(CRASH_LOG, "a", encoding="utf-8") as f:
            f.write(f"\n[{ts}] {tb}\n{'=' * 60}\n")
    except Exception:
        pass

# 网络参数
HTTP_RETRY = 2
TIMEOUT_SEC = 15
CONNECT_TIMEOUT = 8
MAX_LOG_LINES = 5000
CONTINUOUS_FAIL_THRESHOLD = 6

TASK_REGISTER = "register"          # 注册+签到
TASK_REGISTER_ONLY = "register_only"  # 仅注册, 不签到
TASK_SIGN = "sign"

# ===================== 豪猪接码配置 =====================
HAOZHUMA_API = "http://api.haozhuma.com/sms"
HAOZHUMA_USER = ""
HAOZHUMA_PASS = ""
HAOZHUMA_SID = ""
HAOZHUMA_COUNTRY_CODE = "CN"
HAOZHUMA_AUTHOR = "sjxh1122"
HAOZHUMA_ASCRIPTION = ""

_haozhuma_token = ""
_haozhuma_logged_in = False

# 确保目录存在
for folder in [BASE_FOLDER, SIGN_LOG_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# ===================== 极致拟真设备指纹生成器 V2 (已修复KeyError) =====================
class DeviceProfile:
    """
    V2版本：增加 WebGL、Canvas、AudioContext 等高级指纹字段，
    并确保硬件参数、系统版本、浏览器内核、GPU厂商之间的严格逻辑自洽。
    """
    
    # GPU 渲染器映射表 (确保品牌与GPU对应)
    # 注意：Key 必须与 ANDROID_BRANDS 的 Key 严格一致 (Title Case)
    GPU_MAP = {
        "Xiaomi": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 640"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 650"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 618"},
            {"vendor": "ARM", "renderer": "Mali-G78 MC4"},
        ],
        "Redmi": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 620"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 610"},
            {"vendor": "MediaTek", "renderer": "Mali-G57 MC3"},
            {"vendor": "ARM", "renderer": "Mali-G77 MC4"},
        ],
        "Huawei": [
            {"vendor": "HiSilicon", "renderer": "Mali-G76 MC12"},
            {"vendor": "HiSilicon", "renderer": "Mali-G76 MC8"},
            {"vendor": "HiSilicon", "renderer": "Mali-G72 MP12"},
            {"vendor": "ARM", "renderer": "Mali-G78 MC4"},
        ],
        "Honor": [
            {"vendor": "HiSilicon", "renderer": "Mali-G76 MC8"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 610"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 620"},
            {"vendor": "MediaTek", "renderer": "Mali-G57 MC3"},
        ],
        "Oppo": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 620"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 610"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 618"},
            {"vendor": "MediaTek", "renderer": "Mali-G57 MC5"},
        ],
        "Realme": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 610"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 620"},
            {"vendor": "MediaTek", "renderer": "Mali-G57 MC3"},
            {"vendor": "MediaTek", "renderer": "Mali-G57 MC5"},
        ],
        "OnePlus": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 640"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 650"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 660"},
            {"vendor": "ARM", "renderer": "Mali-G78 MC4"},
        ],
        "Vivo": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 610"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 620"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 618"},
            {"vendor": "MediaTek", "renderer": "Mali-G57 MC3"},
        ],
        "iQOO": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 640"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 650"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 610"},
            {"vendor": "ARM", "renderer": "Mali-G78 MC4"},
        ],
        "Samsung": [
            {"vendor": "ARM", "renderer": "Mali-G76 MP12"},
            {"vendor": "ARM", "renderer": "Mali-G78 MP10"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 650"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 618"},
        ],
        "Google": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 650"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 640"},
            {"vendor": "ARM", "renderer": "Mali-G78 MC4"},
        ],
        "BlackShark": [
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 640"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 650"},
            {"vendor": "Qualcomm", "renderer": "Adreno (TM) 660"},
        ],
        "iPhone": [
            {"vendor": "Apple Inc.", "renderer": "Apple GPU"},
        ],
    }

    CPU_MAP = {
        "Xiaomi": ["Qualcomm Snapdragon 865", "Qualcomm Snapdragon 888", "MediaTek Dimensity 1100", "Qualcomm Snapdragon 870"],
        "Redmi": ["Qualcomm Snapdragon 660", "Qualcomm Snapdragon 720G", "MediaTek Helio G80", "Qualcomm Snapdragon 860"],
        "Huawei": ["HiSilicon Kirin 980", "HiSilicon Kirin 990", "HiSilicon Kirin 9000", "HiSilicon Kirin 820"],
        "Honor": ["HiSilicon Kirin 980", "HiSilicon Kirin 990", "Qualcomm Snapdragon 778G", "MediaTek Dimensity 1000"],
        "Oppo": ["Qualcomm Snapdragon 765G", "Qualcomm Snapdragon 865", "MediaTek Dimensity 1000L", "Qualcomm Snapdragon 888"],
        "Realme": ["Qualcomm Snapdragon 765G", "Qualcomm Snapdragon 865", "MediaTek Dimensity 1000", "Qualcomm Snapdragon 870"],
        "OnePlus": ["Qualcomm Snapdragon 865", "Qualcomm Snapdragon 888", "Qualcomm Snapdragon 870", "MediaTek Dimensity 1000"],
        "Vivo": ["Qualcomm Snapdragon 765G", "Qualcomm Snapdragon 865", "MediaTek Dimensity 1000L", "Qualcomm Snapdragon 888"],
        "iQOO": ["Qualcomm Snapdragon 865", "Qualcomm Snapdragon 888", "Qualcomm Snapdragon 870", "Qualcomm Snapdragon 860"],
        "Samsung": ["Qualcomm Snapdragon 865", "Samsung Exynos 990", "Qualcomm Snapdragon 888", "Samsung Exynos 1080"],
        "Google": ["Qualcomm Snapdragon 765G", "Qualcomm Snapdragon 888", "Google Tensor G1"],
        "BlackShark": ["Qualcomm Snapdragon 865", "Qualcomm Snapdragon 888", "Qualcomm Snapdragon 870"],
        "iPhone": ["Apple A11 Bionic", "Apple A12 Bionic", "Apple A13 Bionic", "Apple A14 Bionic", "Apple A15 Bionic", "Apple A16 Bionic", "Apple A17 Pro", "Apple A18 Pro", "Apple A19 Pro"],
    }

    IMEI_TAC = {
        "Xiaomi": ["86712303", "86871705", "86983805", "86776405", "86816705", "86846005", "86983802", "86725705", "86919603", "86776402"],
        "Redmi": ["86816705", "86919603", "86776405", "86725705", "86983805", "86712303", "86846005", "86983802"],
        "Huawei": ["86098203", "86712303", "86871705", "86010307", "86776402", "86776405", "86871701", "86712301", "86871705"],
        "Honor": ["86712303", "86871705", "86776405", "86919603", "86816705", "86725705", "86983802"],
        "Oppo": ["86851805", "86919303", "86776403", "86871705", "86712303", "86816705", "86919303", "86851801"],
        "Realme": ["86919303", "86851805", "86776403", "86871705", "86816705", "86712303"],
        "OnePlus": ["86871705", "86712303", "86851805", "86919603", "86816705", "86725705"],
        "Vivo": ["86776405", "86871705", "86712303", "86919303", "86851805", "86919603", "86816705"],
        "iQOO": ["86871705", "86776405", "86712303", "86919303", "86851805", "86919603"],
        "Samsung": ["35678905", "35345678", "35210908", "35612345", "35280109", "35609905", "35688405", "35280110"],
        "Google": ["35678905", "35345678", "35210908", "35678901", "35678902"],
        "BlackShark": ["86871705", "86712303", "86851805", "86919603"],
        "iPhone": ["35070523", "35076809", "35101908", "35456505", "35907305", "35301905", "35910705", "35684508", "35651405", "35703705", "35198308", "35488405"],
    }

    MAC_OUI = {
        "Xiaomi": ["78:11:dc", "28:6c:07", "c8:47:8c", "f0:9f:c2", "68:6c:c4", "2c:be:08"],
        "Redmi": ["78:11:dc", "28:6c:07", "c8:47:8c", "f0:9f:c2", "68:6c:c4"],
        "Huawei": ["10:48:29", "00:25:9e", "3c:71:de", "84:ad:8d", "28:31:c4", "54:89:98"],
        "Honor": ["10:48:29", "28:31:c4", "54:89:98", "3c:71:de", "84:ad:8d"],
        "Oppo": ["10:07:44", "1c:1c:09", "86:31:c6", "3c:71:de", "a8:96:75"],
        "Realme": ["10:07:44", "86:31:c6", "1c:1c:09", "a8:96:75", "3c:71:de"],
        "OnePlus": ["10:07:44", "86:31:c6", "1c:1c:09", "a8:96:75"],
        "Vivo": ["18:a2:b1", "3c:2a:f4", "27:01:c5", "51:5e:c5", "78:4f:43"],
        "iQOO": ["18:a2:b1", "3c:2a:f4", "27:01:c5", "51:5e:c5"],
        "Samsung": ["38:25:d3", "28:ba:c6", "00:25:90", "2c:be:08", "60:d0:2c", "84:5c:12"],
        "Google": ["10:48:c1", "3c:71:de", "84:ad:8d", "28:31:c4"],
        "BlackShark": ["78:11:dc", "28:6c:07", "c8:47:8c"],
        "iPhone": ["00:03:93", "a4:5e:60", "d4:61:9d", "f8:15:47", "88:63:df", "10:40:f3", "00:26:bb", "a0:ec:80"],
    }

    # 真·设备指纹库: 以 model 为主键, fingerprint/device/display/id/incremental 严格自洽
    # 格式: BRAND/PRODUCT/DEVICE:RELEASE/ID/INCREMENTAL:TYPE/TAGS
    MODEL_FINGERPRINT = {
        # ===== Xiaomi =====
        "MI 9":        ("Xiaomi", "cepheus",   "cepheus",   "11", "RKQ1.200826.002",        "V12.5.1.0.RFACNXM"),
        "Mi 10":       ("Xiaomi", "umi",       "umi",       "11", "RKQ1.200826.002",        "V12.5.1.0.RJBCNXM"),
        "Mi 11":       ("Xiaomi", "venus",     "venus",     "12", "RKQ1.211001.000",        "V13.0.6.0.SKBCNXM"),
        "Mi 11 Ultra": ("Xiaomi", "star",      "star",      "12", "SKQ1.211006.001",        "V13.0.22.0.SKACNXM"),
        "Mi 12":       ("Xiaomi", "cupid",     "cupid",     "13", "TKQ1.220829.002",        "V14.0.4.0.TLBCNXM"),
        "Mi 12 Pro":   ("Xiaomi", "zeus",      "zeus",      "13", "TKQ1.220829.002",        "V14.0.3.0.TLBCNXM"),
        "Mi 13":       ("Xiaomi", "fuxi",      "fuxi",      "13", "TKQ1.220905.001",        "V14.0.5.0.TMCCNXM"),
        "Mi MIX 3":    ("Xiaomi", "perseus",   "perseus",   "10", "QKQ1.190828.002",        "V12.0.4.0.QEACNXM"),
        # ===== Redmi =====
        "Redmi K30":      ("Redmi", "phoenix",   "phoenix",   "11", "RKQ1.200826.002",   "V12.5.2.0.RJGCNXM"),
        "Redmi K30 Pro":  ("Redmi", "lmipro",    "lmipro",   "11", "RKQ1.200826.002",   "V12.5.2.0.RJKCNXM"),
        "Redmi K40":      ("Redmi", "alioth",    "alioth",   "13", "TKQ1.221013.002",   "V14.0.4.0.TLHCMIXM"),
        "Redmi K50":      ("Redmi", "rubens",    "rubens",   "13", "TKQ1.221013.002",   "V14.0.4.0.TLCCNXM"),
        "Redmi Note 9":   ("Redmi", "gauguin",   "gauguin",  "11", "RKQ1.200826.002",   "V12.5.1.0.RJSMIXM"),
        "Redmi Note 10":  ("Redmi", "mojito",    "mojito",   "11", "RKQ1.200826.002",   "V12.5.7.0.RJSMIXM"),
        "Redmi Note 11":  ("Redmi", "spes",      "spes",     "12", "SKQ1.211019.001",   "V13.0.5.0.SPECNXM"),
        "Redmi Note 12":  ("Redmi", "sunstone",  "sunstone", "13", "TKQ1.221013.002",   "V14.0.6.0.TMQCNXM"),
        # ===== Huawei =====
        "HMA-AL00": ("HUAWEI", "HMA-AL00", "HWMAA", "10", "HUAWEIHMA-AL00", "102.0.0.230C00"),
        "ELE-AL00": ("HUAWEI", "ELE-AL00", "HWELE", "10", "HUAWEIELE-AL00", "102.0.0.230C00"),
        "VOG-AL00": ("HUAWEI", "VOG-AL00", "HWVOG", "10", "HUAWEIVOG-AL00", "102.0.0.230C00"),
        "ANA-AN00": ("HUAWEI", "ANA-AN00", "HWANA", "11", "HUAWEIANA-AN00", "102.0.0.230C00"),
        "ELS-AN00": ("HUAWEI", "ELS-AN00", "HWELS", "11", "HUAWEIELS-AN00", "102.0.0.230C00"),
        "TAS-AN00": ("HUAWEI", "TAS-AN00", "HWTAS", "11", "HUAWEITAS-AN00", "102.0.0.230C00"),
        "NOH-AN00": ("HUAWEI", "NOH-AN00", "HWNOH", "11", "HUAWEINOH-AN00", "102.0.0.218C00"),
        "LIO-AN00": ("HUAWEI", "LIO-AN00", "HWLIO", "11", "HUAWEILIO-AN00", "102.0.0.230C00"),
        # ===== Honor (品牌字段=HONOR, 早期部分为HUAWEI) =====
        "LRA-AL00": ("HONOR", "LRA-AL00", "HWLRA", "10", "HONORLRA-AL00", "102.0.0.230C00"),
        "YAL-AL00": ("HONOR", "YAL-AL00", "HWYAL", "10", "HONORYAL-AL00", "102.0.0.230C00"),
        "NTH-AN00": ("HONOR", "NTH-AN00", "HWNTH", "11", "HONORNTH-AN00", "102.0.0.230C00"),
        "NEH-AN00": ("HONOR", "NEH-AN00", "HWNEH", "11", "HONORNEH-AN00", "102.0.0.230C00"),
        "TAS-AN00_Honor": ("HONOR", "TAS-AN00", "HWTAS", "11", "HONORTAS-AN00", "102.0.0.230C00"),
        # ===== Oppo =====
        "PCKM00":   ("OPPO", "PCKM00",   "OP5757",  "11", "RP1A.200720.009", "OPM02.104.0920"),
        "PDYM20":   ("OPPO", "PDYM20",   "OP5757L1","11", "RP1A.200720.009", "OPM02.104.0920"),
        "RMX2185L1":("OPPO", "RMX2185L1","OP56A7",  "11", "RP1A.200720.009", "OPM02.104.0920"),
        "PCLM50":   ("OPPO", "PCLM50",   "OP4F2F",  "11", "RP1A.200720.009", "PHG_10_A.05"),
        "PDKM00":   ("OPPO", "PDKM00",   "OP5D0D",  "11", "RP1A.200720.009", "OPM02.104.0920"),
        "PHM110":   ("OPPO", "PHM110",   "OP5969L1","13", "TP1A.220905.001", "TP1A.220905.001"),
        "PJJ110":   ("OPPO", "PJJ110",   "OP5969",  "12", "SP1A.210812.016",  "SP1A.210812.016"),
        "CPH2079":  ("OPPO", "CPH2079",  "OP5953",  "11", "RP1A.200720.009", "OPM02.104.0920"),
        # ===== Realme =====
        "RMX2185L1_Realme": ("realme", "RMX2185L1", "RE879A",  "11", "RP1A.200720.009", "TP1A.220624.014"),
        "RMX3031":           ("realme", "RMX3031",   "RE879B",  "12", "SP1A.210812.016",  "SP1A.210812.016"),
        "RMX3330":           ("realme", "RMX3330",   "RE879C",  "13", "TP1A.220905.001", "TP1A.220905.001"),
        "RMX3551":           ("realme", "RMX3551",   "RE879D",  "13", "TP1A.220905.001", "TP1A.220905.001"),
        "RMX2121":           ("realme", "RMX2121",   "RE879E",  "11", "RP1A.200720.009", "RP1A.200720.009"),
        "RMX1901":           ("realme", "RMX1901",   "RE879F",  "10", "QKQ1.190918.001", "QKQ1.190918.001"),
        "RMX2076":           ("realme", "RMX2076",   "RE879G",  "11", "RP1A.200720.009", "RP1A.200720.009"),
        # ===== OnePlus =====
        "instantnoodle":  ("OnePlus", "OnePlus8",     "OnePlus8",     "11", "RP1A.200819.026", "OP8_Oxygen_Open.21"),
        "instantnoodlep": ("OnePlus", "OnePlus8Pro",  "OnePlus8Pro",  "12", "SKQ1.211103.001", "OP8Pro_Oxygen_Open.21"),
        "sofiap":         ("OnePlus", "OnePlus8T",    "OnePlus8T",    "12", "SKQ1.211103.001", "OP8T_Oxygen_Open.21"),
        "OnePlus9":       ("OnePlus", "OnePlus9",     "OnePlus9",     "12", "SKQ1.211103.001", "OP9_Oxygen_Open.21"),
        "OnePlus10":      ("OnePlus", "OnePlus10",    "OnePlus10",    "13", "TP1A.220905.001", "OP10_Oxygen_Open.21"),
        "OnePlus11":      ("OnePlus", "OnePlus11",    "OnePlus11",    "13", "TP1A.220905.001", "OP11_Oxygen_Open.21"),
        # ===== Vivo =====
        "V1938CT": ("vivo", "V1938CT", "PD1938", "11", "RP1A.200720.009", "compiler03241220"),
        "V2059A":  ("vivo", "V2059A",  "PD2059", "11", "RP1A.200720.009", "compiler04241220"),
        "V2072A":  ("vivo", "V2072A",  "PD2072", "12", "SP1A.210812.016",  "compiler05161220"),
        "V2166A":  ("vivo", "V2166A",  "PD2166", "12", "SP1A.210812.016",  "compiler06121220"),
        "V2156A":  ("vivo", "V2156A",  "PD2156", "12", "SP1A.210812.016",  "compiler06121220"),
        "V2227A":  ("vivo", "V2227A",  "PD2227", "13", "TP1A.220905.001", "compiler07181220"),
        "V2318A":  ("vivo", "V2318A",  "PD2318", "13", "TP1A.220905.001", "compiler08181220"),
        "PD2057A": ("vivo", "PD2057A", "PD2057", "11", "RP1A.200720.009", "compiler03241220"),
        # ===== iQOO =====
        "iQOO Neo5": ("iQOO", "I2121",  "I2121",  "12", "SP1A.210812.016",  "compiler04241220"),
        "iQOO 7":    ("iQOO", "I2012",  "I2012",  "11", "RP1A.200720.009", "compiler03241220"),
        "iQOO 9":    ("iQOO", "I2202",  "I2202",  "12", "SP1A.210812.016",  "compiler05161220"),
        "iQOO 10":   ("iQOO", "I2212",  "I2212",  "13", "TP1A.220905.001", "compiler07181220"),
        # ===== Samsung =====
        "SM-G9750": ("samsung", "beyond1q", "beyond1q", "12", "SP1A.210812.016", "G9750ZHU5FVH2"),
        "SM-N9860": ("samsung", "beyond2q", "beyond2q", "12", "SP1A.210812.016", "N9860ZUU3FVH2"),
        "SM-S105B": ("samsung", "q2q",     "q2q",     "13", "TP1A.220624.014", "S105BXXU2BVA2"),
        "SM-F9360": ("samsung", "b5q",     "b5q",     "13", "TP1A.220905.001", "F9360ZHU2CVJ1"),
        "SM-S908B": ("samsung", "b0q",     "b0q",     "13", "TP1A.220624.014", "S908BXXU2BVA2"),
        "SM-S918B": ("samsung", "dm3q",    "dm3q",    "13", "TP1A.220624.014", "S918BXXU2BVA2"),
        "SM-A715F": ("samsung", "a71q",    "a71q",    "12", "SP1A.210812.016", "A715FXXU4FVA2"),
        "SM-M325F": ("samsung", "m32q",    "m32q",    "12", "SP1A.210812.016", "M325FXXU3FVH1"),
        # ===== Google Pixel =====
        "Pixel 4":    ("google", "flame",     "flame",     "13", "TQ3A.230805.001",  "TQ3A.230805.001"),
        "Pixel 5":    ("google", "redfin",    "redfin",    "13", "TQ3A.230805.001",  "TQ3A.230805.001"),
        "Pixel 6":    ("google", "oriole",    "oriole",    "13", "TQ3A.230805.001",  "TQ3A.230805.001"),
        "Pixel 7":    ("google", "panther",   "panther",   "13", "TQ3A.230805.001",  "TQ3A.230805.001"),
        "Pixel 4 XL": ("google", "coral",     "coral",     "13", "TQ3A.230805.001",  "TQ3A.230805.001"),
        "Pixel 6 Pro":("google", "raven",     "raven",     "13", "TQ3A.230805.001",  "TQ3A.230805.001"),
        "Pixel 7 Pro":("google", "cheetah",   "cheetah",   "13", "TQ3A.230805.001",  "TQ3A.230805.001"),
        # ===== BlackShark =====
        "SKW-A0":       ("BlackShark", "SKW-A0",       "SKW-A0",       "11", "RP1A.200720.009", "SKW-A0_20220913"),
        "SHARK PRS-A0": ("BlackShark", "SHARK-PRS-A0", "SHARK-PRS-A0", "11", "RP1A.200720.009", "PRS-A0_20221011"),
        "BlackShark 3": ("BlackShark", "SHARK3",       "SHARK3",       "11", "RP1A.200720.009", "SHARK3_20221024"),
        "BlackShark 4": ("BlackShark", "SHARK4",       "SHARK4",       "12", "SP1A.210812.016",  "SHARK4_20221011"),
        "BlackShark 5": ("BlackShark", "SHARK5",       "SHARK5",       "13", "TP1A.220905.001", "SHARK5_20221011"),
    }

    # 旧表保留兼容(已弃用, 实际从 MODEL_FINGERPRINT 解析)
    BUILD_FINGERPRINT = {
        "Xiaomi": ["google/redfin/redfin:11/RP1A.200720.009/7591302:user/release-keys"],
        "Redmi":   ["google/redfin/redfin:11/RP1A.200720.009/7591302:user/release-keys"],
        "Huawei":  ["HUAWEI/HWNOA/HWNOA:10/HUAWEIHWNOA/102.0.0.230:user/release-keys"],
        "Oppo":    ["OPPO/RMX2185L1/RMX2185L1:11/RP1A.200720.009/OPM02.104.0920:user/release-keys"],
        "Vivo":    ["vivo/V1938CT/V1938CT:11/RP1A.200720.009/compiler03241220:user/release-keys"],
        "Samsung": ["samsung/beyond1/beyond1:11/RP1A.200720.009/T3s:user/release-keys"],
    }

    BUILD_DISPLAY = {
        "Xiaomi": ["RP1A.200720.009", "SQ3A.220705.003", "UP1A.231005.007"],
        "Redmi": ["RP1A.200720.009", "SQ3A.220705.003"],
        "Huawei": ["102.0.0.230", "102.0.0.210", "102.0.0.180"],
        "Honor": ["102.0.0.230", "102.0.0.210", "102.0.0.180"],
        "Oppo": ["OPM02.104.0920", "PHG_10_A.05", "PKG_10_A.15"],
        "Realme": ["RMX2185L1", "RMX3031", "RMX3330"],
        "OnePlus": ["UP1A.231005.007", "RD2A.231005.007", "OXYGEN.14.1.2"],
        "Vivo": ["compiler03241220", "compiler04241220", "compiler05161220"],
        "iQOO": ["compiler03241220", "compiler04241220"],
        "Samsung": ["T3s", "T4", "T5", "T6"],
        "Google": ["UP1A.231005.007", "QD4A.230810.003"],
        "BlackShark": ["SRK_SF_1.0", "SRK_SF_2.0"],
    }

    BUILD_HARDWARE = {
        "Xiaomi": ["taro", "redfin", "oriole", "sunfish", "barbet"],
        "Redmi": ["taro", "redfin", "sunfish"],
        "Huawei": ["HWMP40", "HWNOA", "HWLSA", "HWTAH"],
        "Honor": ["HWNOA", "HLSA", "HWBVL"],
        "Oppo": ["RMX2185L1", "PCLM50", "PCKM00"],
        "Realme": ["RMX2185L1", "RMX3031", "RMX3330"],
        "OnePlus": ["instantnoodlep", "instantnoodle", "sofiap"],
        "Vivo": ["V1938CT", "V2059A", "V2072A"],
        "iQOO": ["V1938CT", "V2072A"],
        "Samsung": ["beyond1", "crown", "z3q", "r3q"],
        "Google": ["oriole", "redfin", "barbet", "sunfish"],
        "BlackShark": ["SRK_SF_1", "SRK_SF_2"],
    }

    ANDROID_BRANDS = {
        "Xiaomi": {
            "brand": "Xiaomi",
            "models": [
                {"model": 'MI 9', "res": (1080, 2340), "density": 2.75, "android": ['11'], "ram": [6, 8]},
{"model": 'Mi 11', "res": (1440, 3200), "density": 3.0, "android": ['11', '12'], "ram": [8, 12]},
{"model": 'Mi 12', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12]},
{"model": 'Mi 13', "res": (1080, 2400), "density": 3.0, "android": ['13'], "ram": [8, 12, 16]},
{"model": 'MI 10', "res": (1080, 2340), "density": 2.75, "android": ['11'], "ram": [6, 8, 12]},
{"model": 'Mi 11 Ultra', "res": (1440, 3200), "density": 3.0, "android": ['11', '12'], "ram": [12, 16]},
{"model": 'Mi 12 Pro', "res": (1440, 3200), "density": 3.0, "android": ['12', '13'], "ram": [12, 16]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Redmi": {
            "brand": "Redmi",
            "models": [
                {"model": 'Redmi K30', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [6, 8]},
{"model": 'Redmi Note 10', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [4, 6, 8]},
{"model": 'Redmi Note 11', "res": (1080, 2400), "density": 2.5, "android": ['11', '12'], "ram": [4, 6, 8]},
{"model": 'Redmi K40', "res": (1080, 2400), "density": 3.0, "android": ['11', '12'], "ram": [6, 8, 12]},
{"model": 'Redmi K50', "res": (1440, 3200), "density": 3.0, "android": ['12', '13'], "ram": [8, 12]},
{"model": 'Redmi Note 12', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [6, 8, 12]},
{"model": 'Redmi Note 9', "res": (1080, 2340), "density": 2.75, "android": ['11'], "ram": [4, 6, 8]},
{"model": 'Redmi K30 Pro', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [8, 12]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Huawei": {
            "brand": "Huawei",
            "models": [
                {"model": 'ANA-AN00', "res": (1080, 2340), "density": 3.0, "android": ['11'], "ram": [6, 8, 12]},
{"model": 'ELS-AN00', "res": (1440, 3200), "density": 3.0, "android": ['11'], "ram": [8, 12]},
{"model": 'TAS-AN00', "res": (1440, 3200), "density": 3.0, "android": ['11'], "ram": [8, 12]},
{"model": 'NOH-AN00', "res": (1440, 3200), "density": 3.0, "android": ['11'], "ram": [8, 12]},
{"model": 'LIO-AN00', "res": (1080, 2340), "density": 3.0, "android": ['11'], "ram": [6, 8]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Honor": {
            "brand": "HUAWEI",
            "models": [
                {"model": 'LIO-AN00', "res": (1080, 2340), "density": 3.0, "android": ['11'], "ram": [6, 8]},
{"model": 'TAS-AN00', "res": (1440, 3200), "density": 3.0, "android": ['11'], "ram": [8, 12]},
{"model": 'NEH-AN00', "res": (1080, 2340), "density": 3.0, "android": ['11'], "ram": [6, 8]},
{"model": 'NTH-AN00', "res": (1080, 2340), "density": 3.0, "android": ['11'], "ram": [8, 12]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Oppo": {
            "brand": "OPPO",
            "models": [
                {"model": 'PDYM20', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [4, 6, 8]},
{"model": 'RMX2185L1', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [6, 8]},
{"model": 'PCLM50', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [6, 8, 12]},
{"model": 'PDKM00', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [8, 12]},
{"model": 'PHM110', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12, 16]},
{"model": 'PJJ110', "res": (1080, 2400), "density": 3.0, "android": ['11', '12'], "ram": [6, 8, 12]},
{"model": 'CPH2079', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [4, 6, 8]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Realme": {
            "brand": "realme",
            "models": [
                {"model": 'RMX2185L1', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [6, 8]},
{"model": 'RMX3031', "res": (1080, 2400), "density": 2.5, "android": ['11', '12'], "ram": [6, 8, 12]},
{"model": 'RMX3330', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12]},
{"model": 'RMX3551', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12, 16]},
{"model": 'RMX2121', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [4, 6, 8]},
{"model": 'RMX2076', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [4, 6, 8]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "OnePlus": {
            "brand": "OnePlus",
            "models": [
                {"model": 'instantnoodle', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [8, 12]},
{"model": 'instantnoodlep', "res": (1440, 3200), "density": 3.0, "android": ['11'], "ram": [8, 12]},
{"model": 'sofiap', "res": (1440, 3200), "density": 3.0, "android": ['11', '12'], "ram": [8, 12, 16]},
{"model": 'OnePlus9', "res": (1080, 2400), "density": 3.0, "android": ['11', '12'], "ram": [8, 12]},
{"model": 'OnePlus10', "res": (1440, 3200), "density": 3.0, "android": ['12'], "ram": [8, 12, 16]},
{"model": 'OnePlus11', "res": (1440, 3200), "density": 3.0, "android": ['13'], "ram": [12, 16]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Vivo": {
            "brand": "vivo",
            "models": [
                {"model": 'V1938CT', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [4, 6, 8]},
{"model": 'V2059A', "res": (1080, 2376), "density": 2.5, "android": ['11'], "ram": [4, 6, 8]},
{"model": 'V2072A', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [6, 8]},
{"model": 'V2166A', "res": (1080, 2400), "density": 2.5, "android": ['11', '12'], "ram": [4, 6, 8]},
{"model": 'V2156A', "res": (1080, 2400), "density": 2.5, "android": ['11', '12'], "ram": [6, 8, 12]},
{"model": 'V2227A', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [6, 8, 12]},
{"model": 'V2318A', "res": (1080, 2400), "density": 3.0, "android": ['13'], "ram": [8, 12]},
{"model": 'PD2057A', "res": (1080, 2340), "density": 2.75, "android": ['11'], "ram": [6, 8]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "iQOO": {
            "brand": "iQOO",
            "models": [
                {"model": 'V1938CT', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [6, 8, 12]},
{"model": 'V2072A', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [8, 12]},
{"model": 'V2227A', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12, 16]},
{"model": 'iQOO Neo5', "res": (1080, 2400), "density": 2.5, "android": ['11', '12'], "ram": [8, 12]},
{"model": 'iQOO 7', "res": (1080, 2400), "density": 3.0, "android": ['11'], "ram": [8, 12]},
{"model": 'iQOO 9', "res": (1440, 3200), "density": 3.0, "android": ['12'], "ram": [12, 16]},
{"model": 'iQOO 10', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12, 16]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Samsung": {
            "brand": "Samsung",
            "models": [
                {"model": 'SM-N9860', "res": (1440, 3200), "density": 3.5, "android": ['11'], "ram": [8, 12]},
{"model": 'SM-F9360', "res": (1080, 2340), "density": 4.2, "android": ['11', '12'], "ram": [12, 16]},
{"model": 'SM-S908B', "res": (1440, 3200), "density": 3.5, "android": ['12', '13'], "ram": [12, 16]},
{"model": 'SM-S918B', "res": (1440, 3200), "density": 3.5, "android": ['13'], "ram": [12, 16]},
{"model": 'SM-A715F', "res": (1080, 2400), "density": 3.0, "android": ['11'], "ram": [6, 8]},
{"model": 'SM-M325F', "res": (720, 1600), "density": 2.7, "android": ['11'], "ram": [4, 6, 8]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Google": {
            "brand": "Google",
            "models": [
                {"model": 'Pixel 5', "res": (1080, 2340), "density": 2.75, "android": ['11'], "ram": [8]},
{"model": 'Pixel 6', "res": (1080, 2400), "density": 2.75, "android": ['12'], "ram": [8]},
{"model": 'Pixel 7', "res": (1080, 2400), "density": 2.75, "android": ['13'], "ram": [8]},
{"model": 'Pixel 6 Pro', "res": (1440, 3200), "density": 3.5, "android": ['12'], "ram": [8, 12]},
{"model": 'Pixel 7 Pro', "res": (1440, 3200), "density": 3.5, "android": ['13'], "ram": [8, 12]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "BlackShark": {
            "brand": "BlackShark",
            "models": [
                {"model": 'SKW-A0', "res": (1080, 2340), "density": 2.75, "android": ['11'], "ram": [8, 12]},
{"model": 'SHARK PRS-A0', "res": (1080, 2400), "density": 2.5, "android": ['11'], "ram": [8, 12]},
{"model": 'BlackShark 4', "res": (1080, 2400), "density": 3.0, "android": ['11', '12'], "ram": [8, 12, 16]},
{"model": 'BlackShark 5', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [12, 16]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Meizu": {
            "brand": "Meizu",
            "models": [
                {"model": '18 Pro', "res": (1440, 3200), "density": 3.0, "android": ['11', '12'], "ram": [8, 12]},
{"model": '20 Pro', "res": (1440, 3200), "density": 3.5, "android": ['13'], "ram": [12, 16]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Nubia": {
            "brand": "Nubia",
            "models": [
                {"model": 'NX669J', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12]},
{"model": 'NX721J', "res": (1080, 2480), "density": 3.0, "android": ['13'], "ram": [12, 16]},
{"model": 'NX729J', "res": (1116, 2480), "density": 3.5, "android": ['13'], "ram": [8, 12, 16]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "ZTE": {
            "brand": "ZTE",
            "models": [
                {"model": 'A2023P', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12]},
{"model": 'A2022', "res": (1080, 2400), "density": 3.0, "android": ['11', '12'], "ram": [8, 12]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Motorola": {
            "brand": "Motorola",
            "models": [
                {"model": 'XT2201-2', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12]},
{"model": 'XT2249-2', "res": (1080, 2400), "density": 2.75, "android": ['11', '12'], "ram": [8, 12]},
{"model": 'XT2251-1', "res": (1080, 2400), "density": 3.0, "android": ['12'], "ram": [8, 12]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Lenovo": {
            "brand": "Lenovo",
            "models": [
                {"model": 'Lenovo Y70', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [8, 12, 16]},
{"model": 'Lenovo K14 Pro', "res": (1080, 2400), "density": 2.75, "android": ['11', '12'], "ram": [6, 8]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "POCO": {
            "brand": "POCO",
            "models": [
                {"model": '22101316G', "res": (1440, 3200), "density": 3.5, "android": ['13'], "ram": [8, 12]},
{"model": '22101320G', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [6, 8]},
{"model": '220333QAG', "res": (720, 1600), "density": 2.5, "android": ['11'], "ram": [4, 6]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "TCL": {
            "brand": "TCL",
            "models": [
                {"model": 'TCL 40R', "res": (720, 1612), "density": 2.5, "android": ['12'], "ram": [4, 6]},
{"model": 'TCL 50 Pro NXTPAPER', "res": (1080, 2436), "density": 3.0, "android": ['13', '14'], "ram": [8, 12]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "Nokia": {
            "brand": "Nokia",
            "models": [
                {"model": 'Nokia X30 5G', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [6, 8]},
{"model": 'Nokia G60 5G', "res": (1080, 2400), "density": 3.0, "android": ['12', '13'], "ram": [4, 6]}
            ],
            "ua_template": 'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36'
        },
        "HTC": {
            "brand": "HTC",
            "models": [
                {"model": "HTC Desire 22 Pro", "res": (1080, 2412), "density": 3.0, "android": ["12"], "ram": [8]}
            ],
            "ua_template": "Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"
        },
        "iPhone": {
            "brand": "iPhone",
            "models": [
                {"model": "iPhone 7", "res": (750, 1334), "density": 2.0, "android": ["12", "13", "14", "15"], "ram": [2]},
                {"model": "iPhone 7 Plus", "res": (1080, 1920), "density": 3.0, "android": ["12", "13", "14", "15"], "ram": [3]},
                {"model": "iPhone 8", "res": (750, 1334), "density": 2.0, "android": ["12", "13", "14", "15", "16"], "ram": [2]},
                {"model": "iPhone 8 Plus", "res": (1080, 1920), "density": 3.0, "android": ["12", "13", "14", "15", "16"], "ram": [3]},
                {"model": "iPhone X", "res": (1125, 2436), "density": 3.0, "android": ["12", "13", "14", "15", "16"], "ram": [3]},
                {"model": "iPhone XR", "res": (828, 1792), "density": 2.0, "android": ["12", "13", "14", "15", "16", "17"], "ram": [3]},
                {"model": "iPhone XS", "res": (1125, 2436), "density": 3.0, "android": ["12", "13", "14", "15", "16", "17"], "ram": [4]},
                {"model": "iPhone XS Max", "res": (1242, 2688), "density": 3.0, "android": ["12", "13", "14", "15", "16", "17"], "ram": [4]},
                {"model": "iPhone 11", "res": (828, 1792), "density": 2.0, "android": ["13", "14", "15", "16", "17", "18"], "ram": [4]},
                {"model": "iPhone 11 Pro", "res": (1125, 2436), "density": 3.0, "android": ["13", "14", "15", "16", "17", "18"], "ram": [4]},
                {"model": "iPhone 11 Pro Max", "res": (1242, 2688), "density": 3.0, "android": ["13", "14", "15", "16", "17", "18"], "ram": [4]},
                {"model": "iPhone SE (2nd generation)", "res": (750, 1334), "density": 2.0, "android": ["13", "14", "15", "16", "17", "18"], "ram": [3]},
                {"model": "iPhone 12", "res": (1170, 2532), "density": 3.0, "android": ["14", "15", "16", "17", "18"], "ram": [4]},
                {"model": "iPhone 12 mini", "res": (1080, 2340), "density": 3.0, "android": ["14", "15", "16", "17", "18"], "ram": [4]},
                {"model": "iPhone 12 Pro", "res": (1179, 2556), "density": 3.0, "android": ["14", "15", "16", "17", "18"], "ram": [6]},
                {"model": "iPhone 12 Pro Max", "res": (1284, 2778), "density": 3.0, "android": ["14", "15", "16", "17", "18"], "ram": [6]},
                {"model": "iPhone 13", "res": (1170, 2532), "density": 3.0, "android": ["15", "16", "17", "18", "19"], "ram": [4]},
                {"model": "iPhone 13 mini", "res": (1080, 2340), "density": 3.0, "android": ["15", "16", "17", "18", "19"], "ram": [4]},
                {"model": "iPhone 13 Pro", "res": (1179, 2556), "density": 3.0, "android": ["15", "16", "17", "18", "19"], "ram": [6]},
                {"model": "iPhone 13 Pro Max", "res": (1284, 2778), "density": 3.0, "android": ["15", "16", "17", "18", "19"], "ram": [6]},
                {"model": "iPhone SE (3rd generation)", "res": (750, 1334), "density": 2.0, "android": ["15", "16", "17", "18", "19"], "ram": [4]},
                {"model": "iPhone 14", "res": (1170, 2532), "density": 3.0, "android": ["16", "17", "18", "19"], "ram": [6]},
                {"model": "iPhone 14 Plus", "res": (1284, 2778), "density": 3.0, "android": ["16", "17", "18", "19"], "ram": [6]},
                {"model": "iPhone 14 Pro", "res": (1179, 2556), "density": 3.0, "android": ["16", "17", "18", "19", "20"], "ram": [6]},
                {"model": "iPhone 14 Pro Max", "res": (1284, 2778), "density": 3.0, "android": ["16", "17", "18", "19", "20"], "ram": [6]},
                {"model": "iPhone 15", "res": (1170, 2532), "density": 3.0, "android": ["17", "18", "19", "20"], "ram": [6]},
                {"model": "iPhone 15 Plus", "res": (1284, 2778), "density": 3.0, "android": ["17", "18", "19", "20"], "ram": [6]},
                {"model": "iPhone 15 Pro", "res": (1179, 2556), "density": 3.0, "android": ["17", "18", "19", "20", "21"], "ram": [8]},
                {"model": "iPhone 15 Pro Max", "res": (1290, 2796), "density": 3.0, "android": ["17", "18", "19", "20", "21"], "ram": [8]},
                {"model": "iPhone 16", "res": (1179, 2556), "density": 3.0, "android": ["18", "19", "20", "21", "22"], "ram": [8]},
                {"model": "iPhone 16 Plus", "res": (1284, 2778), "density": 3.0, "android": ["18", "19", "20", "21", "22"], "ram": [8]},
                {"model": "iPhone 16 Pro", "res": (1206, 2622), "density": 3.0, "android": ["18", "19", "20", "21", "22"], "ram": [8]},
                {"model": "iPhone 16 Pro Max", "res": (1320, 2868), "density": 3.0, "android": ["18", "19", "20", "21", "22"], "ram": [8]},
                {"model": "iPhone 17", "res": (1206, 2622), "density": 3.0, "android": ["26"], "ram": [8]},
                {"model": "iPhone 17 Pro", "res": (1206, 2622), "density": 3.0, "android": ["26"], "ram": [8]},
                {"model": "iPhone 17 Pro Max", "res": (1320, 2868), "density": 3.0, "android": ["26"], "ram": [12]}
            ],
            "ua_template": "Mozilla/5.0 (iPhone; CPU iPhone OS {android_ver} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{chrome_ver} Mobile/15E148 Safari/604.1"
        },

    }
    def __init__(self, province_code=None, carrier_code=None):
        self._province_code = province_code
        self._carrier_code = carrier_code
        self.province_code = province_code
        self.city_core = ""
        self.is_ios = False
        self._generate_hardware_info()
        self._generate_network_info()
        self._generate_software_info()
        self._generate_advanced_fingerprints()

    def _generate_hardware_info(self):
        """生成硬件唯一标识及物理参数"""
        brand_key = random.choice(list(self.ANDROID_BRANDS.keys()))
        brand_info = self.ANDROID_BRANDS[brand_key]
        self.is_ios = (brand_key == "iPhone")
        self.brand_key = brand_key
        self.brand = brand_info['brand']

        model_info = random.choice(brand_info['models'])
        self.model = model_info['model']
        self.manufacturer = brand_key

        self.android_id = "".join(random.choices("0123456789abcdef", k=16))
        self.oaid = "".join(random.choices("0123456789abcdef", k=32))
        self.imei = self._generate_imei()
        self.mac_address = self._generate_mac()
        self.device_id = str(fake.uuid4())

        self.screen_width, self.screen_height = model_info['res']
        self.density = model_info['density']

        self.cpu_cores = random.choice([4, 6, 8])
        self.ram_gb = random.choice(model_info.get('ram', [4, 6, 8]))
        # 充电状态与电量相关: 充电中电量偏高, 未充电偏低, 充电概率约15%
        self.is_charging = random.random() < 0.15
        if self.is_charging:
            self.battery_level = random.randint(40, 100)
        else:
            self.battery_level = random.randint(10, 95)

        cpu_list = self.CPU_MAP.get(brand_key, ["Unknown"])
        self.cpu_model = random.choice(cpu_list)

        # 电池详细信息
        self.battery_temperature = round(random.uniform(25.0, 40.0), 1)  # 电池温度
        self.battery_voltage = random.randint(3500, 4200)  # 电池电压(mV)
        self.battery_health = random.choice(["good", "good", "good", "overheat"])  # 电池健康状态
        self.battery_technology = random.choice(["Li-ion", "Li-polymer"])  # 电池类型

        # 网络详细信息
        self.network_strength = random.randint(-100, -50)  # 信号强度(dBm)
        self.network_operator = {
            "CMCC": "中国移动", "CUCC": "中国联通", "CTCC": "中国电信", "CBN": "中国广电"
        }.get(self._carrier_code, random.choice(["中国移动", "中国联通", "中国电信"]))
        self.network_country = "CN"
        self.network_roaming = False

        # 传感器数据
        self.accelerometer_x = round(random.uniform(-0.5, 0.5), 4)
        self.accelerometer_y = round(random.uniform(-0.5, 0.5), 4)
        self.accelerometer_z = round(random.uniform(9.5, 10.0), 4)  # 重力加速度
        self.gyroscope_x = round(random.uniform(-0.1, 0.1), 4)
        self.gyroscope_y = round(random.uniform(-0.1, 0.1), 4)
        self.gyroscope_z = round(random.uniform(-0.1, 0.1), 4)
        self.magnetic_x = round(random.uniform(-50.0, 50.0), 2)  # 磁力计
        self.magnetic_y = round(random.uniform(-50.0, 50.0), 2)
        self.magnetic_z = round(random.uniform(-50.0, 50.0), 2)
        self.light_sensor = round(random.uniform(10.0, 1000.0), 1)  # 光线传感器(lux)
        self.proximity_sensor = random.choice([0, 1])  # 接近传感器
        self.pressure_sensor = round(random.uniform(990.0, 1030.0), 1)  # 气压传感器(hPa)

        # 设备状态
        self.orientation = random.choice(["portrait", "landscape"])  # 屏幕方向
        self.screen_brightness = random.randint(30, 100)  # 屏幕亮度
        self.ringer_mode = random.choice(["normal", "silent", "vibrate"])  # 铃声模式
        self.is_rooted = False  # 是否root
        self.is_emulator = False  # 是否模拟器
        self.is_tablet = False  # 是否平板

        # 存储信息
        self.storage_total = random.choice([64, 128, 256, 512])  # 总存储(GB)
        self.storage_available = random.randint(10, self.storage_total - 10)  # 可用存储(GB)
        self.sd_card = random.choice([True, False])  # 是否有SD卡

        # 设备指纹严格自洽: 从 MODEL_FINGERPRINT 按 model 查表派生
        # 同步覆盖 build_fingerprint / build_display / build_hardware / build_id / build_incremental
        if self.is_ios:
            # iPhone: 无 Android build fingerprint, 系统版本取机型支持的 iOS 版本, build 字段用 Apple 格式
            self.ios_ver = random.choice(model_info['android'])
            self.android_ver = self.ios_ver
            self.build_fingerprint = f"Apple/iPhone/{self.model}"
            self.build_display = self.ios_ver
            self.build_hardware = "iPhone"
            self.build_id = self.ios_ver
            self.build_incremental = self.ios_ver
            self.build_product = self.model
            self.build_manufacturer = "Apple"
            self.build_device = "iPhone"
        else:
            fp_tuple = self.MODEL_FINGERPRINT.get(self.model)
            if not fp_tuple:
                # 兜底: 同品牌任意一条
                same_brand = [v for v in self.MODEL_FINGERPRINT.values() if v[0] == self.brand]
                fp_tuple = random.choice(same_brand) if same_brand else \
                           ("google", "redfin", "redfin", "13", "TQ3A.230805.001", "TQ3A.230805.001")
            fp_brand, fp_product, fp_device, fp_release, fp_id, fp_incremental = fp_tuple
            # Android 系统版本以 fingerprint 的 RELEASE 为准 (覆盖 UA 端的随机版本)
            self.android_ver = fp_release
            self.build_fingerprint = f"{fp_brand}/{fp_product}/{fp_device}:{fp_release}/{fp_id}/{fp_incremental}:user/release-keys"
            self.build_display = fp_incremental or fp_id
            self.build_hardware = fp_device
            self.build_id = fp_id
            self.build_incremental = fp_incremental
            self.build_product = fp_product
            self.build_manufacturer = fp_brand
            self.build_device = fp_device

        # 模拟真实用户行为轨迹(仅作为反馈数据随请求上报, 不增加真实等待, 不影响注册速度)
        # 默认60-180秒; 注册时会按身份证年龄重设(见 set_behavior_by_age)
        self._gen_behavior(60000, 180000)

    def _gen_behavior(self, lo_ms, hi_ms):
        """生成行为轨迹反馈: 总时长在 lo_ms-hi_ms 间随机, 输入占比15-60%, 轨迹时间轴覆盖总时长
        仅作为上报数据, 不产生任何真实等待"""
        total_ms = random.randint(lo_ms, hi_ms)
        # 表单输入耗时: 与停留时长相加=总操作时长
        self.behavior_input_ms = random.randint(int(total_ms * 0.15), int(total_ms * 0.6))
        self.behavior_stay_ms = total_ms - self.behavior_input_ms
        # 模拟滑动轨迹: 若干坐标点+相对时间戳(ms), 时间轴覆盖整个操作周期
        trace_points = []
        _t = 0
        _x, _y = random.randint(50, 400), random.randint(300, 700)
        n = random.randint(5, 10)
        for _i in range(n):
            _t += int(total_ms * random.uniform(0.08, 0.22))
            _x += random.randint(-60, 80)
            _y += random.randint(-50, 120)
            _x = max(10, min(710, _x))
            _y = max(10, min(1270, _y))
            trace_points.append({"x": _x, "y": _y, "t": _t})
        if trace_points:
            trace_points[-1]["t"] = total_ms  # 末点时间戳对齐总时长, 上报自洽
        self.behavior_trace = json.dumps(trace_points, separators=(",", ":"))

    def set_behavior_by_age(self, age):
        """按身份证年龄设置行为时长(仅改上报值, 不影响实际注册速度):
        - 年龄>45(46-55岁/50岁左右): 操作时长180-300秒(年长者偏慢)
        - 年龄20-30岁(年轻人): 操作时长80-180秒(年轻偏快)
        - 其余(31-45岁): 70%概率120-180秒, 30%概率60-120秒"""
        if age > 45:
            self._gen_behavior(180000, 300000)
        elif 20 <= age <= 30:
            self._gen_behavior(80000, 180000)
        elif random.random() < 0.70:
            self._gen_behavior(120000, 180000)
        else:
            self._gen_behavior(60000, 120000)

    def _generate_network_info(self):
        """生成真实运营商IP - 使用运营商实际分配的IP网段"""
        carrier_ip_pools = [
            {"carrier": "CMCC", "ranges": [
                (112, 4, 0, 14), (117, 136, 0, 14), (183, 232, 0, 14),
                (211, 136, 0, 14), (218, 200, 0, 14), (223, 104, 0, 14),
                (117, 136, 0, 15), (120, 192, 0, 15), (112, 64, 0, 14),
                (117, 114, 0, 14), (121, 40, 0, 14), (123, 125, 0, 14),
            ]},
            {"carrier": "CUCC", "ranges": [
                (123, 125, 0, 15), (125, 39, 0, 14), (202, 106, 0, 14),
                (218, 75, 0, 14), (221, 7, 0, 14), (123, 125, 64, 18),
                (125, 40, 0, 14), (125, 41, 0, 14), (202, 108, 0, 14),
                (202, 110, 0, 14), (218, 76, 0, 14), (218, 77, 0, 14),
            ]},
            {"carrier": "CTCC", "ranges": [
                (36, 64, 0, 14), (42, 56, 0, 14), (49, 64, 0, 14),
                (59, 48, 0, 14), (115, 164, 0, 14), (118, 74, 0, 14),
                (180, 120, 0, 14), (180, 128, 0, 14), (222, 172, 0, 14),
                (222, 176, 0, 14), (222, 186, 0, 14), (61, 165, 0, 14),
            ]},
            {"carrier": "CBN", "ranges": [
                (162, 14, 0, 14), (165, 11, 0, 14), (167, 12, 0, 14),
                (192, 168, 0, 16),
            ]},
        ]

        provinces = [
            ("BJ", 110), ("SH", 310), ("GD", 440), ("JS", 320),
            ("ZJ", 330), ("SD", 370), ("HA", 410), ("SC", 510),
            ("HB", 420), ("HN", 430), ("FJ", 350), ("AH", 340),
            ("HE", 130), ("SN", 610), ("LN", 110), ("JL", 210),
            ("HL", 230), ("JX", 360), ("GX", 450), ("YN", 530),
            ("GZ", 520), ("SX", 140), ("GS", 620), ("HI", 460),
            ("NM", 150), ("XJ", 650), ("NX", 640), ("QH", 630),
            ("XZ", 540), ("TJ", 120), ("CQ", 500),
        ]

        if self._province_code and self._province_code in PROVINCE_IP_RANGES:
            prov_data = PROVINCE_IP_RANGES[self._province_code]
            if self._carrier_code:
                carrier_ranges = dict(prov_data)
                if self._carrier_code in carrier_ranges:
                    carrier = self._carrier_code
                    ranges = carrier_ranges[carrier]
                else:
                    carrier, ranges = random.choice(prov_data)
            else:
                carrier, ranges = random.choice(prov_data)
            base_a, base_b, base_c, prefix_len = random.choice(ranges)
        else:
            pool = random.choice(carrier_ip_pools)
            carrier = pool["carrier"]
            base_a, base_b, base_c, prefix_len = random.choice(pool["ranges"])

        if prefix_len == 14:
            c = base_c + random.randint(0, 3)
            d = random.randint(1, 254)
        elif prefix_len == 15:
            c = base_c + random.randint(0, 1)
            d = random.randint(1, 254)
        elif prefix_len == 16:
            c = base_c
            d = random.randint(1, 254)
        elif prefix_len == 18:
            c = base_c + random.randint(0, 63)
            d = random.randint(1, 254)
        else:
            c = base_c
            d = random.randint(1, 254)

        if self._province_code:
            matched = [p for p in provinces if p[0] == self._province_code]
            if matched:
                province_name, area_code = matched[0]
            else:
                province_name, area_code = random.choice(provinces)
        else:
            province_name, area_code = random.choice(provinces)

        self.fake_ip = f"{base_a}.{base_b}.{c}.{d}"
        self.ip_carrier = carrier
        self.ip_carrier_cn = CARRIER_CN_MAP.get(carrier, carrier)
        self.ip_location = province_name
        self.ip_location_cn = PROVINCE_CN_MAP.get(province_name, province_name)
        self.ip_area_code = str(area_code)
        self.ip_type = "ipv4"
        # 真实网络分布: 4G/WIFI为主, 5G占比约20%
        self.network_type = random.choices(["4G", "5G", "WIFI"], weights=[45, 20, 35])[0]

    def _generate_software_info(self):
        """生成软件和UA信息 (版本严格匹配) + 真实浏览器指纹参数"""
        version_mapping = {
            "10": ["99.0.4844.117", "100.0.4896.127"],
            "11": ["100.0.4896.127", "108.0.5359.128"],
            "12": ["108.0.5359.128", "114.0.5735.130", "116.0.5845.110"],
            "13": ["114.0.5735.130", "116.0.5845.110", "120.0.6099.144"],
            "14": ["120.0.6099.144", "124.0.6367.160", "126.0.6478.188", "128.0.6613.127"]
        }

        # ===== iPhone/iOS Safari 分支 =====
        if self.is_ios:
            ios_major = self.ios_ver.split('.')[0]
            self.chrome_ver = self.ios_ver  # 复用字段存 Safari 版本号
            # iOS Safari 真实 UA: 不携带机型名, WebKit 内核固定
            self.user_agent = (
                f"Mozilla/5.0 (iPhone; CPU iPhone OS {self.ios_ver.replace('.', '_')} like Mac OS X) "
                f"AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{self.ios_ver} Mobile/15E148 Safari/604.1"
            )
            # iOS 16.4+ Safari 的 Sec-Ch-Ua 真实格式 (GREASE 品牌为 Not_A Brand)
            self.sec_ch_ua = f'"Not_A Brand";v="8", "Safari";v="{ios_major}", "Mobile Safari";v="{ios_major}"'
            self.sec_ch_ua_mobile = "?1"
            self.sec_ch_ua_platform = '"iOS"'
            self.sec_ch_ua_platform_version = f'"{self.ios_ver.replace(".", "_")}"'
            self.sec_ch_ua_arch = '"arm"'
            self.sec_ch_ua_bitness = '"64"'
            self.sec_ch_ua_model = '""'
            self.sec_ch_ua_full_version = '"605.1.15"'
            self.sec_ch_ua_full_version_list = '""'
            self.language = "zh-CN"
            # 时区与IP归属地对应: 新疆用乌鲁木齐时区, 其余主流为上海时区
            if self.ip_location == "XJ":
                self.timezone = "Asia/Urumqi"
            elif random.random() < 0.9:
                self.timezone = "Asia/Shanghai"
            else:
                self.timezone = random.choice(["Asia/Chongqing", "Asia/Harbin", "Asia/Urumqi"])
            if self.timezone == "Asia/Urumqi":
                self.accept_language = "zh-CN,zh;q=0.9"
            else:
                self.accept_language = "zh-CN,zh;q=0.9,en;q=0.8"
            self.color_depth = "24"
            self.pixel_ratio = str(self.density)
            self.hardware_concurrency = str(self.cpu_cores)
            self.device_memory = str(self.ram_gb)
            self.platform = "iPhone"
            self.vendor = "Apple Computer, Inc."
            self.webgl_version = "WebGL 2.0"
            self.audio_context_sample_rate = str(random.choice([44100, 48000]))
            self.browser_session_id = "".join(random.choices("abcdef0123456789", k=32))
            self.browser_fp_hash = hashlib.sha256(
                f"{self.android_id}{self.user_agent}{self.screen_width}x{self.screen_height}".encode()
            ).hexdigest()[:32]
            # 移动端 Safari 真实 referer (H5 SPA, referer 是入口 HTML 而非 API URL)
            self.referer = URL_INDEX
            return

        # 注意: self.android_ver 已在 _generate_hardware_info 中按 fingerprint 设定
        # 这里只做安全兜底 (Android 版本必须与 fingerprint 严格一致, 否则一查就穿)
        if not hasattr(self, "android_ver") or not self.android_ver:
            model_and = self.ANDROID_BRANDS[self.brand_key]['models']
            found = None
            for m in model_and:
                if m['model'] == self.model:
                    found = m
                    break
            if found and 'android' in found:
                self.android_ver = random.choice(found['android'])
            else:
                self.android_ver = random.choice(list(version_mapping.keys()))

        self.chrome_ver = random.choice(version_mapping[self.android_ver])

        ua_template = self.ANDROID_BRANDS[self.brand_key]['ua_template']
        self.user_agent = ua_template.format(
            android_ver=self.android_ver,
            model=self.model,
            chrome_ver=self.chrome_ver
        )

        # Sec-Ch-Ua 严格按 Chrome 大版本映射 Not-A.Brand 版本 (Chromium GREASE 策略)
        # 真实 Chrome: 99=v"99", 100-109=v"99", 110-119=v"24", 120-129=v"8", 130+=v"99"
        chrome_major = int(self.chrome_ver.split('.')[0])
        if chrome_major < 100:
            not_a_brand_ver = "99"
        elif chrome_major < 110:
            not_a_brand_ver = "99"
        elif chrome_major < 120:
            not_a_brand_ver = "24"
        elif chrome_major < 130:
            not_a_brand_ver = "8"
        elif chrome_major < 140:
            not_a_brand_ver = "99"
        else:
            not_a_brand_ver = "24"
        # Chromium GREASE: 顺序与品牌名也按版本略有变化, 这里采用 Chrome 120 标准格式
        self.sec_ch_ua = f'"Not_A Brand";v="{not_a_brand_ver}", "Chromium";v="{chrome_major}", "Google Chrome";v="{chrome_major}"'
        self.sec_ch_ua_mobile = "?1"
        self.sec_ch_ua_platform = '"Android"'
        # 移动端 Chrome 还会带 Sec-Ch-Ua-Arch / Model / Platform-Version / Bitness
        self.sec_ch_ua_arch = '"arm"'
        self.sec_ch_ua_bitness = '"64"'
        self.sec_ch_ua_full_version = f'"{self.chrome_ver}"'
        self.sec_ch_ua_full_version_list = f'"Not_A Brand";v="{not_a_brand_ver}.0.0.0", "Chromium";v="{self.chrome_ver}", "Google Chrome";v="{self.chrome_ver}"'
        self.sec_ch_ua_model = f'"{self.model}"'
        self.sec_ch_ua_platform_version = f'"{self.android_ver}.0.0"'

        self.language = "zh-CN"
        # 时区与IP归属地对应: 新疆用乌鲁木齐时区, 其余主流为上海时区
        if self.ip_location == "XJ":
            self.timezone = "Asia/Urumqi"
        elif random.random() < 0.9:
            self.timezone = "Asia/Shanghai"
        else:
            self.timezone = random.choice(["Asia/Chongqing", "Asia/Harbin", "Asia/Urumqi"])
        # Accept-Language 联动 timezone (更真实)
        if self.timezone == "Asia/Urumqi":
            self.accept_language = "zh-CN,zh;q=0.9"
        else:
            self.accept_language = "zh-CN,zh;q=0.9,en;q=0.8"

        self.color_depth = "24"  # Android Chrome 固定 24-bit
        self.pixel_ratio = str(self.density)  # 联动屏幕密度, 而非随机
        self.hardware_concurrency = str(self.cpu_cores)
        self.device_memory = str(self.ram_gb)
        self.platform = "Linux armv8l"
        self.vendor = "Google Inc."
        self.webgl_version = "WebGL 2.0"
        self.audio_context_sample_rate = str(random.choice([44100, 48000]))
        self.browser_session_id = "".join(random.choices("abcdef0123456789", k=32))
        self.browser_fp_hash = hashlib.sha256(
            f"{self.android_id}{self.user_agent}{self.screen_width}x{self.screen_height}".encode()
        ).hexdigest()[:32]
        # 移动端 Chrome 真实 referer (H5 SPA, referer 是入口 HTML 而非 API URL)
        self.referer = URL_INDEX

    def _generate_advanced_fingerprints(self):
        """生成高级浏览器指纹 - 使用品牌对应的GPU列表"""
        gpu_list = self.GPU_MAP.get(self.brand_key, self.GPU_MAP["Xiaomi"])
        gpu_info = random.choice(gpu_list)
        self.webgl_vendor = gpu_info['vendor']
        self.webgl_renderer = gpu_info['renderer']

        self.canvas_hash = hashlib.md5(f"{self.model}{self.screen_width}{self.density}".encode()).hexdigest()[:16]
        self.audio_hash = hashlib.md5(f"{self.brand_key}{self.cpu_cores}".encode()).hexdigest()[:16]

    def _generate_imei(self):
        """使用真实TAC码前缀生成符合Luhn算法的IMEI"""
        tac_list = self.IMEI_TAC.get(self.brand_key, self.IMEI_TAC.get("Xiaomi"))
        tac = random.choice(tac_list)
        body = tac + "".join([str(random.randint(0, 9)) for _ in range(6)])
        sum_val = 0
        for i, digit in enumerate(body):
            d = int(digit)
            if i % 2 == 1:
                d *= 2
                if d > 9:
                    d -= 9
            sum_val += d
        check_digit = (10 - (sum_val % 10)) % 10
        return body + str(check_digit)

    def _generate_mac(self):
        """使用真实OUI前缀生成MAC地址"""
        oui_list = self.MAC_OUI.get(self.brand_key, self.MAC_OUI.get("Xiaomi"))
        oui = random.choice(oui_list)
        oui_parts = oui.split(":")
        tail = [f"{random.randint(0, 255):02x}" for _ in range(3)]
        return ":".join(oui_parts + tail)

    def to_dict(self):
        return {
            "brand": self.brand, "model": self.model, "android_id": self.android_id,
            "oaid": self.oaid, "imei": self.imei, "mac": self.mac_address,
            "ip": self.fake_ip, "ua": self.user_agent,
            "screen": f"{self.screen_width}x{self.screen_height}",
            "network": self.network_type, "cpu": self.cpu_cores, "ram": self.ram_gb,
            "webgl_vendor": self.webgl_vendor, "webgl_renderer": self.webgl_renderer,
            "timezone": self.timezone, "color_depth": self.color_depth,
            "pixel_ratio": self.pixel_ratio, "browser_fp": self.browser_fp_hash,
            "device_memory": self.device_memory,
            # 新增字段
            "battery_level": self.battery_level, "is_charging": self.is_charging,
            "battery_temperature": self.battery_temperature, "battery_voltage": self.battery_voltage,
            "battery_health": self.battery_health, "battery_technology": self.battery_technology,
            "network_strength": self.network_strength, "network_operator": self.network_operator,
            "network_country": self.network_country, "network_roaming": self.network_roaming,
            "accelerometer": f"{self.accelerometer_x},{self.accelerometer_y},{self.accelerometer_z}",
            "gyroscope": f"{self.gyroscope_x},{self.gyroscope_y},{self.gyroscope_z}",
            "magnetic": f"{self.magnetic_x},{self.magnetic_y},{self.magnetic_z}",
            "light_sensor": self.light_sensor, "proximity_sensor": self.proximity_sensor,
            "pressure_sensor": self.pressure_sensor,
            "orientation": self.orientation, "screen_brightness": self.screen_brightness,
            "ringer_mode": self.ringer_mode, "is_rooted": self.is_rooted,
            "is_emulator": self.is_emulator, "is_tablet": self.is_tablet,
            "storage_total": self.storage_total, "storage_available": self.storage_available,
            "sd_card": self.sd_card
        }

def create_new_device(province_code=None, carrier_code=None, city_core="") -> DeviceProfile:
    dev = DeviceProfile(province_code=province_code, carrier_code=carrier_code)
    dev.city_core = city_core
    return dev

# ===================== Curl_cffi 会话管理 =====================
class CurlSessionManager:
    # 优化：根据 Android 版本选择最接近的浏览器指纹
    @staticmethod
    def get_profile_for_android(android_ver):
        if android_ver == "10": return "chrome99_android"
        if android_ver == "11": return "chrome100"
        if android_ver == "12": return "chrome116"
        if android_ver == "13": return "chrome131_android"
        return "chrome120"

    @staticmethod
    def create_session(device: DeviceProfile = None):
        profile = CurlSessionManager.get_profile_for_android(device.android_ver) if device else "chrome120"
        
        session = AsyncSession(
            impersonate=profile,
            verify=False,
            timeout=(CONNECT_TIMEOUT, TIMEOUT_SEC)
        )

        if device:
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": device.accept_language,
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Type": "application/json;charset=UTF-8",
                "DNT": "1",
                "Origin": f"https://{DOMAIN}",
                "Referer": URL_INDEX,
                "Sec-Ch-Ua": device.sec_ch_ua,
                "Sec-Ch-Ua-Mobile": device.sec_ch_ua_mobile,
                "Sec-Ch-Ua-Platform": device.sec_ch_ua_platform,
                "Sec-Ch-Ua-Arch": device.sec_ch_ua_arch,
                "Sec-Ch-Ua-Bitness": device.sec_ch_ua_bitness,
                "Sec-Ch-Ua-Model": device.sec_ch_ua_model,
                "Sec-Ch-Ua-Platform-Version": device.sec_ch_ua_platform_version,
                "Sec-Ch-Ua-Full-Version": device.sec_ch_ua_full_version,
                "Sec-Ch-Ua-Full-Version-List": device.sec_ch_ua_full_version_list,
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": device.user_agent,
            }
        else:
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Content-Type": "application/json;charset=UTF-8",
                "Origin": f"https://{DOMAIN}",
                "Referer": URL_INDEX,
                "Sec-Ch-Ua": '"Chromium";v="120", "Google Chrome";v="120", "Not-A.Brand";v="99"',
                "Sec-Ch-Ua-Mobile": "?1",
                "Sec-Ch-Ua-Platform": '"Android"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
        
        if getattr(device, "is_ios", False):
            # iOS Safari 真实客户端不发送这些 Sec-Ch-Ua 扩展头, 移除避免伪造痕迹
            for _k in ("Sec-Ch-Ua-Arch", "Sec-Ch-Ua-Bitness", "Sec-Ch-Ua-Model",
                       "Sec-Ch-Ua-Full-Version", "Sec-Ch-Ua-Full-Version-List"):
                headers.pop(_k, None)

        session.headers.update(headers)
        return session

    @staticmethod
    async def warm_up_session(session, device: DeviceProfile = None):
        # TODO: 填写抓包预热请求
        pass

# ===================== 拟人化延时算法 =====================
def human_delay(base_seconds):
    if base_seconds <= 0:
        base_seconds = 1
    r = random.random()
    if r < 0.92:
        return random.uniform(base_seconds * 0.6, base_seconds * 1.1)
    else:
        return random.uniform(base_seconds * 1.1, base_seconds * 1.6)

def parse_random_range(text, default=0):
    """解析 'min-max' 格式返回随机浮点数，支持 '2'（固定值）或 '0-2'（随机范围）
    - 空字符串或None返回default
    - 格式错误返回default
    - '0-空'或'空-0'等不完整格式返回0
    - 支持运行时动态调节
    """
    if text is None:
        return default
    text = str(text).strip()
    if not text:
        return default
    try:
        if '-' in text:
            parts = text.split('-')
            # 处理 '0-' 或 '-0' 等不完整格式
            lo_str = parts[0].strip()
            hi_str = parts[1].strip() if len(parts) > 1 else ''
            
            # 如果一边为空，另一边有值，则用有值的一边作为固定值
            if lo_str and not hi_str:
                return float(lo_str)
            elif not lo_str and hi_str:
                return float(hi_str)
            elif not lo_str and not hi_str:
                return default
            
            lo = float(lo_str)
            hi = float(hi_str)
            if lo > hi:
                lo, hi = hi, lo
            return random.uniform(lo, hi)
        else:
            return float(text)
    except (ValueError, IndexError):
        return default

# ===================== HTTP请求封装 =====================
async def http_request_async(session, method, url, json_data=None, headers=None, params=None):
    try:
        req_headers = {**session.headers, **(headers or {})}
        
        if method.upper() == "POST":
            resp = await session.post(url, json=json_data, headers=req_headers, params=params)
        else:
            resp = await session.get(url, headers=req_headers, params=params)
            
        return True, resp.text, resp.status_code
    except Exception as e:
        return False, str(e), 0

async def _ensure_index_cookies(session, traffic=None):
    """已实测跳过首页不影响注册/登录: 会话Cookie(PHPSESSID等)由接口请求下发,
    无需拉取首页h5/1.html(省下每号约73KB)。保留函数契约, 直接返回True。"""
    return True

def _looks_like_proxy(t):
    """判断一行文本是否为合法代理(ip:port / user:pwd@ip:port / 带协议前缀), 返回True/False。
    代理API限流时可能返回 '1000:提取过快,你已进入黑名单.' 这类错误信息, 需识别并过滤, 避免被当成IP拉黑"""
    t = (t or "").strip()
    if not t or ":" not in t:
        return False
    s = t
    if "://" in s:
        s = s.split("://", 1)[1]
    hp = s.split("@")[-1]
    host, _, port = hp.rpartition(":")
    if host and port and port.split("/")[0].isdigit():
        return True
    return False

def _extract_proxy_ip(proxy_server):
    """从代理字符串提取IP部分, 兼容 ip:port / user:pwd@ip:port / http://ip:port / socks5://user:pwd@ip:port 等51代理格式"""
    ps = (proxy_server or "").strip()
    if not ps:
        return ""
    if "://" in ps:
        ps = ps.split("://", 1)[1]
    if "@" in ps:
        ps = ps.rsplit("@", 1)[1]
    return ps.split(":")[0]

def _build_proxy_url(proxy_server):
    """构造代理URL, 兼容多个代理软件API格式:
    纯 ip:port → http://ip:port
    user:pwd@ip:port → http://user:pwd@ip:port
    已带协议前缀 → 原样透传(http:// / socks5:// / socks5h:// / https://)"""
    ps = (proxy_server or "").strip()
    if not ps:
        return ""
    if "://" in ps:
        return ps
    return f"http://{ps}"

def _t_up(traffic, payload):
    """累计上行字节(请求体)"""
    if not traffic:
        return
    try:
        data = payload if isinstance(payload, (dict, list, tuple)) else {"data": payload}
        traffic["up"] += len(json.dumps(data, ensure_ascii=False).encode("utf-8"))
    except Exception:
        pass

def _t_down(traffic, resp):
    """累计下行字节(响应体): 优先取Content-Length(压缩后实际/代理计费口径), 不读流式响应正文以免破坏断流省流量"""
    if not traffic or resp is None:
        return
    try:
        cl = resp.headers.get("Content-Length")
        if cl:
            traffic["down"] += int(cl)
            return
    except Exception:
        pass
    try:
        content = getattr(resp, "content", None)
        if content:
            traffic["down"] += len(content)
    except Exception:
        pass

def _t_fmt(traffic):
    """格式化成日志文本"""
    up, down = (traffic or {}).get("up", 0), (traffic or {}).get("down", 0)
    total = up + down
    return f"↑上行{min(up/1024,99999):.1f}KB ↓下行{down/1024:.1f}KB 合计{total/1024:.1f}KB"

# ===================== 业务逻辑函数 =====================

def generate_sign_payload(payload: dict, timestamp: int = None) -> dict:
    # TODO: 填写抓包签名逻辑
    return payload

# ===================== 豪猪接码封装 =====================

def haozhuma_login(user, pwd) -> Tuple[bool, str, str]:
    """登录豪猪接码平台, 返回(成功, token, 余额)"""
    global _haozhuma_token, _haozhuma_logged_in
    url = f"{HAOZHUMA_API}/?api=login&user={user}&pass={pwd}"
    try:
        r = requests.get(url, timeout=15)
        data = r.json()
        if data.get("code") == 0:
            _haozhuma_token = data.get("token", "")
            _haozhuma_logged_in = True
            balance = ""
            summary_url = f"{HAOZHUMA_API}/?api=getSummary&token={_haozhuma_token}"
            r2 = requests.get(summary_url, timeout=15)
            data2 = r2.json()
            if data2.get("code") == 0:
                balance = data2.get("money", "")
            return True, _haozhuma_token, balance
        else:
            return False, "", data.get("msg", "登录失败")
    except Exception as e:
        return False, "", str(e)

def haozhuma_get_phone(sid, token=None, country_code="CN", author="sjxh1122", ascription="") -> str:
    """从豪猪接码取号, 返回手机号, 失败返回空字符串"""
    t = token or _haozhuma_token
    if not t:
        return ""
    url = f"{HAOZHUMA_API}/?api=getPhone&token={t}&sid={sid}&country_code={country_code}&author={author}"
    if ascription:
        url += f"&ascription={ascription}"
    try:
        r = requests.get(url, timeout=15)
        data = r.json()
        if data.get("code") == 0:
            return data.get("phone", "")
        else:
            return ""
    except Exception:
        return ""

def haozhuma_get_message(sid, phone, token=None, country_code="CN") -> str:
    """从豪猪接码取短信验证码, 返回短信内容, 失败返回空字符串"""
    t = token or _haozhuma_token
    if not t:
        return ""
    url = f"{HAOZHUMA_API}/?api=getMessage&token={t}&sid={sid}&country_code={country_code}&phone={phone}"
    try:
        r = requests.get(url, timeout=15)
        data = r.json()
        if data.get("msg") == "success":
            return data.get("sms", "")
        return ""
    except Exception:
        return ""

def haozhuma_get_sms_code(sid, phone, token=None, max_wait=60, interval=2,
                           code_keywords=None) -> str:
    """轮询取短信验证码, 返回验证码, 超时返回空字符串
    max_wait: 最大等待秒数
    interval: 轮询间隔秒数
    code_keywords: 短信模板关键字列表, 用于提取验证码, 如 ['验证码为：', '验证码:']
    """
    if code_keywords is None:
        code_keywords = ["验证码为：", "验证码:", "验证码是", "code is"]
    elapsed = 0
    while elapsed < max_wait:
        sms = haozhuma_get_message(sid, phone, token)
        if sms:
            for kw in code_keywords:
                idx = sms.find(kw)
                if idx >= 0:
                    code_area = sms[idx + len(kw):]
                    match = re.search(r'\d{4,6}', code_area)
                    if match:
                        return match.group(0)
            match = re.search(r'\d{4,6}', sms)
            if match:
                return match.group(0)
        time.sleep(interval)
        elapsed += interval
    return ""

async def haozhuma_login_async(user, pwd) -> Tuple[bool, str, str]:
    """异步登录豪猪（通过to_thread包装）"""
    return await asyncio.to_thread(haozhuma_login, user, pwd)

async def haozhuma_get_phone_async(sid, token=None, country_code="CN",
                                    author="sjxh1122", ascription="") -> str:
    """异步取号"""
    return await asyncio.to_thread(haozhuma_get_phone, sid, token, country_code, author, ascription)

async def haozhuma_get_sms_code_async(sid, phone, token=None, max_wait=60,
                                       interval=2, code_keywords=None) -> str:
    """异步轮询取验证码"""
    return await asyncio.to_thread(
        haozhuma_get_sms_code, sid, phone, token, max_wait, interval, code_keywords
    )

def detect_invite_type(invite_code: str) -> str:
    """自动识别邀请码类型: 11位以1开头的手机号→phone(邀请码手机号), 其余→id(邀请码ID)"""
    code = str(invite_code or "").strip()
    if re.fullmatch(r"1\d{10}", code):
        return "phone"
    return "id"

async def http_register_async(tel, realname, usercard, invite_code, invite_type, dev: DeviceProfile,
                              session, use_proxy: bool, proxy_url: str = "",
                              haozhuma_cfg: dict = None, log_callback=None, reg_pwd="123456",
                              progress_callback=None, traffic=None) -> Tuple[bool, dict, str]:
    """
    注册流程（本网页注册无需短信验证码, 直接提交注册）
    豪猪仅保留取号功能(可选), 不依赖验证码
    haozhuma_cfg: {
        "enabled": True/False,
        "user": "豪猪账号",
        "pass": "豪猪密码",
        "sid": "项目ID",
        "country_code": "CN",
        "author": "sjxh1122",
        "ascription": "2" (虚拟号可选),
        "use_hz_phone": True/False
    }
    progress_callback(step_desc): 每步前调用, 用于更新 UI 状态
    """
    log = log_callback or (lambda msg: None)
    _prog = progress_callback or (lambda s: None)

    use_haozhuma = haozhuma_cfg and haozhuma_cfg.get("enabled", False)
    haozhuma_token = ""

    if use_haozhuma:
        # 1. 豪猪登录（用于取号, 失败不阻塞注册）
        hz_user = haozhuma_cfg.get("user", "")
        hz_pass = haozhuma_cfg.get("pass", "")
        if hz_user and hz_pass:
            log(f"[{tel}] 豪猪登录中...")
            ok_login, token, balance = await haozhuma_login_async(hz_user, hz_pass)
            if not ok_login:
                log(f"[{tel}] 豪猪登录失败: {token}（继续使用本地手机号注册）")
            else:
                haozhuma_token = token
                log(f"[{tel}] 豪猪登录成功, 余额: {balance}元")

                # 2. 如需豪猪取号（替代本地生成的手机号）
                hz_sid = haozhuma_cfg.get("sid", "")
                use_hz_phone = haozhuma_cfg.get("use_hz_phone", False)
                if use_hz_phone and hz_sid:
                    hz_country = haozhuma_cfg.get("country_code", "CN")
                    hz_author = haozhuma_cfg.get("author", "sjxh1122")
                    hz_ascription = haozhuma_cfg.get("ascription", "")
                    log(f"[{tel}] 豪猪取号中...")
                    hz_phone = await haozhuma_get_phone_async(
                        hz_sid, haozhuma_token, hz_country, hz_author, hz_ascription
                    )
                    if hz_phone:
                        tel = hz_phone
                        log(f"[{tel}] 豪猪取号成功: {tel}")
                    else:
                        log(f"[{tel}] 豪猪取号失败，使用本地手机号")

    # 1. 先访问首页获取 Cookie (H5 SPA 入口, Set-Cookie 在此生效; 省流量: 只收Header断流, 失败回退整包)
    _prog("获取首页Cookie...")
    if not await _ensure_index_cookies(session, traffic=traffic):
        return False, {}, "获取首页Cookie失败(未取得Set-Cookie)"

    # 2. 注册预热 GET ApiIndex/reg —— 已确认其返回(warm_data)在本流程中未被使用,
    #    且注册本身不依赖它(实测跳过仍 regist 成功)。跳过以省下每号约71KB配置流量,
    #    不影响注册参数与真实性。仅保留拟人节奏延时。
    _prog("跳过注册预热配置(省71KB/号)...")
    await asyncio.sleep(human_delay(0.6))

    # 3. 提交注册 POST ApiIndex/regsubnew
    # 邀请码ID和邀请码手机号是两种不同的注册包:
    #   邀请码手机号(phone): pid=0, yqcode=邀请码(手机号)  -- 与参考易语言代码一致
    #   邀请码ID(id):       pid=邀请码ID, yqcode=""       -- ID放pid, yqcode留空
    # 平台不发验证码, smscode 固定为 ""
    if invite_type == "id":
        try:
            pid_val = int(invite_code)
        except (ValueError, TypeError):
            pid_val = 0
        reg_payload = {
            "tel": tel,
            "cardtype": 0,
            "realname": realname,
            "usercard": usercard,
            "passport": "",
            "pwd": reg_pwd,
            "smscode": "",
            "pid": pid_val,
            "yqcode": "",
            "regbid": 0,
        }
    else:
        reg_payload = {
            "tel": tel,
            "cardtype": 0,
            "realname": realname,
            "usercard": usercard,
            "passport": "",
            "pwd": reg_pwd,
            "smscode": "",
            "pid": 0,
            "yqcode": invite_code,
            "regbid": 0,
        }
    _prog("提交注册请求...")
    _t_up(traffic, reg_payload)
    try:
        resp = await session.post(_url_with_session(URL_REG_BASE, session), json=reg_payload, timeout=(CONNECT_TIMEOUT, TIMEOUT_SEC))
        _t_down(traffic, resp)
        text = resp.text
    except Exception as e:
        return False, {}, f"注册请求异常: {str(e)}"

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return False, {}, text[:300]

    if data.get("status") == 1:
        return True, data, text
    return False, data, text

async def http_login_async(tel, pwd, session, dev: DeviceProfile, use_proxy: bool, proxy_url: str = "", invite_code: str = "", progress_callback=None, home_loaded: bool = False, traffic=None) -> Tuple[bool, dict, str]:
    """登录: 预热GET ApiIndex/login → 提交POST ApiIndex/loginsub
    home_loaded=True: 注册阶段已拉过首页并建立Cookie(同一会话同一IP), 登录复用跳过重复首页整包下载省流量;
    登录若遇网络异常会自动回退补拉一次首页重试。"""
    _prog = progress_callback or (lambda s: None)
    if not home_loaded:
        _prog("获取登录Cookie...")
        if not await _ensure_index_cookies(session, traffic=traffic):
            return False, {}, "登录前获取Cookie失败(未取得Set-Cookie)"

    # 预热 GET ApiIndex/login
    # 逆向 login.js @ 31502: a.get("ApiIndex/login", {pid, checknickname}, cb)
    _prog("预热登录接口...")
    try:
        warm_payload = {"pid": 0, "checknickname": 0}
        warm_resp = await session.get(URL_LOGIN_WARM, params=warm_payload, timeout=(CONNECT_TIMEOUT, TIMEOUT_SEC))
        _t_down(traffic, warm_resp)
        warm_data = {}
        try:
            warm_data = json.loads(warm_resp.text)
        except Exception:
            warm_data = {}
    except Exception:
        warm_data = {}
    await asyncio.sleep(human_delay(0.6))

    # 逆向 login.js @ 35500 logintype 推导逻辑:
    #   预热响应返回 logintype_1 / logintype_2 / logintype_3 等开关位
    #   if logintype_1 -> logintype = 1 (密码登录)
    #   elif logintype_2 -> logintype = 2 (短信登录)
    #   elif logintype_3 -> logintype = 3 (三方登录)
    #   默认 = 1
    if isinstance(warm_data, dict) and warm_data:
        if warm_data.get("logintype_1"):
            login_type = 1
        elif warm_data.get("logintype_2"):
            login_type = 2
        elif warm_data.get("logintype_3"):
            login_type = 3
        else:
            login_type = 1
    else:
        login_type = 1
    # 参考可用的易语言版登录结构(全自动代码): body = {tel,pwd,logintype,pid,regbid}, 无 smscode/yqcode
    login_payload = {
        "tel": tel,
        "pwd": pwd,
        "logintype": login_type,
        "pid": 0,
        "regbid": 0,
    }
    _prog("提交登录请求...")
    text = ""
    _t_up(traffic, login_payload)
    # 跳过首页时(max_attempts=4): 首次网络异常补拉一次首页(Cookie可能未建全)后重试; 平时最多重试2次
    max_attempts = 4 if home_loaded else 2
    for attempt in range(max_attempts):
        try:
            resp = await session.post(_url_with_session(URL_LOGIN, session), json=login_payload, timeout=(CONNECT_TIMEOUT, TIMEOUT_SEC))
            _t_down(traffic, resp)
            text = resp.text
            break
        except Exception as e:
            if attempt == max_attempts - 1:
                return False, {}, f"登录请求异常: {str(e)}"
            # 跳过首页且首次失败: 回退补拉一次首页再重试
            if home_loaded and attempt == 0:
                try:
                    await _ensure_index_cookies(session, traffic=traffic)
                except Exception:
                    pass
            # 慢代理/网络抖动时自动重试
            await asyncio.sleep(human_delay(0.5))

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return False, {}, text[:300]

    if data.get("status") == 1:
        return True, data, text
    return False, data, text

async def http_sign_async(sid: str, session, dev: DeviceProfile, use_proxy: bool, proxy_url: str = "", progress_callback=None, traffic=None) -> Tuple[bool, dict, str]:
    """签到: 预热GET ApiSign/index → POST ApiSign/signin"""
    _prog = progress_callback or (lambda s: None)
    # 省流量优化: 去掉预热GET ApiSign/index(仅省一次~7KB配置请求, 不影响注册/登录参数/真实性)
    # session_id 由 cookie 维持, 不需要 URL 传 sid
    await asyncio.sleep(human_delay(0.6))

    # POST ApiSign/signin
    # 参考可用的易语言版签到(全自动代码): URL 带 &sid=<sid>&pid=0&scene=1001
    # 逆向 sign.js @ 10682: o.post("ApiSign/signin", {sign_img, sign_video, time, forget}, cb)
    sign_payload = {
        "sign_img": "",
        "sign_video": "",
        "time": "",
        "forget": 0,
    }
    sign_url = URL_SIGN.replace("SID_PLACEHOLDER", str(sid or ""))
    _prog("提交签到请求...")
    _t_up(traffic, sign_payload)
    try:
        resp = await session.post(sign_url, json=sign_payload, timeout=(CONNECT_TIMEOUT, TIMEOUT_SEC))
        _t_down(traffic, resp)
        text = resp.text
    except Exception as e:
        return False, {}, f"签到请求异常: {str(e)}"

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return False, {}, text[:300]

    if data.get("status") == 1:
        return True, data, text
    return False, data, text

# 身份证区划码(6位): 核心市名 -> 区县码列表 (内联自 城市区划码表.py, 单文件运行)
CITY_IDCARD_CODES = {
    # ---- 直辖市 ----
    "北京": ["110101", "110102", "110105", "110108", "110113", "110114"],
    "上海": ["310101", "310104", "310105", "310106", "310107", "310115"],
    "天津": ["120101", "120102", "120103", "120104", "120105", "120110"],
    "重庆": ["500103", "500104", "500105", "500106", "500107", "500112"],
    # ---- 河北 ----
    "石家庄": ["130102", "130104", "130105", "130107", "130108", "130123"],
    "唐山": ["130202", "130203", "130204", "130207", "130208", "130209"],
    "秦皇岛": ["130302", "130303", "130304", "130306"],
    "邯郸": ["130402", "130403", "130404", "130406"],
    "邢台": ["130502", "130503", "130505", "130506"],
    "保定": ["130602", "130603", "130606", "130607"],
    "张家口": ["130702", "130703", "130705", "130706"],
    "承德": ["130802", "130803", "130804", "130805"],
    "沧州": ["130902", "130903", "130921", "130922"],
    "廊坊": ["131002", "131003", "131022", "131023"],
    "衡水": ["131102", "131103", "131121", "131122"],
    # ---- 山西 ----
    "太原": ["140105", "140106", "140107", "140108", "140109", "140110"],
    "大同": ["140213", "140214", "140215", "140221"],
    "阳泉": ["140302", "140303", "140311"],
    "长治": ["140403", "140404", "140405", "140406"],
    "晋城": ["140502", "140521", "140522"],
    "朔州": ["140602", "140603", "140621"],
    "晋中": ["140702", "140721", "140722"],
    "运城": ["140802", "140821", "140822"],
    "忻州": ["140902", "140921", "140922"],
    "临汾": ["141002", "141021", "141022"],
    "吕梁": ["141102", "141121", "141122"],
    # ---- 内蒙古 ----
    "呼和浩特": ["150102", "150103", "150104", "150105", "150121", "150122"],
    "包头": ["150202", "150203", "150204", "150205", "150206", "150207"],
    "乌海": ["150302", "150303", "150304"],
    "赤峰": ["150402", "150403", "150404", "150421"],
    "通辽": ["150502", "150521", "150522"],
    "鄂尔多斯": ["150602", "150603", "150621", "150622"],
    "呼伦贝尔": ["150702", "150721", "150722"],
    "巴彦淖尔": ["150802", "150821", "150822"],
    "乌兰察布": ["150902", "150921", "150922"],
    "兴安": ["152201", "152202", "152221", "152222"],
    "锡林郭勒": ["152501", "152502", "152522", "152523"],
    "阿拉善": ["152921", "152922", "152923"],
    # ---- 辽宁 ----
    "沈阳": ["210102", "210103", "210104", "210105", "210106", "210111"],
    "大连": ["210202", "210203", "210204", "210211", "210212", "210213"],
    "鞍山": ["210302", "210303", "210304", "210311"],
    "抚顺": ["210402", "210403", "210404", "210411"],
    "本溪": ["210502", "210503", "210504", "210505"],
    "丹东": ["210602", "210603", "210604", "210624"],
    "锦州": ["210702", "210703", "210711", "210726"],
    "营口": ["210802", "210803", "210804", "210811"],
    "阜新": ["210902", "210903", "210904", "210905"],
    "辽阳": ["211002", "211003", "211004", "211005"],
    "盘锦": ["211102", "211103", "211104", "211122"],
    "铁岭": ["211202", "211204", "211221", "211223"],
    "朝阳": ["211302", "211303", "211321", "211322"],
    "葫芦岛": ["211402", "211403", "211404", "211421"],
    # ---- 吉林 ----
    "长春": ["220102", "220103", "220104", "220105", "220106", "220112"],
    "吉林": ["220202", "220203", "220204", "220211", "220221"],
    "四平": ["220302", "220303", "220322", "220323"],
    "辽源": ["220402", "220403", "220421", "220422"],
    "通化": ["220502", "220503", "220521", "220523"],
    "白山": ["220602", "220605", "220621", "220622"],
    "松原": ["220702", "220721", "220722", "220723"],
    "白城": ["220802", "220821", "220822", "220881"],
    "延边": ["222401", "222402", "222403", "222404"],
    # ---- 黑龙江 ----
    "哈尔滨": ["230102", "230103", "230104", "230108", "230109", "230110"],
    "齐齐哈尔": ["230202", "230203", "230204", "230205", "230206", "230207"],
    "鸡西": ["230302", "230303", "230304", "230305"],
    "鹤岗": ["230402", "230403", "230404", "230405"],
    "双鸭山": ["230502", "230503", "230505", "230506"],
    "大庆": ["230602", "230603", "230604", "230605"],
    "伊春": ["230702", "230703", "230704", "230705"],
    "佳木斯": ["230802", "230803", "230804", "230805"],
    "七台河": ["230902", "230903", "230904", "230921"],
    "牡丹江": ["231002", "231003", "231004", "231005"],
    "黑河": ["231102", "231123", "231124", "231181"],
    "绥化": ["231202", "231221", "231222", "231223"],
    "大兴安岭": ["232701", "232702", "232703", "232721"],
    # ---- 江苏 ----
    "南京": ["320102", "320104", "320105", "320106", "320111", "320113"],
    "无锡": ["320205", "320206", "320211", "320213", "320214"],
    "徐州": ["320302", "320303", "320305", "320311", "320312"],
    "常州": ["320402", "320404", "320411", "320412", "320413"],
    "苏州": ["320505", "320506", "320507", "320508", "320509", "320581"],
    "南通": ["320602", "320611", "320612", "320613", "320614"],
    "连云港": ["320703", "320706", "320707", "320722"],
    "淮安": ["320812", "320813", "320826", "320830"],
    "盐城": ["320902", "320903", "320904", "320921"],
    "扬州": ["321002", "321003", "321012", "321023"],
    "镇江": ["321102", "321111", "321112", "321181"],
    "泰州": ["321202", "321203", "321204", "321281"],
    "宿迁": ["321302", "321311", "321322", "321323"],
    # ---- 浙江 ----
    "杭州": ["330102", "330105", "330106", "330108", "330109", "330110"],
    "宁波": ["330203", "330205", "330206", "330211", "330212", "330213"],
    "温州": ["330302", "330303", "330304", "330305", "330326"],
    "嘉兴": ["330402", "330411", "330421", "330482"],
    "湖州": ["330502", "330503", "330521", "330522"],
    "绍兴": ["330602", "330603", "330604", "330624"],
    "金华": ["330702", "330703", "330723", "330782"],
    "衢州": ["330802", "330803", "330822", "330881"],
    "舟山": ["330902", "330903", "330921", "330922"],
    "台州": ["331002", "331003", "331004", "331081"],
    "丽水": ["331102", "331121", "331122", "331181"],
    # ---- 安徽 ----
    "合肥": ["340102", "340103", "340104", "340111", "340121", "340122"],
    "芜湖": ["340202", "340207", "340208", "340221", "340222"],
    "巢湖": ["340181", "340202", "340207"],
    "蚌埠": ["340302", "340303", "340304", "340311", "340321"],
    "淮南": ["340402", "340403", "340404", "340405", "340406"],
    "马鞍山": ["340503", "340504", "340506", "340521", "340522"],
    "淮北": ["340602", "340603", "340604", "340621"],
    "铜陵": ["340705", "340706", "340711", "340722"],
    "安庆": ["340802", "340803", "340811", "340822"],
    "黄山": ["341002", "341003", "341004", "341021"],
    "滁州": ["341102", "341103", "341122", "341124"],
    "阜阳": ["341202", "341203", "341204", "341221"],
    "宿州": ["341302", "341321", "341322", "341323"],
    "六安": ["341502", "341503", "341504", "341525"],
    "亳州": ["341602", "341621", "341622", "341623"],
    "池州": ["341702", "341721", "341722", "341723"],
    "宣城": ["341802", "341821", "341822", "341881"],
    # ---- 福建 ----
    "福州": ["350102", "350103", "350104", "350105", "350111", "350112"],
    "厦门": ["350203", "350205", "350206", "350211", "350212", "350213"],
    "莆田": ["350302", "350303", "350304", "350305"],
    "三明": ["350403", "350421", "350424", "350425"],
    "泉州": ["350502", "350503", "350504", "350505", "350521"],
    "漳州": ["350602", "350603", "350604", "350605", "350622"],
    "南平": ["350702", "350703", "350721", "350722"],
    "龙岩": ["350802", "350803", "350821", "350822"],
    "宁德": ["350902", "350921", "350922", "350925"],
    # ---- 江西 ----
    "南昌": ["360102", "360103", "360104", "360111", "360112", "360113"],
    "景德镇": ["360202", "360203", "360222", "360281"],
    "萍乡": ["360302", "360313", "360321", "360322"],
    "九江": ["360402", "360403", "360404", "360423"],
    "新余": ["360502", "360521", "360602", "360603"],
    "鹰潭": ["360602", "360603", "360681"],
    "赣州": ["360702", "360703", "360704", "360723"],
    "吉安": ["360802", "360803", "360821", "360822"],
    "宜春": ["360902", "360921", "360922", "360923"],
    "抚州": ["361002", "361021", "361022", "361023"],
    "上饶": ["361102", "361103", "361104", "361123"],
    # ---- 山东 ----
    "济南": ["370102", "370103", "370104", "370105", "370112", "370113"],
    "青岛": ["370202", "370203", "370211", "370212", "370213", "370214"],
    "淄博": ["370302", "370303", "370304", "370305", "370306"],
    "枣庄": ["370402", "370403", "370404", "370405", "370406"],
    "东营": ["370502", "370503", "370505", "370522"],
    "烟台": ["370602", "370611", "370612", "370613", "370614"],
    "潍坊": ["370702", "370703", "370704", "370705", "370724"],
    "济宁": ["370811", "370812", "370826", "370827"],
    "泰安": ["370902", "370911", "370921", "370923"],
    "威海": ["371002", "371003", "371082", "371083"],
    "日照": ["371102", "371103", "371121", "371122"],
    "临沂": ["371302", "371311", "371312", "371313", "371322"],
    "德州": ["371402", "371403", "371422", "371423"],
    "聊城": ["371502", "371503", "371521", "371522"],
    "滨州": ["371602", "371603", "371621", "371622"],
    "菏泽": ["371702", "371703", "371721", "371722"],
    # ---- 河南 ----
    "郑州": ["410102", "410103", "410104", "410105", "410106", "410108"],
    "开封": ["410202", "410203", "410204", "410205", "410212"],
    "洛阳": ["410302", "410303", "410304", "410305", "410311"],
    "平顶山": ["410402", "410403", "410404", "410411"],
    "安阳": ["410502", "410503", "410505", "410506"],
    "鹤壁": ["410602", "410603", "410611", "410621"],
    "新乡": ["410702", "410703", "410704", "410711"],
    "焦作": ["410802", "410803", "410804", "410811"],
    "濮阳": ["410902", "410922", "410923", "410926"],
    "许昌": ["411002", "411003", "411023", "411024"],
    "漯河": ["411102", "411103", "411104", "411121"],
    "三门峡": ["411202", "411203", "411221", "411222"],
    "南阳": ["411302", "411303", "411321", "411322"],
    "商丘": ["411402", "411403", "411421", "411422"],
    "信阳": ["411502", "411503", "411521", "411522"],
    "周口": ["411602", "411621", "411622", "411623"],
    "驻马店": ["411702", "411721", "411722", "411723"],
    "济源": ["419001"],
    # ---- 湖北 ----
    "武汉": ["420102", "420103", "420104", "420105", "420106", "420111"],
    "黄石": ["420202", "420203", "420204", "420205", "420222"],
    "十堰": ["420302", "420303", "420304", "420322"],
    "宜昌": ["420502", "420503", "420504", "420505"],
    "襄阳": ["420602", "420606", "420607", "420624"],
    "鄂州": ["420702", "420703", "420704"],
    "荆门": ["420802", "420804", "420822", "420881"],
    "孝感": ["420902", "420921", "420922", "420984"],
    "荆州": ["421002", "421003", "421022", "421024"],
    "黄冈": ["421102", "421121", "421122", "421127"],
    "咸宁": ["421202", "421221", "421222", "421224"],
    "随州": ["421302", "421303", "421321", "421381"],
    "恩施": ["422801", "422802", "422822", "422823"],
    "仙桃": ["429004"],
    "潜江": ["429005"],
    "天门": ["429006"],
    "神农架": ["429021"],
    # ---- 湖南 ----
    "长沙": ["430102", "430103", "430104", "430105", "430111", "430112"],
    "株洲": ["430202", "430203", "430204", "430211", "430212"],
    "湘潭": ["430302", "430304", "430321", "430381"],
    "衡阳": ["430405", "430406", "430407", "430408", "430412"],
    "邵阳": ["430502", "430503", "430511", "430522"],
    "岳阳": ["430602", "430603", "430611", "430621"],
    "常德": ["430702", "430703", "430721", "430722"],
    "张家界": ["430802", "430811", "430821", "430822"],
    "益阳": ["430902", "430903", "430921", "430922"],
    "郴州": ["431002", "431003", "431021", "431022"],
    "永州": ["431102", "431103", "431121", "431122"],
    "怀化": ["431202", "431221", "431222", "431223"],
    "娄底": ["431302", "431321", "431322", "431381"],
    "湘西": ["433101", "433122", "433123", "433124"],
    # ---- 广东 ----
    "广州": ["440103", "440104", "440105", "440106", "440111", "440112"],
    "韶关": ["440203", "440204", "440205", "440222", "440224"],
    "深圳": ["440303", "440304", "440305", "440306", "440307", "440308"],
    "珠海": ["440402", "440403", "440404"],
    "汕头": ["440507", "440511", "440512", "440513", "440514"],
    "佛山": ["440604", "440605", "440606", "440607", "440608"],
    "江门": ["440703", "440704", "440705", "440781"],
    "湛江": ["440802", "440803", "440804", "440811"],
    "茂名": ["440902", "440904", "440981", "440982"],
    "肇庆": ["441202", "441203", "441204", "441223"],
    "惠州": ["441302", "441303", "441322", "441323"],
    "梅州": ["441402", "441421", "441422", "441423"],
    "汕尾": ["441502", "441521", "441523", "441581"],
    "河源": ["441602", "441621", "441622", "441623"],
    "阳江": ["441702", "441704", "441721", "441781"],
    "清远": ["441802", "441803", "441821", "441823"],
    "东莞": ["441900"],
    "中山": ["442000"],
    "潮州": ["445102", "445103", "445122"],
    "揭阳": ["445202", "445203", "445222", "445224"],
    "云浮": ["445302", "445303", "445321", "445322"],
    # ---- 广西 ----
    "南宁": ["450102", "450103", "450105", "450107", "450108", "450110"],
    "柳州": ["450202", "450203", "450204", "450205", "450206"],
    "桂林": ["450302", "450303", "450304", "450305", "450311"],
    "梧州": ["450403", "450405", "450406", "450421"],
    "北海": ["450502", "450503", "450512", "450521"],
    "防城港": ["450602", "450603", "450621"],
    "钦州": ["450702", "450703", "450721"],
    "贵港": ["450802", "450803", "450804", "450821"],
    "玉林": ["450902", "450903", "450921", "450922"],
    "百色": ["451002", "451003", "451022", "451023"],
    "贺州": ["451102", "451103", "451121", "451122"],
    "河池": ["451202", "451203", "451221", "451222"],
    "来宾": ["451302", "451321", "451322", "451323"],
    "崇左": ["451402", "451421", "451422", "451423"],
    # ---- 海南 ----
    "海口": ["460105", "460106", "460107", "460108"],
    "三亚": ["460202", "460203", "460204", "460205"],
    "三沙": ["460301", "460302", "460303", "460304"],
    "儋州": ["460401"],
    # ---- 四川 ----
    "成都": ["510104", "510105", "510106", "510107", "510108", "510112"],
    "自贡": ["510302", "510303", "510304", "510311"],
    "攀枝花": ["510402", "510403", "510411", "510421"],
    "泸州": ["510502", "510503", "510504", "510521"],
    "德阳": ["510603", "510623", "510681", "510682"],
    "绵阳": ["510703", "510704", "510705", "510722"],
    "广元": ["510802", "510811", "510812", "510821"],
    "遂宁": ["510903", "510904", "510921", "510922"],
    "内江": ["511002", "511011", "511024", "511025"],
    "乐山": ["511102", "511111", "511112", "511113"],
    "南充": ["511302", "511303", "511304", "511321"],
    "眉山": ["511402", "511403", "511421", "511422"],
    "宜宾": ["511502", "511503", "511504", "511523"],
    "广安": ["511602", "511603", "511621", "511622"],
    "达州": ["511702", "511703", "511722", "511723"],
    "雅安": ["511802", "511803", "511822", "511823"],
    "巴中": ["511902", "511903", "511921", "511922"],
    "资阳": ["512002", "512021", "512022", "512081"],
    "阿坝": ["513221", "513222", "513223", "513224"],
    "甘孜": ["513321", "513322", "513323", "513324"],
    "凉山": ["513401", "513422", "513423", "513424"],
    # ---- 贵州 ----
    "贵阳": ["520102", "520103", "520111", "520112", "520113", "520121"],
    "六盘水": ["520201", "520203", "520221", "520281"],
    "遵义": ["520302", "520303", "520304", "520322"],
    "安顺": ["520402", "520403", "520422", "520423"],
    "毕节": ["520502", "520521", "520522", "520523"],
    "铜仁": ["520602", "520621", "520622", "520623"],
    "黔西南": ["522301", "522302", "522323", "522324"],
    "黔东南": ["522601", "522602", "522622", "522623"],
    "黔南": ["522701", "522702", "522722", "522723"],
    # ---- 云南 ----
    "昆明": ["530102", "530103", "530111", "530112", "530113", "530114"],
    "曲靖": ["530302", "530303", "530304", "530322"],
    "玉溪": ["530402", "530403", "530423", "530424"],
    "保山": ["530502", "530521", "530523", "530524"],
    "昭通": ["530602", "530621", "530622", "530623"],
    "丽江": ["530702", "530721", "530722", "530723"],
    "普洱": ["530802", "530821", "530822", "530823"],
    "临沧": ["530902", "530921", "530922", "530923"],
    "楚雄": ["532301", "532322", "532323", "532324"],
    "红河": ["532501", "532502", "532503", "532523"],
    "文山": ["532601", "532622", "532623", "532624"],
    "西双版纳": ["532801", "532822", "532823"],
    "大理": ["532901", "532922", "532923", "532924"],
    "德宏": ["533103", "533122", "533123", "533124"],
    "怒江": ["533301", "533323", "533324", "533325"],
    "迪庆": ["533401", "533422", "533423"],
    # ---- 西藏 ----
    "拉萨": ["540102", "540103", "540104", "540121"],
    "日喀则": ["540202", "540221", "540222", "540223"],
    "昌都": ["540302", "540321", "540322", "540323"],
    "林芝": ["540402", "540421", "540422", "540423"],
    "山南": ["540502", "540521", "540522", "540523"],
    "那曲": ["540602", "540621", "540622", "540623"],
    # ---- 陕西 ----
    "西安": ["610102", "610103", "610104", "610111", "610112", "610113"],
    "铜川": ["610202", "610203", "610204", "610222"],
    "宝鸡": ["610302", "610303", "610304", "610322"],
    "咸阳": ["610402", "610403", "610404", "610422"],
    "渭南": ["610502", "610503", "610522", "610523"],
    "延安": ["610602", "610603", "610621", "610622"],
    "汉中": ["610702", "610703", "610722", "610723"],
    "榆林": ["610802", "610803", "610822", "610824"],
    "安康": ["610902", "610921", "610922", "610923"],
    "商洛": ["611002", "611021", "611022", "611023"],
    # ---- 甘肃 ----
    "兰州": ["620102", "620103", "620104", "620105", "620111"],
    "嘉峪关": ["620201"],
    "金昌": ["620302", "620321", "620322"],
    "白银": ["620402", "620403", "620421", "620422"],
    "天水": ["620502", "620503", "620521", "620522"],
    "武威": ["620602", "620621", "620622", "620623"],
    "张掖": ["620702", "620721", "620722", "620723"],
    "平凉": ["620802", "620821", "620822", "620823"],
    "酒泉": ["620902", "620921", "620922", "620923"],
    "庆阳": ["621002", "621021", "621022", "621023"],
    "定西": ["621102", "621121", "621122", "621123"],
    "陇南": ["621202", "621221", "621222", "621223"],
    "临夏": ["622901", "622921", "622922", "622923"],
    "甘南": ["623001", "623021", "623022", "623023"],
    # ---- 青海 ----
    "西宁": ["630102", "630103", "630104", "630105", "630106"],
    "海东": ["630202", "630203", "630222", "630223"],
    "海北": ["632221", "632222", "632223", "632224"],
    "黄南": ["632321", "632322", "632323"],
    "海南州": ["632521", "632522", "632523"],
    "果洛": ["632621", "632622", "632623"],
    "玉树": ["632701", "632722", "632723", "632724"],
    "海西": ["632801", "632802", "632821", "632822"],
    # ---- 宁夏 ----
    "银川": ["640104", "640105", "640106", "640121", "640122"],
    "石嘴山": ["640202", "640205", "640221"],
    "吴忠": ["640302", "640303", "640323", "640324"],
    "固原": ["640402", "640422", "640423", "640424"],
    "中卫": ["640502", "640521", "640522"],
    # ---- 新疆 ----
    "乌鲁木齐": ["650102", "650103", "650104", "650105", "650106", "650107"],
    "克拉玛依": ["650202", "650203", "650204", "650205"],
    "吐鲁番": ["650402", "650421", "650422"],
    "哈密": ["650502", "650521", "650522"],
    "昌吉": ["652301", "652302", "652323", "652324"],
    "博尔塔拉": ["652701", "652702", "652722", "652723"],
    "巴音郭楞": ["652801", "652802", "652822", "652823"],
    "阿克苏": ["652901", "652902", "652922", "652923"],
    "克孜勒苏": ["653001", "653022", "653023", "653024"],
    "喀什": ["653101", "653121", "653122", "653123"],
    "和田": ["653201", "653221", "653222", "653223"],
    "伊犁": ["654002", "654003", "654021", "654022"],
    "塔城": ["654201", "654202", "654221", "654222"],
    "阿勒泰": ["654301", "654321", "654322", "654323"],
}

# 身份证行政区划码(6位): 省份代码 -> 常见区县码, 与手机号/IP省份保持一致性
_IDCARD_AREA_CODES = {
    "BJ": ["110101", "110102", "110105", "110108", "110113", "110114"],
    "TJ": ["120101", "120102", "120103", "120104", "120105", "120110"],
    "HE": ["130102", "130104", "130105", "130107", "130108", "130123"],
    "SX": ["140105", "140106", "140107", "140108", "140109", "140110"],
    "NM": ["150102", "150103", "150104", "150105", "150121", "150122"],
    "LN": ["210102", "210103", "210104", "210105", "210106", "210111"],
    "JL": ["220102", "220103", "220104", "220105", "220106", "220112"],
    "HL": ["230102", "230103", "230104", "230106", "230107", "230108"],
    "SH": ["310101", "310104", "310105", "310106", "310107", "310115"],
    "JS": ["320102", "320104", "320105", "320106", "320107", "320111"],
    "ZJ": ["330102", "330103", "330104", "330105", "330106", "330110"],
    "AH": ["340102", "340103", "340104", "340111", "340121", "340122"],
    "FJ": ["350102", "350103", "350104", "350105", "350111", "350112"],
    "JX": ["360102", "360103", "360104", "360111", "360121", "360123"],
    "SD": ["370102", "370103", "370104", "370105", "370112", "370113"],
    "HA": ["410102", "410103", "410104", "410105", "410106", "410108"],
    "HB": ["420102", "420103", "420104", "420105", "420106", "420111"],
    "HN": ["430102", "430103", "430104", "430105", "430111", "430121"],
    "GD": ["440103", "440104", "440105", "440106", "440111", "440305"],
    "GX": ["450102", "450103", "450105", "450107", "450108", "450110"],
    "HI": ["460105", "460106", "460107", "460108"],
    "CQ": ["500103", "500104", "500105", "500106", "500107", "500112"],
    "SC": ["510104", "510105", "510106", "510107", "510108", "510112"],
    "GZ": ["520102", "520103", "520111", "520112", "520113", "520115"],
    "YN": ["530102", "530103", "530111", "530112", "530113", "530114"],
    "XZ": ["540102", "540103", "540121", "540122"],
    "SN": ["610102", "610103", "610104", "610111", "610112", "610113"],
    "GS": ["620102", "620103", "620104", "620105", "620111", "620121"],
    "QH": ["630102", "630103", "630104", "630105", "630121", "630122"],
    "NX": ["640104", "640105", "640106", "640121", "640122"],
    "XJ": ["650102", "650103", "650104", "650105", "650106", "650121"],
}

# ===================== 后台任务线程 =====================
class WorkThread(QThread):
    log_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()
    pre_reg_signal = pyqtSignal(str, str, str, str, str, str)
    update_reg_signal = pyqtSignal(str, str, str)          # (tel, ip, status) 用手机号定位行, 避免任务完成顺序与行号错位
    update_card_signal = pyqtSignal(str, str, str)         # (tel, name, card) 重试时更新已有行的姓名/身份证
    update_tel_signal = pyqtSignal(str, str, str, str)     # (old_tel, new_tel, name, card) 手机号已注册时换新号并更新已有行
    update_yang_status_signal = pyqtSignal(int, str, str)
    progress_signal = pyqtSignal(int, int)
    stats_signal = pyqtSignal(int, int, int)   # (成功数, 失败数, 总数) 实时成功率/速度/预计剩余统计
    batch_progress_signal = pyqtSignal(str)    # 批量注册实时进度快照(文本, 直接显示)
    task_break_signal = pyqtSignal(str)
    notify_signal = pyqtSignal(str)   # 一次性通知(如代理耗尽降级虚拟IP): 弹提示框但不影响任务
    clear_reg_table_signal = pyqtSignal() # 新增：清空注册表信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_running = False
        self.task_type = TASK_REGISTER
        self.account_list = []
        self.config = {}
        self.continuous_fail = 0
        self.lock = threading.Lock()
        self.completed_count = 0
        self.total_count = 0
        self.stop_event = None
        self._task_list = []
        # 本批任务已使用过的代理IP: 批次内同一IP最多复用到配额, 避免同IP过多重复注册
        self._proxy_limit_until = 0.0  # 代理API限流退避截止时间(时间戳): 检测到'提取过快/黑名单'时设置, 取号前等待到该时刻
        self.used_proxy_ips = {}  # 批次内IP使用次数统计 {ip: 次数}: 用于尽量分散取不同IP, 池子不够时允许复用
        self._no_proxy_notified = False  # "API取号失败降级虚拟IP" 一次性提示标志(每批任务只提示一次)

    async def _interruptible_sleep(self, seconds):
        """可中断的异步睡眠，收到停止信号时跳过等待继续执行"""
        if self.stop_event is None:
            self.stop_event = asyncio.Event()
        sleep_task = None
        try:
            sleep_task = asyncio.create_task(asyncio.sleep(seconds))
            self._task_list.append(sleep_task)
            done, _ = await asyncio.wait(
                [sleep_task, asyncio.create_task(self.stop_event.wait())],
                return_when=asyncio.FIRST_COMPLETED
            )
            if self.stop_event.is_set():
                for t in done:
                    if not t.done():
                        t.cancel()
                return True
            return True
        except asyncio.CancelledError:
            return True
        except Exception:
            return not self.stop_event.is_set()
        finally:
            if sleep_task and sleep_task in self._task_list:
                self._task_list.remove(sleep_task)

    def _live_thread_count(self, default=5):
        """运行时动态读取当前并发线程数(运行中修改UI立即生效), 限制1-99"""
        try:
            n = int(self.config.get("thread_count", default))
        except (TypeError, ValueError):
            n = default
        return max(1, min(n, 99))

    def _append_account_to_file(self, file_path, line):
        """即时追加一行到文件(防崩溃丢数据, 跨进程文件锁保证多软件并发写同一文件不丢数据)"""
        if not line:
            return
        try:
            folder = os.path.dirname(file_path)
            if folder and not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)
            line_to_write = line if line.endswith("\n") else line + "\n"
            # 用独立 lock 文件做跨进程互斥, 避免直接锁数据文件的指针问题
            lock_path = file_path + ".lock"
            with open(lock_path, "a", encoding="utf-8") as lock_f:
                _file_lock(lock_f)
                try:
                    with open(file_path, "a", encoding="utf-8") as f:
                        f.write(line_to_write)
                        f.flush()
                        try:
                            os.fsync(f.fileno())
                        except OSError:
                            pass
                finally:
                    _file_unlock(lock_f)
        except PermissionError:
            self.log_signal.emit(f"⚠️文件被占用，保存失败：{os.path.basename(file_path)}")
        except Exception as e:
            self.log_signal.emit(f"文件写入异常：{str(e)}")

    def _emit_batch_progress(self):
        """批量注册实时进度快照: 按提交的每一行分别显示 成功/失败/剩余 (同名邀请码也分开)"""
        if not self._batch_entries:
            return
        total_target = sum(n for _, n in self._batch_entries)
        total_done = sum(self._batch_done)
        lines = []
        for ei, (code, n) in enumerate(self._batch_entries):
            ok = self._batch_done[ei]
            fail = self._batch_fail[ei]
            left = max(0, n - ok - fail)
            lines.append(f"    {code}: 成功{ok}/{n} 失败{fail} 剩余{left}")
        self.batch_progress_signal.emit(f"批量进度 已完成 {total_done} / {total_target}\n" + "\n".join(lines))

    def _save_register_result(self, result, invite):
        """单个账号注册结果即时落盘(成功/失败/签到成功分别写入对应文件)"""
        if not result or not isinstance(result, dict):
            return
        tel = result.get("tel", "")
        name = result.get("name", "")
        card = result.get("card", "")
        pwd = result.get("pwd", "")
        status = result.get("status", "")
        if not tel:
            return
        if result.get("success"):
            suc_path = os.path.join(REG_SUCCESS_FOLDER, f"注册成功{invite}.txt")
            self._append_account_to_file(suc_path, f"{tel}----{name}----{card}")
            # 所有注册成功的账号都保存进签到专用(含密码), 便于后续手动签到
            sign_path = os.path.join(REG_SIGN_FOLDER, f"注册成功{invite}签到专用.txt")
            self._append_account_to_file(sign_path, f"{tel}----{pwd}")
        else:
            fail_path = os.path.join(REG_FAIL_FOLDER, f"注册失败{invite}.txt")
            self._append_account_to_file(fail_path, f"{tel}----{name}----{card} 原因:{status}")

    def _save_sign_result(self, result, suc_file, fail_file):
        """单个账号签到结果即时落盘"""
        if not result or not isinstance(result, dict):
            return
        tel = result.get("tel", "")
        pwd = result.get("pwd", "")
        if not tel:
            return
        if result.get("success"):
            self._append_account_to_file(suc_file, f"{tel}----{pwd}")
        else:
            self._append_account_to_file(fail_file, f"{tel}----{pwd}")

    def run(self):
        self.is_running = True
        self.continuous_fail = 0
        self.completed_count = 0
        self.stop_event = asyncio.Event()
        self._task_list = []
        try:
            if self.task_type in (TASK_REGISTER, TASK_REGISTER_ONLY):
                asyncio.run(self.run_register_async())
            elif self.task_type == TASK_SIGN:
                asyncio.run(self.run_sign_async())
        except Exception as e:
            self.log_signal.emit(f"⚠️ 任务线程异常(任务已结束, 软件保持运行): {str(e)}")
            _write_crash_log(*sys.exc_info())
        finally:
            self.finish_signal.emit()
            self.is_running = False

    def _test_proxy_sync(self, proxy_server, test_url=None, connect_timeout=4, total_timeout=5):
        """同步测试代理是否可用, 快速过滤死代理, 避免等到15秒连接超时才失败. 返回 True/False.
        预检统一用百度做探测(更贴近真实外网访问), 5秒内拿不到响应即判定该IP不可用并放弃;
        只读取响应头即判定可用(stream+立即关闭), 不下载页面正文, 既省时间也省流量;
        不影响真实注册请求(注册/登录/签到仍为完整请求)"""
        if not proxy_server:
            return False
        proxy_url = _build_proxy_url(proxy_server)
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        baidu_urls = ["http://www.baidu.com", test_url or f"https://{DOMAIN}/h5/1.html"]
        # socks5 代理: requests 无 PySocks, 改用 curl_cffi 同步测试(curl 原生支持 socks5)
        if proxy_url.startswith(("socks5", "socks5h")):
            try:
                from curl_cffi.requests import Session as CurlCffiSession
                for url in baidu_urls:
                    try:
                        with CurlCffiSession() as cs:
                            cs.proxies = proxies
                            r = cs.get(url, timeout=connect_timeout)
                        if r.status_code in (200, 301, 302, 304, 403, 404):
                            return True
                    except Exception:
                        continue
                return False
            except Exception:
                return False
        try:
            import requests as req_lib
            # 优先测百度, 失败再退到通用检测站; 5秒内无响应即放弃
            for fu in baidu_urls:
                try:
                    with req_lib.get(fu, proxies=proxies, timeout=(connect_timeout, total_timeout),
                                    headers={"User-Agent": "Mozilla/5.0"}, verify=False, stream=True) as r:
                        status = r.status_code
                        r.close()
                    if status in (200, 301, 302, 304, 403, 404):
                        return True
                except Exception:
                    continue
            # 兜底: 用公共检测站
            fallback_urls = ["http://httpbin.org/get", "http://www.baidu.com"]
            for fu in fallback_urls:
                try:
                    with req_lib.get(fu, proxies=proxies, timeout=(connect_timeout, total_timeout),
                                    headers={"User-Agent": "Mozilla/5.0"}, stream=True) as r:
                        status = r.status_code
                        r.close()
                    if status in (200, 301, 302):
                        return True
                except Exception:
                    continue
            return False
        except Exception:
            return False

    async def _test_proxy(self, proxy_server, test_url=None):
        return await asyncio.to_thread(self._test_proxy_sync, proxy_server, test_url)

    async def _get_good_proxy(self, api_url, max_try=5, test_url=None, log_callback=None, prefix=""):
        """取代理+预检, 取号失败或预检失败都继续重试, 最多 max_try 次, 失败返回空串。
        同批次IP尽量不重复(优先取全新的), 但池子IP不够时允许复用已用IP, 不做跨批/累计记录"""
        dup_skip = 0
        max_loop = max_try + 13
        for i in range(max_loop):
            if not self.is_running:
                return ""
            # 代理API限流退避: 检测到'提取过快/黑名单'后, 所有线程统一等待到退避时刻再取号, 避免疯狂刷号被锁库
            wait = self._proxy_limit_until - time.time()
            if wait > 0:
                if log_callback:
                    log_callback(f"{prefix}🕐 检测到代理API限流, 等待{int(wait) + 1}秒后继续取号...")
                await asyncio.to_thread(time.sleep, min(wait + 1, 15))
                continue
            proxy = await self._get_proxy_with_retry(api_url)
            if not proxy:
                if log_callback:
                    log_callback(f"{prefix}⚠️ 代理取号失败, 重试...({i + 1}/{max_try})")
                await asyncio.to_thread(time.sleep, human_delay(0.5))
                continue
            ip_part = _extract_proxy_ip(proxy)
            with self.lock:
                used = self.used_proxy_ips.get(ip_part, 0)
                self.used_proxy_ips[ip_part] = used + 1  # 记录本批使用次数(用于尽量分散)
            # 同批可重复但尽可能不重复: 该IP本批已用过, 且还没积累太多重复时, 再抽一次新IP碰运气;
            # 但若连续多次(dup_skip>=8)抽到的都是已用IP, 说明池子IP不够, 直接复用不再死等
            if used > 0 and dup_skip < 8:
                dup_skip += 1
                await asyncio.to_thread(time.sleep, human_delay(0.2))
                continue
            dup_skip = 0
            ok = await self._test_proxy(proxy, test_url=test_url)
            if ok:
                return proxy
            # 预检失败: 释放本次记录(该IP仍可被本批其他账号复用)
            with self.lock:
                v = self.used_proxy_ips.get(ip_part, 1)
                self.used_proxy_ips[ip_part] = max(1, v - 1)
            if log_callback:
                log_callback(f"{prefix}⚠️ 代理{proxy} 预检失败, 换一个...({i + 1}/{max_try})")
        return ""

    def _get_proxy_sync(self, api_url):
        import requests as req_lib
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        for t in range(2):
            if not self.is_running:
                return ""
            try:
                r = req_lib.get(api_url, timeout=15)
                text = r.text
                lines = text.splitlines()
                proxy_server = lines[0].strip() if lines else ""
                # 兼容JSON格式代理API(如 syhttp): {"code":0,"data":[{"ip":"..","port":123}]}
                if proxy_server.startswith("{"):
                    try:
                        obj = json.loads(text)
                        data = obj.get("data") or []
                        if obj.get("success") and data:
                            it = data[0]
                            if it.get("ip") and it.get("port"):
                                return f"{it['ip']}:{it['port']}"
                        if not obj.get("success"):
                            msg = str(obj.get("msg", ""))
                            # 白名单待更新/限流: 短暂退避, 不疯狂重试
                            if ("白名单" in msg or "等待更新" in msg or "太快" in msg):
                                self._proxy_limit_until = time.time() + 10.0
                    except Exception:
                        pass
                elif proxy_server and _looks_like_proxy(proxy_server):
                    return proxy_server
                if proxy_server:
                    # 代理API返回非代理信息(常见为限流错误, 如 '1000:提取过快,你已进入黑名单.'/'代理1000'等):
                    # 触发全局退避, 避免多线程疯狂取号再次锁进黑名单; 该类信息绝不当代理解析/拉黑
                    if ("提取过快" in proxy_server or "黑名单" in proxy_server
                            or "频繁" in proxy_server or "限制" in proxy_server
                            or proxy_server.startswith("1000")):
                        self._proxy_limit_until = time.time() + 12.0  # 全局退避12秒, 让代理池恢复
                    time.sleep(human_delay(0.5))
            except Exception:
                time.sleep(human_delay(0.3))
        return ""

    async def _get_proxy_with_retry(self, api_url):
        # 支持填两个代理API(主API + proxy_api2): 随机打乱顺序实现"轮流取号",
        # 每个账号只从其中一个API取IP(不多取不浪费配额): 先从随机选中的API取, 取空才fallback另一个, 两个都空返回""
        candidates = []
        for u in (api_url, self.config.get("proxy_api2", "")):
            u = (u or "").strip()
            if u and u not in candidates:
                candidates.append(u)
        if not candidates:
            return ""
        random.shuffle(candidates)
        for a in candidates:
            r = await asyncio.to_thread(self._get_proxy_sync, a)
            if r:
                return r
        return ""

    async def _process_single_registration(self, row_idx, total, tel, name, card, dev, pre_fetched_proxy="", invite=None, invite_type="auto"):
        use_proxy = self.config.get("use_proxy", False)
        api_proxy = self.config.get("proxy_api", "")
        if invite is None:
            invite = self.config.get("invite", "")
            invite_type = self.config.get("invite_type", "auto")
        if invite_type == "auto":
            invite_type = detect_invite_type(invite)
            self.log_signal.emit(f"第{row_idx + 1}组 >> 自动识别邀请码[{invite}]类型: {'手机号' if invite_type == 'phone' else 'ID'}")
        else:
            self.log_signal.emit(f"第{row_idx + 1}组 >> 邀请码[{invite}] 类型: {'手机号' if invite_type == 'phone' else 'ID'}")
        reg_pwd = self.config.get("reg_pwd", "123456")
        traffic = {"up": 0, "down": 0}   # 本号消耗流量统计(仅日志显示, 不落盘)

        proxy_server = pre_fetched_proxy
        current_ip = dev.fake_ip
        # 注册用IP归属地(省份中文+城市) 用于表格IP列展示 "IP(地区)"
        try:
            reg_loc = (getattr(dev, "ip_location_cn", "") or "") + (getattr(dev, "city_core", "") or "")
        except Exception:
            reg_loc = ""
        session = None
        effective_use_proxy = use_proxy

        try:
            # 1. 获取代理 (如果 bounded_process 已预取则直接使用)
            if use_proxy and api_proxy.strip() and proxy_server != "__NO_PROXY__":
                if not proxy_server:
                    proxy_server = await self._get_proxy_with_retry(api_proxy)
                if not proxy_server:
                    msg = f"第{row_idx + 1}组 >> 获取代理失败，跳过账号 {tel}"
                    self.log_signal.emit(msg)
                    self.update_reg_signal.emit(tel, f"{current_ip}({reg_loc})", "代理获取失败")
                    with self.lock:
                        self.continuous_fail += 1
                        fail_count = self.continuous_fail
                    if fail_count >= CONTINUOUS_FAIL_THRESHOLD:
                        self.task_break_signal.emit(f"连续{fail_count}次获取代理失败，任务自动终止！")
                        self.is_running = False
                    return {"success": False, "tel": tel, "pwd": reg_pwd, "name": name,
                            "card": card, "status": "代理获取失败", "ip": current_ip, "raw": "", "row_idx": row_idx}

                ip_part = _extract_proxy_ip(proxy_server)
                # 归属地未知时(use_real_ip=False)保留与资料同省的模拟IP, 避免跨省不一致
                if getattr(dev, "use_real_ip", True):
                    dev.fake_ip = ip_part
                    current_ip = ip_part
                self.update_reg_signal.emit(tel, f"{current_ip}({reg_loc})", "注册中...")
            else:
                if proxy_server == "__NO_PROXY__":
                    effective_use_proxy = False

            # 2. 创建 Session 并预热
            session = CurlSessionManager.create_session(device=dev)
            
            if use_proxy and proxy_server and proxy_server != "__NO_PROXY__":
                session.proxies = {
                    "http": _build_proxy_url(proxy_server),
                    "https": _build_proxy_url(proxy_server)
                }

            await CurlSessionManager.warm_up_session(session, device=dev)

            log_info = f"[IP:{current_ip}][{dev.ip_location_cn} {dev.ip_carrier_cn}][{dev.brand} {dev.model}]"
            self.log_signal.emit(f"第{row_idx + 1}组 [{tel}] 开始注册 {log_info}")

            # 3. 执行注册 (身份证已注册时最多重试5次)
            haozhuma_cfg = self.config.get("haozhuma", None)
            ok_reg = False
            resp_data = {}
            raw_text = ""
            max_retry = 5
            province_code = getattr(dev, "province_code", "")

            for reg_attempt in range(max_retry):
                if reg_attempt > 0:
                    # 重新生成新的身份证和姓名
                    name = gen_chinese_name()
                    card = self._generate_fake_idcard(province_code=province_code, city=getattr(dev, "city_core", ""))
                    # 重试只更新已有行的姓名/身份证, 不再新增表格行(避免行数多于任务总数)
                    self.update_card_signal.emit(tel, name, card)
                    self.log_signal.emit(f"第{row_idx + 1}组 >> 第{reg_attempt + 1}次重试: 新身份证={card} 新姓名={name}")

                ok_reg, resp_data, raw_text = await http_register_async(
                    tel, name, card, invite, invite_type, dev, session, effective_use_proxy, proxy_server,
                    haozhuma_cfg=haozhuma_cfg, log_callback=self.log_signal.emit, reg_pwd=reg_pwd,
                    progress_callback=lambda s, _t=tel, _ip=current_ip: self.update_reg_signal.emit(_t, f"{_ip}({reg_loc})", s),
                    traffic=traffic
                )

                # 注册成功直接跳出循环
                if ok_reg and resp_data.get("status") == 1:
                    break

                # 检测错误类型: 手机号已注册 / 身份证已注册 / 网络错误
                msg_text = (resp_data.get("msg", "") if isinstance(resp_data, dict) else "") + raw_text
                is_phone_dup = any(k in msg_text for k in [
                    "该账号已注册", "账号已注册", "请直接登录", "该号码已注册",
                    "号码已注册", "手机号已注册", "手机号码已注册"
                ])
                is_card_dup = (not is_phone_dup) and any(k in msg_text for k in [
                    "身份证", "usercard", "证件", "已注册", "已存在", "已绑定", "重复", "该号码已"
                ])
                # 网络类错误(超时/连接失败/代理异常): 换新代理重试, 不判死
                is_net_err = (not resp_data) and any(k in raw_text for k in [
                    "timeout", "timed out", "超时", "curl: (", "Connection", "连接失败",
                    "Could not resolve", "proxy", "代理", "Failed to perform"
                ])

                if not is_phone_dup and not is_card_dup and not is_net_err:
                    break

                # 网络类错误: 重新取代理+预检通过后再重试, 避免连续踩死代理等15秒
                if is_net_err:
                    self.log_signal.emit(f"第{row_idx + 1}组 >> 网络异常, 换代理重试: {raw_text[:120]}")
                    if use_proxy and api_proxy.strip():
                        new_proxy = await self._get_good_proxy(
                            api_proxy, max_try=5, log_callback=self.log_signal.emit,
                            prefix=f"第{row_idx + 1}组 >> "
                        )
                        if new_proxy:
                            proxy_server = new_proxy
                            session.proxies = {
                                "http": _build_proxy_url(new_proxy),
                                "https": _build_proxy_url(new_proxy)
                            }
                            dev.fake_ip = _extract_proxy_ip(new_proxy)
                            current_ip = dev.fake_ip
                    if reg_attempt < max_retry - 1:
                        continue
                    else:
                        self.log_signal.emit(f"第{row_idx + 1}组 >> 网络异常重试{max_retry}次，全部失败")
                        break

                # 手机号已注册: 重新生成一个与IP/身份证同省市一致的新手机号后重试(与身份证重复同理)
                if is_phone_dup:
                    old_tel = tel
                    new_carrier = None
                    city_matched = False
                    for _ in range(5):
                        cand, new_carrier, new_city, city_matched = gen_phone_for_ip(
                            getattr(dev, "province_code", ""), getattr(dev, "city_core", ""))
                        if cand and cand != old_tel:
                            break
                    if not cand or cand == old_tel:
                        self.log_signal.emit(f"第{row_idx + 1}组 >> 手机号已注册且无法生成新号, 判定失败: {raw_text[:120]}")
                        break
                    tel = cand
                    if new_carrier:
                        dev.ip_carrier = new_carrier
                        dev.ip_carrier_cn = CARRIER_CN_MAP.get(new_carrier, new_carrier)
                    # 三地一致: 新手机号所在市与IP市一致则保持市一致; 不一致则降为省一致,
                    # 身份证改按省生成, 保证 手机号/身份证/IP 三者同省一致
                    if not city_matched:
                        dev.city_core = ""
                    self.update_tel_signal.emit(old_tel, tel, name, card)
                    self.log_signal.emit(f"第{row_idx + 1}组 >> 手机号已注册, 换新号 {old_tel} → {tel} {'市一致' if city_matched else '省一致'} 重试")
                    if reg_attempt < max_retry - 1:
                        continue
                    else:
                        self.log_signal.emit(f"第{row_idx + 1}组 >> 手机号已注册换号重试{max_retry}次，全部失败")
                        break

                # 身份证重复，继续循环重试
                if reg_attempt < max_retry - 1:
                    self.log_signal.emit(f"第{row_idx + 1}组 >> 身份证重复: {raw_text}")
                    continue
                else:
                    self.log_signal.emit(f"第{row_idx + 1}组 >> 身份证重复{max_retry}次，全部失败")
                    break

            log_prefix = f"第{row_idx + 1}组 [{tel}] IP:{current_ip}"

            if not ok_reg or resp_data.get("status") != 1:
                with self.lock:
                    self.continuous_fail += 1
                    fail_count = self.continuous_fail
                if fail_count >= CONTINUOUS_FAIL_THRESHOLD:
                    self.task_break_signal.emit(f"连续{fail_count}次注册失败，疑似IP封禁，任务终止！")
                    self.is_running = False

                log_msg = f"{log_prefix} 注册失败: {raw_text}"
                self.log_signal.emit(log_msg)
                self.log_signal.emit(f"{log_prefix} 注册失败 >> 本号流量: {_t_fmt(traffic)}")
                self.update_reg_signal.emit(tel, f"{current_ip}({reg_loc})", "注册失败")
                return {"success": False, "tel": tel, "pwd": reg_pwd, "name": name,
                        "card": card, "status": "注册失败", "ip": current_ip, "raw": raw_text, "row_idx": row_idx}

            with self.lock:
                self.continuous_fail = 0

            if self.task_type == TASK_REGISTER_ONLY:
                # 仅注册任务: 注册成功即完成, 不进行登录/签到 (仍即时落盘保存)
                final_status = "注册成功(仅注册)"
                self.update_reg_signal.emit(tel, f"{current_ip}({reg_loc})", final_status)
                self.log_signal.emit(f"{log_prefix} {final_status} >> 本号流量: {_t_fmt(traffic)}")
                return {"success": True, "tel": tel, "pwd": reg_pwd, "name": name,
                        "card": card, "status": final_status, "ip": current_ip,
                        "raw": raw_text, "row_idx": row_idx}

            self.log_signal.emit(f"{log_prefix} 注册成功，准备登录签到...")

            # 5. 登录 (账号已注册成功, 遇网络/代理异常自动换新代理重试, 避免死代理误判登录失败)
            ok_login, login_data, login_raw = False, {}, ""
            for login_attempt in range(5):
                ok_login, login_data, login_raw = await http_login_async(
                    tel, reg_pwd, session, dev, effective_use_proxy, proxy_server, invite,
                    progress_callback=lambda s, _t=tel, _ip=current_ip: self.update_reg_signal.emit(_t, f"{_ip}({reg_loc})", s),
                    home_loaded=True, traffic=traffic
                )
                if ok_login and login_data.get("status") == 1:
                    break

                # 网络/代理类错误(超时/连接失败/CONNECT 403/407/代理拒连): 换新代理重试
                _lb = login_raw or (login_data.get("msg", "") if isinstance(login_data, dict) else "")
                _is_log_net = any(k in _lb for k in [
                    "timeout", "timed out", "超时", "curl: (", "Connection", "连接失败",
                    "Could not resolve", "proxy", "代理", "Failed to perform", "CONNECT"
                ])
                if not _is_log_net:
                    break  # 业务类失败(账号/密码错误等)不换代理, 直接判定失败

                self.log_signal.emit(f"{log_prefix} 登录网络异常, 换代理重试({login_attempt + 1}/5): {_lb[:120]}")
                if use_proxy and api_proxy.strip():
                    newp = await self._get_good_proxy(
                        api_proxy, max_try=5, log_callback=self.log_signal.emit,
                        prefix=f"第{row_idx + 1}组 >> "
                    )
                    if newp:
                        proxy_server = newp
                        session.proxies = {
                            "http": _build_proxy_url(newp),
                            "https": _build_proxy_url(newp)
                        }
                        dev.fake_ip = _extract_proxy_ip(newp)
                        current_ip = dev.fake_ip
                        self.update_reg_signal.emit(tel, f"{current_ip}({reg_loc})", "登录换代理")
                        log_prefix = f"第{row_idx + 1}组 [{tel}] IP:{current_ip}"

            if not ok_login or login_data.get("status") != 1:
                log_msg = f"{log_prefix} 注册成功但登录失败: {login_raw}"
                self.log_signal.emit(log_msg)
                self.log_signal.emit(f"{log_prefix} 登录失败 >> 本号流量: {_t_fmt(traffic)}")
                self.update_reg_signal.emit(tel, f"{current_ip}({reg_loc})", "注册成功登录失败")
                return {"success": True, "tel": tel, "pwd": reg_pwd, "name": name,
                        "card": card, "status": "注册成功登录失败", "ip": current_ip,
                        "raw": login_raw, "row_idx": row_idx}

            sid = login_data.get("session_id", "")
            if not sid:
                log_msg = f"{log_prefix} 登录成功但缺失session_id"
                self.log_signal.emit(log_msg)
                self.update_reg_signal.emit(tel, f"{current_ip}({reg_loc})", "注册成功无SID")
                return {"success": True, "tel": tel, "pwd": reg_pwd, "name": name,
                        "card": card, "status": "注册成功无SID", "ip": current_ip,
                        "raw": login_raw, "row_idx": row_idx}

            self.log_signal.emit(f"{log_prefix} 登录成功，准备签到...")

            # 6. 签到
            ok_sign, sign_data, sign_raw = await http_sign_async(sid, session, dev, effective_use_proxy, proxy_server,
                progress_callback=lambda s, _t=tel, _ip=current_ip: self.update_reg_signal.emit(_t, f"{_ip}({reg_loc})", s),
                traffic=traffic
            )

            final_status = ""
            if ok_sign:
                if sign_data.get("status") == 1:
                    final_status = "注册成功签到成功"
                    self.log_signal.emit(f"{log_prefix} ✅签到成功")
                else:
                    msg_content = sign_data.get("msg", "")
                    if "已签到" in msg_content or "重复" in msg_content or "today" in msg_content.lower():
                        final_status = "注册成功今日已签到"
                        self.log_signal.emit(f"{log_prefix} 今日已签到（平台已签到状态）")
                    else:
                        final_status = "注册成功签到失败"
                        self.log_signal.emit(f"{log_prefix} 签到失败: {sign_raw}")
            else:
                final_status = "注册成功签到失败"
                self.log_signal.emit(f"{log_prefix} 签到请求异常: {sign_raw}")

            self.update_reg_signal.emit(tel, f"{current_ip}({reg_loc})", final_status)
            self.log_signal.emit(f"{log_prefix} {final_status} >> 本号流量: {_t_fmt(traffic)}")

            return {
                "success": True, "tel": tel, "pwd": reg_pwd, "name": name,
                "card": card, "status": final_status, "ip": current_ip,
                "raw": sign_raw if ok_sign else login_raw, "row_idx": row_idx
            }
        finally:
            if session:
                try:
                    await session.close()
                except Exception:
                    pass
    async def run_register_async(self):
        # 批量注册(仅注册): 邀请码----数量, 数量以填写为准; 多邀请码打乱交叉做, 线程随机分配到待做数据
        batch = self.config.get("batch_invites", [])
        if batch:
            total = 0
            self._invite_plan = []
            # 按提交的每一行分别统计(同名邀请码分多行也各自显示, 不合并)
            self._batch_entries = batch          # [(邀请码, 数量), ...] 保持提交顺序
            self._batch_done = [0] * len(batch)
            self._batch_fail = [0] * len(batch)
            self.log_signal.emit("🟢 已开启批量注册(仅注册), 数量以「邀请码----数量」为准")
            for ei, (code, n) in enumerate(batch):
                t = detect_invite_type(code)
                total += int(n)
                self.log_signal.emit(f"📋 批量: 邀请码[{code}] 类型={'手机号' if t == 'phone' else 'ID'} 注册{n}个")
                self._invite_plan.extend([(code, t, ei)] * int(n))
            random.shuffle(self._invite_plan)  # 打乱: 多个邀请码交叉做, 线程随机分配, 互不影响
            self._emit_batch_progress()
        else:
            total = int(self.config.get("count", 10))
            self._invite_plan = None
            self._batch_entries = []
            self._batch_done = []
            self._batch_fail = []
        # 运行时动态获取延迟设置，支持实时调节
        # 初始值从config获取，但后续每次使用时会重新读取UI控件的值
        thread_delay_range = self.config.get("thread_delay_range", "0-0.2")
        delay_range = self.config.get("delay_range", "0-0.2")

        self.total_count = total
        success_cnt = 0
        fail_cnt = 0
        completed_cnt = 0
        self.used_proxy_ips.clear()  # 新一批任务开始, 清空已用IP记录(重新去重)
        self._no_proxy_notified = False  # 重置"降级虚拟IP"一次性提示标志(每批任务提示一次)

        invite = self.config.get("invite", "")
        reg_pwd = self.config.get("reg_pwd", "123456")
        
        use_proxy = self.config.get("use_proxy", False)
        api_proxy = self.config.get("proxy_api", "")
        
        async def bounded_process(idx):
            tel = ""
            name = ""
            card = ""
            dev = None
            # 本账号使用的邀请码: 批量计划优先(每个账号固定一个邀请码, 数量不超), 否则用配置里的单个邀请码
            if self._invite_plan is not None:
                invite, invite_type, _ = self._invite_plan[idx]
            else:
                invite = self.config.get("invite", "")
                invite_type = "auto"
            try:
                # 已停止则不再生成新表单, 直接退出(已生成表单的线程继续完成)
                if not self.is_running:
                    self.log_signal.emit(f"第{idx + 1}组 >> 已停止, 跳过(未生成表单)")
                    return {"success": False, "tel": "", "pwd": reg_pwd, "name": "",
                            "card": "", "status": "任务已停止", "ip": "",
                            "raw": "", "row_idx": idx}

                # 运行时动态获取延迟设置，支持实时调节
                current_thread_delay_range = self.config.get("thread_delay_range", "0-0.2")
                thread_delay = parse_random_range(current_thread_delay_range)
                self.log_signal.emit(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] >>线程延迟>>{thread_delay:.2f}s")

                proxy_server = ""
                proxy_task = None
                if use_proxy and api_proxy.strip():
                    # 创建取代理+健康预检任务: 与线程延迟并行执行, 延迟计时期间代理已就绪, 到点即马上进入注册, 不再取号卡几秒
                    proxy_task = asyncio.create_task(self._get_good_proxy(
                        api_proxy, max_try=5, log_callback=self.log_signal.emit,
                        prefix=f"第{idx + 1}组 >> "
                    ))
                    self._task_list.append(proxy_task)
                # 线程延迟(有代理时与取代理并行计时, 无代理时正常等待)
                await self._interruptible_sleep(thread_delay)
                if proxy_task is not None:
                    try:
                        self._task_list.remove(proxy_task)
                    except ValueError:
                        pass
                    if not self.is_running:
                        proxy_task.cancel()
                        return {"success": False, "tel": "", "pwd": reg_pwd, "name": "",
                                "card": "", "status": "任务已停止", "ip": "",
                                "raw": "", "row_idx": idx}
                    proxy_server = await proxy_task
                    if not proxy_server:
                        # 限流(提取过快/白名单待更新)属【临时限制】, API池仍有IP, 跳过该账号继续, 不熔断, 不使用本地IP
                        if self._proxy_limit_until > time.time():
                            self.log_signal.emit(f"第{idx + 1}组 >> 代理API正处于限流退避中, 跳过该账号(退避后继续取号), 不使用本地IP")
                            return {"success": False, "tel": "", "pwd": reg_pwd, "name": "",
                                    "card": "", "status": "代理获取失败", "ip": "",
                                    "raw": "", "row_idx": idx}
                        # 非限流性失败(数量用完/接口异常): 连续失败计数, 达到阈值才弹框结束整个任务, 绝不降级为本地虚拟IP(避免暴露真实IP)
                        with self.lock:
                            self.continuous_fail += 1
                            fail_count = self.continuous_fail
                        if fail_count >= CONTINUOUS_FAIL_THRESHOLD:
                            self.log_signal.emit(f"第{idx + 1}组 >> 代理API连续{fail_count}次取号失败(数量用完), 终止任务, 不使用本地IP")
                            self.task_break_signal.emit(f"代理API取号失败(数量用完), 任务已终止! 请补充代理IP数量后再启动, 未启动的账号已跳过")
                            self.is_running = False
                        return {"success": False, "tel": "", "pwd": reg_pwd, "name": "",
                                "card": "", "status": "代理获取失败", "ip": "",
                                "raw": "", "row_idx": idx}
                    else:
                        with self.lock:
                            self.continuous_fail = 0
                        ip_part = _extract_proxy_ip(proxy_server)
                        # 同步阻塞的IP查询放到线程池, 避免多线程并发时卡死事件循环
                        prov_code, city_core = await asyncio.to_thread(lookup_ip_province, ip_part)
                        if not prov_code:
                            self.log_signal.emit(f"⚠️ 第{idx + 1}组 >> 代理IP:{ip_part} 归属地查询失败！降级为模拟IP(资料保持三省一致)")
                            tel, province_code, city_core, carrier_code = gen_phone_and_location()
                            dev = create_new_device(province_code=province_code, carrier_code=carrier_code, city_core=city_core)
                            # 归属地未知, 不覆盖fake_ip, 保留与手机号/身份证同省的模拟IP
                            dev.use_real_ip = False
                        elif not _PHONE_DB_AVAILABLE:
                            self.log_signal.emit(f"⚠️ 第{idx + 1}组 >> 手机号数据库不可用！改用随机号段匹配{prov_code}地区")
                            tel, carrier_code, city_core = gen_phone_by_province_any(prov_code, city_core)
                            province_code = prov_code
                            dev = create_new_device(province_code=prov_code, carrier_code=carrier_code, city_core=city_core)
                            dev.fake_ip = ip_part
                            dev.ip_location_cn = PROVINCE_CN_MAP.get(prov_code, "")
                            self.log_signal.emit(f"✅ 第{idx + 1}组 >> 代理IP:{ip_part} [{dev.ip_location_cn}{city_core}] 匹配手机号:{tel} ({carrier_code})")
                        else:
                            # 代理IP省市为准: 手机号优先匹配IP所在市(市一致), 无该市号段则省内匹配(省一致); 身份证随手机号市/省
                            ip_city_src = city_core  # 代理IP查询到的市
                            phone, carrier_code, phone_city, city_matched = gen_phone_for_ip(prov_code, city_core)
                            if phone:
                                tel = phone
                            else:
                                self.log_signal.emit(f"⚠️ 第{idx + 1}组 >> 省份{prov_code}无可用手机号段！改用随机号段匹配{prov_code}地区")
                                tel, carrier_code, phone_city = gen_phone_by_province_any(prov_code, city_core)
                                city_matched = _same_city(phone_city, ip_city_src)
                            province_code = prov_code
                            if city_matched and phone_city:
                                city_core = phone_city          # 市一致: 手机号/身份证与IP同市
                                lvl = "市一致"
                                ip_show = f"{PROVINCE_CN_MAP.get(prov_code, '')}{phone_city}"
                            else:
                                city_core = ""                  # 省一致: 身份证按省生成, 三地同省
                                lvl = "省一致"
                                ip_show = f"{PROVINCE_CN_MAP.get(prov_code, '')}(IP市:{ip_city_src or '?'},手机市:{phone_city or '?'})"
                            dev = create_new_device(province_code=prov_code, carrier_code=carrier_code, city_core=city_core)
                            dev.fake_ip = ip_part
                            dev.ip_location_cn = PROVINCE_CN_MAP.get(prov_code, "")
                            self.log_signal.emit(f"✅ 第{idx + 1}组 >> 代理IP:{ip_part} [{ip_show}] {lvl} 匹配手机号:{tel} ({carrier_code})")
                else:
                    # 无代理: 虚拟IP注册 (IP优先: 生成真实网段IP→查真实省市→手机号/身份证按该省市生成, 三地一致)
                    fake_ip, province_code, ip_city, ip_carrier = await asyncio.to_thread(gen_verified_fake_ip)
                    if not province_code:
                        # 查询全部失败: 退回随机省份生成(兜底, 不卡注册)
                        province_code = random.choice(list(PROVINCE_IP_RANGES.keys()))
                        ip_city = ""
                    # 手机号优先精确匹配IP所在市(市一致), 无该市号段则省内匹配(省一致)
                    phone, carrier_code, phone_city, city_matched = gen_phone_for_ip(province_code, ip_city)
                    if phone:
                        tel = phone
                    else:
                        tel, carrier_code, phone_city = gen_phone_by_province_any(province_code, ip_city)
                        city_matched = _same_city(phone_city, ip_city)
                    # 市一致: 手机号/身份证与IP同市; 省一致: 三地同省(身份证按省生成)
                    if city_matched and phone_city:
                        city_core = phone_city
                        lvl = "市一致"
                        ip_show = f"{PROVINCE_CN_MAP.get(province_code, '')}{phone_city}"
                    else:
                        city_core = ""
                        lvl = "省一致"
                        ip_show = f"{PROVINCE_CN_MAP.get(province_code, '')}(IP市:{ip_city or '?'},手机市:{phone_city or '?'})"
                    dev = create_new_device(province_code=province_code, carrier_code=carrier_code, city_core=city_core)
                    dev.fake_ip = fake_ip
                    dev.ip_carrier = ip_carrier or carrier_code
                    dev.ip_carrier_cn = CARRIER_CN_MAP.get(dev.ip_carrier, dev.ip_carrier)
                    dev.ip_location = province_code
                    dev.ip_location_cn = PROVINCE_CN_MAP.get(province_code, "")
                    self.log_signal.emit(f"✅ 第{idx + 1}组 >> 虚拟IP:{dev.fake_ip} [{ip_show}] {lvl} 匹配手机号:{tel} ({carrier_code})")

                name = gen_chinese_name()
                card = self._generate_fake_idcard(province_code=province_code, city=city_core)
                # 按身份证年龄重设行为轨迹时长: >45岁(50岁左右)180-300秒, 其余70%为120-180秒, 30%为60-120秒
                dev.set_behavior_by_age(datetime.now().year - int(card[6:10]))

                # 生成表单前再次检查, 已停止则不生成表单直接退出
                if not self.is_running:
                    self.log_signal.emit(f"第{idx + 1}组 >> 已停止, 跳过(未生成表单)")
                    return {"success": False, "tel": "", "pwd": reg_pwd, "name": "",
                            "card": "", "status": "任务已停止", "ip": "",
                            "raw": "", "row_idx": idx}

                self.pre_reg_signal.emit(tel, reg_pwd, name, invite, dev.fake_ip, card)

                result = await asyncio.wait_for(
                    self._process_single_registration(idx, total, tel, name, card, dev, proxy_server, invite, invite_type),
                    timeout=90
                )
                # 即时落盘: 注册结果立即写入文件, 防止崩溃/关软件丢数据
                self._save_register_result(result, invite)
                return result
            except asyncio.TimeoutError:
                self.log_signal.emit(f"第{idx + 1}组 >> 注册超时(90秒)，跳过")
                _timeout_result = {"success": False, "tel": tel, "pwd": reg_pwd, "name": name,
                        "card": card, "status": "注册超时", "ip": dev.fake_ip if dev else "",
                        "raw": "", "row_idx": idx}
                # 超时也立即更新 UI 状态, 避免一直卡在"注册中"
                self.update_reg_signal.emit(tel, f"{dev.fake_ip}({reg_loc})" if dev else "", "注册超时")
                self._save_register_result(_timeout_result, invite)
                return _timeout_result
            except asyncio.CancelledError:
                self.log_signal.emit(f"第{idx + 1}组 >> 任务被取消")
                _cancel_result = {"success": False, "tel": tel, "pwd": reg_pwd, "name": name,
                        "card": card, "status": "任务被取消", "ip": dev.fake_ip if dev else "",
                        "raw": "", "row_idx": idx}
                self.update_reg_signal.emit(tel, f"{dev.fake_ip}({reg_loc})" if dev else "", "任务被取消")
                self._save_register_result(_cancel_result, invite)
                return _cancel_result
            except Exception as e:
                self.log_signal.emit(f"第{idx + 1}组 >> 未知异常: {str(e)}")
                _err_result = {"success": False, "tel": tel, "pwd": reg_pwd, "name": name,
                        "card": card, "status": f"未知异常: {str(e)[:80]}", "ip": dev.fake_ip if dev else "",
                        "raw": "", "row_idx": idx}
                self.update_reg_signal.emit(tel, f"{dev.fake_ip}({reg_loc})" if dev else "", "异常结束")
                self._save_register_result(_err_result, invite)
                return _err_result

        tasks = []          # 当前运行中的任务 (最多 thread_count 个, 与填写的并发线程数一致)
        results = []        # 已完成任务的结果
        row_idx_counter = 0 # 下一个任务的行号
        started_cnt = 0     # 已启动任务数

        def _make_task(r_idx):
            """创建一个任务并登记"""
            nonlocal started_cnt
            t = asyncio.create_task(bounded_process(r_idx))
            tasks.append(t)
            self._task_list.append(t)
            started_cnt += 1
            return t

        # 先启动 thread_count 个任务(即填写的线程数), 之后每完成一个再补一个; 运行中可实时修改线程数
        for _ in range(min(self._live_thread_count(), total)):
            if not self.is_running or row_idx_counter >= total:
                break
            _make_task(row_idx_counter)
            row_idx_counter += 1
            if row_idx_counter < total:
                # 运行时动态获取延迟设置，支持实时调节
                current_delay_range = self.config.get("delay_range", "0-0.2")
                if not await self._interruptible_sleep(parse_random_range(current_delay_range)):
                    break

        while tasks:
            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            # asyncio.wait 返回的 pending 是 set, 必须转回 list 才能继续 append 补任务
            tasks = list(pending)
            for d in done:
                if d.cancelled():
                    results.append(None)
                elif d.exception() is not None:
                    results.append(d.exception())
                else:
                    result = d.result()
                    results.append(result)
                    # 实时进度: 每完成一个立即上报, 顶部进度条实时跳动
                    completed_cnt += 1
                    self.progress_signal.emit(completed_cnt, started_cnt)
                    if result["success"]:
                        success_cnt += 1
                    else:
                        fail_cnt += 1
                    self.stats_signal.emit(success_cnt, fail_cnt, total)
                    # 批量注册实时进度: 每个账号完成即更新对应提交行成功/失败数并上报显示
                    if self._invite_plan is not None and isinstance(result, dict):
                        _ei = self._invite_plan[result.get("row_idx", 0)][2]
                        if result.get("success"):
                            self._batch_done[_ei] += 1
                        else:
                            self._batch_fail[_ei] += 1
                        self._emit_batch_progress()
            # 跑完一个补一个, 始终保持并发数 = 当前填写的线程数(可实时调节)
            while self.is_running and len(tasks) < self._live_thread_count() and row_idx_counter < total:
                _make_task(row_idx_counter)
                row_idx_counter += 1
                if row_idx_counter < total:
                    # 运行时动态获取延迟设置，支持实时调节
                    current_delay_range = self.config.get("delay_range", "0-0.2")
                    if not await self._interruptible_sleep(parse_random_range(current_delay_range)):
                        break

        if started_cnt == 0:
            self.log_signal.emit("⚠️ 没有启动任何任务")
            return

        for result in results:
            if isinstance(result, Exception):
                self.log_signal.emit(f"子任务异常: {str(result)}")

        not_started = total - started_cnt
        if not_started > 0:
            final_msg = f"======= 注册任务结束（已停止） =======\n总请求:{total} 实际启动:{started_cnt} 成功:{success_cnt} 失败:{fail_cnt} 未启动:{not_started}"
        else:
            final_msg = f"======= 注册任务结束 =======\n总数:{total} 成功:{success_cnt} 失败:{fail_cnt}"
        self.log_signal.emit(final_msg)
        # 数据已在每个账号完成时即时落盘, 此处无需再写文件

    def _match_city_code(self, city):
        """在城市表匹配城市区县码, 支持精确/包含匹配(如"大理白族"->"大理"), 未收录返回None"""
        if not city:
            return None
        if city in CITY_IDCARD_CODES:
            return CITY_IDCARD_CODES[city]
        for key, codes in CITY_IDCARD_CODES.items():
            if key in city:
                return codes
        return None

    def _generate_fake_idcard(self, province_code=None, gender=None, city=None):
        """生成合法且真实感强的18位身份证号:
        - 行政区划码优先与手机号/IP的省市一致(城市表未收录时降级到省份)
        - 出生日期统一22-45岁(不再生成其他年龄段), 并校验闰年/大小月
        - 第17位性别位与姓名性别一致(奇男偶女)
        - 校验位按GB 11643-1999计算
        - 全程去重: 已生成过的号码自动重新生成, 最大限度降低重复概率
        """
        if gender is None:
            gender = _LAST_GENDER

        city_codes = self._match_city_code(city)
        if city_codes:
            code = random.choice(city_codes)
        elif province_code and province_code in _IDCARD_AREA_CODES:
            code = random.choice(_IDCARD_AREA_CODES[province_code])
        else:
            code = random.choice(random.choice(list(_IDCARD_AREA_CODES.values())))

        cur_year = datetime.now().year
        # 年龄统一: 全部22-45岁(不再生成其他年龄段), 按当前年份动态计算
        for _attempt in range(30):
            year = random.randint(cur_year - 45, cur_year - 22)   # 22-45岁

            month = random.randint(1, 12)
            leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
            month_days = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            day = random.randint(1, month_days[month - 1])
            birth = f"{year}{month:02d}{day:02d}"

            seq = random.randint(0, 998)
            if gender == "M":
                seq |= 1          # 男性: 奇数
            else:
                seq -= seq % 2    # 女性: 偶数
            pre17 = code + birth + f"{seq:03d}"

            w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            ck = "10X98765432"
            s = 0
            for i in range(17):
                s += int(pre17[i]) * w[i]
            check = ck[s % 11]
            card = pre17 + check

            # 去重: 已生成过的号码重新生成, 30次内仍未唯一则使用当前号码
            if card not in _GENERATED_IDCARDS:
                _register_idcard(card)
                return card
        return card

    async def run_sign_async(self):
        thread_delay_range = self.config.get("thread_delay_range", "0-0.2")
        delay_range = self.config.get("sign_delay_range", "5-15")
        success_cnt = 0
        row_list = self.account_list
        total = len(row_list)
        completed_cnt = 0
        self.used_proxy_ips.clear()  # 新一批签到任务开始, 清空已用IP记录(重新去重)

        # 文件名提前确定, 每个签到结果即时追加写入(防崩溃丢数据)
        timestr = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        suc_file = os.path.join(SIGN_LOG_FOLDER, f"签到成功{timestr}.txt")
        fail_file = os.path.join(SIGN_LOG_FOLDER, f"签到失败{timestr}.txt")

        async def bounded_sign(idx, row):
            try:
                # 已停止则不再执行签到(签到无表单生成, 直接退出)
                if not self.is_running:
                    self.log_signal.emit(f"第{idx + 1}行 >> 已停止, 跳过签到")
                    _stopped_result = {"idx": idx, "success": False, "tel": row[0], "pwd": row[1], "status": "任务已停止", "ip": ""}
                    self._save_sign_result(_stopped_result, suc_file, fail_file)
                    return _stopped_result

                # 运行时动态获取延迟设置，支持实时调节
                current_thread_delay_range = self.config.get("thread_delay_range", "0-0.2")
                thread_delay = parse_random_range(current_thread_delay_range)
                self.log_signal.emit(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] >>线程延迟>>{thread_delay:.2f}s")
                await self._interruptible_sleep(thread_delay)

                result = await asyncio.wait_for(
                    self._sign_single_task_async(idx, row),
                    timeout=90
                )
                # 即时落盘: 签到结果立即写入文件
                self._save_sign_result(result, suc_file, fail_file)
                return result
            except asyncio.TimeoutError:
                self.log_signal.emit(f"第{idx + 1}行 >> 签到超时(90秒)")
                _to_result = {"idx": idx, "success": False, "tel": row[0], "pwd": row[1], "status": "签到超时", "ip": ""}
                self._save_sign_result(_to_result, suc_file, fail_file)
                return _to_result
            except asyncio.CancelledError:
                _cancel_result = {"idx": idx, "success": False, "tel": row[0], "pwd": row[1], "status": "签到被取消", "ip": ""}
                self._save_sign_result(_cancel_result, suc_file, fail_file)
                return _cancel_result
            except Exception as e:
                self.log_signal.emit(f"第{idx + 1}行 >> 签到异常: {str(e)}")
                _err_result = {"idx": idx, "success": False, "tel": row[0], "pwd": row[1], "status": f"签到异常: {str(e)[:80]}", "ip": ""}
                self._save_sign_result(_err_result, suc_file, fail_file)
                return _err_result

        tasks = []          # 当前运行中的任务 (最多 thread_count 个)
        results = []        # 已完成任务的结果
        started_cnt = 0
        idx_counter = 0     # 下一个任务的行号

        def _make_sign_task(r_idx, r_row):
            """创建一个签到任务并登记"""
            nonlocal started_cnt
            t = asyncio.create_task(bounded_sign(r_idx, r_row))
            tasks.append(t)
            self._task_list.append(t)
            started_cnt += 1
            return t

        # 先启动 thread_count 个任务, 之后每完成一个再补一个; 运行中可实时修改线程数
        for _ in range(min(self._live_thread_count(), total)):
            if not self.is_running or idx_counter >= total:
                break
            _make_sign_task(idx_counter, row_list[idx_counter])
            idx_counter += 1
            if idx_counter < total:
                # 运行时动态获取延迟设置，支持实时调节
                current_delay_range = self.config.get("sign_delay_range", "5-15")
                if not await self._interruptible_sleep(parse_random_range(current_delay_range)):
                    break

        while tasks:
            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            # asyncio.wait 返回的 pending 是 set, 必须转回 list 才能继续 append 补任务
            tasks = list(pending)
            for d in done:
                if d.cancelled():
                    results.append(None)
                elif d.exception() is not None:
                    results.append(d.exception())
                else:
                    result = d.result()
                    results.append(result)
                    # 实时进度: 每完成一个立即上报, 顶部进度条实时跳动
                    completed_cnt += 1
                    self.progress_signal.emit(completed_cnt, started_cnt)
                    self.update_yang_status_signal.emit(result["idx"], result["status"], result["ip"])
                    if result["success"]:
                        success_cnt += 1
                    # 实时统计上报: 签到任务也显示 成功/失败/总数
                    self.stats_signal.emit(success_cnt, completed_cnt - success_cnt, total)
            # 跑完一个补一个, 始终保持并发数 = 当前填写的线程数(可实时调节)
            while self.is_running and len(tasks) < self._live_thread_count() and idx_counter < total:
                _make_sign_task(idx_counter, row_list[idx_counter])
                idx_counter += 1
                if idx_counter < total:
                    # 运行时动态获取延迟设置，支持实时调节
                    current_delay_range = self.config.get("sign_delay_range", "5-15")
                    if not await self._interruptible_sleep(parse_random_range(current_delay_range)):
                        break

        if started_cnt == 0:
            self.log_signal.emit("⚠️ 没有启动任何签到任务")
            return

        for result in results:
            if isinstance(result, Exception):
                self.log_signal.emit(f"签到子任务异常: {str(result)}")

        # 数据已在每个账号签到完成时即时落盘, 此处无需再写文件
        not_started = total - started_cnt
        if not_started > 0:
            self.log_signal.emit(f"====签到流程执行完成（已停止）===总请求:{total} 实际启动:{started_cnt} 成功:{success_cnt} 未启动:{not_started}")
        else:
            self.log_signal.emit(f"====签到流程执行完成===总数:{total} 成功:{success_cnt}")

    async def _sign_single_task_async(self, idx, row):
        tel, pwd, name, inv = row
        inferred_prov, inferred_carrier = infer_location_from_phone(tel)
        dev = create_new_device(province_code=inferred_prov, carrier_code=inferred_carrier)
        proxy_server = ""
        current_ip = dev.fake_ip
        session = None

        try:
            use_proxy = self.config.get("use_proxy", False)
            api_proxy = self.config.get("proxy_api", "")

            if use_proxy and api_proxy.strip():
                # 取代理+健康预检, 快速过滤死代理
                proxy_server = await self._get_good_proxy(
                    api_proxy, max_try=5, log_callback=self.log_signal.emit,
                    prefix=f"第{idx + 1}行>>{tel} "
                )
                if not proxy_server:
                    self.log_signal.emit(f"{tel} >> 获取代理/预检多次失败，跳过")
                    with self.lock:
                        self.continuous_fail += 1
                        fail_count = self.continuous_fail
                    if fail_count >= CONTINUOUS_FAIL_THRESHOLD:
                        self.task_break_signal.emit(f"连续{fail_count}次代理失败，任务终止")
                        self.is_running = False
                    return {"idx": idx, "success": False, "tel": tel, "pwd": pwd, "status": "代理获取失败", "ip": current_ip}

                ip_part = _extract_proxy_ip(proxy_server)
                dev.fake_ip = ip_part
                current_ip = ip_part

            session = CurlSessionManager.create_session(device=dev)
            if use_proxy and proxy_server:
                session.proxies = {"http": _build_proxy_url(proxy_server), "https": _build_proxy_url(proxy_server)}

            await CurlSessionManager.warm_up_session(session, device=dev)

            self.log_signal.emit(f"第{idx + 1}行>>{tel} [IP:{current_ip}] 开始登录...")

            ok_login, login_data, login_raw = await http_login_async(
                tel, pwd, session, dev, use_proxy, proxy_server,
                progress_callback=lambda s, _i=idx, _ip=current_ip: self.update_yang_status_signal.emit(_i, s, _ip)
            )

            if not ok_login or login_data.get("status") != 1:
                self.log_signal.emit(f"第{idx + 1}行>>{tel} 使用IP:{current_ip} 登录失败 返回:{login_raw}")
                with self.lock:
                    self.continuous_fail += 1
                    fail_count = self.continuous_fail
                if fail_count >= CONTINUOUS_FAIL_THRESHOLD:
                    self.task_break_signal.emit(f"连续{fail_count}登录失败，疑似封禁，任务终止")
                    self.is_running = False
                return {"idx": idx, "success": False, "tel": tel, "pwd": pwd, "status": "登录失败", "ip": current_ip}

            with self.lock:
                self.continuous_fail = 0

            sid = login_data.get("session_id", "")
            if not sid:
                self.log_signal.emit(f"第{idx + 1}行>>登录成功但缺失session_id>{tel} IP:{current_ip}")
                return {"idx": idx, "success": False, "tel": tel, "pwd": pwd, "status": "缺失session_id", "ip": current_ip}

            await self._interruptible_sleep(human_delay(0.6))

            ok_sign, sign_data, sign_raw = await http_sign_async(sid, session, dev, use_proxy, proxy_server,
                progress_callback=lambda s, _i=idx, _ip=current_ip: self.update_yang_status_signal.emit(_i, s, _ip)
            )

            if ok_sign and sign_data.get("status") == 1:
                self.log_signal.emit(f"第{idx + 1}行>>{tel} 使用IP:{current_ip} 签到成功")
                return {"idx": idx, "success": True, "tel": tel, "pwd": pwd, "status": "✅签到成功", "ip": current_ip}
            else:
                msg = sign_data.get("msg", "") if sign_data else ""
                if "已签到" in msg or "重复" in msg:
                    self.log_signal.emit(f"第{idx + 1}行>>{tel} 使用IP:{current_ip} 今日已签到")
                    return {"idx": idx, "success": True, "tel": tel, "pwd": pwd, "status": "✅今日已签到", "ip": current_ip}

                self.log_signal.emit(f"第{idx + 1}行>>{tel} 使用IP:{current_ip} 签到失败 返回:{sign_raw}")
                return {"idx": idx, "success": False, "tel": tel, "pwd": pwd, "status": "❌签到失败", "ip": current_ip}
        finally:
            if session:
                try:
                    await session.close()
                except Exception:
                    pass

    def stop_force(self):
        if self.is_running:
            self.log_signal.emit("⏹ 已发送停止指令：当前正在执行的任务将继续完成，不再生成新任务...")
        self.is_running = False
        if self.stop_event:
            self.stop_event.set()


# ===================== 主窗口UI =====================
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("统壹出行最终版本6.6v")
        # 基准设计尺寸: 整个界面按此尺寸布局, 再整体跟随窗口等比缩放(缩小一起缩小, 放大一起放大)
        self.BASE_W = 1420
        self.BASE_H = 960
        self.resize(1420, 960)
        # 允许缩得很小, 界面内容会整体等比缩小, 不会被裁掉看不见
        self.setMinimumSize(640, 420)
        self.init_ui()
        self.load_config()
        self.work_thread = WorkThread()

        # 缩放节流定时器: 拖动窗口时最多每80ms重绘一次, 避免卡顿
        self._zoom_timer = QTimer(self)
        self._zoom_timer.setInterval(80)
        self._zoom_timer.timeout.connect(self._apply_zoom)

        self.work_thread.log_signal.connect(self.append_log)
        self.work_thread.finish_signal.connect(self.task_finish)
        self.work_thread.pre_reg_signal.connect(self.pre_reg_row)
        self.work_thread.update_reg_signal.connect(self.update_reg_row)
        self.work_thread.update_card_signal.connect(self.update_card_row)
        self.work_thread.update_tel_signal.connect(self.update_tel_row)
        self.work_thread.update_yang_status_signal.connect(self.update_yang_table_status)
        self.work_thread.progress_signal.connect(self.update_progress)
        self.work_thread.stats_signal.connect(self.update_stats)   # 实时成功率/速度/预计剩余统计
        self.work_thread.batch_progress_signal.connect(self.on_batch_progress_snapshot)  # 批量注册实时进度
        self.work_thread.task_break_signal.connect(self.on_task_break)
        self.work_thread.notify_signal.connect(self.on_notify)
        self.work_thread.clear_reg_table_signal.connect(self.clear_reg_table) # 连接清空信号

        self.running_flag = False
        self._reg_row_map = {}  # 注册表: 手机号 -> 行号, 任务完成时按手机号定位更新状态
        self._stats = {"success": 0, "fail": 0, "total": 0, "curr": 0}
        self._task_start_time = None  # 任务开始时间, 用于计算速度与预计剩余
        self.append_log(f"✅ 统壹出行最终版本{APP_VERSION} 启动成功")

    def init_ui(self):
        central = QWidget()
        main_layout = QHBoxLayout(central)

        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        self.tab = QTabWidget()
        self.tab.setObjectName("mainTab")
        self.tab_reg = QWidget()
        self.tab_yang = QWidget()
        self.tab_material = QWidget()
        self.tab.addTab(self.tab_reg, "注册表单")
        self.tab.addTab(self.tab_yang, "养号表单")
        self.tab.addTab(self.tab_material, "计算器和定时启动")

        ly_reg = QVBoxLayout(self.tab_reg)
        self.table_reg = QTableWidget()
        self.table_reg.setObjectName("tableReg")
        self.table_reg.setColumnCount(7)
        self.table_reg.setHorizontalHeaderLabels(["手机号", "密码", "姓名", "身份证", "IP", "邀请码", "状态"])
        h_header_reg = self.table_reg.horizontalHeader()
        # 固定/自适应前几列, 状态列自动拉伸占满剩余宽度(窗口缩放时跟随), 保证状态始终可见
        h_header_reg.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        h_header_reg.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        h_header_reg.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        h_header_reg.setSectionResizeMode(3, QHeaderView.Interactive)
        self.table_reg.setColumnWidth(3, 170)
        h_header_reg.setSectionResizeMode(4, QHeaderView.Interactive)
        self.table_reg.setColumnWidth(4, 260)
        h_header_reg.setSectionResizeMode(5, QHeaderView.Interactive)
        self.table_reg.setColumnWidth(5, 110)
        h_header_reg.setSectionResizeMode(6, QHeaderView.Stretch)
        ly_reg.addWidget(self.table_reg)

        ly_yang = QVBoxLayout(self.tab_yang)
        top_bar = QHBoxLayout()
        self.edit_input_acc = QLineEdit()
        self.edit_input_acc.setPlaceholderText("输入格式：手机号----密码，按下回车自动添加表格")
        self.edit_input_acc.returnPressed.connect(self.on_enter_fill_row)
        self.btn_clear_yang = QPushButton("清空养号表单")
        self.btn_import_txt = QPushButton("导入TXT")
        self.btn_clear_log = QPushButton("清空日志")
        self.btn_export_yang = QPushButton("导出表格账号")
        self.btn_export_fail = QPushButton("导出失败账号")
        self.btn_import_txt.clicked.connect(self.import_yang_txt)
        self.btn_clear_yang.clicked.connect(self.clear_yang_table)
        self.btn_clear_log.clicked.connect(lambda: self.log_text.clear())
        self.btn_export_yang.clicked.connect(self.export_yang_table)
        self.btn_export_fail.clicked.connect(self.export_fail_account)
        top_bar.addWidget(self.edit_input_acc)
        top_bar.addWidget(self.btn_import_txt)
        top_bar.addWidget(self.btn_clear_yang)
        top_bar.addWidget(self.btn_export_yang)
        top_bar.addWidget(self.btn_export_fail)
        top_bar.addWidget(self.btn_clear_log)
        ly_yang.addLayout(top_bar)

        self.table_yanghao = QTableWidget()
        self.table_yanghao.setObjectName("tableYang")
        self.table_yanghao.setColumnCount(6)
        self.table_yanghao.setHorizontalHeaderLabels(["手机号", "密码", "姓名", "IP", "邀请码", "状态"])
        h_header = self.table_yanghao.horizontalHeader()
        # 固定/自适应前几列, 状态列自动拉伸占满剩余宽度, 保证状态始终可见
        h_header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        h_header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        h_header.setSectionResizeMode(2, QHeaderView.Interactive)
        self.table_yanghao.setColumnWidth(2, 90)
        h_header.setSectionResizeMode(3, QHeaderView.Interactive)
        self.table_yanghao.setColumnWidth(3, 140)
        h_header.setSectionResizeMode(4, QHeaderView.Interactive)
        self.table_yanghao.setColumnWidth(4, 110)
        h_header.setSectionResizeMode(5, QHeaderView.Stretch)
        ly_yang.addWidget(self.table_yanghao)

        ly_material = QVBoxLayout(self.tab_material)
        # 左右分栏: 左侧计算器+定时启动, 右侧批量邀请码注册(利用右侧空白位置)
        ly_material_h = QHBoxLayout()
        ly_material_h.setSpacing(16)
        ly_material_left = QVBoxLayout()
        ly_material_left.setSpacing(14)

        # 小计算器: 只支持加减法, 输入即出结果 (放在空白标签页里)
        group_calc = QGroupBox("计算器")
        group_calc.setStyleSheet("""
            QGroupBox {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ffffff, stop:1 #fafbff);
                border: 1px solid #e2e8f0;
                border-radius: 12px;
                margin-top: 16px;
                padding: 14px 16px 14px 16px;
                color: #475569;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 5px 18px;
                color: #ffffff;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #6366f1, stop:0.5 #8b5cf6, stop:1 #ec4899);
                border: none;
                border-radius: 10px;
            }
        """)
        group_calc.setMaximumWidth(420)
        group_calc.setMinimumHeight(180)

        ly_calc = QVBoxLayout(group_calc)
        ly_calc.setSpacing(14)

        self.edit_calc = QLineEdit()
        self.edit_calc.setPlaceholderText("如: 1000-200, 输入即出结果")
        self.edit_calc.textChanged.connect(self.on_calc_changed)
        self.edit_calc.setStyleSheet("""
            QLineEdit {
                background: #ffffff;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                padding: 4px 12px;
                font-size: 16px;
                font-weight: bold;
                color: #1e293b;
            }
            QLineEdit:focus {
                border: 2px solid #8b5cf6;
                background: #fdfbff;
            }
        """)
        self.edit_calc.setFixedHeight(40)

        btn_calc_clear = QPushButton("清空")
        btn_calc_clear.setFixedSize(64, 40)
        btn_calc_clear.setToolTip("清空")
        btn_calc_clear.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #fbbf24, stop:1 #f97316);
                color: #ffffff;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #fb923c;
            }
            QPushButton:pressed {
                background: #ea580c;
            }
        """)
        btn_calc_clear.clicked.connect(lambda: self.edit_calc.clear())

        row_calc_input = QHBoxLayout()
        row_calc_input.setSpacing(8)
        row_calc_input.addWidget(self.edit_calc, 1)
        row_calc_input.addWidget(btn_calc_clear)

        lbl_calc_tag = QLabel("结果")
        lbl_calc_tag.setStyleSheet("color: #64748b; font-weight: bold; font-size: 14px;")
        self.lbl_calc_result = QLabel("0")
        self.lbl_calc_result.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lbl_calc_result.setFixedHeight(44)
        self.lbl_calc_result.setStyleSheet("""
            QLabel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ede9fe, stop:1 #e0e7ff);
                color: #6d28d9;
                border: 1px solid #c7d2fe;
                border-radius: 10px;
                padding: 4px 16px;
                font-size: 22px;
                font-weight: bold;
            }
        """)
        row_calc_result = QHBoxLayout()
        row_calc_result.setSpacing(8)
        row_calc_result.addWidget(lbl_calc_tag)
        row_calc_result.addWidget(self.lbl_calc_result, 1)

        ly_calc.addLayout(row_calc_input)
        ly_calc.addLayout(row_calc_result)

        ly_material_left.addWidget(group_calc)

        # 定时启动: 月/日/时/分 下拉选择, 到点自动开始任务(配置与手动开始完全一致), 放在计算器下方
        group_timer = QGroupBox("定时启动")
        group_timer.setMaximumWidth(420)
        ly_timer = QFormLayout(group_timer)
        self.check_timer = QCheckBox("启用定时自动启动")
        self.check_timer.setToolTip("勾选后到设定时间自动开始运行, 任务配置与手动点【开始运行】一致")

        now = datetime.now()
        self.spin_timer_month = QSpinBox()
        self.spin_timer_month.setRange(1, 12)
        self.spin_timer_month.setValue(now.month)
        self.spin_timer_month.setFixedHeight(30)
        self.spin_timer_month.setMinimumWidth(74)
        self.spin_timer_day = QSpinBox()
        self.spin_timer_day.setRange(1, 31)
        self.spin_timer_day.setValue(now.day)
        self.spin_timer_day.setFixedHeight(30)
        self.spin_timer_day.setMinimumWidth(74)
        self.spin_timer_hour = QSpinBox()
        self.spin_timer_hour.setRange(0, 23)
        self.spin_timer_hour.setValue(now.hour)
        self.spin_timer_hour.setFixedHeight(30)
        self.spin_timer_hour.setMinimumWidth(86)
        self.spin_timer_min = QSpinBox()
        self.spin_timer_min.setRange(0, 59)
        self.spin_timer_min.setValue(now.minute)
        self.spin_timer_min.setFixedHeight(30)
        self.spin_timer_min.setMinimumWidth(86)
        spin_style = """
            QSpinBox {
                background: #ffffff;
                border: 2px solid #e2e8f0;
                border-radius: 8px;
                padding: 2px 4px 2px 10px;
                font-size: 14px;
                font-weight: bold;
                color: #1e293b;
            }
            QSpinBox:focus {
                border: 2px solid #8b5cf6;
                background: #fdfbff;
            }
        """
        for _s in (self.spin_timer_month, self.spin_timer_day, self.spin_timer_hour, self.spin_timer_min):
            _s.setStyleSheet(spin_style)
        self.spin_timer_month.valueChanged.connect(self._update_timer_days)
        self.spin_timer_month.valueChanged.connect(self._reset_schedule)
        self.spin_timer_day.valueChanged.connect(self._reset_schedule)
        self.spin_timer_hour.valueChanged.connect(self._reset_schedule)
        self.spin_timer_min.valueChanged.connect(self._reset_schedule)
        self._update_timer_days()

        selector_row = QHBoxLayout()
        selector_row.setSpacing(4)
        selector_row.addWidget(self.spin_timer_month)
        selector_row.addWidget(QLabel("月"))
        selector_row.addWidget(self.spin_timer_day)
        selector_row.addWidget(QLabel("日"))
        selector_row.addWidget(self.spin_timer_hour)
        selector_row.addWidget(QLabel("时"))
        selector_row.addWidget(self.spin_timer_min)
        selector_row.addWidget(QLabel("分"))
        selector_row.addStretch()

        self.lbl_timer_status = QLabel("未启用")
        self.lbl_timer_status.setStyleSheet("color: #94a3b8; font-weight: bold;")
        self.lbl_timer_status.setWordWrap(True)
        ly_timer.addRow(self.check_timer)
        ly_timer.addRow("启动时间", selector_row)
        ly_timer.addRow("状态", self.lbl_timer_status)

        ly_material_left.addWidget(group_timer)
        ly_material_left.addStretch()

        # ===== 批量邀请码注册 (右侧空白位置, 仅配合【批量注册(仅注册)】任务模式) =====
        group_batch = QGroupBox("批量邀请码注册（配合任务选择: 批量注册(仅注册)）")
        group_batch.setStyleSheet("""
            QGroupBox {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ffffff, stop:1 #fafbff);
                border: 1px solid #e2e8f0;
                border-radius: 12px;
                margin-top: 16px;
                padding: 14px 16px 14px 16px;
                color: #475569;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 5px 18px;
                color: #ffffff;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #10b981, stop:0.5 #14b8a6, stop:1 #06b6d4);
                border: none;
                border-radius: 10px;
            }
        """)
        ly_batch = QVBoxLayout(group_batch)
        ly_batch.setSpacing(12)

        self.edit_batch_invites = QTextEdit()
        self.edit_batch_invites.setPlaceholderText(
            "每行一个: 邀请码----数量（类型自动识别）\n\n"
            "例如:\n"
            "19378900689----50    (手机号类型, 注册50个)\n"
            "1234567----30        (ID类型, 注册30个)\n\n"
            "【提交批量】后实时显示每个邀请码的成功进度")
        self.edit_batch_invites.setFixedHeight(200)
        self.edit_batch_invites.setStyleSheet("""
            QTextEdit {
                background: #ffffff;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                padding: 8px 12px;
                font-family: Consolas, "Microsoft YaHei";
                font-size: 13px;
                color: #1e293b;
            }
            QTextEdit:focus {
                border: 2px solid #14b8a6;
                background: #fdfbff;
            }
        """)
        ly_batch.addWidget(self.edit_batch_invites)

        row_batch_btn = QHBoxLayout()
        row_batch_btn.setSpacing(10)
        btn_batch_submit = QPushButton("提交批量")
        btn_batch_submit.setFixedSize(110, 32)
        btn_batch_submit.clicked.connect(self.on_batch_submit)
        btn_batch_example = QPushButton("填入示例")
        btn_batch_example.setFixedSize(90, 32)
        btn_batch_example.clicked.connect(self.fill_batch_example)
        btn_batch_clear = QPushButton("清空")
        btn_batch_clear.setFixedSize(70, 32)
        btn_batch_clear.clicked.connect(lambda: self.edit_batch_invites.clear())
        row_batch_btn.addWidget(btn_batch_submit)
        row_batch_btn.addWidget(btn_batch_example)
        row_batch_btn.addWidget(btn_batch_clear)
        row_batch_btn.addStretch(1)
        ly_batch.addLayout(row_batch_btn)

        # 实时进度显示: 提交后显示目标, 运行时每完成一个账号实时刷新
        self.lbl_batch_progress = QLabel("尚未提交批量数据")
        self.lbl_batch_progress.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.lbl_batch_progress.setStyleSheet("""
            QLabel {
                color: #0f766e;
                background: #f0fdfa;
                border: 1px solid #99f6e4;
                border-radius: 10px;
                padding: 10px 14px;
                font-family: Consolas, "Microsoft YaHei";
                font-size: 13px;
                font-weight: bold;
            }
        """)
        self.lbl_batch_progress.setMinimumHeight(90)
        self.lbl_batch_progress.setWordWrap(True)
        ly_batch.addWidget(self.lbl_batch_progress)

        lbl_batch_hint = QLabel(
            "格式: 邀请码----数量（每行一个）\n"
            "类型自动识别: 11位手机号→手机号类型, 其余→ID类型\n"
            "数量以填写为准, 多邀请码可同时交叉做(线程随机分配)\n"
            "其他任务模式不受此框影响")
        lbl_batch_hint.setStyleSheet("color: #64748b; font-weight: bold; font-size: 12px;")
        lbl_batch_hint.setWordWrap(True)
        ly_batch.addWidget(lbl_batch_hint)

        ly_material_h.addLayout(ly_material_left)
        ly_material_h.addWidget(group_batch, 1)
        ly_material.addLayout(ly_material_h)

        # 每秒检查一次是否到点
        self.timer_scheduled_dt = None
        self.timer_fired = False
        self.timer_check = QTimer(self)
        self.timer_check.timeout.connect(self.check_schedule)
        self.timer_check.start(1000)

        self.progress_bar = QProgressBar()
        self.progress_bar.setObjectName("mainProgress")
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(True)

        left_layout.addWidget(self.progress_bar)

        # 日志区域标题栏
        log_header_layout = QHBoxLayout()
        log_label = QLabel("运行日志")
        log_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        self.btn_clear_log_area = QPushButton("清空日志")
        self.btn_clear_log_area.setObjectName("btnClearLog")
        self.btn_clear_log_area.clicked.connect(self.clear_log_text)
        self.btn_copy_log = QPushButton("复制日志")
        self.btn_copy_log.setObjectName("btnCopyLog")
        self.btn_copy_log.clicked.connect(self.copy_log_text)
        self.btn_delete_selected = QPushButton("删除选中")
        self.btn_delete_selected.setObjectName("btnDeleteSelected")
        self.btn_delete_selected.clicked.connect(self.delete_selected_log)
        log_header_layout.addWidget(log_label)
        log_header_layout.addStretch()
        log_header_layout.addWidget(self.btn_clear_log_area)
        log_header_layout.addWidget(self.btn_copy_log)
        log_header_layout.addWidget(self.btn_delete_selected)
        left_layout.addLayout(log_header_layout)

        self.log_text = QTextEdit()
        self.log_text.setObjectName("logText")
        self.log_text.setMinimumHeight(120)  # 日志区最小高度, 缩小窗口时不会被压没
        self.log_text.setReadOnly(False)  # 允许编辑和删除
        self.log_text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.log_text.customContextMenuRequested.connect(self.show_log_context_menu)

        left_layout.addWidget(self.tab)
        left_layout.addWidget(self.log_text)

        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        group_cfg = QGroupBox("注册配置")
        ly_cfg = QFormLayout(group_cfg)

        self.edit_num = QLineEdit("10")
        self.edit_reg_pwd = QLineEdit("123456")
        self.edit_invite = QLineEdit("19378900689")

        self.cmb_invite_type = QComboBox()
        self.cmb_invite_type.addItems(["自动识别"])

        self.cmb_thread_count = QLineEdit("5")
        self.cmb_thread_count.setToolTip("运行中可实时修改, 立即生效: 改大加速(立即多开), 改小限流(完成中的任务跑完才停)")
        # 运行中修改线程数实时同步到后台任务, 无需重启任务
        self.cmb_thread_count.textChanged.connect(self._sync_thread_count_to_worker)

        self.edit_thread_delay = QLineEdit("0-0.2")
        self.edit_thread_delay.setPlaceholderText("如: 0-2 或 1.5")

        self.edit_delay = QLineEdit("0-0.2")
        self.edit_delay.setPlaceholderText("如: 0-2 或 1.5")

        self.edit_sign_delay = QLineEdit("5-15")
        self.edit_sign_delay.setPlaceholderText("如: 5-15 或 10")

        self.cmb_task = QComboBox()
        self.cmb_task.addItems(["仅注册任务", "注册签到任务", "签到任务", "批量注册(仅注册)"])

        # 免码: 本地生成手机号; 内置料子: 内置生成身份证 (豪猪取号时无需理会)
        self.check_mianma = QCheckBox("免码")
        self.check_mianma.setChecked(True)
        self.check_mianma.setToolTip("免码 = 代码按IP省市生成的手机号\n勾选后使用本地生成手机号注册\n未勾选时需配合豪猪取号, 否则无法获取手机号")
        self.check_neizhi = QCheckBox("内置料子")
        self.check_neizhi.setChecked(True)
        self.check_neizhi.setToolTip("内置料子 = 代码生成的身份证\n勾选后使用内置生成的身份证料子\n不勾选将弹出提示, 不启动任务")
        mianma_row = QHBoxLayout()
        mianma_row.addWidget(self.check_mianma)
        mianma_row.addWidget(self.check_neizhi)

        ly_cfg.addRow("注册数量", self.edit_num)
        ly_cfg.addRow("注册密码", self.edit_reg_pwd)
        ly_cfg.addRow("邀请码内容", self.edit_invite)
        ly_cfg.addRow("邀请码类型", self.cmb_invite_type)
        ly_cfg.addRow("并发线程数", self.cmb_thread_count)
        ly_cfg.addRow("线程延迟(秒)", self.edit_thread_delay)
        ly_cfg.addRow("注册间隔(秒)", self.edit_delay)
        ly_cfg.addRow("签到间隔(秒)", self.edit_sign_delay)
        ly_cfg.addRow("任务选择", self.cmb_task)
        ly_cfg.addRow("", mianma_row)

        group_proxy = QGroupBox("代理配置")
        ly_proxy = QFormLayout(group_proxy)
        self.edit_proxy_api = QLineEdit()
        self.edit_proxy_api2 = QLineEdit()  # 第二个代理API(可选): 两个API轮流取号, 每个账号只取一个
        self.check_use_proxy = QCheckBox("启用代理IP")
        self.btn_test_proxy = QPushButton("测试代理API")
        self.btn_test_proxy.clicked.connect(self.test_proxy_api)
        ly_proxy.addRow("代理API地址", self.edit_proxy_api)
        ly_proxy.addRow("代理API2(可选)", self.edit_proxy_api2)
        ly_proxy.addRow("", self.check_use_proxy)
        ly_proxy.addRow("", self.btn_test_proxy)

        group_haozhuma = QGroupBox("豪猪接码配置")
        ly_hz = QFormLayout(group_haozhuma)
        self.check_use_haozhuma = QCheckBox("启用豪猪接码")
        self.edit_hz_user = QLineEdit()
        self.edit_hz_user.setPlaceholderText("豪猪平台账号")
        self.edit_hz_pass = QLineEdit()
        self.edit_hz_pass.setPlaceholderText("豪猪平台密码")
        self.edit_hz_pass.setEchoMode(QLineEdit.Password)
        self.edit_hz_sid = QLineEdit()
        self.edit_hz_sid.setPlaceholderText("项目SID")
        self.edit_hz_ascription = QLineEdit()
        self.edit_hz_ascription.setPlaceholderText("留空=实号, 填2=虚拟号")
        self.check_hz_use_phone = QCheckBox("使用豪猪取号(替代本地手机号)")
        self.edit_hz_max_wait = QLineEdit("60")
        self.edit_hz_max_wait.setPlaceholderText("最长等待验证码(秒)")
        self.btn_test_haozhuma = QPushButton("测试豪猪登录")
        self.btn_test_haozhuma.clicked.connect(self.test_haozhuma_login)
        ly_hz.addRow("", self.check_use_haozhuma)
        ly_hz.addRow("账号", self.edit_hz_user)
        ly_hz.addRow("密码", self.edit_hz_pass)
        ly_hz.addRow("项目SID", self.edit_hz_sid)
        ly_hz.addRow("号码类型", self.edit_hz_ascription)
        ly_hz.addRow("", self.check_hz_use_phone)
        ly_hz.addRow("验证码等待", self.edit_hz_max_wait)
        ly_hz.addRow("", self.btn_test_haozhuma)

        self.btn_start = QPushButton("▶  开始运行")
        self.btn_start.setObjectName("btnStart")
        self.btn_stop = QPushButton("■  停止运行")
        self.btn_stop.setObjectName("btnStop")
        self.btn_start.clicked.connect(self.start_task)
        self.btn_stop.clicked.connect(self.stop_task)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)

        right_layout.addWidget(group_cfg)
        right_layout.addWidget(group_proxy)
        right_layout.addWidget(group_haozhuma)
        right_layout.addLayout(btn_layout)
        right_layout.addStretch()

        main_layout.addWidget(left_widget, stretch=7)
        main_layout.addWidget(right_widget, stretch=3)

        self.table_reg.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_reg.customContextMenuRequested.connect(lambda pos: self.table_right_menu(self.table_reg, pos))
        self.table_yanghao.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_yanghao.customContextMenuRequested.connect(lambda pos: self.table_right_menu(self.table_yanghao, pos))

        # 整个界面放进画布, 跟随窗口等比缩放(缩小一起缩小, 放大一起放大, 内容不会被裁掉)
        central.setFixedSize(self.BASE_W, self.BASE_H)   # 固定设计尺寸, 由视图整体缩放
        self._scene = QGraphicsScene(self)
        self._scene.addWidget(central)
        self._view = QGraphicsView(self._scene)
        self._view.setFrameShape(QFrame.NoFrame)
        self._view.setRenderHint(QPainter.Antialiasing)
        self._view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._view.setBackgroundBrush(QColor("#eef1f7"))
        self.setCentralWidget(self._view)
        self._apply_zoom()

    def _apply_zoom(self):
        """整个界面跟随窗口铺满缩放: 窗口多大界面就铺多满, 缩小一起缩小, 放大一起放大, 不会被裁掉"""
        vw = self._view.viewport().width()
        vh = self._view.viewport().height()
        if vw <= 0 or vh <= 0:
            return
        self._view.resetTransform()
        self._view.scale(vw / self.BASE_W, vh / self.BASE_H)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # 节流: 拖动过程中持续应用缩放, 但最多每80ms重绘一次, 避免卡顿
        if not self._zoom_timer.isActive():
            self._zoom_timer.start()

    def showEvent(self, event):
        super().showEvent(event)
        # 打开软件时, 等布局完成后立即强制铺满(立即执行会拿到旧/零尺寸导致留白)
        QTimer.singleShot(0, self._apply_zoom)

    def _sync_thread_count_to_worker(self, text):
        """运行中修改并发线程数时, 实时同步到后台任务(立即生效, 无需重启任务)"""
        try:
            if hasattr(self, "work_thread") and self.work_thread and self.work_thread.config:
                self.work_thread.config["thread_count"] = text
        except Exception:
            pass

    def set_ctrl_enabled(self, enable: bool):
        self.btn_start.setEnabled(enable)
        self.edit_num.setEnabled(enable)
        self.edit_reg_pwd.setEnabled(enable)
        self.edit_invite.setEnabled(enable)
        self.cmb_invite_type.setEnabled(enable)
        # 并发线程数在运行时也可以实时调节(改多少立即生效), 所以始终启用
        self.cmb_thread_count.setEnabled(True)
        # 延迟设置在运行时也可以调节，所以始终启用
        self.edit_thread_delay.setEnabled(True)
        self.edit_delay.setEnabled(True)
        self.edit_sign_delay.setEnabled(True)
        self.cmb_task.setEnabled(enable)
        self.edit_proxy_api.setEnabled(enable)
        self.edit_proxy_api2.setEnabled(enable)
        self.check_use_proxy.setEnabled(enable)
        self.btn_test_proxy.setEnabled(enable)
        self.check_use_haozhuma.setEnabled(enable)
        self.edit_hz_user.setEnabled(enable)
        self.edit_hz_pass.setEnabled(enable)
        self.edit_hz_sid.setEnabled(enable)
        self.edit_hz_ascription.setEnabled(enable)
        self.check_hz_use_phone.setEnabled(enable)
        self.edit_hz_max_wait.setEnabled(enable)
        self.btn_test_haozhuma.setEnabled(enable)
        self.btn_import_txt.setEnabled(enable)
        self.btn_export_yang.setEnabled(enable)
        self.btn_export_fail.setEnabled(enable)
        self.btn_clear_yang.setEnabled(enable)
        if hasattr(self, "edit_batch_invites"):
            self.edit_batch_invites.setEnabled(enable)

    # ---------- 批量邀请码注册 ----------
    def parse_batch_invites(self):
        """解析批量邀请码框: 每行 [邀请码]----[数量]
        返回 [(邀请码, 数量), ...]; 非法行跳过并记录日志"""
        text = self.edit_batch_invites.toPlainText().strip()
        if not text:
            return []
        result = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            line = line.rstrip("个").strip()
            m = re.match(r"^(.+?)\s*-{1,4}\s*(\d+)\s*$", line)
            if not m:
                self.append_log(f"⚠️ 批量邀请码行格式错误, 已忽略: [{line}]")
                continue
            code = m.group(1).strip()
            num = int(m.group(2))
            if not code or num <= 0:
                self.append_log(f"⚠️ 批量邀请码行格式错误, 已忽略: [{line}]")
                continue
            result.append((code, num))
        return result

    def on_batch_submit(self):
        """提交批量: 解析并校验, 显示目标数量, 供实时进度对比"""
        batch = self.parse_batch_invites()
        if not batch:
            QMessageBox.warning(self, "提示", "批量邀请码为空或全部格式错误！\n正确格式: 邀请码----数量(每行一个)\n例如: 19378900689----50")
            self.lbl_batch_progress.setText("尚未提交批量数据")
            return
        total = sum(n for _, n in batch)
        lines = "\n".join(f"    {code}: 目标{n}个" for code, n in batch)
        self.lbl_batch_progress.setText(f"已提交 {len(batch)} 条数据, 合计 {total} 个\n{lines}")
        self.append_log(f"📋 批量已提交: {len(batch)}条数据, 合计{total}个 (任务模式须选【批量注册(仅注册)】)")

    def fill_batch_example(self):
        self.edit_batch_invites.setPlainText("19378900689----50\n1234567----30")

    def on_batch_progress_snapshot(self, text):
        """批量注册实时进度刷新(来自工作线程)"""
        self.lbl_batch_progress.setText(text)

    def save_config(self):
        cfg = {
            "invite": self.edit_invite.text(),
            "invite_type": self.cmb_invite_type.currentText(),
            "thread_count": self.cmb_thread_count.text(),
            "thread_delay": self.edit_thread_delay.text(),
            "reg_delay": self.edit_delay.text(),
            "sign_delay": self.edit_sign_delay.text(),
            "reg_pwd": self.edit_reg_pwd.text(),
            "proxy_api": self.edit_proxy_api.text(),
            "proxy_api2": self.edit_proxy_api2.text(),
            "use_proxy": self.check_use_proxy.isChecked(),
            "reg_count": self.edit_num.text(),
            "haozhuma_enabled": self.check_use_haozhuma.isChecked(),
            "haozhuma_user": self.edit_hz_user.text(),
            "haozhuma_pass": self.edit_hz_pass.text(),
            "haozhuma_sid": self.edit_hz_sid.text(),
            "haozhuma_ascription": self.edit_hz_ascription.text(),
            "haozhuma_use_phone": self.check_hz_use_phone.isChecked(),
            "haozhuma_max_wait": self.edit_hz_max_wait.text(),
            "mianma": self.check_mianma.isChecked(),
            "neizhi": self.check_neizhi.isChecked(),
            "batch_invites_text": self.edit_batch_invites.toPlainText()
        }
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(cfg, f, ensure_ascii=False, indent=2)
        except:
            pass

    def load_config(self):
        default_cfg = {
            "invite": "19378900689",
            "invite_type": "自动识别",
            "thread_count": "5",
            "thread_delay": "0-0.2",
            "reg_pwd": "123456",
            "proxy_api": "",
            "proxy_api2": "",
            "use_proxy": False,
            "reg_delay": "0-0.2",
            "sign_delay": "5-15",
            "reg_count": "10"
        }
        if not os.path.exists(CONFIG_FILE):
            cfg = default_cfg
        else:
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    cfg = json.load(f)
            except:
                cfg = default_cfg

        self.edit_invite.setText(cfg.get("invite", default_cfg["invite"]))
        invite_type_str = cfg.get("invite_type", default_cfg["invite_type"])
        index = self.cmb_invite_type.findText(invite_type_str)
        if index >= 0:
            self.cmb_invite_type.setCurrentIndex(index)

        self.cmb_thread_count.setText(cfg.get("thread_count", default_cfg["thread_count"]))
        self.edit_thread_delay.setText(cfg.get("thread_delay", default_cfg["thread_delay"]))
        self.edit_delay.setText(cfg.get("reg_delay", default_cfg["reg_delay"]))
        self.edit_sign_delay.setText(cfg.get("sign_delay", default_cfg["sign_delay"]))

        self.edit_reg_pwd.setText(cfg.get("reg_pwd", default_cfg["reg_pwd"]))
        self.edit_proxy_api.setText(cfg.get("proxy_api", default_cfg["proxy_api"]))
        self.edit_proxy_api2.setText(cfg.get("proxy_api2", default_cfg["proxy_api2"]))
        self.check_use_proxy.setChecked(cfg.get("use_proxy", False))
        self.edit_num.setText(cfg.get("reg_count", default_cfg["reg_count"]))
        if hasattr(self, "edit_batch_invites"):
            self.edit_batch_invites.setPlainText(cfg.get("batch_invites_text", ""))

        self.check_use_haozhuma.setChecked(cfg.get("haozhuma_enabled", False))
        self.edit_hz_user.setText(cfg.get("haozhuma_user", ""))
        self.edit_hz_pass.setText(cfg.get("haozhuma_pass", ""))
        self.edit_hz_sid.setText(cfg.get("haozhuma_sid", ""))
        self.edit_hz_ascription.setText(cfg.get("haozhuma_ascription", ""))
        self.check_hz_use_phone.setChecked(cfg.get("haozhuma_use_phone", False))
        self.edit_hz_max_wait.setText(cfg.get("haozhuma_max_wait", "60"))
        self.check_mianma.setChecked(cfg.get("mianma", True))
        self.check_neizhi.setChecked(cfg.get("neizhi", True))

    def test_proxy_api(self):
        api = self.edit_proxy_api.text().strip()
        if not api:
            QMessageBox.warning(self, "提示", "请填写代理API地址")
            return
        try:
            import requests as req_lib
            resp = req_lib.get(api, timeout=12)
            ip = resp.text.strip().splitlines()[0]
            QMessageBox.information(self, "测试成功", f"获取代理：{ip}")
        except Exception as e:
            QMessageBox.critical(self, "测试失败", str(e))

    def test_haozhuma_login(self):
        user = self.edit_hz_user.text().strip()
        pwd = self.edit_hz_pass.text().strip()
        if not user or not pwd:
            QMessageBox.warning(self, "提示", "请填写豪猪账号和密码")
            return
        try:
            ok, token, balance = haozhuma_login(user, pwd)
            if ok:
                QMessageBox.information(self, "测试成功", f"登录成功！余额: {balance}元")
            else:
                QMessageBox.critical(self, "测试失败", f"登录失败: {token}")
        except Exception as e:
            QMessageBox.critical(self, "测试失败", str(e))

    def export_fail_account(self):
        path, _ = QFileDialog.getSaveFileName(self, "导出失败账号", "签到失败账号.txt", "Text(*.txt)")
        if not path:
            return
        content = ""
        for r in range(self.table_yanghao.rowCount()):
            phone = self.table_yanghao.item(r, 0).text() if self.table_yanghao.item(r, 0) else ""
            pwd = self.table_yanghao.item(r, 1).text() if self.table_yanghao.item(r, 1) else ""
            status = self.table_yanghao.item(r, 5).text() if self.table_yanghao.item(r, 5) else ""
            if phone and pwd and ("失败" in status or "代理" in status or "缺失" in status):
                content += f"{phone}----{pwd}\n"
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            QMessageBox.information(self, "成功", "失败账号导出完成")
        except Exception as e:
            QMessageBox.critical(self, "失败", str(e))

    def export_yang_table(self):
        path, _ = QFileDialog.getSaveFileName(self, "导出账号", "养号账号.txt", "Text(*.txt)")
        if not path:
            return
        content = ""
        for r in range(self.table_yanghao.rowCount()):
            phone = self.table_yanghao.item(r, 0).text() if self.table_yanghao.item(r, 0) else ""
            pwd = self.table_yanghao.item(r, 1).text() if self.table_yanghao.item(r, 1) else ""
            if phone and pwd:
                content += f"{phone}----{pwd}\n"
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            QMessageBox.information(self, "成功", "导出完成")
        except Exception as e:
            QMessageBox.critical(self, "失败", str(e))

    def update_yang_table_status(self, row_idx, status_text, ip_text):
        if row_idx < self.table_yanghao.rowCount():
            self.table_yanghao.setItem(row_idx, 3, QTableWidgetItem(ip_text))
            self.table_yanghao.setItem(row_idx, 5, QTableWidgetItem(status_text))

    def update_progress(self, curr, total):
        self._stats["curr"] = curr
        self._stats["total"] = total
        if self._task_start_time is None:
            self._task_start_time = time.time()
        self._refresh_progress()

    def update_stats(self, success, fail, total):
        """实时成功率/失败数统计"""
        self._stats["success"] = success
        self._stats["fail"] = fail
        self._stats["total"] = total
        self._refresh_progress()

    def _refresh_progress(self):
        """刷新进度条: 进度/成功率/速度/预计剩余时间"""
        st = self._stats
        total = st["total"]
        curr = st["curr"]
        done = st["success"] + st["fail"]
        pct = (st["success"] / done * 100) if done else 0.0

        speed = ""
        remain = ""
        if self._task_start_time is not None and done > 0:
            elapsed = time.time() - self._task_start_time
            if elapsed > 0:
                speed_val = done / elapsed
                speed = f" {speed_val:.2f}个/秒"
                if speed_val > 0 and total > 0 and done < total:
                    remain_sec = (total - done) / speed_val
                    if remain_sec >= 60:
                        remain = f" 剩余约{int(remain_sec // 60)}分{int(remain_sec % 60)}秒"
                    else:
                        remain = f" 剩余约{int(remain_sec)}秒"

        self.progress_bar.setMaximum(total)
        self.progress_bar.setValue(curr)
        self.progress_bar.setFormat(
            f"进度 {curr}/{total} | 成功 {st['success']} | 失败 {st['fail']} | 总计 {total} | 成功率 {pct:.1f}% |{speed}{remain}"
        )

    def on_task_break(self, msg):
        self.append_log(f"⚠️任务熔断终止：{msg}")
        QMessageBox.warning(self, "任务熔断", msg)

    def on_notify(self, msg):
        """一次性提示框(不中断任务): 如代理API耗尽降级虚拟IP注册"""
        self.append_log(msg)
        QMessageBox.information(self, "提示", msg)

    def table_right_menu(self, table: QTableWidget, pos):
        indexes = table.selectedIndexes()
        menu = QMenu(table)
        act_copy_phone = QAction("复制手机号", table)
        act_copy_pwd = QAction("复制密码", table)
        act_del_sel = QAction("删除选中行", table)
        act_del_all = QAction("全部删除", table)
        menu.addAction(act_copy_phone)
        menu.addAction(act_copy_pwd)
        menu.addSeparator()
        menu.addAction(act_del_sel)
        menu.addAction(act_del_all)

        def copy_phone():
            if indexes:
                item = table.item(indexes[0].row(), 0)
                if item:
                    QApplication.clipboard().setText(item.text())

        def copy_pwd():
            if indexes:
                item = table.item(indexes[0].row(), 1)
                if item:
                    QApplication.clipboard().setText(item.text())

        def del_sel():
            rows = list(set(i.row() for i in indexes))
            rows.sort(reverse=True)
            for r in rows:
                table.removeRow(r)

        def del_all():
            table.setRowCount(0)

        act_copy_phone.triggered.connect(copy_phone)
        act_copy_pwd.triggered.connect(copy_pwd)
        act_del_sel.triggered.connect(del_sel)
        act_del_all.triggered.connect(del_all)
        menu.exec(table.viewport().mapToGlobal(pos))

    def calc_expr(self, text):
        # 安全计算: 只支持加减乘除和括号, 用 ast 解析避免注入
        t = text.replace(" ", "")
        if not t:
            return "0"
        if not re.fullmatch(r'[0-9+\-*/().]+', t):
            return "0"
        try:
            node = ast.parse(t, mode="eval").body
        except SyntaxError:
            return "0"

        def _eval(n):
            if isinstance(n, ast.BinOp):
                l = _eval(n.left)
                r = _eval(n.right)
                if isinstance(n.op, ast.Add):
                    return l + r
                if isinstance(n.op, ast.Sub):
                    return l - r
                if isinstance(n.op, ast.Mult):
                    return l * r
                if isinstance(n.op, ast.Div):
                    if r == 0:
                        raise ZeroDivisionError
                    return l / r
                raise ValueError
            if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.UAdd, ast.USub)):
                v = _eval(n.operand)
                return v if isinstance(n.op, ast.UAdd) else -v
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
                return n.value
            raise ValueError

        try:
            result = _eval(node)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            return str(result)
        except (ZeroDivisionError, ValueError, TypeError):
            return "错误"

    def on_calc_changed(self, text):
        # 输入即算: 加减乘除, 非法/除0显示 错误
        self.lbl_calc_result.setText(self.calc_expr(text))

    def _get_schedule_dt(self):
        # 从数字框读取 月/日/时/分 组装成今天(今年)的 datetime
        now = datetime.now()
        m = self.spin_timer_month.value()
        d = self.spin_timer_day.value()
        h = self.spin_timer_hour.value()
        mi = self.spin_timer_min.value()
        return now.replace(month=m, day=d, hour=h, minute=mi, second=0, microsecond=0)

    def _update_timer_days(self):
        # 根据所选月份自动更新最大天数 (2月平年28天/闰年29天, 大月31天, 小月30天)
        if not hasattr(self, "spin_timer_day"):
            return
        m = self.spin_timer_month.value()
        days = calendar.monthrange(datetime.now().year, m)[1]
        self.spin_timer_day.setMaximum(days)
        if self.spin_timer_day.value() > days:
            self.spin_timer_day.setValue(days)

    def _reset_schedule(self):
        # 修改定时时间后重新解析
        if hasattr(self, "timer_scheduled_dt"):
            self.timer_scheduled_dt = None
        if hasattr(self, "lbl_timer_status"):
            self.lbl_timer_status.setStyleSheet("color: #94a3b8; font-weight: bold;")
            self.lbl_timer_status.setText("已修改时间, 等待生效")

    def check_schedule(self):
        # 每秒检查: 定时到点自动开始任务
        if not hasattr(self, "check_timer"):
            return
        if not self.check_timer.isChecked():
            self.timer_scheduled_dt = None
            self.timer_fired = False
            self._last_countdown_log = None
            if hasattr(self, "lbl_timer_status") and self.lbl_timer_status.text() != "未启用":
                self.lbl_timer_status.setStyleSheet("color: #94a3b8; font-weight: bold;")
                self.lbl_timer_status.setText("未启用")
            return
        if self.timer_fired:
            return
        # 读取下拉框选择的 月/日/时/分
        if self.timer_scheduled_dt is None:
            dt = self._get_schedule_dt()
            now = datetime.now()
            if dt is None or dt <= now:
                self.lbl_timer_status.setStyleSheet("color: #ef4444; font-weight: bold;")
                self.lbl_timer_status.setText("时间已过, 请选未来时间")
                return
            self.timer_scheduled_dt = dt
            self.lbl_timer_status.setStyleSheet("color: #16a34a; font-weight: bold;")
            self.lbl_timer_status.setText(f"已设定: {dt.strftime('%m月%d日 %H:%M')}, 等待自动启动")
            self.append_log(f"⏰ 定时任务已设定: {dt.strftime('%Y-%m-%d %H:%M')} 自动开始运行")
        # 到点触发
        remain = self.timer_scheduled_dt - datetime.now()
        if remain.total_seconds() <= 0:
            if self.running_flag:
                self.lbl_timer_status.setText("任务已在运行, 本次定时跳过")
                self.append_log("⏰ 定时时间到, 但任务正在运行, 已跳过自动启动")
                self.check_timer.setChecked(False)
                self.timer_fired = True
                self.timer_scheduled_dt = None
                self._last_countdown_log = None
                return
            self.lbl_timer_status.setText("已到时间, 正在自动启动...")
            self.append_log("⏰ 定时时间到, 正在自动开始任务")
            self.check_timer.setChecked(False)
            self.timer_scheduled_dt = None
            self._last_countdown_log = None
            self.start_task()
            if self.running_flag:
                self.timer_fired = True
                self.append_log("⏰ 定时任务已自动启动")
            else:
                self.timer_fired = False  # 被配置校验拦截, 下轮重试
                self.lbl_timer_status.setText("自动启动被拦截, 请检查配置后重新勾选")
            return
        # 倒计时
        total_s = int(remain.total_seconds())
        if 0 < total_s <= 30:
            # 最后30秒每秒在工作日志显示 时间处理 X秒
            if total_s != getattr(self, "_last_countdown_log", None):
                self._last_countdown_log = total_s
                self.append_log(f"时间处理 {total_s}秒")
        else:
            self._last_countdown_log = None
        h, rem = divmod(total_s, 3600)
        m, s = divmod(rem, 60)
        if h > 0:
            self.lbl_timer_status.setText(f"⏳ 倒计时: {h}时{m}分{s}秒")
        else:
            self.lbl_timer_status.setText(f"⏳ 倒计时: {m}分{s}秒")

    def clear_log_text(self):
        """清空日志内容"""
        self.log_text.clear()

    def copy_log_text(self):
        """复制全部日志到剪贴板"""
        text = self.log_text.toPlainText()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.append_log("日志已复制到剪贴板")

    def delete_selected_log(self):
        """删除选中的日志内容"""
        cursor = self.log_text.textCursor()
        if cursor.hasSelection():
            cursor.removeSelectedText()
            self.log_text.setTextCursor(cursor)

    def show_log_context_menu(self, pos):
        """显示日志右键菜单"""
        menu = QMenu(self)
        copy_action = menu.addAction("复制")
        copy_action.triggered.connect(self.log_text.copy)
        delete_action = menu.addAction("删除选中")
        delete_action.triggered.connect(self.delete_selected_log)
        menu.addSeparator()
        select_all_action = menu.addAction("全选")
        select_all_action.triggered.connect(self.log_text.selectAll)
        clear_action = menu.addAction("清空日志")
        clear_action.triggered.connect(self.clear_log_text)
        menu.exec_(self.log_text.mapToGlobal(pos))

    def append_log(self, text):
        ts = datetime.now().strftime('%H:%M:%S')
        if not text.startswith('['):
            text = f"[{ts}] {text}"
        self.log_text.append(text)
        doc = self.log_text.document()
        if doc.blockCount() > MAX_LOG_LINES:
            cursor = self.log_text.textCursor()
            cursor.movePosition(cursor.MoveOperation.Start)
            cursor.select(cursor.SelectionType.LineUnderCursor)
            cursor.removeSelectedText()
            self.log_text.setTextCursor(cursor)

    def pre_reg_row(self, tel, pwd, name, invite, ip, idcard):
        try:
            row = self.table_reg.rowCount()
            self.table_reg.insertRow(row)
            self.table_reg.setItem(row, 0, QTableWidgetItem(tel))
            self.table_reg.setItem(row, 1, QTableWidgetItem(pwd))
            self.table_reg.setItem(row, 2, QTableWidgetItem(name))
            self.table_reg.setItem(row, 3, QTableWidgetItem(idcard))
            self.table_reg.setItem(row, 4, QTableWidgetItem(ip))
            self.table_reg.setItem(row, 5, QTableWidgetItem(invite))
            self.table_reg.setItem(row, 6, QTableWidgetItem("注册中..."))
            # 记录 手机号 -> 行号 映射, 后续任务完成时用手机号定位行, 避免任务完成顺序与插入顺序不同导致错位
            self._reg_row_map[tel] = row
            self.table_reg.scrollToBottom()
        except Exception as e:
            self.append_log(f"UI更新错误(预显示): {str(e)}")

    def update_reg_row(self, tel, ip, status):
        try:
            row_idx = self._reg_row_map.get(tel)
            if row_idx is None:
                return  # 行尚未插入或已被清空, 忽略
            if ip:
                self.table_reg.setItem(row_idx, 4, QTableWidgetItem(ip))
            self.table_reg.setItem(row_idx, 6, QTableWidgetItem(status))
            self.table_reg.scrollToBottom()
        except Exception as e:
            self.append_log(f"UI更新错误(状态): {str(e)}")

    def update_card_row(self, tel, name, card):
        """重试时更新已有行的姓名/身份证, 不新增行"""
        try:
            row_idx = self._reg_row_map.get(tel)
            if row_idx is None:
                return
            self.table_reg.setItem(row_idx, 2, QTableWidgetItem(name))
            self.table_reg.setItem(row_idx, 3, QTableWidgetItem(card))
        except Exception as e:
            self.append_log(f"UI更新错误(资料): {str(e)}")

    def update_tel_row(self, old_tel, new_tel, name, card):
        """手机号已注册时换新号: 更新已有行的手机号/姓名/身份证并重定位行映射, 不新增行"""
        try:
            row_idx = self._reg_row_map.get(old_tel)
            if row_idx is None:
                return
            self.table_reg.setItem(row_idx, 0, QTableWidgetItem(new_tel))
            self.table_reg.setItem(row_idx, 2, QTableWidgetItem(name))
            self.table_reg.setItem(row_idx, 3, QTableWidgetItem(card))
            self._reg_row_map[new_tel] = row_idx
            self._reg_row_map.pop(old_tel, None)
        except Exception as e:
            self.append_log(f"UI更新错误(换号): {str(e)}")

    def on_enter_fill_row(self):
        text = self.edit_input_acc.text().strip()
        if not text:
            return
        if "----" not in text:
            QMessageBox.warning(self, "格式错误", "格式要求：手机号----密码")
            return
        tel, pwd = text.split("----", 1)
        tel = tel.strip()
        pwd = pwd.strip()
        row = self.table_yanghao.rowCount()
        self.table_yanghao.insertRow(row)
        self.table_yanghao.setItem(row, 0, QTableWidgetItem(tel))
        self.table_yanghao.setItem(row, 1, QTableWidgetItem(pwd))
        self.table_yanghao.setItem(row, 2, QTableWidgetItem(""))
        self.table_yanghao.setItem(row, 3, QTableWidgetItem(""))
        self.table_yanghao.setItem(row, 4, QTableWidgetItem(""))
        self.table_yanghao.setItem(row, 5, QTableWidgetItem("待执行"))
        self.edit_input_acc.clear()

    def import_yang_txt(self):
        path, _ = QFileDialog.getOpenFileName(self, "导入账号文本", "", "Text Files(*.txt)")
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line or "----" not in line:
                    continue
                tel, pwd = line.split("----", 1)
                tel = tel.strip()
                pwd = pwd.strip()
                row = self.table_yanghao.rowCount()
                self.table_yanghao.insertRow(row)
                self.table_yanghao.setItem(row, 0, QTableWidgetItem(tel))
                self.table_yanghao.setItem(row, 1, QTableWidgetItem(pwd))
                self.table_yanghao.setItem(row, 2, QTableWidgetItem(""))
                self.table_yanghao.setItem(row, 3, QTableWidgetItem(""))
                self.table_yanghao.setItem(row, 4, QTableWidgetItem(""))
                self.table_yanghao.setItem(row, 5, QTableWidgetItem("待执行"))
            QMessageBox.information(self, "导入完成", "账号导入成功！")
        except Exception as e:
            QMessageBox.critical(self, "导入失败", str(e))

    def clear_yang_table(self):
        self.table_yanghao.setRowCount(0)
        
    def clear_reg_table(self):
        """清空注册表单数据"""
        self.table_reg.setRowCount(0)
        self._reg_row_map.clear()  # 同步清空 手机号->行号 映射
        self.append_log("🧹 已自动清空注册表单，准备下一次任务")

    def start_task(self):
        if self.running_flag:
            QMessageBox.information(self, "提示", "任务正在运行中！")
            return

        # 定时已启用且时间在未来时, 不立即运行, 等待定时到点自动启动
        if hasattr(self, "check_timer") and self.check_timer.isChecked() and not self.timer_fired:
            if self.timer_scheduled_dt is None:
                self.timer_scheduled_dt = self._get_schedule_dt()
            if self.timer_scheduled_dt is not None and self.timer_scheduled_dt > datetime.now():
                self.append_log(f"⏰ 已勾选定时, 等待 {self.timer_scheduled_dt.strftime('%m月%d日 %H:%M')} 自动开始, 暂不立即运行")
                return

        task_sel = self.cmb_task.currentText()
        self.save_config()

        # 内置料子未勾选时信息框提示, 不启动任务
        if not self.check_neizhi.isChecked():
            QMessageBox.warning(self, "提示", "未勾选【内置料子】！\n将不会内置生成身份证料子，任务不启动。\n请勾选【内置料子】后再运行。")
            return

        # 免码未勾选且未启用豪猪取号时, 将无法获取手机号
        mianma_on = self.check_mianma.isChecked()
        hz_phone_on = self.check_use_haozhuma.isChecked() and self.check_hz_use_phone.isChecked()
        if not mianma_on and not hz_phone_on:
            QMessageBox.warning(self, "提示", "未勾选【免码】且未启用豪猪取号！\n将无法获取手机号注册。\n请勾选【免码】或启用豪猪取号。")
            return

        invite_type_val = "auto"

        # 批量注册(仅注册): 只有该任务模式才使用批量邀请码框, 其他模式不受影响
        batch_invites = []
        if task_sel == "批量注册(仅注册)":
            batch_invites = self.parse_batch_invites()
            if not batch_invites:
                QMessageBox.warning(self, "提示", "【批量注册(仅注册)】需要先填写批量邀请码！\n"
                                    "正确格式: 邀请码----数量(每行一个)\n"
                                    "例如:\n19378900689----50   (手机号类型)\n1234567----30       (ID类型)\n"
                                    "请到【计算器和定时启动】页右侧的批量框填写后点【提交批量】")
                return
            batch_total = sum(n for _, n in batch_invites)
            self.append_log(f"📋 批量注册(仅注册): 共{len(batch_invites)}条数据, 合计{batch_total}个账号")

        cfg = {
            "count": self.edit_num.text(),
            "invite": self.edit_invite.text(),
            "invite_type": invite_type_val,
            "batch_invites": batch_invites,
            "thread_count": self.cmb_thread_count.text(),
            "thread_delay_range": self.edit_thread_delay.text(),
            "delay_range": self.edit_delay.text(),
            "sign_delay_range": self.edit_sign_delay.text(),
            "reg_pwd": self.edit_reg_pwd.text(),
            "use_proxy": self.check_use_proxy.isChecked(),
            "proxy_api": self.edit_proxy_api.text(),
            "proxy_api2": self.edit_proxy_api2.text(),
            "mianma": mianma_on,
            "neizhi": self.check_neizhi.isChecked(),
            "haozhuma": {
                "enabled": self.check_use_haozhuma.isChecked(),
                "user": self.edit_hz_user.text().strip(),
                "pass": self.edit_hz_pass.text().strip(),
                "sid": self.edit_hz_sid.text().strip(),
                "country_code": "CN",
                "ascription": self.edit_hz_ascription.text().strip(),
                "use_hz_phone": self.check_hz_use_phone.isChecked(),
                "max_wait": int(self.edit_hz_max_wait.text() or "60"),
                "interval": 2,
                "code_keywords": ["验证码为：", "验证码:", "验证码是"]
            }
        }
        self.work_thread.config = cfg

        if task_sel == "仅注册任务":
            self.work_thread.task_type = TASK_REGISTER_ONLY
            self.clear_reg_table()
        elif task_sel == "注册签到任务":
            self.work_thread.task_type = TASK_REGISTER
            self.clear_reg_table()
        elif task_sel == "批量注册(仅注册)":
            self.work_thread.task_type = TASK_REGISTER_ONLY
            self.clear_reg_table()
            # 重置批量实时进度显示为已提交的目标
            self.on_batch_submit()
        else:
            self.work_thread.task_type = TASK_SIGN
            acc_list = []
            for r in range(self.table_yanghao.rowCount()):
                tel = self.table_yanghao.item(r, 0).text() if self.table_yanghao.item(r, 0) else ""
                pwd = self.table_yanghao.item(r, 1).text() if self.table_yanghao.item(r, 1) else ""
                name = self.table_yanghao.item(r, 2).text() if self.table_yanghao.item(r, 2) else ""
                inv = self.table_yanghao.item(r, 4).text() if self.table_yanghao.item(r, 4) else ""
                if tel and pwd:
                    acc_list.append((tel, pwd, name, inv))
            if not acc_list:
                QMessageBox.warning(self, "警告", "养号表格为空，请先导入账号！\n（当前任务为【签到任务】；如需注册请将【任务选择】切换为【注册任务】）")
                return
            self.work_thread.account_list = acc_list

        self.set_ctrl_enabled(False)
        self.running_flag = True
        # 重置实时统计(成功率/速度/预计剩余)
        self._stats = {"success": 0, "fail": 0, "total": 0, "curr": 0}
        self._task_start_time = time.time()
        self.work_thread.start()

    def stop_task(self):
        # 停止优先级最高: 任何时候点击立即生效
        # 1) 先取消定时(倒计时中/已设定都取消)
        if hasattr(self, "timer_scheduled_dt") and self.timer_scheduled_dt is not None:
            self.timer_scheduled_dt = None
            if hasattr(self, "timer_fired"):
                self.timer_fired = False
            self._last_countdown_log = None
            if hasattr(self, "check_timer"):
                self.check_timer.setChecked(False)
            if hasattr(self, "lbl_timer_status"):
                self.lbl_timer_status.setStyleSheet("color: #94a3b8; font-weight: bold;")
                self.lbl_timer_status.setText("定时已取消")
            self.append_log("⏹ 已取消定时任务")
        if not self.running_flag:
            self.append_log("⏹ 当前没有运行中的任务")
            return
        self.append_log("⚠️已发送停止指令：正在立即终止所有任务...")
        self.work_thread.stop_force()

    def task_finish(self):
        self.running_flag = False
        self.set_ctrl_enabled(True)
        self._task_start_time = None  # 任务结束, 清空计时, 下次任务重新统计
        self.append_log("======= 当前任务全部结束 =======")


# ===================== 深色主题样式表 =====================
PREMIUM_QSS = """
QMainWindow, QWidget {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #fefefe, stop:0.3 #f5f7fb, stop:0.7 #eef1f7, stop:1 #e8ecf4);
    color: #1e293b;
    font-family: "Microsoft YaHei", "PingFang SC", "Segoe UI", sans-serif;
    font-size: 13px;
}

QGroupBox {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #fafbff);
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    margin-top: 16px;
    padding: 10px 12px 10px 12px;
    color: #475569;
    font-weight: bold;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 5px 18px;
    color: #ffffff;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #6366f1, stop:0.5 #8b5cf6, stop:1 #ec4899);
    border: none;
    border-radius: 10px;
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #f1f5f9);
    color: #475569;
    border: 1px solid #dbe1ea;
    border-radius: 10px;
    padding: 8px 18px;
    font-weight: bold;
    min-height: 18px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ede9fe, stop:1 #ddd6fe);
    border: 1px solid #a5b4fc;
    color: #6d28d9;
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #c7d2fe, stop:1 #a5b4fc);
}

QPushButton:disabled {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #f8fafc, stop:1 #f1f5f9);
    color: #94a3b8;
    border: 1px solid #e2e8f0;
}

QPushButton#btnStart {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #10b981, stop:0.5 #06b6d4, stop:1 #3b82f6);
    color: #ffffff;
    border: none;
    font-weight: bold;
    font-size: 14px;
    padding: 14px 24px;
    border-radius: 12px;
}

QPushButton#btnStart:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #34d399, stop:0.5 #22d3ee, stop:1 #60a5fa);
    color: #ffffff;
}

QPushButton#btnStart:disabled {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #cbd5e1, stop:1 #94a3b8);
    color: #f1f5f9;
    border: none;
}

QPushButton#btnStop {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #f43f5e, stop:0.5 #ef4444, stop:1 #f97316);
    color: #ffffff;
    border: none;
    font-weight: bold;
    font-size: 14px;
    padding: 14px 24px;
    border-radius: 12px;
}

QPushButton#btnStop:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #fb7185, stop:0.5 #f87171, stop:1 #fb923c);
    color: #ffffff;
}

QPushButton#btnStop:disabled {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #cbd5e1, stop:1 #94a3b8);
    color: #f1f5f9;
    border: none;
}

QPushButton#btnClearLog, QPushButton#btnCopyLog, QPushButton#btnDeleteSelected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #e2e8f0, stop:1 #cbd5e1);
    color: #475569;
    border: 1px solid #94a3b8;
    border-radius: 6px;
    padding: 4px 12px;
    font-size: 12px;
    min-height: 24px;
}

QPushButton#btnClearLog:hover, QPushButton#btnCopyLog:hover, QPushButton#btnDeleteSelected:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #cbd5e1, stop:1 #94a3b8);
    border: 1px solid #64748b;
}

QPushButton#btnClearLog:pressed, QPushButton#btnCopyLog:pressed, QPushButton#btnDeleteSelected:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #94a3b8, stop:1 #64748b);
    color: #ffffff;
}

QLineEdit, QComboBox, QTextEdit {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #fafbff);
    color: #0f172a;
    font-size: 14px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 2px 10px;
    min-height: 34px;
    selection-background-color: #a5b4fc;
    selection-color: #ffffff;
}

QLineEdit:focus, QComboBox:focus {
    border: 1px solid #8b5cf6;
    background: #ffffff;
}

QLineEdit:hover, QComboBox:hover {
    border: 1px solid #c4b5fd;
}

QLineEdit:disabled, QComboBox:disabled, QTextEdit:disabled {
    color: #94a3b8;
    background: #f1f5f9;
}

QLabel {
    color: #475569;
}

QComboBox {
    padding-right: 20px;
}

QComboBox::drop-down {
    border: none;
    width: 24px;
}

QComboBox QAbstractItemView {
    background: #ffffff;
    color: #1e293b;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    selection-background-color: #ede9fe;
    selection-color: #6d28d9;
    outline: 0;
    padding: 6px;
}

QTabWidget::pane {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #fafbff);
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    top: -1px;
}

QTabBar::tab {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #f8fafc, stop:1 #eef1f7);
    color: #94a3b8;
    border: 1px solid #e2e8f0;
    border-bottom: none;
    border-top-left-radius: 12px;
    border-top-right-radius: 12px;
    padding: 10px 26px;
    margin-right: 2px;
    font-weight: bold;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #fafbff);
    color: #7c3aed;
    border-color: #c4b5fd;
    border-bottom: 3px solid #8b5cf6;
}

QTabBar::tab:hover:!selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #f1f5f9, stop:1 #e2e8f0);
    color: #6366f1;
}

QTableWidget {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #fafbff);
    color: #334155;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    gridline-color: #edf0f5;
    selection-background-color: #ede9fe;
    selection-color: #6d28d9;
    alternate-background-color: #f8fafc;
}

QTableWidget::item {
    padding: 6px 10px;
    border-bottom: 1px solid #f1f5f9;
}

QHeaderView::section {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ede9fe, stop:0.5 #e0e7ff, stop:1 #dbeafe);
    color: #5b21b6;
    border: 1px solid #c7d2fe;
    border-top: none;
    padding: 9px 10px;
    font-weight: bold;
}

QProgressBar {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    text-align: center;
    color: #1e293b;
    font-weight: bold;
    font-size: 13px;
    min-height: 24px;
}

QProgressBar#mainProgress {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #f1f5f9);
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    text-align: center;
    color: #1e293b;
    font-weight: bold;
    font-size: 14px;
    min-height: 30px;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #10b981, stop:0.25 #06b6d4, stop:0.5 #8b5cf6, stop:0.75 #ec4899, stop:1 #f59e0b);
    border-radius: 12px;
}

QCheckBox {
    color: #475569;
    spacing: 10px;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border-radius: 6px;
    border: 2px solid #cbd5e1;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #f8fafc);
}

QCheckBox::indicator:checked {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #6366f1, stop:0.5 #8b5cf6, stop:1 #ec4899);
    border: 2px solid #8b5cf6;
    image: none;
}

QCheckBox::indicator:hover {
    border: 2px solid #a78bfa;
}

QScrollBar:vertical {
    background: #f1f5f9;
    width: 12px;
    border: none;
    border-radius: 6px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #cbd5e1, stop:1 #94a3b8);
    border-radius: 6px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #c4b5fd, stop:1 #8b5cf6);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background: #f1f5f9;
    height: 12px;
    border: none;
    border-radius: 6px;
    margin: 2px;
}

QScrollBar::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #cbd5e1, stop:1 #94a3b8);
    border-radius: 6px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #c4b5fd, stop:1 #8b5cf6);
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

QMenu {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #f8fafc);
    color: #1e293b;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 8px;
}

QMenu::item {
    padding: 8px 28px;
    border-radius: 8px;
}

QMenu::item:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ede9fe, stop:1 #ddd6fe);
    color: #6d28d9;
}

QMenu::separator {
    height: 1px;
    background-color: #e2e8f0;
    margin: 6px 10px;
}

QMessageBox {
    background: #f8fafc;
}

QMessageBox QLabel {
    color: #1e293b;
}

QFileDialog {
    background: #f8fafc;
}

QStatusBar {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #f1f5f9);
    color: #64748b;
    border-top: 1px solid #e2e8f0;
}

/* 顶部状态栏: 跟随任务进程实时更新 */
QFrame#topStatus {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #ffffff, stop:0.6 #f8fafc, stop:1 #eef2f9);
    border: 1px solid #e2e8f0;
    border-radius: 10px;
}
QLabel#statusLabel {
    color: #334155;
    font-size: 14px;
    font-weight: bold;
}
QLabel#statusDot {
    font-size: 18px;
}

/* 右侧配置区滚动区域: 透明无边框, 缩小窗口时输入框不会被裁掉 */
QScrollArea#rightScroll {
    background: transparent;
    border: none;
}
QScrollArea#rightScroll > QWidget > QWidget {
    background: transparent;
}
QScrollArea#rightScroll QScrollBar:vertical {
    background: transparent;
    width: 10px;
    margin: 2px;
}
QScrollArea#rightScroll QScrollBar::handle:vertical {
    background: #c7d2fe;
    border-radius: 5px;
    min-height: 30px;
}
QScrollArea#rightScroll QScrollBar::handle:vertical:hover {
    background: #a5b4fc;
}

QToolTip {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #f8fafc);
    color: #1e293b;
    border: 1px solid #e2e8f0;
    padding: 6px 10px;
    border-radius: 8px;
}

QTextEdit#logText {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:0.5 #fafbff, stop:1 #f5f7fb);
    color: #059669;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    font-family: "Consolas", "Microsoft YaHei", monospace;
    font-size: 12px;
    padding: 12px;
}

QTextEdit#logText:focus {
    border: 1px solid #c4b5fd;
}
"""

if __name__ == "__main__":
    # 启用高DPI缩放支持
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    # 强制使用 Fusion 样式 + 深色文字调色板, 避免 Windows 深色模式下输入框/表格文字变白看不见
    app.setStyle(QStyleFactory.create("Fusion"))
    _pal = QPalette()
    _pal.setColor(QPalette.WindowText, QColor("#1e293b"))
    _pal.setColor(QPalette.Text, QColor("#0f172a"))
    _pal.setColor(QPalette.PlaceholderText, QColor("#64748b"))
    _pal.setColor(QPalette.ButtonText, QColor("#475569"))
    _pal.setColor(QPalette.Base, QColor("#ffffff"))
    _pal.setColor(QPalette.Window, QColor("#f5f7fb"))
    _pal.setColor(QPalette.ToolTipBase, QColor("#ffffff"))
    _pal.setColor(QPalette.ToolTipText, QColor("#1e293b"))
    _pal.setColor(QPalette.Highlight, QColor("#8b5cf6"))
    _pal.setColor(QPalette.HighlightedText, QColor("#ffffff"))
    _pal.setColor(QPalette.Disabled, QPalette.Text, QColor("#94a3b8"))
    _pal.setColor(QPalette.Disabled, QPalette.WindowText, QColor("#94a3b8"))
    app.setPalette(_pal)
    app.setStyleSheet(PREMIUM_QSS)

    win = MainWin()
    win.show()

    # ===== 全局异常兜底: 出现未处理异常只结束任务, 不退出软件 =====
    _main_win = win

    def _safe_excepthook(exc_type, exc_value, exc_tb):
        """PyQt槽函数/主线程未处理异常统一拦截: 记录日志 + 停止任务, 保持软件不关闭"""
        _write_crash_log(exc_type, exc_value, exc_tb)
        try:
            if _main_win is not None:
                _main_win.append_log(f"⚠️ 发生异常(软件保持运行): {exc_value}")
                if getattr(_main_win, "running_flag", False):
                    # 延迟到事件循环空闲时停止任务, 避免在异常回调中直接操作UI/线程导致二次崩溃
                    QTimer.singleShot(0, _main_win.stop_task)
        except Exception:
            pass

    sys.excepthook = _safe_excepthook

    sys.exit(app.exec_())