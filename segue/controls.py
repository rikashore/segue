from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QColorDialog, QLabel

class QQrControls(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.light_colour = "#FFFFFF"
        self.dark_colour = "#111111"

        layout = QVBoxLayout()

        layout.addStretch()

        layout.addWidget(QLabel("QR Contents"))

        self.contents = QLineEdit("Hey segue into this...")
        layout.addWidget(self.contents)

        light_btn = QPushButton("Select Light Colour")
        light_btn.clicked.connect(self.light_button_clicked)

        layout.addWidget(light_btn)

        dark_btn = QPushButton("Select Dark Colour")
        self.darkbtn = dark_btn
        dark_btn.clicked.connect(self.dark_button_clicked)

        layout.addWidget(dark_btn)

        self.update_btn = QPushButton("Update")
        layout.addWidget(self.update_btn)

        layout.addStretch()

        self.setLayout(layout)


    def light_button_clicked(self):
        dlg = QColorDialog()
        l_color = dlg.getColor(
            initial=QColor.fromString(self.light_colour), 
            title="Choose Light Colour"
        )
        self.light_colour = l_color.name()

    def dark_button_clicked(self):
        dlg = QColorDialog()
        d_color = dlg.getColor(
            initial=QColor.fromString(self.dark_colour), 
            title="Choose Dark Colour"
        )
        self.dark_colour = d_color.name()
        