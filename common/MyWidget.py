from typing import List

from PyQt5.QtCore import QPoint, Qt, pyqtSignal, QUrl
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel, QFileDialog
from qfluentwidgets import CardWidget, RoundMenu, Action, FluentIcon, IconWidget, BodyLabel, CaptionLabel, \
    TransparentToolButton, ExpandLayout, FluentStyleSheet, setFont, MessageBoxBase, SubtitleLabel, LineEdit, ToolButton

from common.MyFluentIcon import LetterIcon
from loguru import logger


class ProjectCard(CardWidget):
    def __init__(self, title, content, index, parent=None):
        super().__init__(parent)
        self.content = content
        self.index = index

        self.iconWidget = IconWidget(LetterIcon.A, self)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.iconWidget.setFixedSize(48, 48)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignRight)

        self.moreButton.setFixedSize(32, 32)
        self.moreButton.clicked.connect(self.on_more_button_clicked)

    def on_more_button_clicked(self):
        menu = RoundMenu(parent=self)
        menu.addAction(Action(FluentIcon.FOLDER, self.tr('Open in explorer'), self))
        menu.addAction(Action(FluentIcon.EDIT, self.tr('Rename'), self))
        menu.addAction(Action(FluentIcon.DELETE, self.tr('Remove'), self, triggered=self.remove_card))

        x = (self.moreButton.width() - menu.width()) // 2 + 10
        pos = self.moreButton.mapToGlobal(QPoint(x, self.moreButton.height()))
        menu.exec(pos)

    def remove_card(self):
        logger.debug(self.content)


class ProjectGroup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.cardLayout = ExpandLayout()

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.setSpacing(0)
        self.cardLayout.setContentsMargins(0, 0, 0, 0)
        self.cardLayout.setSpacing(2)

        self.vBoxLayout.addLayout(self.cardLayout, 1)

        FluentStyleSheet.SETTING_CARD_GROUP.apply(self)

    def add_card(self, card: QWidget):
        """ add card to group """
        card.setParent(self)
        self.cardLayout.addWidget(card)
        self.adjustSize()

    def add_cards(self, cards: List[QWidget]):
        """ add cards to group """
        for card in cards:
            self.addSettingCard(card)

    def adjustSize(self):
        h = self.cardLayout.heightForWidth(self.width()) + 46
        return self.resize(self.width(), h)


class ProjectDialog(MessageBoxBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel(self.tr('New Project'), self)

        self.name_input = LineEdit(self)
        self.name_input.setPlaceholderText(self.tr('Project Name'))

        self.path_widget = QWidget(self)
        self.path_layout = QHBoxLayout(self.path_widget)
        self.path_input = LineEdit(self.path_widget)
        self.path_btn = ToolButton(FluentIcon.FOLDER, self.path_widget)
        self.path_layout.addWidget(self.path_input)
        self.path_layout.addWidget(self.path_btn)
        self.path_layout.setContentsMargins(0, 0, 0, 0)

        self.path_input.setPlaceholderText(self.tr('Project Location'))
        self.path_input.setClearButtonEnabled(True)

        # add widget to view layout
        self.viewLayout.setAlignment(Qt.AlignHCenter)
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.name_input)
        self.viewLayout.addWidget(self.path_widget)
        self.viewLayout.addStretch(1)

        # change the text of button
        self.yesButton.setText(self.tr('Finish'))
        self.cancelButton.setText(self.tr('Cancel'))

        self.widget.setMinimumSize(600, 400)
        self.yesButton.setDisabled(True)
        self.path_input.textChanged.connect(self.validate_url)
        self.path_btn.clicked.connect(self.select_path)

        # self.hideYesButton()

    def validate_url(self, text):
        self.yesButton.setEnabled(QUrl(text).isValid())

    def select_path(self):
        folder = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        self.path_input.setText(folder)
