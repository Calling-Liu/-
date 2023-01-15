import sys

from PyQt5.QtWidgets import QApplication

from ui.LoginInterface import *
from ui.PlanEditInterface import *
from ui.TaskEditInterface import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = LoginInterface()
    interface.show()
    sys.exit(app.exec_())

