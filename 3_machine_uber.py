'''November'''

from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException        
from random import choice
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
import string
from time import sleep
from random import randint
# import org.openqa.selenium.support.ui.Select
from selenium.webdriver.support.ui import Select

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

# def main():
#     print(generate_random_emails(10, 7))


def randomString(stringLength=3):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def getProxyList():
    proxyList = []
    with open('./proxy_list_git.txt') as f:
        proxys = f.readlines()
    for i in proxys:
        if len(i) > 5:
            if i[:4] != 'http':
                proxyList.append('http://' + i.split('\n')[0])
            else:
                proxyList.append(i.split('\n')[0])
    proxyList = list(set(proxyList))
    return proxyList


proxy = getProxyList()

'''checks for validity of a given xpath'''
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

'''checks for validity of a given css selector'''
def check_exists_by_css_selector(css_selector):
    try:
        driver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True
 
# list_time = ['AM','MIDDAY', 'PM', 'EVENING', 'EARLY_MORNING']
list_time = ['AM']
for t in list_time:
    for date_me in range(9,10):
        for i in range(227,291):
                try:
                    if date_me <= 9:
                        date_me_temp = str("0"+str(date_me))
                    url = 'https://movement.uber.com/explore/new_delhi/travel-times/query?lang=hi-IN&si=%s&ti=1&ag=wards&dt[tpb]=%s&dt[wd;]=1,2,3,4,5,6,7&dt[dr][sd]=2016-11-%s&dt[dr][ed]=2016-11-%s&cd=&lat.=28.6203201&lng.=77.1405719&z.=13&sa;=&sdn=&ta;=&tdn='%(i,t,date_me_temp,date_me_temp)
 
                    PROXY = choice(proxy)
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument('--proxy-server=%s' % PROXY)

                    driver = webdriver.Chrome(executable_path='./chromedriver')
                    driver.get(url)
                    flag = 0
                    wait = WebDriverWait(driver, 10)
                    time.sleep(5)
                    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.gg.ib.d1.d0.cz.d2.ic > div.ai.ay.bc.cf.ii.gf.h0 > div > div.is.it.iu > div > div.ai.aw > button")) or EC.presence_of_element_located(By.CSS_SELECTOR,"body > div.gg.ii.d1.d0.cz.d2.ij > div.ai.ay.bc.cf.ip.gf.h0 > div > div.iz.j0.j1 > div > div.ai.aw > button"))
                    # body > div.gg.ii.d1.d0.cz.d2.ij > div.ai.ay.bc.cf.ip.gf.h0 > div > div.iz.j0.j1 > div > div.ai.aw > button
                    # body > div.gg.ii.d1.d0.cz.d2.ij > div.ai.ay.bc.cf.ip.gf.h0 > div > div.iz.j0.j1 > div > div.ai.aw > button
                    # body > div.gg.ii.d1.d0.cz.d2.ij > div.ai.ay.bc.cf.ip.gf.h0 > div > div.iz.j0.j1 > div > div.ai.aw > button
                    # body > div.gg.ii.d1.d0.cz.d2.ij > div.ai.ay.bc.cf.ip.gf.h0 > div > div.iz.j0.j1 > div > div.ai.aw > button
                    if check_exists_by_css_selector('body > div.gg.ib.d1.d0.cz.d2.ic > div.ai.ay.bc.cf.ii.gf.h0 > div > div.is.it.iu > div > div.ai.aw > button'):
                        flag = 1
                        skip = driver.find_element_by_css_selector('body > div.gg.ib.d1.d0.cz.d2.ic > div.ai.ay.bc.cf.ii.gf.h0 > div > div.is.it.iu > div > div.ai.aw > button')
                    elif check_exists_by_xpath('body > div.gg.ii.d1.d0.cz.d2.ij > div.ai.ay.bc.cf.ip.gf.h0 > div > div.iz.j0.j1 > div > div.ai.aw > button'):
                        flag = 1
                        skip = driver.find_element_by_css_selector('body > div.gg.ii.d1.d0.cz.d2.ij > div.ai.ay.bc.cf.ip.gf.h0 > div > div.iz.j0.j1 > div > div.ai.aw > button')
                    # wait.until(flag == 1)
                    # skip = driver.find_element_by_css_selector('body > div.gg.ib.d1.d0.cz.d2.ic > div.ai.ay.bc.cf.ii.gf.h0 > div > div.is.it.iu > div > div.ai.aw > button')
                    skip.click()

                    download_button = driver.find_element_by_css_selector('button.b5')
                    download_button.click()
                    
                    download_file = driver.find_element_by_css_selector('button.btn:nth-child(2)')
                    download_file.click()
                    time.sleep(1)

                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.dk:nth-child(2)')))
                    query = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="firstName"]')))
                    temp_first = randomString()
                    query.send_keys(temp_first)
                    WebDriverWait(driver, 5).until(lambda driver: query.get_attribute('value') == temp_first)
                    
                    query2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lastName"]')))
                    temp_last = randomString()
                    query2.send_keys(temp_last)
                    WebDriverWait(driver, 10).until(lambda driver: query2.get_attribute('value') == temp_last)
                    
                    query3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
                    temp_email = generate_random_emails(1,2)
                    query3.send_keys(temp_email)
                    # WebDriverWait(driver, 10).until(lambda driver: query3.get_attribute('value') == temp_email)
                    print("D")
                    query4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div/div/div/form/div[3]/div/div[1]/div/span/div[2]/input')))
                    print("C")
                    drop_down = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/form/div[3]/div/div[1]/div/span/div[2]/input')
                    print("A")

                    drop_down.send_keys('Curiosity\n')

                    # query4.send_keys('Curiosity')
                    time.sleep(1)
                    # wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[2]/div/div/div/form/div[6]/button[2]")))
                    download_button = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/form/div[6]/button[2]')
                    download_button.click()
                    # reason = Select(driver.find_element_by_css_selector("svg.d8:nth-child(2)"))
                    # reason.select_by_visible_text('Curiosity')
                    time.sleep(2)
                    driver.quit()
                    timedelay = random.randrange(3, 10)                
                    time.sleep(timedelay)
                    # //*[@id="email"]
# ae b5 ag bz dd ge d3 b1 an cp d8 d9 c9 cb cc ca c7 c8 bt bw
                except Exception as e:
                    print("i,date_me,t : ",i,date_me_temp,t)
                    print('\n')
                    print(e)
