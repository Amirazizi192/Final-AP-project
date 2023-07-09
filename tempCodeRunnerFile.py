#main_menu code
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sqlite3
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon, QDesktopServices
from PIL import Image
import io
import tempfile
import requests


class Window(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Price Comparison")
        self.setGeometry(0, 0, 1900, 1000)
        self.username_title = username
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        usernamelayout = QHBoxLayout()
        searchLayout = QHBoxLayout()
        midLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()

        self.favorite = QPushButton('Favorite Products')
        self.favorite.setObjectName('favoriteButton')
        self.title = QLabel('Price Comparison')
        self.title.setObjectName('titleLabel')
        self.search_in_app_rbut = QRadioButton('Internal Search')
        self.search_in_net_rbut = QRadioButton('Online Search')
        self.search_box = QLineEdit()
        self.search_but = QPushButton('Search')
        self.username = QLabel(f'Welcome {self.username_title}')
        self.username.setObjectName('usernameLabel')
        self.username_icon = QLabel()
        user_icon = QPixmap('user.png')
        user_icon = user_icon.scaled(30, 30)
        self.username_icon.setPixmap(user_icon)
        self.username_icon.setObjectName('usernameLabel')
        self.username_icon.setFixedSize(30, 30)
        self.title.setAlignment(Qt.AlignCenter)  # Center align the title label

        # topLayout.addWidget(self.username)
        topLayout.addWidget(self.title)
        usernamelayout.addWidget(self.username_icon)
        usernamelayout.addWidget(self.username)
        searchLayout.addWidget(self.search_in_app_rbut)
        searchLayout.addWidget(self.search_in_net_rbut)
        searchLayout.addWidget(self.search_box)
        searchLayout.addWidget(self.search_but)
        midLayout.addSpacing(30)

        self.cat_but1 = QPushButton('Mobile')
        self.cat_but2 = QPushButton('Tablet')
        self.cat_but3 = QPushButton('Headphone')
        self.cat_but4 = QPushButton('Laptop')
        self.cat_but5 = QPushButton('TV')
        self.cat_but6 = QPushButton('Dynamic Product')
        self.cat_title = QLabel('Categories :')
        self.cat_title.setObjectName('catLabel')
        midLayout.addSpacing(30)
        midLayout.addWidget(self.cat_title)
        midLayout.addWidget(self.cat_but1)
        midLayout.addWidget(self.cat_but2)
        midLayout.addWidget(self.cat_but3)
        midLayout.addWidget(self.cat_but4)
        midLayout.addWidget(self.cat_but5)
        midLayout.addWidget(self.cat_but6)
        midLayout.addWidget(self.favorite)

        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()
        self.image1 = QLabel()
        pixmap = QPixmap('iphone 13 ch.png')
        pixmap = pixmap.scaled(200, 200)
        self.image1.setPixmap(pixmap)
        self.image1_caption = QPushButton('iphone 13 ch')
        self.image1.setAlignment(Qt.AlignCenter)


        self.image2 = QLabel()
        pixmap2 = QPixmap('airpad 3.png')
        pixmap2 = pixmap2.scaled(200, 200)
        self.image2.setPixmap(pixmap2)
        self.image2_caption = QPushButton('airpad 3')
        self.image2.setAlignment(Qt.AlignCenter)
        
        self.image3 = QLabel()
        pixmap3 = QPixmap('galaxy tab a8.png')
        pixmap3 = pixmap3.scaled(200, 200)
        self.image3.setPixmap(pixmap3)
        self.image3_caption = QPushButton('galaxy tab a8')
        self.image3.setAlignment(Qt.AlignCenter)
        
        
        v1.addWidget(self.image1)
        v1.addWidget(self.image1_caption)
        v2.addWidget(self.image2)
        v2.addWidget(self.image2_caption)
        v3.addWidget(self.image3)
        v3.addWidget(self.image3_caption)

        bottomLayout.addLayout(v1)
        bottomLayout.addLayout(v2)
        bottomLayout.addLayout(v3)

        mainLayout.addLayout(topLayout)
        mainLayout.addStretch()
        mainLayout.addLayout(usernamelayout)
        mainLayout.addStretch()
        mainLayout.addLayout(searchLayout)
        mainLayout.addStretch()
        mainLayout.addLayout(midLayout)
        mainLayout.addStretch()
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)

        # self.cat_but1.clicked.connect(lambda: self.open_category_page('Mobile'))
        # self.cat_but2.clicked.connect(lambda: self.open_category_page('Tablet'))
        # self.cat_but3.clicked.connect(lambda: self.open_category_page('Headphone'))
        # self.cat_but4.clicked.connect(lambda: self.open_category_page('Laptop'))
        # self.cat_but5.clicked.connect(lambda: self.open_category_page('TV'))
        # self.cat_but6.clicked.connect(lambda: self.open_dynamic_window())
        # self.image1_caption.clicked.connect(self.open_product_page)
        # self.image2_caption.clicked.connect(self.open_product_page)
        # self.image3_caption.clicked.connect(self.open_product_page)
        # self.favorite.clicked.connect(self.open_favorite_page)
        # self.search_but.clicked.connect(self.show_search_result)

        self.setStyleSheet('''
            QWidget {
                background-color: #F5F5F5;
            }
            QPushButton {
                background-color: #007BFF;
                color: #FFFFFF;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QRadioButton {
                font-size: 14px;
            }
            QLabel {
                font-size: 20px;
            }
            #titleLabel {
                color: red;
                font-size: 48px;
                font-weight: bold;
            }
            #usernameLabel {
                font-size: 24px;
            }
            #favoriteButton {
                background-color: #17A2B8;
            }
           #catLabel {
           color: green;
           font-size: 30px                        
                           }               
        ''')

        self.show()
def main():
    App = QApplication(sys.argv)
    window = Window('sample')
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()