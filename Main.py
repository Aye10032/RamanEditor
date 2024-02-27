import os
import sys

from loguru import logger
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator
from qfluentwidgetspro import setLicense, ProTranslator

from common.Config import cfg
from view.MainWindow import MainWindow

# enable dpi scale
if cfg.get(cfg.dpiScale) == "Auto":
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
else:
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

logger.add('log/run_time.log')

with open('resources/pyqt_license.txt', 'r', encoding='utf-8') as f:
    license_text = f.read()

setLicense(license_text)

app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

locale = cfg.get(cfg.language).value
translator = FluentTranslator(locale)
proTranslator = ProTranslator(locale)

app.installTranslator(translator)
app.installTranslator(proTranslator)

w = MainWindow()
w.show()

logger.info('start')

app.exec()
