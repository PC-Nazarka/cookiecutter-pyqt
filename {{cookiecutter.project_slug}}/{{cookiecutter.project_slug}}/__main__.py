import sys

from PyQt6 import QtWidgets

from {{cookiecutter.project_slug}}.windows import MainWindow

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    application_window = MainWindow()
    application_window.show()
    application_window.setWindowTitle("{{cookiecutter.project_name}}")
    application.exec()
