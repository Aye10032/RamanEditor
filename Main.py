import os
import sys

from loguru import logger
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator

from common.Config import cfg
from view.MainWindow import MainWindow

# enable dpi scale
if cfg.get(cfg.dpiScale) == "Auto":
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
else:
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

logger.add('log/run_time.log')

if not os.path.exists('./data'):
    os.mkdir('./data')

app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

locale = cfg.get(cfg.language).value
translator = FluentTranslator(locale)

app.installTranslator(translator)

w = MainWindow()
w.show()

logger.info('start')

app.exec()
