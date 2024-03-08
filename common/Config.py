import sys
from enum import Enum

from PySide6.QtCore import QLocale
from qfluentwidgets import ConfigSerializer, QConfig, ConfigItem, BoolValidator, qconfig, Theme, OptionsConfigItem, \
    OptionsValidator


class Language(Enum):
    """ Language enumeration """

    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)
    CHINESE_TRADITIONAL = QLocale(QLocale.Chinese, QLocale.HongKong)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    """ Language serializer """

    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else 'Auto'

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != 'Auto' else Language.AUTO


def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


class Config(QConfig):
    """ Configuration """

    # main window
    micaEnabled = ConfigItem("MainWindow", "MicaEnabled", isWin11(), BoolValidator())
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)
    language = OptionsConfigItem(
        "MainWindow", "Language", Language.AUTO, OptionsValidator(Language), LanguageSerializer(), restart=True)


YEAR = 2023
AUTHOR = 'Aye10032'
VERSION = '1.0.0_beta'

cfg = Config()
cfg.themeMode.value = Theme.AUTO
qconfig.load('config/config.json', cfg)
