import math

from PyQt5.QtCore import QLine
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QGraphicsScene


class NodeGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.grid_seize = 20

        self.pen = QPen(QColor('#2f2f2f'))
        self.pen.setWidth(1)

        self.width, self.height = 64000, 64000
        self.setSceneRect(self.width / 2, self.height / 2, self.width, self.height)

        self.setBackgroundBrush(QColor('#393939'))

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.grid_seize)
        first_top = top - (top % self.grid_seize)

        lines = []
        for x in range(first_left, right, self.grid_seize):
            lines.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_seize):
            lines.append(QLine(left, y, right, y))

        painter.setPen(self.pen)
        painter.drawLines(lines)

