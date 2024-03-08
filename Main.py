import os
import sys

from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator

from common.Config import cfg
from view.MainWindow import MainWindow

# enable dpi scale
if cfg.get(cfg.dpiScale) != "Auto":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

logger.add('log/run_time.log')


app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

locale = cfg.get(cfg.language).value
translator = FluentTranslator(locale)

app.installTranslator(translator)

w = MainWindow()
w.show()

logger.info('start')

app.exec()
