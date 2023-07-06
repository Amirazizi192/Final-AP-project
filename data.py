import sqlite3
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading


driver=webdriver.Chrome()
conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        name TEXT,
        price1 TEXT,
        price2 TEXT,
        price3 TEXT,
        description TEXT,
        picture BLOB,
        url1 TEXT,
        url2 TEXT,
        url3 TEXT
    )
''')

conn.commit()
conn.close()
#png
with open('iphone 13 ch.png', 'rb') as file:
    iphone13ch_image_data = file.read()
with open('Poco X4.png', 'rb') as file:
    PocoX4_image_data = file.read()
with open('sumsung A32.png', 'rb') as file:
    sumsungA32_image_data = file.read()
with open('sumsung a53.png', 'rb') as file:
    sumsunga53_image_data = file.read()
with open('sumsung s22 ultra.png', 'rb') as file:
    sumsungs22ultra_image_data = file.read()
with open('galaxy tab a7.png', 'rb') as file:
    galaxytaba7_image_data = file.read()
with open('galaxy tab a8.png', 'rb') as file:
    galaxytaba8_image_data = file.read()
with open('tablet microsoft 8 pro.png', 'rb') as file:
    tabletmicrosoft8pro_image_data = file.read()
with open('tablet ipad mini 6.png', 'rb') as file:
    tabletipadmini6_image_data = file.read()
with open('tablet ipad 10 wifi(2021).png', 'rb') as file:
    tabletipad10wifi_image_data = file.read()
with open('ROG Strix G15 G513RM R7 16G 1T SSD.png', 'rb') as file:
    ROg_image_data = file.read()
with open('lenovo legion 5.png', 'rb') as file:
    legion_image_data = file.read()
with open('tuf fx517z.png', 'rb') as file:
    tuf_image_data = file.read()
with open('Apple MacBook Air MGN63.png', 'rb') as file:
    mac_image_data = file.read()
with open('ideapad 5.png', 'rb') as file:
    ideapad5image_data = file.read()
with open('qcy t13.png', 'rb') as file:
    qcyt13image_data = file.read()
with open('airpad 3.png', 'rb') as file:
    airpad3image_data = file.read()
with open('galaxy buds2 pro.png', 'rb') as file:
    galaxybuds2proimage_data = file.read()
with open('haylou gt5.png', 'rb') as file:
    haylougt5image_data = file.read()
with open('haylou t15.png', 'rb') as file:
    haylout15image_data = file.read()
with open('xvision XCU635.png', 'rb') as file:
    xvisionXCU635image_data = file.read()
with open('tv zelmond pana43.png', 'rb') as file:
    tvzelmondpana43image_data = file.read()
with open('tv sam ua55tu7550.png', 'rb') as file:
    tvsamua55tu7550image_data = file.read()
with open('tv neksar.png', 'rb') as file:
    tvneksarimage_data = file.read()
with open('Gplus GTV-75PQM922S.png', 'rb') as file:
    GplusGTV75PQM922Simage_data = file.read()