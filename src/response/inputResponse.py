import re

from PyQt5 import QtCore
from ui.PlanEditInterface import *

"""
对于输入的信息进行响应

author: liuyilei7566@gmail.com
date:   2022.10.16
"""


class InputResponse(object):

    # 对输入的message进行response
    def __init__(self):
        self.planInterface = None

    def getResponse(self, message):
        if message.isspace():
            return "你好!"
        elif re.match("^几点了*", message, re.I):
            return QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        elif re.match("^你叫什么名字*", message, re.I):
            return "上月由良"
        elif re.match("^晚安*", message, re.I):
            return "えん、こんばんは"
        elif re.match("^打开聊天界面*", message, re.I):
            self.planInterface = PlanEditInterface()
            self.planInterface.show()
            return "好的"
        else:
            return "请重新输入"
