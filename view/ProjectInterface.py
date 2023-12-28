from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QSplitter, QHBoxLayout, QVBoxLayout
from qfluentwidgets import ScrollArea, ExpandLayout, SearchLineEdit, PushButton, ToolButton, ToolTipFilter, FluentIcon, \
    SmoothScrollArea

from common.MyWidget import ProjectCard, ProjectGroup
from common.StyleSheet import StyleSheet


class ProjectInterface(QWidget):
    """ Home interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.base_layout = QVBoxLayout(self)

        self.top_widget = QWidget(self)
        self.top_layout = QHBoxLayout(self.top_widget)
        self.search_input = SearchLineEdit(self.top_widget)
        self.new_button = PushButton(FluentIcon.ADD, self.tr('new project'), self.top_widget)
        self.open_btn = PushButton(FluentIcon.FOLDER, self.tr('open folder'), self.top_widget)

        self.h_line = QFrame(self)

        self.scroll_area = ScrollArea(self)
        self.scroll_widget = QWidget(self)
        self.scroll_layout = ExpandLayout(self.scroll_widget)

        self.project_group = ProjectGroup(self.scroll_widget)

        # self.pj1 = ProjectCard('Project 1', 'C:/Users/DELL/Desktop/Project 1', self.project_group)

        self.init_widget()

    def init_widget(self):
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.setViewportMargins(0, 10, 0, 20)
        self.setLayout(self.base_layout)
        # self.setAlignment(Qt.AlignHCenter)
        # self.setWidgetResizable(True)

        # self.base_layout.setContentsMargins(30, 0, 30, 0)
        self.base_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.top_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top_widget.setMinimumHeight(60)

        self.new_button.installEventFilter(ToolTipFilter(self.new_button))
        self.new_button.setToolTip(self.tr('create new project'))
        self.open_btn.installEventFilter(ToolTipFilter(self.open_btn))
        self.open_btn.setToolTip(self.tr('open exist folder as project'))

        self.h_line.setFrameShape(QFrame.HLine)
        self.h_line.setFrameShadow(QFrame.Sunken)

        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_widget.setMaximumWidth(1000)

        self.init_layout()
        self.set_qss()

    def init_layout(self):
        self.top_layout.addWidget(self.search_input)
        self.top_layout.addWidget(self.new_button)
        self.top_layout.addWidget(self.open_btn)

        self.base_layout.addWidget(self.top_widget)
        self.base_layout.addWidget(self.h_line)

        for i in range(14):
            self.project_group.add_card(
                ProjectCard(f'Project {i}', 'C:/Users/DELL/Desktop/Project 1', self.project_group))
        self.scroll_layout.addWidget(self.project_group)
        self.base_layout.addWidget(self.scroll_area)

    def set_qss(self):
        self.setObjectName('ProjectInterface')
        self.scroll_widget.setObjectName('ScrollWidget')

        StyleSheet.SCROLL.apply(self)
