from PySide6.QtWidgets import QApplication
from app import SegueMainWindow

app = QApplication([])

window = SegueMainWindow()
window.show()

app.exec()