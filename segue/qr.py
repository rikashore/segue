from io import BytesIO
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class QrViz(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._buf = BytesIO()

        layout = QVBoxLayout()
        self.viz_label = QLabel("No QR generated")
        self.viz_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sv_btn = QPushButton("Save")

        layout.addWidget(self.viz_label)
        layout.addWidget(self.sv_btn)

        self.setLayout(layout)
