import segno
from io import BytesIO
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class QQrViz(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__("No QR Generated", *args, **kwargs)


    def genQr(self, content, light, dark, scale):
        buf = BytesIO()
        qrc = segno.make(content, error='H', micro=False)
        qrc.save(buf, kind="png", dark=dark, light=light, scale=scale)
        buf.seek(0)
        pix = QPixmap()
        pix.loadFromData(buf.read())
        self.clear()
        self.setPixmap(pix)
