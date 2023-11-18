from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, SplashScreen


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.splash_screen: SplashScreen = None
        self.init_window()

        # enable acrylic effect
        self.navigationInterface.setAcrylicEnabled(True)

        # self.connectSignalToSlot()

        # add items to navigation interface
        # self.initNavigation()
        self.splash_screen.finish()

    def init_window(self):
        self.resize(960, 780)
        self.setMinimumWidth(760)
        # self.setWindowIcon(QIcon(':/gallery/images/logo.png'))
        self.setWindowTitle('PyQt-Fluent-Widgets')

        # self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))

        # create splash screen
        self.splash_screen = SplashScreen(self.windowIcon(), self)
        self.splash_screen.setIconSize(QSize(106, 106))
        self.splash_screen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()
