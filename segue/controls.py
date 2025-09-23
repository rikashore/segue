from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QColorDialog, QLabel, QSpinBox
from color_box import QColorBox

class QQrControls(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.light_color = QColor.fromString("#ffffff")
        self.dark_color = QColor.fromString("#111111")

        layout = QVBoxLayout()

        layout.addStretch()

        content_label = QLabel("QR Contents")
        content_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(content_label)
        self.contents = QLineEdit("Hey segue into this...")
        layout.addWidget(self.contents)

        layout.addSpacing(20)

        self.logo_file_label = QLabel("File Selected:")
        self.logo_file_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.logo_file_label)

        logo_choose_button = QPushButton("Select Logo File")
        layout.addWidget(logo_choose_button)

        layout.addSpacing(20)

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

        layout.addSpacing(20)

        scale_layout = QHBoxLayout()

        scale_layout.addWidget(QLabel("Scale (1-50)"))
        
        self.scale_amount = QSpinBox()
        self.scale_amount.setMinimum(1)
        self.scale_amount.setMaximum(50)
        self.scale_amount.setValue(5)

        scale_layout.addWidget(self.scale_amount)

        layout.addLayout(scale_layout)

        scale_info_label = QLabel("The image scale factor is used to scale up the final image by the chosen factor. Useful for generating larger QR codes. A sane default is 5, though your requirements might vary.")
        scale_info_label.setWordWrap(True)
        layout.addWidget(scale_info_label)

        layout.addSpacing(20)

        meta_btns_layout = QHBoxLayout()

        self.update_btn = QPushButton("Update")
        meta_btns_layout.addWidget(self.update_btn)

        meta_btns_layout.addSpacing(100)

        self.save_btn = QPushButton("Save")
        meta_btns_layout.addWidget(self.save_btn)

        layout.addLayout(meta_btns_layout)

        layout.addStretch()

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        