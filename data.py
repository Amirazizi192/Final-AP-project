import sqlite3
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading


driver=webdriver.Chrome()

def static_technolife(url) :
    # driver=webdriver.Chrome()
    try :
      driver.get(url)
      time.sleep(5)
      try :
       price2=driver.find_element(By.CLASS_NAME,"ProductComp_main_price__XgWce")
       time.sleep(2)
       try :
        price1=driver.find_element(By.CLASS_NAME,"ProductComp_offer_price__HAQ6N")
        time.sleep(2)
        if int(persian_to_english(price2.text[:-5]).replace(",",""))<(1/2)*int(persian_to_english(price1.text[:-5]).replace(",","")):
          return(persian_to_english(price1.text[:-5]).replace(",",""))
        else:
           return (persian_to_english(price2.text[:-5]).replace(",",""))
       except :
        # print(va)
        # print("not found")
        return(persian_to_english(price2.text[:-5]).replace(",",""))
      except :
        price1=driver.find_element(By.CLASS_NAME,"ProductComp_offer_price__HAQ6N")
        time.sleep(2)
        return (persian_to_english(price1.text[:-5]).replace(",",""))
    except ValueError as va:
        print(va)
        # print("not found")
        return 'None'


def persian_to_english(text):
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"
    translation_table = str.maketrans(persian_digits, english_digits)
    return text.translate(translation_table)

def static_divar(url) :
    # driver=webdriver.Chrome()
    try:
        driver.get(url)
        time.sleep(5)
        price3=driver.find_elements(By.CLASS_NAME,"kt-post-card__description")
        time.sleep(2)
        a = persian_to_english(price3[1].text)[:-5]
        return (a)
        # print(persian_to_english(price3[1].text)[:-5])
        # return persian_to_english(price3[1].text)[:-5]
    except :
        # print("not found")
        return 'None'

def static_digikala(url) :
     try :
        # driver=webdriver.Chrome()
        driver.get(url)
        time.sleep(7)
        price2=driver.find_elements(By.CSS_SELECTOR,"div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)")
        time.sleep(5)
        if len(price2)==0 :
            try:
                price1=driver.find_elements(By.CSS_SELECTOR,"div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")
                time.sleep(5)
                # print(persian_to_english(price1[0].text))
                return(persian_to_english(price1[0].text))
            except :
                return (None)

        if "٪" in price2[0].text :
            if len(price2)>=2 :
                # print(persian_to_english(price2[1].text))
                return (persian_to_english(price2[1].text))
            else :
                price1=driver.find_elements(By.CSS_SELECTOR,"div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")
                time.sleep(5)
                # print(persian_to_english(price1[0].text))
                return(persian_to_english(price1[0].text))
        else :
            return(persian_to_english(price2[0].text))

     except ValueError as va:
        print(va)
        # print("not found")
        return 'None'

# png
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


# static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=309660000&price%5Bmin%5D=124195187&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85")

# products = {
#     'Mobiles': [
#         {'category': 'Mobile','picture':sumsungA32_image_data , 'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF+a32",'url2':"https://www.digikala.com/search/mobile-phone/?q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a32",'url3':"https://divar.ir/s/tehran?price=10000000-10000000&q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a32",'name': 'sumsung A32', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF+a32")', 'price2':'static_digikala("https://www.digikala.com/search/?q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a32")', 'price3':'static_divar("https://divar.ir/s/tehran?price=10000000-10000000&q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a32")', 'description': '''نوع پردازنده - CPU
# Mediatek Helio G80 (12 nm) / هشت هسته‌ای - دو هسته‌ی 2.0 گیگاهرتز Cortex-A75 به همراه شش هسته 1.8 گیگاهرتز Cortex-A55
# تعداد هسته پردازشگر
# هشت هسته
# پردازنده گرافیکی - GPU
# Mali-G52 MC2
# تعداد سیم کارت
# دو / نانو سیم کارت / همزمان فعال
# کیفیت دوربین
# دوربین چهارگانه 64 مگاپیکسل + 8 مگاپیکسل + 5 مگاپیکسل + 5 مگاپیکسل
# سیستم عامل
# Android OS, 11.0 - این نسخه برای زمانی است که این گوشی معرفی شده است و ممکن است در هنگام خرید شما، آپدیت جدیدتری برای آن آمده باشد و به اندروید ورژن بالاتر ارتقا پیدا کند. / رابط کاربری One UI 3.1
# ابعاد/ وزن
# 158.9 × 73.6 × 8.4 میلی متر / 184گرم
# ساختار بدنه
# جلو شیشه‌ای (Gorilla Glass 5) و پشت و فریم پلاستیکی
# '''},
#         {'category': 'Mobile','picture': iphone13ch_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=iphone+13",'url2':"https://www.digikala.com/search/mobile-phone/?q=iphone%2013%20ch",'url3':"https://divar.ir/s/tehran?price=10000000-10000000&q=iphone%2013" , 'name': 'iphone 13 ch', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=iphone+13")', 'price2':'static_digikala("https://www.digikala.com/search/mobile-phone/?q=iphone%2013%20ch")', 'price3': 'static_divar("https://divar.ir/s/tehran?price=10000000-10000000&q=iphone%2013")', 'description': '''ظرفیت باتری: 3240 میلی‌ آمپر ساعت
# کیفیت دوربین: دوگانه 12 مگاپیکسل + 12 مگاپیکسل
# سایز صفحه نمایش: 6.1 اینچ
# حافظه RAM: 4 گیگابایت
# حافظه داخلی: 128 گیگابایت
# نوع پردازنده - CPU: Apple A15 Bionic (5 nm) '''},
#         {'category': 'Mobile','picture': PocoX4_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=poco+x4",'url2':"https://www.digikala.com/search/mobile-phone/?q=%DA%AF%D9%88%D8%B4%DB%8C%20%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C%20poco%20x4",'url3':"https://divar.ir/s/tehran?goods-business-type=all&price=10000000-10000000&q=%D9%BE%D9%88%DA%A9%D9%88%20X5", 'name': 'Poco X4', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=poco+x4")', 'price2': 'static_digikala("https://www.digikala.com/search/mobile-phone/?q=%DA%AF%D9%88%D8%B4%DB%8C%20%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C%20poco%20x4")', 'price3': 'static_divar("https://divar.ir/s/tehran?goods-business-type=all&price=10000000-10000000&q=%D9%BE%D9%88%DA%A9%D9%88%20X5")', 'description': '''    ظرفیت باتری: 5000 میلی آمپر ساعت
#     کیفیت دوربین: سه گانه 108 مگاپیکسل + 8 مگاپیکسل + 2 مگاپیکسل
#     سایز صفحه نمایش: 6.67 اینچ
#     حافظه RAM: 8 گیگابایت
#     حافظه داخلی: 256 گیگابایت
#     نوع پردازنده - CPU: Qualcomm SM6375 Snapdragon 695 5G (6 nm)'''},
#         {'category': 'Mobile','picture': sumsunga53_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=a53",'url2':"https://www.digikala.com/search/mobile-phone/?q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a53",'url3':"https://divar.ir/s/tehran?goods-business-type=all&price=10000000-10000000&q=a53", 'name': 'sumsung a53', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=a53")', 'price2': 'static_digikala("https://www.digikala.com/search/mobile-phone/?q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a53")', 'price3': 'static_divar("https://divar.ir/s/tehran?goods-business-type=all&price=10000000-10000000&q=a53")', 'description': '''ظرفیت باتری: 5000 میلی آمپر ساعت
# کیفیت دوربین: چهارگانه 64 مگاپیکسل + 12 مگاپیکسل + 5 مگاپیکسل + 5 مگاپیکسل
# سایز صفحه نمایش: 6.5 اینچ
# حافظه RAM: 8 گیگابایت
# حافظه داخلی: 256 گیگابایت
# نوع پردازنده - CPU: Exynos 1280 '''},
#         {'category': 'Mobile','picture': sumsungs22ultra_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=s+22+ultra",'url2':"https://www.digikala.com/search/mobile-phone/?q=s%2022",'url3':"https://divar.ir/s/tehran/mobile-phones?goods-business-type=all&price=10000000-10000000&q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20s%2022", 'name': 'sumsung s22 ultra', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=s+22+ultra")', 'price2': 'static_digikala("https://www.digikala.com/search/mobile-phone/?q=s%2022")', 'price3': 'static_divar("https://divar.ir/s/tehran/mobile-phones?goods-business-type=all&price=10000000-10000000&q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20s%2022")', 'description': '''ظرفیت باتری: 5000 میلی آمپر
# کیفیت دوربین: چهارگانه 108 مگاپیکسل + 10 مگاپیکسل + 10 مگاپیکسل + 12 مگاپیکسل
# سایز صفحه نمایش: 6.8 اینچ
# حافظه RAM: 12 گیگابایت
# حافظه داخلی: 256 گیگابایت
# نوع پردازنده - CPU: Qualcomm SM8450 Snapdragon 8 Gen 1 (چهار نانومتر) / هشت هسته ای (یک هسته‌ی 3.00 '''}
#     ],
#     'Tablet': [
#         {'category': 'Tablet','picture':galaxytaba7_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA",'url3':"https://divar.ir/s/tehran?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF", 'name': 'galaxy tab a7', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA")', 'price3': 'static_divar("https://www.digikala.com/search/?q=%D8%AA%D8%A8%D9%84%D8%AA")', 'description': '''حافظه داخلی

# ۳۲ گیگابایت

# مقدار رم

# سه گیگابایت

# ساختار بدنه

# فریم آلومینیومی قاب پشت از آلومینیوم

# قطع سیم کارت

# سایز نانو (۸.۸ × ۱۲.۳ میلی‌متر)

# تراشه

# Mediatek MT۸۷۶۸T Helio P۲۲T (۱۲ nm) Chipset

# دوربین سلفی

# دوربین سلفی با کیفیت ۲ مگاپیکسل

# رزولوشن دوربین

# ۸ مگاپیکسل

# '''},
#         {'category': 'Tablet','picture':tabletmicrosoft8pro_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA",'url3':"https://divar.ir/s/tehran?goods-business-type=all&price=20000000-&q=%D8%AA%D8%A8%D9%84%D8%AA%20%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA", 'name': 'tablet microsoft 8 pro', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA")', 'price3': 'static_divar("https://divar.ir/s/tehran?goods-business-type=all&price=20000000-&q=%D8%AA%D8%A8%D9%84%D8%AA%20%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA")', 'description': '''حافظه داخلی

# ۲۵۶ گیگابایت

# مقدار رم

# هشت گیگابایت

# ساختار بدنه

# ساختار آلومینیومی با پوشش‌دهی الکتروشیمیایی

# انواع قلم نوری

# قلم سرفیس

# دوربین سلفی

# حسگر ۵ مگاپیکسلی با وضوح فیلم‌برداری ۱۰۸۰p / با پشتیبانی از قابلیت تشخیص چهره Windows Hello

# Wi-Fi

# Wi-Fi ۶: ۸۰۲.۱۱ax

# تراکم پیکسلی

# ۲۶۷ پیکسل بر اینچ

# سایر توضیحات

# دارای قلم Surface Slim Pen ۲ و کیبورد Surface Pro Signature Black / دارای چیپ امنیتی TPM / پشتیبانی از قابلیت Surface Dial off-screen / دارای سنسورهای Ambient Color و Magnetometer / حافظه داخلی SSD با قابلیت تعویض / دارای پردازنده مرکزی با ۴ هسته و ۸ رشته

# اقلام همراه

# دفترچه‌ راهنما

# شارژر

# کیبورد

# قلم

# کارکرد باتری

# تا ۱۶ ساعت


# رزولوشن

# ۱۹۲۰×۲۸۸۰ پیکسل

# فناوری‌های ارتباطی

# Wi-Fi

# بلوتوث

# حس‌گرها

# شتاب‌سنج (Accelerometer)

# ژیروسکوپ (Gyro)

# '''},
#         {'category': 'Tablet','picture':tabletipad10wifi_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%A7%D9%BE%D9%84",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%A7%D9%BE%D9%84%20ipad10",'url3':"https://divar.ir/s/tehran?price=15000000-15000000&q=ipad%2010%20wifi", 'name': 'tablet ipad 10 wifi(2021)', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%A7%D9%BE%D9%84")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%A7%D9%BE%D9%84%20ipad10")', 'price3': 'static_divar("https://divar.ir/s/tehran?price=15000000-15000000&q=ipad%2010%20wifi")', 'description': '''حافظه داخلی

# ۶۴ گیگابایت

# مقدار رم

# سه گیگابایت

# ساختار بدنه

# قاب پشت و فریم از جنس آلومینیوم

# تراشه

# A۱۳ Bionic chip

# دوربین سلفی

# یک سنسور دوربین سنسور با رزولوشن ۱۲ مگاپیکسل از نوع فوق عریض (ultra wide) توانایی ضبط ویدیو با حداکثر کیفیت ۱۰۸۰P و سرعت ۶۰ فریم در ثانیه لرزشگیر تصویر

# رزولوشن دوربین

# ۸ مگاپیکسل

# دوربین

# دوربین اصلی '''},
#         {'category': 'Tablet','picture':tabletipadmini6_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%A7%D9%BE%D9%84+ipad+mini&pfrom=0&pto=28139280&page=1",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20ipad%20mini",'url3':"https://divar.ir/s/tehran?q=ipad%20mini", 'name': 'tablet ipad mini 6', 'price1':'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%A7%D9%BE%D9%84+ipad+mini&pfrom=0&pto=28139280&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20ipad%20mini")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=ipad%20mini")', 'description': '''حافظه داخلی

# ۶۴ گیگابایت

# مقدار رم

# چهار گیگابایت

# ساختار بدنه

# آلومینیم

# تراشه

# Apple A۱۵ Bionic (۵ nm) Chipset

# دوربین سلفی

# سنسور ۱۲ مگاپیکسل سنسور دوربین از نوع عریض (ultrawide) و دارای دریچه‌ی دیافراگم f/۲.۴ و زاویه دید ۱۲۲ درجه قابلیت عکاسی HDR فیلمبرداری با رزولوشن Full HD و سرعت ۳۰، ۶۰ ، ۲۵ فریم بر ثانیه(۱۰۸۰p@۲۵/۳۰/۶۰fps)

# رزولوشن دوربین

# ۱۲ مگاپیکسل

# دوربین

# دوربین اصلی

# پشتیبانی از کارت حافظه

# فاقد پشتیبانی از کارت حافظه

# Wi-Fi

# Wi-Fi ۸۰۲.۱۱ a/b/g/n/ac/۶, dual-band, hotspot

# تراکم پیکسلی

# ۳۲۷ پیکسل بر اینچ

# پردازنده‌ی گرافیکی

# Apple GPU (۵-core) '''},
#         {'category': 'Tablet','picture':galaxytaba8_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF&pfrom=8611520&pto=23945990&page=1",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a8",'url3':"https://divar.ir/s/tehran?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a8", 'name': 'galaxy tab a8', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF&pfrom=8611520&pto=23945990&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a8")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a8")', 'description': '''حافظه داخلی

# ۶۴ گیگابایت

# مقدار رم

# چهار گیگابایت

# قطع سیم کارت

# سایز نانو (۸.۸ × ۱۲.۳ میلی‌متر)

# امکانات

# قابلیت مکالمه

# تراشه

# Unisoc Tiger T۶۱۸

# دوربین سلفی

# یک حسگر در قسمت جلویی با رزولوشن ۵ مگاپیکسل فیلمبرداری: رزولوشن ۱۰۸۰×۱۹۲۰ پیکسل با سرعت ۳۰ فریم در ثانیه (۱۰۸۰p@۳۰fps)

# رزولوشن دوربین

# ۸ مگاپیکسل

# دوربین

# دوربین اصلی

# پشتیبانی از کارت حافظه

# microSD '''}
#     ],
#     'Laptop' : [
#         {'category': 'Laptop','picture': ROg_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=rog",'url2':"https://www.digikala.com/search/?q=rog%20strix%20g15",'url3':"https://divar.ir/s/tehran?q=rog%20strix%20g15", 'name': 'ROG Strix G15 G513RM R7 16G 1T SSD', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=rog")', 'price2':'static_digikala("https://www.digikala.com/search/?q=rog%20strix%20g15")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=rog%20strix%20g15")', 'description': '''    ظرفیت حافظه داخلی: 1 ترابایت
#     سازنده پردازنده گرافیکی: NVIDIA
#     ظرفیت حافظه RAM: 16 گیگابایت
#     سری پردازنده : Ryzen 7
#     ابعاد نمایشگر: 15.6 اینچ
#     نوع کاربری: گیمینگ/ عمومی/ مالتی مدیا'''},
#         {'category': 'Laptop', 'picture': legion_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=legion+5+&pfrom=0&pto=70014910&page=1",'url2':"https://www.digikala.com/search/?q=legion%205",'url3':"https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=-60000000&q=legion%205%20", 'name': 'lenovo legion 5', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=legion+5+&pfrom=0&pto=70014910&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=legion%205")', 'price3':'static_divar("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=-60000000&q=legion%205%20")' , 'description': ''' ویژگی‌های اصلی

#     ظرفیت حافظه داخلی: 1 ترابایت
#     سازنده پردازنده گرافیکی: NVIDIA
#     ظرفیت حافظه RAM: 16 گیگابایت
#     سری پردازنده : Core i7
#     ابعاد نمایشگر: 15.6 اینچ'''},
#         {'category': 'Laptop','picture': tuf_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=tuf+",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=611905080&price%5Bmin%5D=0&q=tuf&sort=21",'url3':"https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=-60000000&q=tuf%20fx517", 'name': 'tuf fx517z', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=tuf+")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=611905080&price%5Bmin%5D=0&q=tuf&sort=21")', 'price3': 'static_divar("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=-60000000&q=tuf%20fx517")', 'description': '''ظرفیت حافظه داخلی: 512 گیگابایت
# سازنده پردازنده گرافیکی: NVIDA
# ظرفیت حافظه RAM: 16 گیگابایت
# سری پردازنده : Core i7
# ابعاد نمایشگر: 15.6 اینچ '''},
#         {'category': 'Laptop','picture': mac_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=mac",'url2':"https://www.digikala.com/search/?q=mac",'url3':"https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=25000000-60000000&q=mac", 'name': 'Apple MacBook Air MGN63', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=mac")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=mac")', 'price3': 'static_divar("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=25000000-60000000&q=mac")', 'description': '''MacBook Air MGN63 2020
# Apple MacBook Air MGN63 2020 - 13 inch Laptop
# ویژگی‌های اصلی

#     ظرفیت حافظه داخلی: 256 گیگابایت
#     سازنده پردازنده گرافیکی: Apple
#     ظرفیت حافظه RAM: 8 گیگابایت
#     سری پردازنده : Apple M'''},
#         {'category': 'Laptop','picture': ideapad5image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=ideapad",'url2':"https://www.digikala.com/search/notebook-netbook-ultrabook/?price%5Bmax%5D=382011925&price%5Bmin%5D=276733048&q=ideapad%205",'url3':"https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=25000000-60000000&q=ideapad%205", 'name': 'ideapad 5', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=ideapad")', 'price2': 'static_digikala("https://www.digikala.com/search/notebook-netbook-ultrabook/?price%5Bmax%5D=382011925&price%5Bmin%5D=276733048&q=ideapad%205")', 'price3': 'static_divar("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=25000000-60000000&q=ideapad%205")', 'description': ''' ویژگی‌های اصلی

#     ظرفیت حافظه داخلی: 512 گیگابایت
#     سازنده پردازنده گرافیکی: Intel
#     ظرفیت حافظه RAM: 16 گیگابایت
#     سری پردازنده : Core i7
#     ابعاد نمایشگر: 15.6 اینچ'''}
#   ],
#     'Headphone': [
#         {'category': 'Headphone','picture':qcyt13image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+qcy",'url2':"https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20qcy",'url3':"https://divar.ir/s/tehran?q=qcy%20t13", 'name': 'qcy t13', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+qcy")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20qcy")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=qcy%20t13")', 'description': '''اقلام همراه هدفون

# کابل شارژر Type-C - دفترچه راهنما - سه گوش‌گیر در سایز‌های مختلف از جنس سیلیکون

# جنس رابط

# Type-C

# قطر درایور

# ۷.۲ میلی‌متر

# منبع تغذیه هدفون

# باتری

# قابلیت‌های هدفون، هدست و هندزفری

# نشانگر LED

# محدوده عملکرد

# ۱۰ متر

# عمر باتری

# ۲۵ ساعت

# نوع آکوستیک

# بسته

# نوع گوشی

# دو گوشی

# عمر باتری هدفون در حالت مکالمه

# ۵ ساعت

# عمر باتری هدفون در حالت پخش موسیقی

# ۸ ساعت'''},
#         {'category': 'Headphone','picture':airpad3image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=airpad+3",'url2':"https://www.digikala.com/search/?has_selling_stock=1&price%5Bmax%5D=81500000&price%5Bmin%5D=32469251&q=%D8%A7%DB%8C%D8%B1%D9%BE%D8%A7%D8%AF%203",'url3':"https://divar.ir/s/tehran?q=airpad%203", 'name': 'airpad 3', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=airpad+3")', 'price2': 'static_digikala("https://www.digikala.com/search/?has_selling_stock=1&price%5Bmax%5D=81500000&price%5Bmin%5D=32469251&q=%D8%A7%DB%8C%D8%B1%D9%BE%D8%A7%D8%AF%203")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=airpad%203")', 'description': '''عمر باتری

# ۶ ساعت پخش موسیقی

# نوع گوشی

# دو گوشی

# عمر باتری هدفون در حالت پخش موسیقی

# ۶ ساعت

# عمر باتری محفظه شارژ

# ۳۰ ساعت

# وزن

# ۴.۲۵ گرم

# سایر مشخصات

# مجهز به چیپست Apple H۱ دارای استاندارد IPX۴ دارای Force sensor دارای speech-detecting (تشخیص گفتار) دارای شتاب سنج مجهز به تشخیص حرکت(Motion-detecting accelerometer) دارای محفظه با امکان شارژ بی‌سیم و سازگار با استاندراد Qi ساخته شده از مواد با کیفیت و سازگار با محیط زیست

# نوع اتصال

# بی‌سیم

# مناسب برای

# مکالمه

# ویژگی‌های خاص

# میکروفون

# قابلیت‌های مقاومتی

# مقاومت در برابر آب '''},
#         {'category': 'Headphone','picture':galaxybuds2proimage_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF&pfrom=3393280&pto=4299000&page=1",'url2':"https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF",'url3':"https://divar.ir/s/tehran?q=galaxy%20buds2%20pro", 'name': 'galaxy buds2 pro', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF&pfrom=3393280&pto=4299000&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=galaxy%20buds2%20pro")', 'description': '''اقلام همراه هدفون

# کابل Type-C سری هدفون

# قطر درایور

# ۱۰ میلی‌متر

# منبع تغذیه هدفون

# باتری

# عمر باتری

# ۱۸ ساعت

# نوع گوشی

# دو گوشی

# عمر باتری هدفون در حالت مکالمه

# ۳.۵ ساعت با فعال بودن ANC و ۴ ساعت با خاموش بودن ANC ساعت

# عمر باتری هدفون در حالت پخش موسیقی

# ۵ ساعت با فعال بودن ANC و ۸ ساعت با خاموش بودن ANC ساعت

# درگاه‌های ارتباطی

# بلوتوث

# نسخه بلوتوث

# ۵.۳ '''},
#         {'category': 'Headphone','picture':haylout15image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D9%87%D8%A7%DB%8C%D9%84%D9%88&pfrom=0&pto=959540&page=1",'url2':"https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20haylou%20t15",'url3':"https://divar.ir/s/tehran?q=haylou%20t15", 'name': 'haylou t15', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D9%87%D8%A7%DB%8C%D9%84%D9%88&pfrom=0&pto=959540&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20haylou%20t15")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=haylou%20t15")', 'description': '''اقلام همراه هدفون

# کابل شارژ

# قابلیت‌های هدفون، هدست و هندزفری

# نشانگر LED

# محدوده عملکرد

# ۱۰m

# نوع گوشی

# دو گوشی

# عمر باتری هدفون در حالت مکالمه

# ۱۰۰ ساعت

# عمر باتری هدفون در حالت پخش موسیقی

# ۶۰ ساعت

# زمان موردنیاز برای شارژ هدفون

# ۱.۵ ساعت

# وزن

# ۳۷ گرم

# نسخه بلوتوث

# ۵

# نوع اتصال

# بی‌سیم '''},
#         {'category': 'Headphone','picture':haylougt5image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D9%87%D8%A7%DB%8C%D9%84%D9%88+gt5",'url2':"https://www.digikala.com/search/?q=haylou%20gt5",'url3':"https://divar.ir/s/tehran?q=haylou%20gt5", 'name': 'haylou gt5', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D9%87%D8%A7%DB%8C%D9%84%D9%88+gt5")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=haylou%20gt5")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=haylou%20gt5")', 'description': '''قابلیت‌های هدفون، هدست و هندزفری

# نشانگر LED

# نوع گوشی

# تک گوشی

# عمر باتری هدفون در حالت مکالمه

# ۴ ساعت

# عمر باتری محفظه شارژ

# ۲۴ ساعت

# زمان مورد نیاز برای شارژ محفظه

# ۲ ساعت

# وزن

# ۳.۹ گرم

# نسخه بلوتوث

# ۵

# نوع اتصال

# بی‌سیم

# مناسب برای

# ورزش

# ویژگی‌های خاص

# میکروفون '''},
#     ],
#     'TV':[
#         {'category': 'TV','picture':xvisionXCU635image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+x+vision",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=430500000&price%5Bmin%5D=313090909&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20x_vision",'url3':"https://divar.ir/s/tehran/tv-projector?goods-business-type=all&price=25000000-60000000&q=xvision", 'name': 'xvision XCU635', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+x+vision")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=430500000&price%5Bmin%5D=313090909&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20x_vision")', 'price3': 'static_divar("https://divar.ir/s/tehran/tv-projector?goods-business-type=all&price=25000000-60000000&q=xvision")', 'description': ''' ویژگی‌های اصلی

#     قابلیت اتصال به دیوار: ندارد
#     رابط هوشمند: Android 11.0
#     کیفیت تصویر: Ultra HD - 4K
#     تکنولوژی صفحه: LED
#     سایز صفحه نمایش: 65 اینچ'''},
#         {'category': 'TV','picture':tvzelmondpana43image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D8%B2%D9%84%D9%85%D9%88%D9%86%D8%AF&pfrom=0&pto=12933680&page=1",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=222729305&price%5Bmin%5D=107752620&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B2%D9%84%D9%85%D9%88%D9%86%D8%AF",'url3':" ", 'name': 'tv zelmond pana43', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D8%B2%D9%84%D9%85%D9%88%D9%86%D8%AF&pfrom=0&pto=12933680&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=222729305&price%5Bmin%5D=107752620&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B2%D9%84%D9%85%D9%88%D9%86%D8%AF")', 'price3': '12300000', 'description': '''فناوری‌های ارتباطی :

# بلوتوث، Wi-Fi، پورت HDMI، پورت USB، پورت LAN

# تکنولوژی صفحه :

# LED

# نحوه نصب :

# قابلیت اتصال به دیوار

# کیفیت تصویر :

# Full HD'''},
#         {'category': 'TV','picture':tvsamua55tu7550image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%D8%B2%DB%8C%D9%88%D9%86&pfrom=16919030&pto=71450000&page=1",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=309660000&price%5Bmin%5D=124195187&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85",'url3':"https://divar.ir/s/tehran/tv-projector?goods-business-type=all&price=17000000-18000000&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85%20", 'name': 'tv sam ua55tu7550', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%D8%B2%DB%8C%D9%88%D9%86&pfrom=16919030&pto=71450000&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=309660000&price%5Bmin%5D=124195187&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85")', 'price3':'static_divar("https://divar.ir/s/tehran/tv-projector?goods-business-type=all&price=17000000-18000000&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85%20")', 'description': '''فناوری‌های ارتباطی :

# بلوتوث، Wi-Fi، پورت HDMI، پورت USB، پورت LAN

# تکنولوژی صفحه :

# LED

# نحوه نصب :

# قابلیت اتصال به دیوار

# کیفیت تصویر :

# Ultra HD - 4K'''},
#         {'category': 'TV','picture':GplusGTV75PQM922Simage_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D8%AC%DB%8C+%D9%BE%D9%84%D8%A7%D8%B3",'url2':"https://www.digikala.com/search/?q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%AC%DB%8C%20%D9%BE%D9%84%D8%A7%D8%B3",'url3':"https://divar.ir/s/tehran?goods-business-type=all&price=50000000-&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%AC%DB%8C%20%D9%BE%D9%84%D8%A7%D8%B3", 'name': 'Gplus GTV-75PQM922S', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D8%AC%DB%8C+%D9%BE%D9%84%D8%A7%D8%B3")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%AC%DB%8C%20%D9%BE%D9%84%D8%A7%D8%B3")', 'price3': 'static_divar("https://divar.ir/s/tehran?goods-business-type=all&price=50000000-&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%AC%DB%8C%20%D9%BE%D9%84%D8%A7%D8%B3")', 'description': ''' ویژگی‌های اصلی

#     قابلیت اتصال به دیوار: دارد
#     رابط هوشمند: دارد، سیستم عامل 11 Android
#     کیفیت تصویر: Ultra HD - 4K
#     تکنولوژی صفحه: QLED
#     سایز صفحه نمایش: 75 اینچ '''},
#         {'category': 'TV','picture':tvneksarimage_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D9%86%DA%A9%D8%B3%D8%A7%D8%B1",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=750802139&price%5Bmin%5D=107485989&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D9%86%DA%A9%D8%B3%D8%A7%D8%B1",'url3':"https://divar.ir/s/tehran?q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D9%86%DA%A9%D8%B3%D8%A7%D8%B1", 'name': 'tv neksar', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D9%86%DA%A9%D8%B3%D8%A7%D8%B1")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=750802139&price%5Bmin%5D=107485989&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D9%86%DA%A9%D8%B3%D8%A7%D8%B1")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D9%86%DA%A9%D8%B3%D8%A7%D8%B1")', 'description': '''سایر توضیحات

# - گيرنده ديجيتالي، - گريد انرژي A - پنل IPS - قابليت اتصال به اينترنت ندارد - پشتیبانی از طیف رنگی میلیاردی Bilion Rich Color

# کیفیت تصویر

# HD

# رزولوشن

# ۱۳۶۶ × ۷۶۸

# نسبت تصویر

# ۱۶:۹

# سایز صفحه

# ۳۲ اینچ

# پردازنده

# چهار هسته‌ای

# تعداد درگاه های HDMI

# دو عدد '''},
#     ]
# }

class get_data:
    def __init__(self):
        self.products = {
    'Mobiles': [
        {'category': 'Mobile','picture':sumsungA32_image_data , 'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF+a32",'url2':"https://www.digikala.com/search/mobile-phone/?q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a32",'url3':"https://divar.ir/s/tehran?price=10000000-10000000&q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a32",'name': 'sumsung A32', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF+a32")', 'price2':'static_digikala("https://www.digikala.com/search/?q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a32")', 'price3':'static_divar("https://divar.ir/s/tehran?price=10000000-10000000&q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a32")', 'description': '''نوع پردازنده - CPU
Mediatek Helio G80 (12 nm) / هشت هسته‌ای - دو هسته‌ی 2.0 گیگاهرتز Cortex-A75 به همراه شش هسته 1.8 گیگاهرتز Cortex-A55
تعداد هسته پردازشگر
هشت هسته
پردازنده گرافیکی - GPU
Mali-G52 MC2
تعداد سیم کارت
دو / نانو سیم کارت / همزمان فعال
کیفیت دوربین
دوربین چهارگانه 64 مگاپیکسل + 8 مگاپیکسل + 5 مگاپیکسل + 5 مگاپیکسل
سیستم عامل
Android OS, 11.0 - این نسخه برای زمانی است که این گوشی معرفی شده است و ممکن است در هنگام خرید شما، آپدیت جدیدتری برای آن آمده باشد و به اندروید ورژن بالاتر ارتقا پیدا کند. / رابط کاربری One UI 3.1
ابعاد/ وزن
158.9 × 73.6 × 8.4 میلی متر / 184گرم
ساختار بدنه
جلو شیشه‌ای (Gorilla Glass 5) و پشت و فریم پلاستیکی
'''},
        {'category': 'Mobile','picture': iphone13ch_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=iphone+13",'url2':"https://www.digikala.com/search/mobile-phone/?q=iphone%2013%20ch",'url3':"https://divar.ir/s/tehran?price=10000000-10000000&q=iphone%2013" , 'name': 'iphone 13 ch', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=iphone+13")', 'price2':'static_digikala("https://www.digikala.com/search/mobile-phone/?q=iphone%2013%20ch")', 'price3': 'static_divar("https://divar.ir/s/tehran?price=10000000-10000000&q=iphone%2013")', 'description': '''ظرفیت باتری: 3240 میلی‌ آمپر ساعت
کیفیت دوربین: دوگانه 12 مگاپیکسل + 12 مگاپیکسل
سایز صفحه نمایش: 6.1 اینچ
حافظه RAM: 4 گیگابایت
حافظه داخلی: 128 گیگابایت
نوع پردازنده - CPU: Apple A15 Bionic (5 nm) '''},
        {'category': 'Mobile','picture': PocoX4_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=poco+x4",'url2':"https://www.digikala.com/search/mobile-phone/?q=%DA%AF%D9%88%D8%B4%DB%8C%20%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C%20poco%20x4",'url3':"https://divar.ir/s/tehran?goods-business-type=all&price=10000000-10000000&q=%D9%BE%D9%88%DA%A9%D9%88%20X5", 'name': 'Poco X4', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=poco+x4")', 'price2': 'static_digikala("https://www.digikala.com/search/mobile-phone/?q=%DA%AF%D9%88%D8%B4%DB%8C%20%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C%20poco%20x4")', 'price3': 'static_divar("https://divar.ir/s/tehran?goods-business-type=all&price=10000000-10000000&q=%D9%BE%D9%88%DA%A9%D9%88%20X5")', 'description': '''    ظرفیت باتری: 5000 میلی آمپر ساعت
    کیفیت دوربین: سه گانه 108 مگاپیکسل + 8 مگاپیکسل + 2 مگاپیکسل
    سایز صفحه نمایش: 6.67 اینچ
    حافظه RAM: 8 گیگابایت
    حافظه داخلی: 256 گیگابایت
    نوع پردازنده - CPU: Qualcomm SM6375 Snapdragon 695 5G (6 nm)'''},
        {'category': 'Mobile','picture': sumsunga53_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=a53",'url2':"https://www.digikala.com/search/mobile-phone/?q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a53",'url3':"https://divar.ir/s/tehran?goods-business-type=all&price=10000000-10000000&q=a53", 'name': 'sumsung a53', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=a53")', 'price2': 'static_digikala("https://www.digikala.com/search/mobile-phone/?q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a53")', 'price3': 'static_divar("https://divar.ir/s/tehran?goods-business-type=all&price=10000000-10000000&q=a53")', 'description': '''ظرفیت باتری: 5000 میلی آمپر ساعت
کیفیت دوربین: چهارگانه 64 مگاپیکسل + 12 مگاپیکسل + 5 مگاپیکسل + 5 مگاپیکسل
سایز صفحه نمایش: 6.5 اینچ
حافظه RAM: 8 گیگابایت
حافظه داخلی: 256 گیگابایت
نوع پردازنده - CPU: Exynos 1280 '''},
        {'category': 'Mobile','picture': sumsungs22ultra_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=s+22+ultra",'url2':"https://www.digikala.com/search/mobile-phone/?q=s%2022",'url3':"https://divar.ir/s/tehran/mobile-phones?goods-business-type=all&price=10000000-10000000&q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20s%2022", 'name': 'sumsung s22 ultra', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=s+22+ultra")', 'price2': 'static_digikala("https://www.digikala.com/search/mobile-phone/?q=s%2022")', 'price3': 'static_divar("https://divar.ir/s/tehran/mobile-phones?goods-business-type=all&price=10000000-10000000&q=%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20s%2022")', 'description': '''ظرفیت باتری: 5000 میلی آمپر
کیفیت دوربین: چهارگانه 108 مگاپیکسل + 10 مگاپیکسل + 10 مگاپیکسل + 12 مگاپیکسل
سایز صفحه نمایش: 6.8 اینچ
حافظه RAM: 12 گیگابایت
حافظه داخلی: 256 گیگابایت
نوع پردازنده - CPU: Qualcomm SM8450 Snapdragon 8 Gen 1 (چهار نانومتر) / هشت هسته ای (یک هسته‌ی 3.00 '''}
    ],
    'Tablet': [
        {'category': 'Tablet','picture':galaxytaba7_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA",'url3':"https://divar.ir/s/tehran?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF", 'name': 'galaxy tab a7', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA")', 'price3': 'static_divar("https://www.digikala.com/search/?q=%D8%AA%D8%A8%D9%84%D8%AA")', 'description': '''حافظه داخلی

۳۲ گیگابایت

مقدار رم

سه گیگابایت

ساختار بدنه

فریم آلومینیومی قاب پشت از آلومینیوم

قطع سیم کارت

سایز نانو (۸.۸ × ۱۲.۳ میلی‌متر)

تراشه

Mediatek MT۸۷۶۸T Helio P۲۲T (۱۲ nm) Chipset

دوربین سلفی

دوربین سلفی با کیفیت ۲ مگاپیکسل

رزولوشن دوربین

۸ مگاپیکسل

'''},
        {'category': 'Tablet','picture':tabletmicrosoft8pro_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA",'url3':"https://divar.ir/s/tehran?goods-business-type=all&price=20000000-&q=%D8%AA%D8%A8%D9%84%D8%AA%20%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA", 'name': 'tablet microsoft 8 pro', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA")', 'price3': 'static_divar("https://divar.ir/s/tehran?goods-business-type=all&price=20000000-&q=%D8%AA%D8%A8%D9%84%D8%AA%20%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA")', 'description': '''حافظه داخلی

۲۵۶ گیگابایت

مقدار رم

هشت گیگابایت

ساختار بدنه

ساختار آلومینیومی با پوشش‌دهی الکتروشیمیایی

انواع قلم نوری

قلم سرفیس

دوربین سلفی

حسگر ۵ مگاپیکسلی با وضوح فیلم‌برداری ۱۰۸۰p / با پشتیبانی از قابلیت تشخیص چهره Windows Hello

Wi-Fi

Wi-Fi ۶: ۸۰۲.۱۱ax

تراکم پیکسلی

۲۶۷ پیکسل بر اینچ

سایر توضیحات

دارای قلم Surface Slim Pen ۲ و کیبورد Surface Pro Signature Black / دارای چیپ امنیتی TPM / پشتیبانی از قابلیت Surface Dial off-screen / دارای سنسورهای Ambient Color و Magnetometer / حافظه داخلی SSD با قابلیت تعویض / دارای پردازنده مرکزی با ۴ هسته و ۸ رشته

اقلام همراه

دفترچه‌ راهنما

شارژر

کیبورد

قلم

کارکرد باتری

تا ۱۶ ساعت


رزولوشن

۱۹۲۰×۲۸۸۰ پیکسل

فناوری‌های ارتباطی

Wi-Fi

بلوتوث

حس‌گرها

شتاب‌سنج (Accelerometer)

ژیروسکوپ (Gyro)

'''},
        {'category': 'Tablet','picture':tabletipad10wifi_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%A7%D9%BE%D9%84",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%A7%D9%BE%D9%84%20ipad10",'url3':"https://divar.ir/s/tehran?price=15000000-15000000&q=ipad%2010%20wifi", 'name': 'tablet ipad 10 wifi(2021)', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%A7%D9%BE%D9%84")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%A7%D9%BE%D9%84%20ipad10")', 'price3': 'static_divar("https://divar.ir/s/tehran?price=15000000-15000000&q=ipad%2010%20wifi")', 'description': '''حافظه داخلی

۶۴ گیگابایت

مقدار رم

سه گیگابایت

ساختار بدنه

قاب پشت و فریم از جنس آلومینیوم

تراشه

A۱۳ Bionic chip

دوربین سلفی

یک سنسور دوربین سنسور با رزولوشن ۱۲ مگاپیکسل از نوع فوق عریض (ultra wide) توانایی ضبط ویدیو با حداکثر کیفیت ۱۰۸۰P و سرعت ۶۰ فریم در ثانیه لرزشگیر تصویر

رزولوشن دوربین

۸ مگاپیکسل

دوربین

دوربین اصلی '''},
        {'category': 'Tablet','picture':tabletipadmini6_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%A7%D9%BE%D9%84+ipad+mini&pfrom=0&pto=28139280&page=1",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20ipad%20mini",'url3':"https://divar.ir/s/tehran?q=ipad%20mini", 'name': 'tablet ipad mini 6', 'price1':'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%A7%D9%BE%D9%84+ipad+mini&pfrom=0&pto=28139280&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20ipad%20mini")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=ipad%20mini")', 'description': '''حافظه داخلی

۶۴ گیگابایت

مقدار رم

چهار گیگابایت

ساختار بدنه

آلومینیم

تراشه

Apple A۱۵ Bionic (۵ nm) Chipset

دوربین سلفی

سنسور ۱۲ مگاپیکسل سنسور دوربین از نوع عریض (ultrawide) و دارای دریچه‌ی دیافراگم f/۲.۴ و زاویه دید ۱۲۲ درجه قابلیت عکاسی HDR فیلمبرداری با رزولوشن Full HD و سرعت ۳۰، ۶۰ ، ۲۵ فریم بر ثانیه(۱۰۸۰p@۲۵/۳۰/۶۰fps)

رزولوشن دوربین

۱۲ مگاپیکسل

دوربین

دوربین اصلی

پشتیبانی از کارت حافظه

فاقد پشتیبانی از کارت حافظه

Wi-Fi

Wi-Fi ۸۰۲.۱۱ a/b/g/n/ac/۶, dual-band, hotspot

تراکم پیکسلی

۳۲۷ پیکسل بر اینچ

پردازنده‌ی گرافیکی

Apple GPU (۵-core) '''},
        {'category': 'Tablet','picture':galaxytaba8_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF&pfrom=8611520&pto=23945990&page=1",'url2':"https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a8",'url3':"https://divar.ir/s/tehran?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a8", 'name': 'galaxy tab a8', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D8%A8%D9%84%D8%AA+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF&pfrom=8611520&pto=23945990&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/tablet/?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a8")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=%D8%AA%D8%A8%D9%84%D8%AA%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF%20a8")', 'description': '''حافظه داخلی

۶۴ گیگابایت

مقدار رم

چهار گیگابایت

قطع سیم کارت

سایز نانو (۸.۸ × ۱۲.۳ میلی‌متر)

امکانات

قابلیت مکالمه

تراشه

Unisoc Tiger T۶۱۸

دوربین سلفی

یک حسگر در قسمت جلویی با رزولوشن ۵ مگاپیکسل فیلمبرداری: رزولوشن ۱۰۸۰×۱۹۲۰ پیکسل با سرعت ۳۰ فریم در ثانیه (۱۰۸۰p@۳۰fps)

رزولوشن دوربین

۸ مگاپیکسل

دوربین

دوربین اصلی

پشتیبانی از کارت حافظه

microSD '''}
    ],
    'Laptop' : [
        {'category': 'Laptop','picture': ROg_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=rog",'url2':"https://www.digikala.com/search/?q=rog%20strix%20g15",'url3':"https://divar.ir/s/tehran?q=rog%20strix%20g15", 'name': 'ROG Strix G15 G513RM R7 16G 1T SSD', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=rog")', 'price2':'static_digikala("https://www.digikala.com/search/?q=rog%20strix%20g15")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=rog%20strix%20g15")', 'description': '''    ظرفیت حافظه داخلی: 1 ترابایت
    سازنده پردازنده گرافیکی: NVIDIA
    ظرفیت حافظه RAM: 16 گیگابایت
    سری پردازنده : Ryzen 7
    ابعاد نمایشگر: 15.6 اینچ
    نوع کاربری: گیمینگ/ عمومی/ مالتی مدیا'''},
        {'category': 'Laptop', 'picture': legion_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=legion+5+&pfrom=0&pto=70014910&page=1",'url2':"https://www.digikala.com/search/?q=legion%205",'url3':"https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=-60000000&q=legion%205%20", 'name': 'lenovo legion 5', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=legion+5+&pfrom=0&pto=70014910&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=legion%205")', 'price3':'static_divar("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=-60000000&q=legion%205%20")' , 'description': ''' ویژگی‌های اصلی

    ظرفیت حافظه داخلی: 1 ترابایت
    سازنده پردازنده گرافیکی: NVIDIA
    ظرفیت حافظه RAM: 16 گیگابایت
    سری پردازنده : Core i7
    ابعاد نمایشگر: 15.6 اینچ'''},
        {'category': 'Laptop','picture': tuf_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=tuf+",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=611905080&price%5Bmin%5D=0&q=tuf&sort=21",'url3':"https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=-60000000&q=tuf%20fx517", 'name': 'tuf fx517z', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=tuf+")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=611905080&price%5Bmin%5D=0&q=tuf&sort=21")', 'price3': 'static_divar("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=-60000000&q=tuf%20fx517")', 'description': '''ظرفیت حافظه داخلی: 512 گیگابایت
سازنده پردازنده گرافیکی: NVIDA
ظرفیت حافظه RAM: 16 گیگابایت
سری پردازنده : Core i7
ابعاد نمایشگر: 15.6 اینچ '''},
        {'category': 'Laptop','picture': mac_image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=mac",'url2':"https://www.digikala.com/search/?q=mac",'url3':"https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=25000000-60000000&q=mac", 'name': 'Apple MacBook Air MGN63', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=mac")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=mac")', 'price3': 'static_divar("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=25000000-60000000&q=mac")', 'description': '''MacBook Air MGN63 2020
Apple MacBook Air MGN63 2020 - 13 inch Laptop
ویژگی‌های اصلی

    ظرفیت حافظه داخلی: 256 گیگابایت
    سازنده پردازنده گرافیکی: Apple
    ظرفیت حافظه RAM: 8 گیگابایت
    سری پردازنده : Apple M'''},
        {'category': 'Laptop','picture': ideapad5image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=ideapad",'url2':"https://www.digikala.com/search/notebook-netbook-ultrabook/?price%5Bmax%5D=382011925&price%5Bmin%5D=276733048&q=ideapad%205",'url3':"https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=25000000-60000000&q=ideapad%205", 'name': 'ideapad 5', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=ideapad")', 'price2': 'static_digikala("https://www.digikala.com/search/notebook-netbook-ultrabook/?price%5Bmax%5D=382011925&price%5Bmin%5D=276733048&q=ideapad%205")', 'price3': 'static_divar("https://divar.ir/s/tehran/laptop-notebook-macbook?goods-business-type=all&price=25000000-60000000&q=ideapad%205")', 'description': ''' ویژگی‌های اصلی

    ظرفیت حافظه داخلی: 512 گیگابایت
    سازنده پردازنده گرافیکی: Intel
    ظرفیت حافظه RAM: 16 گیگابایت
    سری پردازنده : Core i7
    ابعاد نمایشگر: 15.6 اینچ'''}
  ],
    'Headphone': [
        {'category': 'Headphone','picture':qcyt13image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+qcy",'url2':"https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20qcy",'url3':"https://divar.ir/s/tehran?q=qcy%20t13", 'name': 'qcy t13', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+qcy")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20qcy")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=qcy%20t13")', 'description': '''اقلام همراه هدفون

کابل شارژر Type-C - دفترچه راهنما - سه گوش‌گیر در سایز‌های مختلف از جنس سیلیکون

جنس رابط

Type-C

قطر درایور

۷.۲ میلی‌متر

منبع تغذیه هدفون

باتری

قابلیت‌های هدفون، هدست و هندزفری

نشانگر LED

محدوده عملکرد

۱۰ متر

عمر باتری

۲۵ ساعت

نوع آکوستیک

بسته

نوع گوشی

دو گوشی

عمر باتری هدفون در حالت مکالمه

۵ ساعت

عمر باتری هدفون در حالت پخش موسیقی

۸ ساعت'''},
        {'category': 'Headphone','picture':airpad3image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=airpad+3",'url2':"https://www.digikala.com/search/?has_selling_stock=1&price%5Bmax%5D=81500000&price%5Bmin%5D=32469251&q=%D8%A7%DB%8C%D8%B1%D9%BE%D8%A7%D8%AF%203",'url3':"https://divar.ir/s/tehran?q=airpad%203", 'name': 'airpad 3', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=airpad+3")', 'price2': 'static_digikala("https://www.digikala.com/search/?has_selling_stock=1&price%5Bmax%5D=81500000&price%5Bmin%5D=32469251&q=%D8%A7%DB%8C%D8%B1%D9%BE%D8%A7%D8%AF%203")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=airpad%203")', 'description': '''عمر باتری

۶ ساعت پخش موسیقی

نوع گوشی

دو گوشی

عمر باتری هدفون در حالت پخش موسیقی

۶ ساعت

عمر باتری محفظه شارژ

۳۰ ساعت

وزن

۴.۲۵ گرم

سایر مشخصات

مجهز به چیپست Apple H۱ دارای استاندارد IPX۴ دارای Force sensor دارای speech-detecting (تشخیص گفتار) دارای شتاب سنج مجهز به تشخیص حرکت(Motion-detecting accelerometer) دارای محفظه با امکان شارژ بی‌سیم و سازگار با استاندراد Qi ساخته شده از مواد با کیفیت و سازگار با محیط زیست

نوع اتصال

بی‌سیم

مناسب برای

مکالمه

ویژگی‌های خاص

میکروفون

قابلیت‌های مقاومتی

مقاومت در برابر آب '''},
        {'category': 'Headphone','picture':galaxybuds2proimage_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF&pfrom=3393280&pto=4299000&page=1",'url2':"https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF",'url3':"https://divar.ir/s/tehran?q=galaxy%20buds2%20pro", 'name': 'galaxy buds2 pro', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF&pfrom=3393280&pto=4299000&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=galaxy%20buds2%20pro")', 'description': '''اقلام همراه هدفون

کابل Type-C سری هدفون

قطر درایور

۱۰ میلی‌متر

منبع تغذیه هدفون

باتری

عمر باتری

۱۸ ساعت

نوع گوشی

دو گوشی

عمر باتری هدفون در حالت مکالمه

۳.۵ ساعت با فعال بودن ANC و ۴ ساعت با خاموش بودن ANC ساعت

عمر باتری هدفون در حالت پخش موسیقی

۵ ساعت با فعال بودن ANC و ۸ ساعت با خاموش بودن ANC ساعت

درگاه‌های ارتباطی

بلوتوث

نسخه بلوتوث

۵.۳ '''},
        {'category': 'Headphone','picture':haylout15image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D9%87%D8%A7%DB%8C%D9%84%D9%88&pfrom=0&pto=959540&page=1",'url2':"https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20haylou%20t15",'url3':"https://divar.ir/s/tehran?q=haylou%20t15", 'name': 'haylou t15', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D9%87%D8%A7%DB%8C%D9%84%D9%88&pfrom=0&pto=959540&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=%D9%87%D8%AF%D9%81%D9%88%D9%86%20haylou%20t15")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=haylou%20t15")', 'description': '''اقلام همراه هدفون

کابل شارژ

قابلیت‌های هدفون، هدست و هندزفری

نشانگر LED

محدوده عملکرد

۱۰m

نوع گوشی

دو گوشی

عمر باتری هدفون در حالت مکالمه

۱۰۰ ساعت

عمر باتری هدفون در حالت پخش موسیقی

۶۰ ساعت

زمان موردنیاز برای شارژ هدفون

۱.۵ ساعت

وزن

۳۷ گرم

نسخه بلوتوث

۵

نوع اتصال

بی‌سیم '''},
        {'category': 'Headphone','picture':haylougt5image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D9%87%D8%A7%DB%8C%D9%84%D9%88+gt5",'url2':"https://www.digikala.com/search/?q=haylou%20gt5",'url3':"https://divar.ir/s/tehran?q=haylou%20gt5", 'name': 'haylou gt5', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D9%87%D8%AF%D9%81%D9%88%D9%86+%D9%87%D8%A7%DB%8C%D9%84%D9%88+gt5")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=haylou%20gt5")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=haylou%20gt5")', 'description': '''قابلیت‌های هدفون، هدست و هندزفری

نشانگر LED

نوع گوشی

تک گوشی

عمر باتری هدفون در حالت مکالمه

۴ ساعت

عمر باتری محفظه شارژ

۲۴ ساعت

زمان مورد نیاز برای شارژ محفظه

۲ ساعت

وزن

۳.۹ گرم

نسخه بلوتوث

۵

نوع اتصال

بی‌سیم

مناسب برای

ورزش

ویژگی‌های خاص

میکروفون '''},
    ],
    'TV':[
        {'category': 'TV','picture':xvisionXCU635image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+x+vision",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=430500000&price%5Bmin%5D=313090909&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20x_vision",'url3':"https://divar.ir/s/tehran/tv-projector?goods-business-type=all&price=25000000-60000000&q=xvision", 'name': 'xvision XCU635', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+x+vision")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=430500000&price%5Bmin%5D=313090909&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20x_vision")', 'price3': 'static_divar("https://divar.ir/s/tehran/tv-projector?goods-business-type=all&price=25000000-60000000&q=xvision")', 'description': ''' ویژگی‌های اصلی

    قابلیت اتصال به دیوار: ندارد
    رابط هوشمند: Android 11.0
    کیفیت تصویر: Ultra HD - 4K
    تکنولوژی صفحه: LED
    سایز صفحه نمایش: 65 اینچ'''},
        {'category': 'TV','picture':tvzelmondpana43image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D8%B2%D9%84%D9%85%D9%88%D9%86%D8%AF&pfrom=0&pto=12933680&page=1",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=222729305&price%5Bmin%5D=107752620&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B2%D9%84%D9%85%D9%88%D9%86%D8%AF",'url3':" ", 'name': 'tv zelmond pana43', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D8%B2%D9%84%D9%85%D9%88%D9%86%D8%AF&pfrom=0&pto=12933680&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=222729305&price%5Bmin%5D=107752620&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B2%D9%84%D9%85%D9%88%D9%86%D8%AF")', 'price3': '12300000', 'description': '''فناوری‌های ارتباطی :

بلوتوث، Wi-Fi، پورت HDMI، پورت USB، پورت LAN

تکنولوژی صفحه :

LED

نحوه نصب :

قابلیت اتصال به دیوار

کیفیت تصویر :

Full HD'''},
        {'category': 'TV','picture':tvsamua55tu7550image_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%D8%B2%DB%8C%D9%88%D9%86&pfrom=16919030&pto=71450000&page=1",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=309660000&price%5Bmin%5D=124195187&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85",'url3':"https://divar.ir/s/tehran/tv-projector?goods-business-type=all&price=17000000-18000000&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85%20", 'name': 'tv sam ua55tu7550', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%D8%B2%DB%8C%D9%88%D9%86&pfrom=16919030&pto=71450000&page=1")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=309660000&price%5Bmin%5D=124195187&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85")', 'price3':'static_divar("https://divar.ir/s/tehran/tv-projector?goods-business-type=all&price=17000000-18000000&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%B3%D8%A7%D9%85%20")', 'description': '''فناوری‌های ارتباطی :

بلوتوث، Wi-Fi، پورت HDMI، پورت USB، پورت LAN

تکنولوژی صفحه :

LED

نحوه نصب :

قابلیت اتصال به دیوار

کیفیت تصویر :

Ultra HD - 4K'''},
        {'category': 'TV','picture':GplusGTV75PQM922Simage_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D8%AC%DB%8C+%D9%BE%D9%84%D8%A7%D8%B3",'url2':"https://www.digikala.com/search/?q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%AC%DB%8C%20%D9%BE%D9%84%D8%A7%D8%B3",'url3':"https://divar.ir/s/tehran?goods-business-type=all&price=50000000-&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%AC%DB%8C%20%D9%BE%D9%84%D8%A7%D8%B3", 'name': 'Gplus GTV-75PQM922S', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D8%AC%DB%8C+%D9%BE%D9%84%D8%A7%D8%B3")', 'price2': 'static_digikala("https://www.digikala.com/search/?q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%AC%DB%8C%20%D9%BE%D9%84%D8%A7%D8%B3")', 'price3': 'static_divar("https://divar.ir/s/tehran?goods-business-type=all&price=50000000-&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D8%AC%DB%8C%20%D9%BE%D9%84%D8%A7%D8%B3")', 'description': ''' ویژگی‌های اصلی

    قابلیت اتصال به دیوار: دارد
    رابط هوشمند: دارد، سیستم عامل 11 Android
    کیفیت تصویر: Ultra HD - 4K
    تکنولوژی صفحه: QLED
    سایز صفحه نمایش: 75 اینچ '''},
        {'category': 'TV','picture':tvneksarimage_data,'url1':"https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D9%86%DA%A9%D8%B3%D8%A7%D8%B1",'url2':"https://www.digikala.com/search/?price%5Bmax%5D=750802139&price%5Bmin%5D=107485989&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D9%86%DA%A9%D8%B3%D8%A7%D8%B1",'url3':"https://divar.ir/s/tehran?q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D9%86%DA%A9%D8%B3%D8%A7%D8%B1", 'name': 'tv neksar', 'price1': 'static_technolife("https://www.technolife.ir/product/list/search?keywords=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86+%D9%86%DA%A9%D8%B3%D8%A7%D8%B1")', 'price2': 'static_digikala("https://www.digikala.com/search/?price%5Bmax%5D=750802139&price%5Bmin%5D=107485989&q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D9%86%DA%A9%D8%B3%D8%A7%D8%B1")', 'price3': 'static_divar("https://divar.ir/s/tehran?q=%D8%AA%D9%84%D9%88%DB%8C%D8%B2%DB%8C%D9%88%D9%86%20%D9%86%DA%A9%D8%B3%D8%A7%D8%B1")', 'description': '''سایر توضیحات

- گيرنده ديجيتالي، - گريد انرژي A - پنل IPS - قابليت اتصال به اينترنت ندارد - پشتیبانی از طیف رنگی میلیاردی Bilion Rich Color

کیفیت تصویر

HD

رزولوشن

۱۳۶۶ × ۷۶۸

نسبت تصویر

۱۶:۹

سایز صفحه

۳۲ اینچ

پردازنده

چهار هسته‌ای

تعداد درگاه های HDMI

دو عدد '''},
    ]
}
    def get__data(self):
        try:
            conn = sqlite3.connect('users3.db')
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
            for category,products_list in self.products.items():
                for product in products_list:
                    new_price1 = eval(product['price1'])
                    new_price2 = eval(product['price2'])
                    new_price3 =eval(product['price3'])
                    cursor.execute("UPDATE products SET price1 = ?, price2 = ?, price3 = ? WHERE name = ?", (new_price1, new_price2, new_price3, product['name']))

            conn.commit()
            conn.close()
            driver.close()
                
        except ValueError as va:
            print(va)

get_data()








