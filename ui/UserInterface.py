from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from src.response.inputResponse import InputResponse

"""
用户输入界面,完成和用户之间的交互

author:  liuyilei7566@gmail.com
date:    2022.10.15
"""


class InterfaceInput(QWidget):
    def __init__(self, parent=None):
        super(InterfaceInput, self).__init__(parent)
        self.messageList = None  # 展示信息的列表
        self.sendMessageButton = None
        self.label1 = None
        self.textInput: QTextEdit = None
        self.responser = InputResponse()
        self.initView()

    # 初始化view
    def initView(self):
        self.setWindowTitle("浅沫")
        self.resize(800, 600)
        self.addView()

    # 添加子view组件
    def addView(self):
        grid = QGridLayout()  # 网格布局
        self.label1 = QLabel()
        self.textInput: QTextEdit = QTextEdit()
        self.sendMessageButton: QPushButton = QPushButton("确认")
        self.messageList: QListWidget = QListWidget()

        self.label1.setText(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss"))
        self.textInput.setFixedWidth(780)
        self.textInput.setFixedHeight(60)
        self.messageList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.messageList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.messageList.setViewMode(QtWidgets.QListView.ListMode)
        self.messageList.setWordWrap(True)

        grid.addWidget(self.label1, 0, 0, 1, 4, QtCore.Qt.AlignCenter)
        grid.addWidget(self.messageList, 1, 0, 3, 4)
        grid.addWidget(self.textInput, 4, 0, 1, 4)
        grid.addWidget(self.sendMessageButton, 5, 3, QtCore.Qt.AlignRight)

        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setText(self.responser.getResponse(" "))
        self.messageList.addItem(item)

        self.sendMessageButton.clicked.connect(self.sendMessage)
        self.setLayout(grid)

    # 发送message获取响应，并添加到显示列表
    def sendMessage(self):
        message = self.textInput.toPlainText()
        self.addMyInputToList(message)
        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setText(self.responser.getResponse(message))
        self.messageList.addItem(item)
        self.textInput.clear()

    # 将用户输入的信息,显示到屏幕上
    def addMyInputToList(self, message):
        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setText(message)
        self.messageList.addItem(item)
