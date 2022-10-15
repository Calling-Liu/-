from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget, QTextEdit

"""
用户输入界面,完成和用户之间的交互

author:  liuyilei7566@gmail.com
date:    2022.10.15
"""


class InterfaceInput(QWidget):
    def __init__(self, parent=None):
        super(InterfaceInput, self).__init__(parent)
        self.sendMessageButton = None
        self.label1 = None
        self.textInput: QTextEdit = None
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

        self.label1.setText(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss"))
        self.textInput.setFixedWidth(780)
        self.textInput.setFixedHeight(60)

        grid.addWidget(self.label1, 0, 0, 1, 4, QtCore.Qt.AlignCenter)
        grid.addWidget(self.textInput, 4, 0, 1, 4)
        grid.addWidget(self.sendMessageButton, 5, 3, QtCore.Qt.AlignRight)

        self.sendMessageButton.clicked.connect(self.sendMessage)
        self.setLayout(grid)

    def sendMessage(self):
        self.label1.setText(self.textInput.toPlainText())
