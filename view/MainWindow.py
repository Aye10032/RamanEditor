from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, SplashScreen
from loguru import logger

from common.Config import cfg, VERSION


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.init_window()

        self.splash_screen.finish()
        logger.debug('init done')

    def init_window(self):
        self.setMinimumSize(1008, 800)
        # self.setWindowIcon(QIcon(':/gallery/images/logo.png'))
        self.setWindowTitle(f'RamanEditor {VERSION}')

        self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))

        # create splash screen
        self.splash_screen = SplashScreen(self.windowIcon(), self)
        self.splash_screen.setIconSize(QSize(106, 106))
        self.splash_screen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.showMaximized()

        # self.navigationInterface.setAcrylicEnabled(True)
        self.navigationInterface.setReturnButtonVisible(False)
        self.navigationInterface.panel.toggle()
        logger.debug(self.navigationInterface.panel.displayMode)

        QApplication.processEvents()
