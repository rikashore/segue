from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QPushButton, QLineEdit, QColorDialog, QLabel
from color_box import QColorBox

class QQrControls(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.light_color = QColor.fromString("#ffffff")
        self.dark_color = QColor.fromString("#111111")

        layout = QVBoxLayout()

        layout.addStretch()

        content_label = QLabel("QR Contents")
        content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(content_label)
        self.contents = QLineEdit("Hey segue into this...")
        layout.addWidget(self.contents)

        layout.addSpacing(15)

        form_layout = QFormLayout()

        light_btn = QPushButton("Select Light Colour")
        light_btn.clicked.connect(self.light_button_clicked)
        self.l_color_box = QColorBox(self.light_color)

        form_layout.addRow(light_btn, self.l_color_box)

        dark_btn = QPushButton("Select Dark Colour")
        dark_btn.clicked.connect(self.dark_button_clicked)
        self.d_color_box = QColorBox(self.dark_color)

        form_layout.addRow(dark_btn, self.d_color_box)

        layout.addLayout(form_layout)

        layout.addStretch()

        self.update_btn = QPushButton("Update")
        layout.addWidget(self.update_btn)

        self.setLayout(layout)


    def light_button_clicked(self):
        dlg = QColorDialog()
        l_color = dlg.getColor(
            initial=self.light_color, 
            title="Choose Light Colour"
        )
        self.l_color_box.setColor(l_color)
        self.light_color = l_color

    def dark_button_clicked(self):
        dlg = QColorDialog()
        d_color = dlg.getColor(
            initial=self.dark_color, 
            title="Choose Dark Colour"
        )
        self.d_color_box.setColor(d_color)
        self.dark_color = d_color
        