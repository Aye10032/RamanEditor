from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QSplitter, QHBoxLayout
from qfluentwidgets import ScrollArea, ExpandLayout, SearchLineEdit, PushButton, ToolButton, ToolTipFilter, FluentIcon

from common.StyleSheet import StyleSheet


class ProjectInterface(ScrollArea):
    """ Home interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scroll_widget = QWidget()
        self.expand_layout = ExpandLayout(self.scroll_widget)

        self.top_widget = QWidget(self.scroll_widget)
        self.top_layout = QHBoxLayout(self.top_widget)
        self.search_input = SearchLineEdit(self.top_widget)
        self.new_button = PushButton(FluentIcon.ADD, self.tr('new project'), self.top_widget)
        self.open_btn = PushButton(FluentIcon.FOLDER, self.tr('open folder'), self.top_widget)

        self.h_line = QFrame(self.scroll_widget)

        self.init_widget()

    def init_widget(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 10, 0, 20)
        self.expand_layout.setContentsMargins(30, 0, 30, 0)
        self.setWidget(self.scroll_widget)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setWidgetResizable(True)

        # self.scroll_widget.setMaximumWidth(1000)

        self.top_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top_widget.setMinimumHeight(60)

        self.new_button.installEventFilter(ToolTipFilter(self.new_button))
        self.new_button.setToolTip(self.tr('create new project'))
        self.open_btn.installEventFilter(ToolTipFilter(self.open_btn))
        self.open_btn.setToolTip(self.tr('open exist folder as project'))

        self.h_line.setFrameShape(QFrame.HLine)
        self.h_line.setFrameShadow(QFrame.Sunken)

        self.init_layout()
        self.set_qss()

    def init_layout(self):
        self.top_layout.addWidget(self.search_input)
        self.top_layout.addWidget(self.new_button)
        self.top_layout.addWidget(self.open_btn)

        self.expand_layout.addWidget(self.top_widget)
        self.expand_layout.addWidget(self.h_line)
        self.expand_layout.addWidget(PushButton(self.scroll_widget))

    def set_qss(self):
        self.setObjectName('ProjectInterface')
        self.scroll_widget.setObjectName('ScrollWidget')

        StyleSheet.SCROLL.apply(self)
