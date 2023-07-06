#main_menu code
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sign
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

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

class Window(QWidget):
    def __init__(self,username):
        super().__init__()
        self.setWindowTitle("Price comparison")
        self.setGeometry(0, 0, 1700, 800)
        self.username_title = username
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        topchild1 = QHBoxLayout()
        topchild2 = QHBoxLayout()
        searchlayout = QHBoxLayout()
        midLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        topLayout.addLayout(topchild1)
        topLayout.addLayout(topchild2)
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(searchlayout)
        mainLayout.addLayout(midLayout)
        mainLayout.addLayout(bottomLayout)
        font_title = QFont()
        font_title.setPointSize(24)  
        font_cat = QFont()
        font_cat.setPixelSize(20)

        self.favorite = QPushButton('Favorite products')
        self.title = QLabel('Price comparison', self)
        self.title.setFont(font_title)
        self.title.setAlignment(Qt.AlignCenter)
        self.search_in_app_rbut =QRadioButton('internal search')
        self.search_in_net_rbut =QRadioButton('online search')
        self.search_box = QLineEdit(self)
        self.search_but = QPushButton('search', self)
        self.username = QLabel(f'Welcome {self.username_title}', self)
        self.username.setStyleSheet("font-size: 24px;")
        topchild1.addWidget(self.username)
        # topchild1.addStretch()
        topchild2.addStretch()
        topchild2.addWidget(self.title)
        topchild2.addStretch()
        topchild2.setAlignment(Qt.AlignCenter)
        topchild2.addStretch()
        self.title.setStyleSheet('color: red;')
        searchlayout.addStretch()
        searchlayout.addWidget(self.search_in_app_rbut)
        searchlayout.addWidget(self.search_in_net_rbut)
        searchlayout.addWidget(self.search_box)
        searchlayout.addWidget(self.search_but)
        searchlayout.addStretch()
        self.cat_but1 = QPushButton('Mobile', self)
        self.cat_but2 = QPushButton('Tablet', self)
        self.cat_but3 = QPushButton('Headphone', self)
        self.cat_but4 = QPushButton('Laptop', self)
        self.cat_but5 = QPushButton('Tv', self)
        self.cat_but6 = QPushButton('Dynamic product', self)
        self.cat_title = QLabel('Categories: ', self)
        self.cat_title.setFont(font_cat)
        midLayout.addStretch()
        midLayout.addWidget(self.cat_title)
        midLayout.addWidget(self.cat_but1)
        midLayout.addWidget(self.cat_but2)
        midLayout.addWidget(self.cat_but3)
        midLayout.addWidget(self.cat_but4)
        midLayout.addWidget(self.cat_but5)
        midLayout.addWidget(self.cat_but6)
        midLayout.addWidget(self.favorite)
        midLayout.addStretch()
        midLayout.setContentsMargins(0, 0, 0, 400)

        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()
        self.image1 = QLabel(self)
        pixmap = QPixmap('iphone 13 ch.png')
        pixmap = pixmap.scaled(200, 200)  # Adjust the dimensions as needed
        self.image1.setPixmap(pixmap)
        self.image1.show()
        self.image1_caption = QPushButton('iphone 13 ch', self)
        self.image1.setAlignment(Qt.AlignCenter)
        self.image2 = QLabel(self)
        pixmap2 = QPixmap('airpad 3.png')
        pixmap2 = pixmap2.scaled(200, 200)  # Adjust the dimensions as needed
        self.image2.setPixmap(pixmap2)
        self.image2.show()
        self.image2_caption = QPushButton('airpad 3', self)
        self.image2.setAlignment(Qt.AlignCenter)
        self.image3 = QLabel(self)
        pixmap3 = QPixmap('galaxy tab a8.png')
        pixmap3 = pixmap3.scaled(200, 200)  # Adjust the dimensions as needed
        self.image3.setPixmap(pixmap3)
        self.image3.show()
        self.image3_caption = QPushButton('galaxy tab a8', self)
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
        self.setLayout(mainLayout)
        self.cat_but1.clicked.connect(
            lambda: self.open_category_page('Mobile'))
        self.cat_but2.clicked.connect(
            lambda: self.open_category_page('Tablet'))
        self.cat_but3.clicked.connect(
            lambda: self.open_category_page('Headphone'))
        self.cat_but4.clicked.connect(
            lambda: self.open_category_page('Laptop'))
        self.cat_but5.clicked.connect(lambda: self.open_category_page('TV'))
        self.cat_but6.clicked.connect(lambda: self.open_dynamic_window())
        self.image1_caption.clicked.connect(self.open_product_page)
        self.image2_caption.clicked.connect(self.open_product_page)
        self.image3_caption.clicked.connect(self.open_product_page)
        self.favorite.clicked.connect(self.open_favorite_page)
        self.search_but.clicked.connect(self.show_search_result)
        self.show()

    def show_search_result(self):
        if self.search_in_app_rbut.isChecked():
            search_text = self.search_box.text()
            cursor.execute('''SELECT name FROM products''')
            products = cursor.fetchall()
            normal_list = [item[0] for item in products]
            matching_products = [product for product in normal_list if search_text.lower() in product.lower()]
            self.open_search_page = search_page(matching_products,'None',self.username_title)
            self.open_search_page.search_UI()
        else:
            driver=webdriver.Chrome()
            search_value = self.search_box.text()
            detail_list = []
            def technolife() :
                global my_current_url
                driver.get(my_current_url)
                time.sleep(2)
                elements_search=driver.find_elements(By.CLASS_NAME,"ProductComp_product_title__bOrf5")
                time.sleep(2)
                name1=elements_search[0].text
                time.sleep(2)
                elements_search[0].send_keys(Keys.ENTER)
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)
                try:
                    Property=driver.find_element(By.ID,"ProductSpecPart")
                    time.sleep(2)
                    Property1=(Property.text)[:-24]
                    detail_list.append(Property1)
                except:
                    Property1 = 'None'
                    detail_list.append(Property1)  
                try:
                    url=driver.current_url
                    detail_list.append(url)
                except:
                    url = 'None'
                    detail_list.append(url)
                try:    
                    detail_list.append(name1)
                except:
                    detail_list.append('None')
                try:
                    time.sleep(2)
                    price=driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div[3]/section[1]/div[3]/div[2]/div/h6/span[1]")
                    price1 = price.text
                    price1=str(price1).replace(',',"")
                    detail_list.append(persian_to_english(price1))
                    time.sleep(2)
                except:
                    detail_list.append('None')
                try:
                    img_element = driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div[3]/section[1]/div[2]/div[2]/div/img")
                    image_url = img_element.get_attribute('src')
                    image_path = self.download_image(image_url)
                    if image_path:
                        detail_list.append(image_path)
                    else:
                        print("Failed to download the image.")
                        detail_list.append('image.png')    
                except ValueError as va:
                    detail_list.append('image.png')
                    print(va)
            def digikala() :
                global price
                driver.get("https://www.digikala.com")
                time.sleep(5)
                s=driver.find_element(By.CSS_SELECTOR,".SearchInput_SearchInput__HB9qi")
                time.sleep(1)
                s.click()
                search_box=driver.find_element(By.CSS_SELECTOR,"input.color-500")
                time.sleep(2)
                search_box.send_keys(search_value)
                time.sleep(2)
                search_box.send_keys(Keys.ENTER)
                time.sleep(2)
                value=driver.find_elements(By.CSS_SELECTOR,"div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)")
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                url=driver.current_url
                try:
                    detail_list.append(url)
                except:
                    detail_list.append('None')   
                try:
                    if "٪" in value[0].text :
                        try:
                            price=str(value[1].text).replace(',',"")
                            detail_list.append(persian_to_english(price))
                        except:
                            detail_list.append('None')
                    else :
                        try:
                            price=str(value[0].text).replace(',',"")
                            detail_list.append(persian_to_english(price))
                        except:
                            detail_list.append('None')
                except:
                    detail_list.append('None')  
                divar(detail_list[6])              
            
            
            
            def divar(digi_price) :
                global price
                driver.get("https://divar.ir/s/tehran")
                time.sleep(3)
                box_search=driver.find_element(By.CLASS_NAME,"kt-nav-text-field__input")
                time.sleep(3)
                box_search.send_keys(search_value)
                box_search.send_keys(Keys.ENTER)
                time.sleep(2)
                current_url=driver.current_url
                url2=re.split("tehran?",str(current_url))
                try:
                    if digi_price != 'None':
                        min=int((6/10)*int(digi_price))
                        max=int((11/10)*int(digi_price))
                    elif detail_list[3] != 'None' :
                        min=int((6/10)*int(detail_list[3]))                    
                        max=int((11/10)*int(detail_list[3]))
                    else:
                        min = 0
                        max = 100000000
                    komaki="price="+str(min)+"-"+str(max)+"&"
                    new_url=url2[0]+"tehran?"+komaki+url2[1][1:]
                    driver.get(new_url)
                    time.sleep(5)
                    values=driver.find_elements(By.CLASS_NAME,"kt-post-card__description")
                    time.sleep(3)
                    pricce=values[1].text
                    values[0].click()
                    time.sleep(2)
                    urrl=driver.current_url
                    try:
                        detail_list.append(urrl)
                    except:
                        detail_list.append('None')
                    try:
                        detail_list.append(persian_to_english(pricce)[:-5].replace(',',""))
                    except:
                        detail_list.append('None')
                except:
                    detail_list.append('None')
                    detail_list.append('None')

            
            def search() :
                global my_current_url
                driver.get("https://www.technolife.ir/")
                time.sleep(5)
                box_search=driver.find_element(By.CSS_SELECTOR,"#search_box")
                time.sleep(1)
                box_search.send_keys(search_value)
                time.sleep(2)
                box_search.send_keys(Keys.ENTER)
                time.sleep(4)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)
                my_current_url=driver.current_url
                # print(my_current_url)
                technolife()
            def persian_to_english(text):
                persian_digits = "۰۱۲۳۴۵۶۷۸۹"
                english_digits = "0123456789"
                translation_table = str.maketrans(persian_digits, english_digits)
                return text.translate(translation_table)
            try:                            
                t1 = threading.Thread(target=search())
                t2 = threading.Thread(target=digikala())
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                driver.close()
                description , techno_url , name , techno_price ,image, digi_url , digi_price, divar_url , divar_price = detail_list
                self.search_page = search_result(name,techno_price,digi_price,description,digi_url,techno_url,divar_url,divar_price,image)
                self.search_page.search_UI()
            except ValueError as va:
                print(va)
                QMessageBox.information(self,"Information","Search was not succesful")

    def download_image(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                f.write(response.content)
                return f.name
        return None
    def open_dynamic_window(self):
        self.dynpage = dynamic_Window(self.username_title)
        self.dynpage.dyn_UI()
    
    def open_category_page(self, category_name):
        self.category_page = category_Window(category_name,self.username_title)
        self.category_page.cat_UI()
    
    def open_favorite_page(self):
        self.favorite_page = display_favorite_products(self.username_title)
        self.favorite_page.fave_UI()
    
    def open_product_page(self):
        button = self.sender()  # Get the button that emitted the signal
        text = button.text()  # Retrieve the text of the button
        cursor.execute('''SELECT category FROM products WHERE name=?''', (text,))
        cat = cursor.fetchall()
        self.product_page = display_product(text,self.username_title,cat[0][0])
        self.product_page.product_UI()

class category_Window(QWidget):
    def __init__(self, category_name,username_title):
        super().__init__()
        self.setWindowTitle(category_name)
        self.setGeometry(0, 0, 1700, 800)
        self.category_name = category_name
        self.username_title = username_title
        self.cat_UI()

    def cat_UI(self):

        font_title = QFont()
        font_title.setPointSize(28)
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        midlayout = QHBoxLayout()
        bottomlayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(midlayout)
        mainLayout.addLayout(bottomlayout)
        cat_title = QLabel(self.category_name, self)
        cat_title.setAlignment(Qt.AlignCenter)
        cat_title.setFont(font_title)
        topLayout.addWidget(cat_title)
        cursor.execute('''SELECT name FROM products WHERE category=?''', (self.category_name,))
        products = cursor.fetchall()
        for product in products:
            name = product[0]
            cursor.execute('''SELECT picture FROM products WHERE name=?''', (name,))
            product_detail = cursor.fetchall()
            picture_data = product_detail[0][0]
            self.product_layout = QVBoxLayout()
            product_image = QLabel(self)
            product_label = QPushButton(name)
            pixmap = QPixmap()
            pixmap.loadFromData(picture_data)
            desired_width = 200  # Set the desired width for resizing
            desired_height = 200  # Set the desired height for resizing
            scaled_pixmap = pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)
            product_image = QLabel(self)
            product_image.setPixmap(scaled_pixmap)
            product_image.setAlignment(Qt.AlignCenter)
            self.product_layout.addWidget(product_image)
            self.product_layout.addWidget(product_label)
            midlayout.addLayout(self.product_layout)
            product_label.clicked.connect(self.open_product_page)
        self.setLayout(mainLayout)
        self.show()

    def open_product_page(self):
        button = self.sender()  # Get the button that emitted the signal
        text = button.text()  # Retrieve the text of the button
        self.product_page = display_product(text,self.username_title,self.category_name)
        self.product_page.product_UI()

class display_product(QWidget):
    def __init__(self,product_name,username_title,category_name):
        super().__init__()
        self.setWindowTitle(product_name)
        self.setGeometry(200, 200, 400, 600)
        self.product_name = product_name
        self.username_title = username_title
        self.category_name = category_name
        self.product_UI()
    
    
    def product_UI(self):
        mainlayout = QVBoxLayout()
        toplayout = QHBoxLayout()
        price1layout = QHBoxLayout()
        price2layout = QHBoxLayout()
        price3layout = QHBoxLayout()
        descriptionlayout = QHBoxLayout()
        add_to_favor_layout = QHBoxLayout()
        compare_box = QHBoxLayout()
        suggest_box = QHBoxLayout()
        mainlayout.addLayout(toplayout)
        # mainlayout.addLayout(mainlayout)
        mainlayout.addLayout(price1layout)
        mainlayout.addLayout(price2layout)
        mainlayout.addLayout(price3layout)
        mainlayout.addLayout(descriptionlayout)
        mainlayout.addLayout(add_to_favor_layout)
        mainlayout.addLayout(compare_box)
        mainlayout.addLayout(suggest_box)
        cursor.execute('''SELECT price1, price2, price3, description, picture,url1,url2,url3 FROM products WHERE name=?''', (self.product_name,))
        product_detail = cursor.fetchall()
        price1 = product_detail[0][0]
        price2 = product_detail[0][1]
        price3 = product_detail[0][2]
        description = product_detail[0][3]
        picture_data =  product_detail[0][4]
        url1 = product_detail[0][5]
        url2 = product_detail[0][6]
        url3 = product_detail[0][7]
        pixmap = QPixmap()
        pixmap.loadFromData(picture_data)
        desired_width = 200  # Set the desired width for resizing
        desired_height = 200  # Set the desired height for resizing
        scaled_pixmap = pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)
        product_image = QLabel(self)
        product_image.setPixmap(scaled_pixmap)
        product_image.setAlignment(Qt.AlignCenter)
        toplayout.addWidget(product_image)
        price1_lable = QLabel('Technolife price :')
        price1_value = QPushButton(str(price1))
        price2_lable = QLabel('Digikala price :')
        price2_value = QPushButton(str(price2))
        price3_lable = QLabel('Divar price :')
        price3_value = QPushButton(str(price3))
        price1_value.clicked.connect(lambda: self.open_web_page(url1))
        price2_value.clicked.connect(lambda: self.open_web_page(url2))
        price3_value.clicked.connect(lambda: self.open_web_page(url3))
        price1layout.addWidget(price1_lable)
        price1layout.addWidget(price1_value)
        price2layout.addWidget(price2_lable)
        price2layout.addWidget(price2_value)
        price3layout.addWidget(price3_lable)
        price3layout.addWidget(price3_value)
        self.setLayout(mainlayout)
        des_label = QLabel('Description:')
        descriptionlayout.addWidget(des_label)
        description_text = QTextEdit()
        description_text.setReadOnly(True)
        description_text.setText(description)
        descriptionlayout.addWidget(description_text)
        add_to_favor_but = QPushButton('Add to favorite')
        add_to_favor_but.clicked.connect(self.add_to_favorite)
        add_to_favor_layout.addWidget(add_to_favor_but)
        if self.category_name == 'None':
            pass
        else:
            combo_box = QComboBox()
            compare_but = QPushButton('Compare')
            cursor.execute('''SELECT name FROM products WHERE category=?''', (self.category_name,))
            products = cursor.fetchall()
            for product in products:
                name = product[0]
                if name != self.product_name:
                    combo_box.addItem(name)        
            compare_box.addWidget(combo_box)
            compare_box.addWidget(compare_but)
            compare_but.clicked.connect(lambda: self.compare_products(combo_box.currentText(), self.product_name))
            sug_label = QLabel('Suggestion:')
            sug_label.setStyleSheet('color: green;')
            suggest_box.addWidget(sug_label)
            cursor.execute('''SELECT name,price1 FROM products WHERE category=?''', (self.category_name,))
            sug_product = cursor.fetchall()
            for product in sug_product:
                sug_name = product[0]
                sug_price1 = product[1]
                if int(price1) < 1.5*int(sug_price1) and int(price1) > 0.5*int(sug_price1) and sug_name != self.product_name:
                    product_label = QPushButton(sug_name)
                    suggest_box.addWidget(product_label)
                    product_label.clicked.connect(self.open_product_page)
                    

        self.show()

    def open_web_page(self,url):
        url1 = QUrl(str(url))
        if not url1.isValid():
            return
        # Open the URL in the default web browser
        QDesktopServices.openUrl(url1)    
    def compare_products(self, product1, product2):
        # Code to open the compare page with the two product names
        self.compare_page = display_compare(product1, product2)
        self.compare_page.compare_UI()

    
    def add_to_favorite(self):
       
        cursor.execute('''SELECT favorite_product_id FROM users WHERE username=?''', (self.username_title,))
        existing_product = cursor.fetchone()
        if self.product_name not in existing_product[0]:
            fave = existing_product[0] +','+self.product_name
            print(fave)
            cursor.execute("UPDATE users SET favorite_product_id = ? WHERE username = ?", (fave,self.username_title))
            conn.commit()
            QMessageBox.information(self,"info","Product added")
        else:
            QMessageBox.information(self,"Error","Product already exists!")
    
    def open_product_page(self):
        button = self.sender()  # Get the button that emitted the signal
        text = button.text()  # Retrieve the text of the button
        self.product_page = display_product(text,self.username_title,self.category_name)
        self.product_page.product_UI()
class display_favorite_products(QWidget):
    def __init__(self,username):
        super().__init__()
        self.setWindowTitle('Favorite products')
        self.setGeometry(0, 0, 1700, 800)
        self.username = username
        self.fave_UI()

    def fave_UI(self):
        font_title = QFont()
        font_title.setPointSize(28)
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        midlayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(midlayout)
        cat_title = QLabel('Favorite products', self)
        cat_title.setAlignment(Qt.AlignCenter)
        cat_title.setFont(font_title)
        combo_box = QComboBox()
        remove_but = QPushButton('Remove')
        topLayout.addWidget(cat_title)
        topLayout.addWidget(combo_box)
        topLayout.addWidget(remove_but)
        cursor.execute('''SELECT favorite_product_id FROM users WHERE username=?''', (self.username,))
        products = cursor.fetchall()
        items = [item for item in products[0][0].split(',') if item]
        for product in items:
            combo_box.addItem(product)
        remove_but.clicked.connect(lambda: self.remove_product(combo_box.currentText()))    
        for product in items:
            cursor.execute('''SELECT picture FROM products WHERE name=?''', (product,))
            product_detail = cursor.fetchall()
            picture_data = product_detail[0][0]
            self.product_layout = QVBoxLayout()
            pixmap = QPixmap()
            pixmap.loadFromData(picture_data)
            desired_width = 200  
            desired_height = 200  
            scaled_pixmap = pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)
            product_image = QLabel(self)
            product_image.setPixmap(scaled_pixmap)
            product_image.setAlignment(Qt.AlignCenter)
            product_label = QPushButton(product)
            self.product_layout.addWidget(product_image)
            self.product_layout.addWidget(product_label)
            midlayout.addLayout(self.product_layout)
            product_label.clicked.connect(lambda : self.open_product_page('None'))            
        self.setLayout(mainLayout)
        self.show()
    def remove_product(self,removed_pro):
        cursor.execute('''SELECT favorite_product_id FROM users WHERE username=?''', (self.username,))
        existing_product = cursor.fetchone()
        a =existing_product[0]
        b =','+removed_pro
        c = str(a).replace(b,"")
        cursor.execute("UPDATE users SET favorite_product_id = ? WHERE username = ?", (c,self.username))
        conn.commit()
        QMessageBox.information(self,"info","Product removed. For see the new list enter again")
        
    def open_product_page(self,category):
        button = self.sender()  # Get the button that emitted the signal
        text = button.text()  # Retrieve the text of the button
        self.product_page = display_product(text,self.username,category)
        self.product_page.product_UI()       

class display_compare(QWidget):
    def __init__(self,product1, product2):
        super().__init__()
        self.setWindowTitle('compare products')
        self.setGeometry(100,100, 1100, 600)
        self.product1 = product1
        self.product2 = product2
        self.compare_UI()

    def compare_UI(self):
        mainLayout = QHBoxLayout()
        pro1_mainlayout = QVBoxLayout()
        pro2_mainlayout = QVBoxLayout()
        mainLayout.addLayout(pro1_mainlayout)
        mainLayout.addLayout(pro2_mainlayout)
        image_left_layout = QHBoxLayout()
        name_left_layout = QHBoxLayout()
        price1_left_layout = QHBoxLayout()
        price2_left_layout = QHBoxLayout()
        price3_left_layout = QHBoxLayout()
        description_left_layout = QHBoxLayout()
        pro1_mainlayout.addLayout(image_left_layout)
        pro1_mainlayout.addLayout(name_left_layout)
        pro1_mainlayout.addLayout(price1_left_layout)
        pro1_mainlayout.addLayout(price2_left_layout)
        pro1_mainlayout.addLayout(price3_left_layout)
        pro1_mainlayout.addLayout(description_left_layout)
        cursor.execute('''SELECT price1, price2, price3, description, picture,url1,url2,url3 FROM products WHERE name=?''', (self.product1,))
        product_detail = cursor.fetchall()
        price1_left = product_detail[0][0]
        price2_left = product_detail[0][1]
        price3_left = product_detail[0][2]
        description_left = product_detail[0][3]
        picture_data_left =  product_detail[0][4]
        url1_left = product_detail[0][5]
        url2_left = product_detail[0][6]
        url3_left = product_detail[0][7]
        pixmap_left = QPixmap()
        pixmap_left.loadFromData(picture_data_left)
        desired_width = 200  # Set the desired width for resizing
        desired_height = 200  # Set the desired height for resizing
        scaled_pixmap = pixmap_left.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)
        product_image_left = QLabel(self)
        product_image_left.setPixmap(scaled_pixmap)
        product_image_left.setAlignment(Qt.AlignCenter)
        image_left_layout.addWidget(product_image_left)
        prodect_left_name = QLabel(self.product1)
        prodect_left_name.setAlignment(Qt.AlignCenter)
        price1_lable = QLabel('Technolife price :')
        price1_value = QPushButton(str(price1_left))
        price2_lable = QLabel('Digikala price :')
        price2_value = QPushButton(str(price2_left))
        price3_lable = QLabel('Divar price :')
        price3_value = QPushButton(str(price3_left))
        price1_value.clicked.connect(lambda: self.open_web_page(url1_left))
        price2_value.clicked.connect(lambda: self.open_web_page(url2_left))
        price3_value.clicked.connect(lambda: self.open_web_page(url3_left))
        name_left_layout.addWidget(prodect_left_name)
        price1_left_layout.addWidget(price1_lable)
        price1_left_layout.addWidget(price1_value)
        price2_left_layout.addWidget(price2_lable)
        price2_left_layout.addWidget(price2_value)
        price3_left_layout.addWidget(price3_lable)
        price3_left_layout.addWidget(price3_value)
        # self.setLayout(mainlayout)
        des_label = QLabel('Description:')
        description_left_layout.addWidget(des_label)
        description_text = QTextEdit()
        description_text.setReadOnly(True)
        description_text.setText(description_left)
        description_left_layout.addWidget(description_text)
        # name_left_layout = QHBoxLayout
        image_right_layout = QHBoxLayout()
        name_right_layout = QHBoxLayout()
        price1_right_layout = QHBoxLayout()
        price2_right_layout = QHBoxLayout()
        price3_right_layout = QHBoxLayout()
        description_right_layout = QHBoxLayout()
        # pro1_mainlayout.addLayout(name_left_layout)
        pro2_mainlayout.addLayout(image_right_layout)
        pro2_mainlayout.addLayout(name_right_layout)
        pro2_mainlayout.addLayout(price1_right_layout)
        pro2_mainlayout.addLayout(price2_right_layout)
        pro2_mainlayout.addLayout(price3_right_layout)
        pro2_mainlayout.addLayout(description_right_layout)
        cursor.execute('''SELECT price1, price2, price3, description, picture,url1,url2,url3 FROM products WHERE name=?''', (self.product2,))
        product_detail = cursor.fetchall()
        price1_right = product_detail[0][0]
        price2_right = product_detail[0][1]
        price3_right = product_detail[0][2]
        description_right = product_detail[0][3]
        picture_data_right =  product_detail[0][4]
        url1_right = product_detail[0][5]
        url2_right = product_detail[0][6]
        url3_right = product_detail[0][7]
        pixmap_right = QPixmap()
        pixmap_right.loadFromData(picture_data_right)
        desired_width = 200  # Set the desired width for resizing
        desired_height = 200  # Set the desired height for resizing
        scaled_pixmap = pixmap_right.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)
        product_image_right = QLabel(self)
        product_image_right.setPixmap(scaled_pixmap)
        product_image_right.setAlignment(Qt.AlignCenter)
        image_right_layout.addWidget(product_image_right)        
        prodect_right_name = QLabel(self.product2)
        prodect_right_name.setAlignment(Qt.AlignCenter)
        name_right_layout.addWidget(prodect_right_name)
        price1_lable2 = QLabel('Technolife price :')
        price1_value2 = QPushButton(str(price1_right))
        price2_lable2 = QLabel('Digikala price :')
        price2_value2 = QPushButton(str(price2_right))
        price3_lable2 = QLabel('Divar price :')
        price3_value2 = QPushButton(str(price3_right))
        price1_value2.clicked.connect(lambda: self.open_web_page(url1_right))
        price2_value2.clicked.connect(lambda: self.open_web_page(url2_right))
        price2_value2.clicked.connect(lambda: self.open_web_page(url3_right))
        price1_right_layout.addWidget(price1_lable2)
        price1_right_layout.addWidget(price1_value2)
        price2_right_layout.addWidget(price2_lable2)
        price2_right_layout.addWidget(price2_value2)
        price3_right_layout.addWidget(price3_lable2)
        price3_right_layout.addWidget(price3_value2)
        # self.setLayout(mainlayout)
        des_label2 = QLabel('Description:')
        description_right_layout.addWidget(des_label2)
        description_text2 = QTextEdit()
        description_text2.setReadOnly(True)
        description_text2.setText(description_right)
        description_right_layout.addWidget(description_text2)                        
        self.setLayout(mainLayout)
        self.show()
    
    def open_web_page(self,url):
        url1 = QUrl(str(url))
        if not url1.isValid():
            return
        # Open the URL in the default web browser
        QDesktopServices.openUrl(url1)        

class dynamic_Window(QWidget):
    def __init__(self,username_title):
        super().__init__()
        self.setWindowTitle('Dynamic products')
        self.setGeometry(0, 0, 1700, 800)
        self.username_title = username_title
        self.dyn_UI()

    def dyn_UI(self):
        font_title = QFont()
        font_title.setPointSize(28)
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        midlayout = QHBoxLayout()
        bottomlayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(midlayout)
        mainLayout.addLayout(bottomlayout)
        topLayout.addStretch()
        cat_title = QLabel('Dynamic products')
        cat_title.setAlignment(Qt.AlignCenter)
        cat_title.setFont(font_title)
        add_product_but = QPushButton('add product')
        product_link = QLineEdit(self)
        combo_box = QComboBox(self)
        # combo_box.addItem('Technolife')
        combo_box.addItem('Digikala')
        # combo_box.addItem('Divar')
        topLayout.addWidget(cat_title)
        midlayout.addWidget(product_link)
        midlayout.addWidget(combo_box)
        midlayout.addWidget(add_product_but)
        topLayout.addStretch()
        self.setLayout(mainLayout)
        add_product_but.clicked.connect(lambda: self.get_first_value(product_link.text(),combo_box.currentText()))
        cursor.execute('''SELECT name FROM products WHERE category=?''', ('Dynamic',))
        products = cursor.fetchall()
        for product in products:
            name = product[0]
            cursor.execute('''SELECT picture FROM products WHERE name=?''', (name,))
            product_detail = cursor.fetchall()
            picture_data = product_detail[0][0]
            self.product_layout = QVBoxLayout()
            product_image = QLabel(self)
            product_label = QPushButton(name)
            pixmap = QPixmap()
            pixmap.loadFromData(picture_data)
            desired_width = 200  # Set the desired width for resizing
            desired_height = 200  # Set the desired height for resizing
            scaled_pixmap = pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)
            product_image = QLabel(self)
            product_image.setPixmap(scaled_pixmap)
            product_image.setAlignment(Qt.AlignCenter)
            self.product_layout.addWidget(product_image)
            self.product_layout.addWidget(product_label)
            bottomlayout.addLayout(self.product_layout)
            product_label.clicked.connect(self.open_product_page)
        self.show()
    def open_product_page(self):
        button = self.sender()  # Get the button that emitted the signal
        text = button.text()  # Retrieve the text of the button
        self.product_page = display_product(text,self.username_title,'Dynamic')
        self.product_page.product_UI()
            
        
        
        
    def get_first_value(self,url,site):
        driver=webdriver.Chrome()
        try:
            if site == 'Digikala':
                detail_list =[]
                driver.get(url)
                time.sleep(5)
                title = driver.find_elements(By.CSS_SELECTOR,'#__next > div.h-100.d-flex.flex-column.bg-000.ai-center > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0 > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w > div.px-5-lg > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ > div.grow-1.w-min-0 > div.d-flex.ai-center.w-full.px-5.px-0-lg > div > h1')
                name = title[0].text
                title_t = title[0].text #############
                title_t = title_t.split()
                search_text =' '.join(title_t[:10])
                try:
                    digi_price = driver.find_elements(By.CSS_SELECTOR,'#__next > div.h-100.d-flex.flex-column.bg-000.ai-center > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0 > div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.container-4xl-w > div.px-5-lg > div.d-flex.flex-column.flex-row-lg.styles_PdpProductContent__sectionBorder--mobile__J7liJ > div.grow-1.w-min-0 > div.styles_InfoSection__leftSection__0vNpX > div.d-flex.flex-column.mr-3-lg.mb-3-lg.gap-y-2-lg.styles_InfoSection__buyBoxContainer__3nOwP > div.styles_Marketable__3IHFu.radius-medium-lg.border-200-lg.bg-000.styles_InfoSection__buybox__tknJ3 > div.pos-relative.w-full.w-auto-lg.px-4-lg.pb-4-lg > div > div > div:nth-child(1) > div.d-flex.jc-start.mr-auto.text-h3 > div.d-flex.ai-center.jc-end.w-100 > span')
                    detail_list.append(self.persian_to_english(digi_price[0].text))#1
                except:
                    detail_list.append('None')
                digi_url=driver.current_url
                detail_list.append(digi_url)#2
                driver.get("https://www.technolife.ir/")
                time.sleep(5)
                box_search=driver.find_element(By.CSS_SELECTOR,"#search_box")
                time.sleep(1)
                box_search.send_keys(search_text)
                time.sleep(2)
                box_search.send_keys(Keys.ENTER)
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)
                elements_search=driver.find_elements(By.CLASS_NAME,"ProductComp_product_title__bOrf5")
                time.sleep(2)
                name1=elements_search[0].text
                time.sleep(2)
                elements_search[0].send_keys(Keys.ENTER)
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)
                try:
                    Property=driver.find_element(By.ID,"ProductSpecPart")
                    detail_list.append(Property.text)#3
                except:
                    detail_list.append('None')                                                
                try:
                    tec_price=driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div[3]/section[1]/div[3]/div[2]/div/h6/span[1]")
                    detail_list.append(self.persian_to_english(tec_price.text))#4
                except:
                    detail_list.append('None')
                try:
                    tec_url=driver.current_url
                    detail_list.append(tec_url)#5
                except:
                    detail_list.append("None")
                try:
                    img_element = driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div[3]/section[1]/div[2]/div[2]/div/img")
                    image_url = img_element.get_attribute('src')
                    image_path = self.download_image(image_url)
                    if image_path:
                        detail_list.append(image_path)#6
                        with open(image_path, 'rb') as file:
                            dyn_picture = file.read()
                    else:
                        print("Failed to download the image.")
                        detail_list.append('image.png')
                        with open('image.png', 'rb') as file:
                            dyn_picture = file.read()    
                except ValueError as va:
                    detail_list.append('image.png')
                    with open('image.png', 'rb') as file:
                            dyn_picture = file.read()
                try:
                    driver.get("https://divar.ir/s/tehran")
                    time.sleep(3)
                    box_search=driver.find_element(By.CLASS_NAME,"kt-nav-text-field__input")
                    time.sleep(3)
                    box_search.send_keys(search_text)
                    box_search.send_keys(Keys.ENTER)
                    time.sleep(2)
                    current_url=driver.current_url
                    url2=re.split("tehran?",str(current_url))
                    if detail_list[0] != 'None':
                        min=int((6/10)*int(detail_list[0]))
                        max=int((11/10)*int(detail_list[0]))
                    elif detail_list[3] != 'None' :
                        min=int((6/10)*int(detail_list[3]))                    
                        max=int((11/10)*int(detail_list[3]))
                    else:
                        min = 0
                        max = 100000000
                    komaki="price="+str(min)+"-"+str(max)+"&"
                    new_url=url2[0]+"tehran?"+komaki+url2[1][1:]
                    driver.get(new_url)
                    time.sleep(5)
                    values=driver.find_elements(By.CLASS_NAME,"kt-post-card__description")
                    time.sleep(3)
                    try:
                        pricce=values[1].text
                        detail_list.append(pricce)#7
                    except:
                        detail_list.append('None')
                    try:
                        values[0].click()
                        time.sleep(2)
                        urrl=driver.current_url
                        detail_list.append(urrl)#8
                    except:
                        detail_list.append('None')    
                except:
                    detail_list.append('None')
                    detail_list.append('None')
                driver.close()    
                print(detail_list)
                cursor.execute('''SELECT id FROM products WHERE name=?''', (name,))
                existing_product = cursor.fetchone()

                if existing_product is None:
                    # Product does not exist, insert it into the database
                    cursor.execute('''INSERT INTO products (category, name, price1, price2, price3, description, picture, url1, url2, url3)
                                    VALUES (?, ?, ?, ?, ?, ?,?,?,?,?)''',
                                ('Dynamic', name, detail_list[0], detail_list[3], detail_list[6], detail_list[2],dyn_picture,detail_list[1],detail_list[4],detail_list[7]))
                else:
                    # Product already exists, skip insertion
                    print(f"Skipping duplicate product: {title_t}")
                conn.commit()

        except ValueError as va:
            print(va)
            QMessageBox.information(self,"Information","Add dynamic was not succesful")
    
    def download_image(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                f.write(response.content)
                return f.name
        return None        
    def persian_to_english(text):
        persian_digits = "۰۱۲۳۴۵۶۷۸۹"
        english_digits = "0123456789"
        translation_table = str.maketrans(persian_digits, english_digits)
        return text.translate(translation_table)
            
class search_result(QWidget):        
    def __init__(self,product_name,price_techno,price_digi,description,digi_url,techno_url,divar_url,divar_price,image_path):
        super().__init__()
        self.setWindowTitle('Search result')
        self.setGeometry(200, 200, 400, 600)
        self.product_name = product_name
        self.price_techno = price_techno
        self.price_digi = price_digi
        self.description = description
        self.digi_url = digi_url
        self.techno_url = techno_url
        self.divar_url = divar_url
        self.divar_price =divar_price
        self.image_path = image_path
        self.search_UI()
    def search_UI(self):
        mainlayout = QVBoxLayout()
        toplayout = QHBoxLayout()
        namelayout = QHBoxLayout()
        price1layout = QHBoxLayout()
        price2layout = QHBoxLayout()
        price3layout = QHBoxLayout()
        descriptionlayout = QHBoxLayout()
        mainlayout.addLayout(toplayout)
        mainlayout.addLayout(namelayout)
        mainlayout.addLayout(price1layout)
        mainlayout.addLayout(price2layout)
        mainlayout.addLayout(price3layout)
        mainlayout.addLayout(descriptionlayout)        
        product_image = QLabel(self)
        # product_image.setPixmap(QPixmap('image.png'))
        # product_image.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(self.image_path)
        scaled_pixmap = pixmap.scaled(200,200, Qt.AspectRatioMode.KeepAspectRatio)
        product_image.setPixmap(scaled_pixmap)
        product_image.setAlignment(Qt.AlignCenter)
        toplayout.addWidget(product_image)
        name_lable = QLabel(self.product_name)
        name_lable.setAlignment(Qt.AlignCenter)
        namelayout.addWidget(name_lable)
        price1_lable = QLabel('Digikala price :')
        price1_value = QPushButton(str(self.price_digi))
        price2_lable = QLabel('Technolife price :')
        price2_value = QPushButton(str(self.price_techno))
        price1_value.clicked.connect(lambda: self.open_web_page(self.digi_url))
        price2_value.clicked.connect(lambda: self.open_web_page(self.techno_url))
        price3_lable = QLabel('Divar Price :')
        price3_value = QPushButton(str(self.divar_price))
        price3_value.clicked.connect(lambda: self.open_web_page(self.divar_url))
        price1layout.addWidget(price1_lable)
        price1layout.addWidget(price1_value)
        price2layout.addWidget(price2_lable)
        price2layout.addWidget(price2_value)
        price3layout.addWidget(price3_lable)
        price3layout.addWidget(price3_value)
        self.setLayout(mainlayout)
        des_label = QLabel('Description:')
        descriptionlayout.addWidget(des_label)
        description_text = QTextEdit()
        description_text.setReadOnly(True)
        description_text.setText(self.description)
        descriptionlayout.addWidget(description_text)        
        self.show()

    def open_web_page(self,url):
            url1 = QUrl(str(url))
            if not url1.isValid():
                return
            # Open the URL in the default web browser
            QDesktopServices.openUrl(url1)

class search_page(QWidget):
    def __init__(self,products,category_name,username_title):
        super().__init__()
        self.setWindowTitle('Search result')
        self.setGeometry(0, 0, 1700, 800)
        self.products = products
        self.category_name = category_name
        self.username_title = username_title
        self.search_UI()

    def search_UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        for product in self.products:    
            cursor.execute('''SELECT picture FROM products WHERE name=?''', (product,))
            product_detail = cursor.fetchall()
            picture_data = product_detail[0][0]
            self.product_layout = QVBoxLayout()
            pixmap = QPixmap()
            pixmap.loadFromData(picture_data)
            desired_width = 200  
            desired_height = 200  
            scaled_pixmap = pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)
            product_image = QLabel(self)
            product_image.setPixmap(scaled_pixmap)
            product_image.setAlignment(Qt.AlignCenter)
            product_label = QPushButton(product)
            self.product_layout.addWidget(product_image)
            self.product_layout.addWidget(product_label)
            topLayout.addLayout(self.product_layout)
            product_label.clicked.connect(self.open_product_page)
        
        self.setLayout(mainLayout)
        self.show()
    
    def open_product_page(self):
        button = self.sender()  # Get the button that emitted the signal
        text = button.text()  # Retrieve the text of the button
        self.product_page = display_product(text,self.username_title,self.category_name)
        self.product_page.product_UI()

    
def main():
    App = QApplication(sys.argv)
    window = Window('sample')
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()
