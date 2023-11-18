import sys

from loguru import logger
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from view.MainWindow import MainWindow


logger.add('log/run_time.log')
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

w = MainWindow()
w.show()

logger.info('start')

app.exec()
