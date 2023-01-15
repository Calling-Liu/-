import os
import re
import string

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtWidgets import *

from resources.values import ProjectValues
from src.model.TaskItemModel import *
from ui.PlanEditInterface import *

"""
编辑任务界面

author: liuyilei7566@gmail.com
date: 2023.1.8
"""


class TaskEditInterface(QWidget):

    def __init__(self, parent=None, plan=None, data=None):
        super(TaskEditInterface, self).__init__(parent)
        self.planInterface: PlanEditInterface = plan
        self.labelPrioritySelect: QComboBox = None
        self.exitBtn = None
        self.checkBtn = None
        self.content: QTextEdit = None
        self.projectPath = None
        self.model: TaskItemModel = data
        self.initParams()
        self.initView()

    def initParams(self):
        self.projectPath = os.path.abspath("../")

    def initView(self):
        self.addView()

    def addView(self):
        form = QFormLayout()

        labelPriority = QLabel()
        labelPriority.setText("优先级")
        listPriority = ['高', "中", "低"]
        self.labelPrioritySelect = QComboBox()
        self.labelPrioritySelect.addItems(listPriority)
        self.labelPrioritySelect.setCurrentIndex(int(self.model.priority))

        label = QLabel()
        label.setText("任务内容: ")
        self.content: QTextEdit = QTextEdit()
        self.content.setText(self.model.content)

        self.checkBtn = QPushButton()
        self.checkBtn.setText("确认")
        self.exitBtn = QPushButton()
        self.exitBtn.setText("取消")

        form.addRow(labelPriority, self.labelPrioritySelect)
        form.addRow(label)
        form.addRow(self.content)
        form.addRow(self.checkBtn)
        form.addRow(self.exitBtn)
        self.checkBtn.clicked.connect(self.saveEdit)
        self.exitBtn.clicked.connect(lambda: self.close())

        self.setLayout(form)

    def saveEdit(self):
        if self.content.toPlainText() == "":
            return
        modelNew = ""
        checked: bool = False
        index: int = 0
        with open(self.projectPath + "\\database\\" + ProjectValues.PLAN_DATABASE, "r+") as f:
            while True:
                srtLine = ""
                line = f.readline()
                dataLine: list = line.split('&')
                if len(dataLine) > 0 and dataLine[0] != '':
                    index = int(dataLine[0])
                    if dataLine[0] == str(self.model.number):
                        srtLine += (dataLine[0] + "&" + self.content.toPlainText() + "&"
                                    + QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
                                    + "&" + str(self.coverPriority(self.labelPrioritySelect.currentText())) + "\n")
                        checked = True
                    else:
                        srtLine = line
                if srtLine != "":
                    if srtLine[len(srtLine) - 1: len(srtLine):1] != "\n":
                        srtLine += "\n"
                    modelNew += srtLine
                if not line:
                    break
            if not checked:
                index += 1
                modelNew += (str(index) + "&" + self.content.toPlainText() + "&"
                             + QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
                             + "&" + str(self.coverPriority(self.labelPrioritySelect.currentText())) + "\n")
            f.seek(0)
            f.truncate()
            modelNew = modelNew[0:(len(modelNew) - 1):1]
            f.write(modelNew)
        self.planInterface.loadData()
        self.planInterface.addPlanList()
        self.close()

    def coverPriority(self, priority):
        if priority == "高":
            return 0
        elif priority == "中":
            return 1
        else:
            return 2
