from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtWidgets import *

from resources.values import ProjectValues
from src.response.inputResponse import InputResponse
import os

"""
用户输入界面,完成和用户之间的交互

author:  liuyilei7566@gmail.com
date:    2022.10.15
"""


class InterfaceInput(QWidget):
    def __init__(self, parent=None):
        super(InterfaceInput, self).__init__(parent)
        self.projectPath = None
        self.messageList: QListWidget = None  # 展示信息的列表
        self.sendMessageButton = None
        self.label1 = None
        self.textInput: QTextEdit = None
        self.responser = InputResponse()
        self.initParams()
        self.initView()

    # 初始化参数
    def initParams(self):
        self.projectPath = os.path.abspath("../")

    # 初始化view
    def initView(self):
        self.setWindowTitle(ProjectValues.PROJECT_NAME)
        self.resize(1067, 600)
        self.addView()
        self.setWindowsBg()

    def setWindowsBg(self):
        # 设置窗口背景
        palette: QtGui.QPalette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,
                         QBrush(QPixmap(self.projectPath + '\\resources\\image\\windowBg.png')
                                .scaled(self.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)))
        self.setPalette(palette)

    # 添加子view组件
    def addView(self):
        grid = QGridLayout()  # 网格布局
        self.label1 = QLabel()
        self.textInput: QTextEdit = QTextEdit()
        self.sendMessageButton: QPushButton = QPushButton("确认")
        self.messageList: QListWidget = QListWidget()

        self.label1.setText(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss"))
        self.textInput.setFixedHeight(50)
        self.messageList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.messageList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.messageList.setViewMode(QtWidgets.QListView.ListMode)
        self.messageList.setWordWrap(True)
        self.messageList.setStyleSheet("background-color:transparent;border:none")

        grid.addWidget(self.label1, 0, 0, 1, 4, QtCore.Qt.AlignCenter)
        grid.addWidget(self.messageList, 1, 0, 3, 4)
        grid.addWidget(self.textInput, 4, 0, 1, 4)
        grid.addWidget(self.sendMessageButton, 5, 3, QtCore.Qt.AlignRight)

        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setSizeHint(QSize(200, 50))
        beginHi = self.responser.getResponse(" ")
        self.messageList.addItem(item)
        self.messageList.setItemWidget(item, self.getMessageViewItemView(beginHi, True))

        self.sendMessageButton.clicked.connect(self.sendMessage)
        self.setLayout(grid)

    # 发送message获取响应，并添加到显示列表
    def sendMessage(self):
        message = self.textInput.toPlainText()
        if message == "":
            return
        self.addMyInputToList(message)
        responseMsg = self.responser.getResponse(message)
        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setSizeHint(QSize(200, 50))
        itemWight = self.getMessageViewItemView(responseMsg, True)
        self.messageList.addItem(item)
        self.messageList.setItemWidget(item, itemWight)
        self.textInput.clear()

    def resizeEvent(self, event):
        self.setWindowsBg()

    # 将用户输入的信息,显示到屏幕上
    def addMyInputToList(self, message):
        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setSizeHint(QSize(200, 50))
        self.messageList.addItem(item)
        self.messageList.setItemWidget(item, self.getMessageViewItemView(message, False))

    # 获取对话的itemView
    def getMessageViewItemView(self, msg, isLeft):
        wight = QWidget()
        layout_main = QHBoxLayout()

        layout_main.setContentsMargins(0, 0, 0, 0)

        # 设置头像
        icon = QLabel()
        icon.setFixedSize(40, 40)
        icon.setStyleSheet("border:none")
        icon.setMargin(0)

        # 设置消息
        text = QLabel()
        text.setText(msg)
        text.setMaximumHeight(40)
        text.setContentsMargins(10, 0, 10, 0)

        if isLeft:
            text.setStyleSheet("background-color:#AEEEEE;border:none")
            bitmap = QPixmap(self.projectPath + '\\resources\\image\\rorih.png').scaled(40, 40)
            icon.setPixmap(bitmap)
            layout_main.addWidget(icon)
            layout_main.addWidget(text)
            layout_main.setAlignment(QtCore.Qt.AlignLeft)
        else:
            text.setStyleSheet("background-color:#00FA9A;border:none")
            bitmap = QPixmap(self.projectPath + '\\resources\\image\\qianmo.png').scaled(40, 40)
            icon.setPixmap(bitmap)
            layout_main.addWidget(text)
            layout_main.addWidget(icon)
            layout_main.setAlignment(QtCore.Qt.AlignRight)

        wight.setLayout(layout_main)
        return wight
