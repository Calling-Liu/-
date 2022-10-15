import sys

from PyQt5.QtWidgets import QApplication
from ui.UserInterface import InterfaceInput

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = InterfaceInput()
    interface.show()
    sys.exit(app.exec_())

