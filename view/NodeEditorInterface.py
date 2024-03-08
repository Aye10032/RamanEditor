from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QFrame, QGraphicsScene
from qfluentwidgets import CommandBar, Action, FluentIcon

from common.NodeGraphicsScene import NodeGraphicsScene
from common.StyleSheet import StyleSheet


class NodeEditorInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.layout = QVBoxLayout()

        self.commandBar = CommandBar(self)
        self.run = Action(FluentIcon.PLAY, self.tr('run'), self)

        self.scene = NodeGraphicsScene(self)
        # self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)

        self.init_widget()

    def init_widget(self):
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.commandBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.commandBar.addAction(self.run)

        self.layout.addWidget(self.commandBar)
        self.layout.addWidget(self.view)

        self.set_qss()

    def set_qss(self):
        self.setObjectName('NodeEditorInterface')
        StyleSheet.NODE.apply(self)
