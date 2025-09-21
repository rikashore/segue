from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from qr import QQrViz
from controls import QQrControls

class SegueMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Segue")

        self.setMinimumSize(960, 540)
        self.setMaximumSize(960, 540)

        self.statusBar().setSizeGripEnabled(False)
        self.statusBar().showMessage("Segue Ready", 3000)

        layout = QHBoxLayout()

        self.qr_viz = QQrViz()
        self.qr_viz.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.qr_viz, stretch=1)

        self.qr_controls = QQrControls()
        self.qr_controls.update_btn.clicked.connect(self.update_button_clicked)

        layout.addWidget(self.qr_controls, stretch=1)

        central = QWidget()
        central.setLayout(layout)

        self.setCentralWidget(central)

    def update_button_clicked(self):
        self.qr_viz.genQr(
            self.qr_controls.contents.text(),
            self.qr_controls.light_color.name(),
            self.qr_controls.dark_color.name(),
            10
        )

        self.statusBar().showMessage("QR Updated", 3000)
