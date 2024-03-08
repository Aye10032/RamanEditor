import math

from PySide6.QtCore import QLine
from PySide6.QtGui import QColor, QPen, QPainterPath
from PySide6.QtWidgets import QGraphicsScene


class NodeGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.grid_seize = 20
        self.grid_count = 5

        self.pen_light = QPen(QColor('#303030'))
        self.pen_light.setWidth(1)
        self.pen_dark = QPen(QColor('#292929'))
        self.pen_dark.setWidth(1)

        self.width, self.height = 64000, 64000
        self.setSceneRect(self.width / 2, self.height / 2, self.width, self.height)

        # self.setBackgroundBrush(QColor('#393939'))

    def drawBackground(self, painter, rect):
        # super().drawBackground(painter, rect)

        # 窗口圆角
        view_rect = self.views()[0].rect()
        view_rect.moveTo(int(rect.topLeft().x()), int(rect.topLeft().y()))
        path = QPainterPath()
        path.addRoundedRect(view_rect, 10, 10)

        # 裁切
        painter.setClipPath(path)

        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.grid_seize)
        first_top = top - (top % self.grid_seize)

        lines_light = []
        lines_dark = []
        for x in range(first_left, right, self.grid_seize):
            lines_light.append(QLine(x, top, x, bottom)) if x % (self.grid_count * self.grid_seize) != 0 \
                else lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_seize):
            lines_light.append(QLine(left, y, right, y)) if y % (self.grid_count * self.grid_seize) != 0 \
                else lines_dark.append(QLine(left, y, right, y))

        painter.setPen(self.pen_light)
        painter.drawLines(lines_light)

        painter.setPen(self.pen_dark)
        painter.drawLines(lines_dark)

        painter.setClipping(False)
