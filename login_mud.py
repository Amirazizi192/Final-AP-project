import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

class log_in_window(QWidget):
    def __init__(self):   
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 600, 400)
        self.log_UI()

    def log_UI(self):
        formLayout=QFormLayout()
        name_txt=QLabel("Username: ")
        name_input=QLineEdit()
        pass_txt=QLabel("Password :")
        pass_input=QLineEdit()
        pass_input.setEchoMode(QLineEdit.Password)
        hbox=QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Login"))
        formLayout.addRow(name_txt,name_input)
        formLayout.addRow(pass_txt,pass_input)
        formLayout.addRow(hbox)
        self.setLayout(formLayout)
        self.show()        


def main():
    App=QApplication(sys.argv)
    windows = log_in_window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()
