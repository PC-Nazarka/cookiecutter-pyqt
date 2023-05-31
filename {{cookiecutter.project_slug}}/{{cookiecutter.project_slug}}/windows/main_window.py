from PyQt6 import QtCore, QtWidgets

from {{cookiecutter.project_slug}}.forms import Ui_MainWindow
from {{cookiecutter.project_slug}}.palettes import main_window_styles


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(main_window_styles)

    @QtCore.pyqtSlot()
    def on_load_button_clicked(self) -> None:
        QtWidgets.QMessageBox.information(
            self,
            "Информация!",
            "Информация",
        )
