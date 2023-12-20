from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import MSFluentWindow, SplashScreen, NavigationItemPosition, FluentIcon
from loguru import logger

from common.Config import cfg, VERSION
from view.ProjectInterface import ProjectInterface
from view.SettingInterface import SettingInterface


class MainWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.init_window()

        self.projectInterface = ProjectInterface(self)
        self.settingInterface = SettingInterface(self)

        self.init_navigation()
        self.splash_screen.finish()
        logger.debug('init done')

    def init_window(self):
        self.setMinimumSize(1008, 800)
        # self.setWindowIcon(QIcon(':/gallery/images/logo.png'))
        self.setWindowTitle(f'RamanEditor {VERSION}')

        # self.hBoxLayout.setContentsMargins(0, 20, 0, 28)

        # self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))

        # create splash screen
        self.splash_screen = SplashScreen(self.windowIcon(), self)
        self.splash_screen.setIconSize(QSize(106, 106))
        self.splash_screen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.showMaximized()

        # self.navigationInterface.setAcrylicEnabled(True)
        # self.navigationInterface.setReturnButtonVisible(False)
        # self.navigationInterface.panel.toggle()
        # logger.debug(self.navigationInterface.panel.displayMode)

        QApplication.processEvents()

    def init_navigation(self):
        self.addSubInterface(self.projectInterface, FluentIcon.FOLDER, self.tr('Projects'))
        self.addSubInterface(
            self.settingInterface, FluentIcon.SETTING, 'Settings', position=NavigationItemPosition.BOTTOM)
