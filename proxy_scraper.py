# import urllib2,cookielib

# from bs4 import BeautifulSoup

# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#        'Accept-Encoding': 'none',
#        'Accept-Language': 'en-US,en;q=0.8',
#        'Connection': 'keep-alive'}


# proxy_page = "https://hidemyna.me/en/proxy-list/#list"

# req = urllib2.Request(proxy_page, headers=hdr)

# page = urllib2.urlopen(req)  
# soup = BeautifulSoup(page, 'html.parser')
# name_box = soup.find('td', attrs={'class': 'tdl'})

# name = name_box.text.strip() # strip() is used to remove starting and trailing
# print(name)

from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException        
from random import choice
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')

url = 'https://hidemyna.me/en/proxy-list/?country=IN#list'
# https://hidemyna.me/en/proxy-list/?country=IN#list

driver.get(url)
time.sleep(10)
proxy = driver.find_elements_by_class_name('tdl')

for i in proxy:
    print(i.text)

for k in range(1,5):
    new_url = 'https://hidemyna.me/en/proxy-list/?country=IN&start=%s#list'%(64*k)
    driver.get(new_url)
    time.sleep(10)
    proxy_list_new = driver.find_elements_by_class_name('tdl')

    for j in proxy_list_new:
        print(j.text)