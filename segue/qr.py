import segno
from io import BytesIO
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class QQrViz(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.viz_label = QLabel("No QR generated")
        self.viz_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sv_btn = QPushButton("Save")

        layout.addWidget(self.viz_label)
        layout.addWidget(self.sv_btn)

        self.setLayout(layout)

    def genQr(self, content, light, dark, scale):
        buf = BytesIO()
        qrc = segno.make(content, error='H', micro=False)
        qrc.save(buf, kind="png", dark=dark, light=light, scale=scale)
        buf.seek(0)
        pix = QPixmap()
        pix.loadFromData(buf.read())
        self.viz_label.clear()
        self.viz_label.setPixmap(pix)
