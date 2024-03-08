from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import ScrollArea, ExpandLayout, SettingCardGroup, SwitchSettingCard, OptionsSettingCard, \
    FluentIcon, CustomColorSettingCard, ComboBoxSettingCard, setTheme, setThemeColor
from loguru import logger

from common.Config import  cfg
from common.StyleSheet import StyleSheet


class SettingInterface(ScrollArea):
    """ Setting interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scroll_widget = QWidget()
        self.expandLayout = ExpandLayout(self.scroll_widget)

        # personalization
        self.personalGroup = SettingCardGroup(
            self.tr('Personalization'), self.scroll_widget)
        self.micaCard = SwitchSettingCard(
            FluentIcon.TRANSPARENT,
            self.tr('Mica effect'),
            self.tr('Apply semi transparent to windows and surfaces'),
            cfg.micaEnabled,
            self.personalGroup
        )
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FluentIcon.BRUSH,
            self.tr('Application theme'),
            self.tr("Change the appearance of your application"),
            texts=[
                self.tr('Light'), self.tr('Dark'),
                self.tr('Use system setting')
            ],
            parent=self.personalGroup
        )
        self.themeColorCard = CustomColorSettingCard(
            cfg.themeColor,
            FluentIcon.PALETTE,
            self.tr('Theme color'),
            self.tr('Change the theme color of you application'),
            self.personalGroup
        )
        self.zoomCard = OptionsSettingCard(
            cfg.dpiScale,
            FluentIcon.ZOOM,
            self.tr("Interface zoom"),
            self.tr("Change the size of widgets and fonts"),
            texts=[
                "100%", "125%", "150%", "175%", "200%",
                self.tr("Use system setting")
            ],
            parent=self.personalGroup
        )
        self.languageCard = ComboBoxSettingCard(
            cfg.language,
            FluentIcon.LANGUAGE,
            self.tr('Language'),
            self.tr('Set your preferred language for UI'),
            texts=['简体中文', '繁體中文', 'English', self.tr('Use system setting')],
            parent=self.personalGroup
        )

        self.init_widget()

    def init_widget(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 60, 0, 20)
        self.setWidget(self.scroll_widget)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setWidgetResizable(True)

        self.scroll_widget.setMaximumWidth(1000)

        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 0, 36, 10)

        self.init_layout()
        self.init_qss()
        self.connect_signals()

    def init_layout(self):
        self.personalGroup.addSettingCard(self.micaCard)
        self.personalGroup.addSettingCard(self.themeCard)
        self.personalGroup.addSettingCard(self.themeColorCard)
        self.personalGroup.addSettingCard(self.zoomCard)
        self.personalGroup.addSettingCard(self.languageCard)

        self.expandLayout.addWidget(self.personalGroup)

    def init_qss(self):
        self.setObjectName('SettingInterface')

        self.scroll_widget.setObjectName('ScrollWidget')

        StyleSheet.SCROLL.apply(self)

    def connect_signals(self):
        self.themeCard.optionChanged.connect(lambda ci: setTheme(cfg.get(ci)))
        self.themeColorCard.colorChanged.connect(setThemeColor)
