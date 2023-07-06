# sign.py code
import sys
import hashlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sqlite3
import main_menu
import data
status = False

class log_in_window(QWidget):
    loginCompleted = pyqtSignal(str)

    def __init__(self, database_conn):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 600, 400)
        self.database_conn = database_conn
        self.log_UI()

    def log_UI(self):
        formLayout = QFormLayout()
        name_txt = QLabel("Username: ")
        self.name_input = QLineEdit()
        pass_txt = QLabel("Password :")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        hbox = QHBoxLayout()
        hbox.addStretch()
        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)
        hbox.addWidget(login_btn)
        formLayout.addRow(name_txt, self.name_input)
        formLayout.addRow(pass_txt, self.pass_input)
        formLayout.addRow(hbox)
        self.setLayout(formLayout)

    def login(self):
        username = self.name_input.text()
        password = self.pass_input.text()

        # Hash the password using hashlib
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the username and hashed password match a record in the database
        cursor = self.database_conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        result = cursor.fetchone()
        cursor.close()

        if result:
            QMessageBox.information(self,"Information","Login successful!")
            # Emit the signal with the username
            self.hide()
            self.loginCompleted.emit(username)
            
        else:
            QMessageBox.information(self,"Information","Login failed!")


class sign_in_window(QWidget):
    signInCompleted = pyqtSignal(str)

    def __init__(self, database_conn):
        super().__init__()
        self.setWindowTitle("Sign in")
        self.setGeometry(100, 100, 600, 400)
        self.database_conn = database_conn
        self.sign_in_status = False
        self.sign_UI()
        self.login_page = log_in_window(database_conn)
        self.login_page.hide()

    def sign_UI(self):
        formLayout = QFormLayout()
        name_txt = QLabel("Username: ")
        self.name_input = QLineEdit()
        pass_txt = QLabel("Password :")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        hbox = QHBoxLayout()
        hbox.addStretch()
        sign_in_btn = QPushButton("Sign in")
        sign_in_btn.clicked.connect(self.sign_in)
        hbox.addWidget(sign_in_btn)
        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(QLabel('Already have an account?'))
        login_but = QPushButton('Go to login page')
        hbox2.addWidget(login_but)
        login_but.clicked.connect(self.display_login_form)
        hbox2.addStretch()
        formLayout.addRow(name_txt, self.name_input)
        formLayout.addRow(pass_txt, self.pass_input)
        formLayout.addRow(hbox)
        formLayout.addRow(hbox2)
        self.setLayout(formLayout)

    def sign_in(self):
        username = self.name_input.text()
        password = self.pass_input.text()

        # Hash the password using hashlib
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the username already exists in the database
        cursor = self.database_conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result:
            QMessageBox.information(self,"Information","Username already exists!")
        else:
            # Insert the username and hashed password into the database
            cursor.execute("INSERT INTO users (username, password, favorite_product_id) VALUES (?, ?, ?)",(username, hashed_password,""))
            self.database_conn.commit()
            cursor.close()
            QMessageBox.information(self,"Information","You signed in!")
            self.hide()
            # Emit the signal with the username
            self.signInCompleted.emit(username)
 

    def display_login_form(self):
        self.hide()
        self.login_page.show()





def sign_main():
    # Connect to the SQLite database
    database_conn = sqlite3.connect("database.db")
    cursor = database_conn.cursor()

    # Create the users table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, favorite_product_id INTEGER)")
    database_conn.commit()  # Commit the changes to create the table

    App = QApplication(sys.argv)
    windows = sign_in_window(database_conn)

    def handle_sign_in_completed(username):
        global appeared_username, status
        appeared_username = username
        status = True
        getdata = data.get_data()
        # getdata.get__data()
        main_menu_window = main_menu.Window(username)  # Create an instance of the main menu window
        main_menu_window.show()  # Show the main menu window

    def handle_login_completed(username):
        global appeared_username, status
        appeared_username = username
        status = True
        getdata = data.get_data()
        # getdata.get__data()
        main_menu_window = main_menu.Window(username)  # Create an instance of the main menu window
        main_menu_window.show()  # Show the main menu window
    windows.signInCompleted.connect(handle_sign_in_completed)
    windows.login_page.loginCompleted.connect(handle_login_completed)

    windows.show()
    sys.exit(App.exec_())


if __name__ == '__main__':
    sign_main()
