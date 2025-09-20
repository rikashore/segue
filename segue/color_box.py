from PySide6.QtCore import QSize, Qt, QRect
from PySide6.QtGui import QPainter, QBrush
from PySide6.QtWidgets import QWidget

class QColorBox(QWidget):
    def __init__(self, initial_color, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.color = initial_color

    def sizeHint(self):
        return QSize(25, 25)
    
    def paintEvent(self, _):
        painter = QPainter(self)

        brush = QBrush()
        brush.setColor(self.color)
        brush.setStyle(Qt.BrushStyle.SolidPattern)

        rect = QRect(
            0, 
            0, 
            painter.device().width(), 
            painter.device().height()
        )

        painter.fillRect(rect, brush)

    def setColor(self, new_color):
        self.color = new_color
        self.update()