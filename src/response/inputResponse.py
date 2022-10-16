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
        elif message == "几点了？":
            return QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        else:
            return "请重新输入"
