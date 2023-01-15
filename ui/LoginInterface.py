import re

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtWidgets import *

from ui.UserInterface import InterfaceInput

"""
登录界面

author: liuyilei7566@gmail.com
date: 2023.1.8
"""


class LoginInterface(QWidget):

    def __init__(self, parent=None):
        super(LoginInterface, self).__init__(parent)
        self.interface = None
        self.loginBtn: QPushButton = None
        self.exitBtn: QPushButton = None
        self.passWordInput: QLineEdit = None
        self.initView()

    # 初始化view
    def initView(self):
        form = QFormLayout()

        labelName = QLabel()
        labelName.setText("お帰りなさい：")
        labelNameUser = QLabel()
        labelNameUser.setText("刘一雷")

        label = QLabel()
        label.setText("密码: ")
        self.passWordInput = QLineEdit()

        self.loginBtn = QPushButton()
        self.loginBtn.setText("登录")
        self.exitBtn = QPushButton()
        self.exitBtn.setText("再见")

        form.addRow(labelName, labelNameUser)
        form.addRow(label, self.passWordInput)
        form.addRow(self.loginBtn, self.exitBtn)
        self.loginBtn.clicked.connect(self.login)
        self.exitBtn.clicked.connect(self.exit)
        self.setLayout(form)

    # 点击登录
    def login(self):
        if re.match("^我回来了*", self.passWordInput.text(), re.I):
            self.interface = InterfaceInput()
            self.interface.show()
            self.hide()
        self.passWordInput.clear()

    # 点击退出
    def exit(self):
        self.close()
