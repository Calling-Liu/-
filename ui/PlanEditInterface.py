import os
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtWidgets import *

from resources.values import ProjectValues
from ui.TaskEditInterface import TaskEditInterface
from src.model.TaskItemModel import *

"""
任务显示界面

author: liuyilei7566@gmail.com
date: 2023.1.8
"""


class PlanEditInterface(QWidget):

    def __init__(self, parent=None):
        super(PlanEditInterface, self).__init__(parent)
        self.newTask: QPushButton = None
        self.editInterface = None
        self.taskList: QListWidget = None
        self.title = None
        self.projectPath = None
        self.planData: list = []
        self.initView()

    def initView(self):
        self.setWindowTitle(ProjectValues.PROJECT_NAME)
        self.resize(1067, 600)
        self.initParams()
        self.loadData()
        self.addView()

    def initParams(self):
        self.projectPath = os.path.abspath("../")

    def addView(self):
        layout_main = QVBoxLayout()
        layout_main.setAlignment(QtCore.Qt.AlignTop)
        # 任务列表
        self.taskList: QListWidget = QListWidget()
        self.taskList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.taskList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.taskList.setViewMode(QtWidgets.QListView.ListMode)
        self.taskList.setWordWrap(True)
        self.taskList.setStyleSheet("background-color:transparent;border:none")
        # 标题
        self.title = QLabel()
        titleBitmap = QPixmap(self.projectPath + '\\resources\\image\\planTitle.png')
        self.title.setPixmap(titleBitmap)
        self.title.setMaximumHeight(80)
        self.title.setStyleSheet("background-color:#AEEEEE")
        self.addPlanList()
        # 新建按钮
        self.newTask = QPushButton()
        self.newTask.setText("新建任务")
        self.newTask.setFixedSize(200, 30)

        data = TaskItemModel()
        data.number = -1
        data.content = ""
        data.updateTime = ""
        data.priority = 2
        self.newTask.clicked.connect(lambda: self.showEditInterface(data))

        layout_main.addWidget(self.title)
        layout_main.addWidget(self.taskList)
        layout_main.addWidget(self.newTask, alignment=QtCore.Qt.AlignCenter)
        self.setLayout(layout_main)

    def addPlanList(self):
        self.taskList.clear()
        size = len(self.planData)
        for i in range(0, size):
            item: QListWidget.QListWidgetItem = QListWidgetItem()
            item.setSizeHint(QSize(200, 80))

            model: TaskItemModel = TaskItemModel()
            model.number = self.planData[i].number
            model.updateTime = self.planData[i].updateTime
            model.content = self.planData[i].content
            model.priority = self.planData[i].priority

            self.taskList.addItem(item)
            self.taskList.setItemWidget(item, self.getItemView(model))

    def loadData(self):
        self.planData = []
        with open(self.projectPath + "\\database\\" + ProjectValues.PLAN_DATABASE, "r") as f:
            while True:
                line = f.readline()
                lineData: list = line.split('&')
                if len(lineData) == 4:
                    model = TaskItemModel()
                    model.number = lineData[0]
                    model.content = lineData[1]
                    model.updateTime = lineData[2]
                    model.priority = lineData[3].replace("\n", "")

                    self.planData.append(model)
                if not line:
                    break

    # 获取任务列表的itemWidget
    def getItemView(self, itemData):
        data: TaskItemModel = itemData

        widget = QWidget()
        # 横向主布局
        layout_main = QHBoxLayout()
        # 右边主布局
        layout_right_main = QVBoxLayout()
        # 右边下面的布局
        layout_right_bottom = QHBoxLayout()
        # 按钮布局
        layout_right_button = QVBoxLayout()

        # 序号
        number = QLabel()
        number.setText(str(data.number))
        number.setMaximumWidth(30)
        number.setStyleSheet("font-size:30px")
        # 内容
        content = QLabel()
        content.setText(data.content)
        content.setContentsMargins(10, 5, 10, 0)

        # 时间
        time = QLabel()
        time.setText(data.updateTime)
        time.setContentsMargins(10, 0, 10, 0)
        time.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)

        # 优先级
        priority = QLabel()

        priority.setContentsMargins(10, 0, 10, 0)
        priority.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        if data.priority == '0':
            priority.setStyleSheet("color:#ff3333")
            priority.setText("优先级: 高")
        elif data.priority == '1':
            priority.setStyleSheet("color:#ff9933")
            priority.setText("优先级: 中")
        else:
            priority.setStyleSheet("color:#00ff66")
            priority.setText("优先级: 低")

        # 编辑
        editBtn = QPushButton()
        editBtn.setText("编辑")
        editBtn.setMaximumWidth(100)
        editBtn.clicked.connect(lambda: self.showEditInterface(data))

        # 删除
        deleteBtn = QPushButton()
        deleteBtn.setText("删除")
        deleteBtn.setMaximumWidth(100)
        deleteBtn.clicked.connect(lambda: self.deletePlan(data.number))

        layout_right_main.addWidget(content)
        layout_right_bottom.addWidget(time)
        layout_right_bottom.addWidget(priority)
        layout_main.addWidget(number)
        layout_right_button.addWidget(editBtn)
        layout_right_button.addWidget(deleteBtn)

        layout_main.addLayout(layout_right_main)
        layout_right_main.addLayout(layout_right_bottom)
        layout_main.addLayout(layout_right_button)
        widget.setLayout(layout_main)
        return widget

    # 展示编辑页面
    def showEditInterface(self, data):
        model: TaskItemModel = data
        self.editInterface = TaskEditInterface(plan=self, data=model)
        self.editInterface.show()

    # 删除计划
    def deletePlan(self, identity):
        modelNew = ""
        index: int = 0
        position: int = 0
        with open(self.projectPath + "\\database\\" + ProjectValues.PLAN_DATABASE, "r+") as f:
            while True:
                srtLine = ""
                line = f.readline()
                dataLine: list = line.split('&')
                if len(dataLine) > 0 and dataLine[0] != '':
                    index = int(dataLine[0])
                    if dataLine[0] == str(identity):
                        continue
                    else:
                        position += 1
                        srtLine = str(position) + "&" + dataLine[1] + "&" + dataLine[2] + "&" + dataLine[3]
                if srtLine != "":
                    if not srtLine.find("\n"):
                        srtLine += "\n"
                    modelNew += srtLine
                if not line:
                    break

            f.seek(0)
            f.truncate()
            modelNew = modelNew[0:(len(modelNew) - 1):1]
            f.write(modelNew)
        self.loadData()
        self.addPlanList()

