from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QColorDialog, QLabel
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

        grid_layout = QGridLayout()

        light_btn = QPushButton("Select Light Colour")
        light_btn.clicked.connect(self.light_button_clicked)
        self.l_color_box = QColorBox(self.light_color)

        grid_layout.addWidget(light_btn, 0, 0)
        grid_layout.addWidget(self.l_color_box, 0, 1)

        dark_btn = QPushButton("Select Dark Colour")
        dark_btn.clicked.connect(self.dark_button_clicked)
        self.d_color_box = QColorBox(self.dark_color)

        grid_layout.addWidget(dark_btn, 1, 0)
        grid_layout.addWidget(self.d_color_box, 1, 1)

        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)

        layout.addLayout(grid_layout)

        layout.addStretch()

        h_layout = QHBoxLayout()

        self.update_btn = QPushButton("Update")
        h_layout.addWidget(self.update_btn)

        h_layout.addSpacing(50)

        self.save_btn = QPushButton("Save")
        h_layout.addWidget(self.save_btn)

        layout.addLayout(h_layout)

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
        