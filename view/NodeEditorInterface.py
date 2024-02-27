from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView

from common.NodeGraphicsScene import NodeGraphicsScene


class NodeEditorInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.layout = QVBoxLayout()
        self.view = QGraphicsView(self)
        self.scene = NodeGraphicsScene()

        self.init_widget()

    def init_widget(self):
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.view.setScene(self.scene)
        self.layout.addWidget(self.view)

        self.set_qss()

    def set_qss(self):
        self.setObjectName('NodeEditorInterface')
