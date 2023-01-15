"""
任务数据模型

author: liuyilei7566@gmail.com
date: 2023.1.8
"""


class TaskItemModel:
    def __init__(self):
        self.number: int = 0
        self.updateTime = ""
        self.content = ""
        self.priority: int = 0