import re

from PyQt5 import QtCore

"""
对于输入的信息进行响应

author: liuyilei7566@gmail.com
date:   2022.10.16
"""


class InputResponse(object):

    # 对输入的message进行response
    def getResponse(self, message):
        if message.isspace():
            return "你好!"
        elif re.match("^几点了*", message, re.I):
            return QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        elif re.match("^你叫什么名字*", message, re.I):
            return "上月由良"
        elif re.match("^晚安*", message, re.I):
            return "えん、こんばんは"
        else:
            return "请重新输入"
