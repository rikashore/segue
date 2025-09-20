from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QLabel
from qr import QQrViz

class SegueMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Segue")

        self.setMinimumSize(960, 540)
        self.setMaximumSize(1600, 900)

        self.statusBar().setSizeGripEnabled(False)
        self.statusBar().showMessage("Segue Ready", 3000)

        layout = QHBoxLayout()

        l1 = QQrViz()
        l2 = QLabel("Naurrr")
        l2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(l1)
        layout.addWidget(l2)

        central = QWidget()
        central.setLayout(layout)

        l1.genQr("Swara why", light="#FFFFFF", dark="#111111", scale=5)

        self.setCentralWidget(central)
