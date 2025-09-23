from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QFileDialog
from qr import QQrViz
from controls import QQrControls
from pathlib import Path

class SegueMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.last_opened_save_dir = Path.home()

        dlg = QFileDialog(self)
        dlg.setFileMode(QFileDialog.FileMode.AnyFile)
        dlg.setViewMode(QFileDialog.ViewMode.Detail)
        dlg.setNameFilter("PNG Files (*.png)")
        self.file_dlg = dlg

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

        self.qr_controls.save_btn.clicked.connect(self.save_button_clicked)

        self.setCentralWidget(central)

        self.qr_viz.regen_preview(
            self.qr_controls.contents.text(),
            self.qr_controls.light_color.name(),
            self.qr_controls.dark_color.name(),
            self.qr_controls.logo_file
        )

    def update_button_clicked(self):
        self.qr_viz.regen_preview(
            self.qr_controls.contents.text(),
            self.qr_controls.light_color.name(),
            self.qr_controls.dark_color.name(),
            self.qr_controls.logo_file
        )

        self.statusBar().showMessage("QR Updated", 3000)

    def save_button_clicked(self):
        self.file_dlg.setDirectory(str(self.last_opened_save_dir))

        sel_file = None
        if self.file_dlg.exec():
            sel_file = Path(self.file_dlg.selectedFiles()[0])

        if not sel_file:
            return

        self.last_opened_save_dir = sel_file.parent

        if len(sel_file.suffix) == 0 or sel_file.suffix != ".png":
            sel_file = sel_file.with_suffix(".png")

        img_bytes = self.qr_viz.create_image(
            self.qr_controls.contents.text(),
            self.qr_controls.light_color.name(),
            self.qr_controls.dark_color.name(),
            self.qr_controls.logo_file,
            self.qr_controls.scale_amount.value(),
        )

        sel_file.write_bytes(img_bytes)

        self.statusBar().showMessage(f"Written QR to: {sel_file}", 3000)
