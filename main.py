from PyQt5.QtWidgets  import QApplication, QMainWindow
from PyQt5 import QtWidgets
import sys

def push_button():
    print("Hello Askhat")

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle(" PYthon  PyQt5")
    window.setGeometry(1080,700,1080,700)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Hello World")
    main_text.move(480,340)

    main_button = QtWidgets.QPushButton(window)
    main_button.setText("Click")
    main_button.move(475,380)
    main_button.clicked.connect(push_button)
    window.show()
    sys.exit(app.exec_())
application()


