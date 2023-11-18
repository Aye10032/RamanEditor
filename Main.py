# create application
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from view.MainWindow import MainWindow

app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

w = MainWindow()
w.show()

app.exec()
