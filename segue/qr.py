import segno
from io import BytesIO
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class QQrViz(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__("No QR Generated", *args, **kwargs)


    def regen_preview(self, content, light, dark):
        buf = BytesIO()
        qrc = segno.make(content, error='H', micro=False)
        qrc.save(buf, kind="png", dark=dark, light=light, scale=9)
        pix = QPixmap()
        pix.loadFromData(buf.getvalue())
        self.clear()
        self.setPixmap(pix)

    def create_image(self, content, light, dark, scale):
        buf = BytesIO()
        buf = BytesIO()
        qrc = segno.make(content, error='H', micro=False)
        qrc.save(buf, kind="png", dark=dark, light=light, scale=scale)

        return buf.getvalue()
