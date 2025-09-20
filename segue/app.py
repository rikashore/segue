from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QLabel
from qr import QQrViz
from controls import QQrControls

class SegueMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Segue")

        self.setMinimumSize(960, 540)
        self.setMaximumSize(1600, 900)

        self.statusBar().setSizeGripEnabled(False)
        self.statusBar().showMessage("Segue Ready", 3000)

        layout = QHBoxLayout()

        self.qr_viz = QQrViz()

        layout.addWidget(self.qr_viz, stretch=1)

        self.qr_controls = QQrControls()
        self.qr_controls.update_btn.clicked.connect(self.update_button_clicked)

        layout.addWidget(self.qr_controls, stretch=1)

        central = QWidget()
        central.setLayout(layout)

        self.setCentralWidget(central)

    def update_button_clicked(self):
        print(self.qr_controls.light_colour)
        print(self.qr_controls.dark_colour)
        print(self.qr_controls.darkbtn.size())
