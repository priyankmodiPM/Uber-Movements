'''September'''

from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException        
from random import choice
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path = '/home/akshay/isb/School/chromedriver')


def getProxyList():
    proxyList = []
    with open('./list.txt') as f:
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
 
list_time = ['AM','MIDDAY', 'PM', 'EVENING', 'EARLY_MORNING']
for t in list_time:
    for date_me in range(1,31):
        for i in range(1,291):
                try:
                    if date_me <= 9:
                        date_me_temp = str("0"+str(date_me))
                    url = 'https://movement.uber.com/explore/new_delhi/travel-times/query?lang=hi-IN&si=%s&ti=&ag=wards&dt[tpb]=%s&dt[wd;]=1,2,3,4,5,6,7&dt[dr][sd]=2016-09-%s&dt[dr][ed]=2016-09-%s&cd=&lat.=28.6203201&lng.=77.1405719&z.=13&sa;=&sdn=&ta;=&tdn='%(i,t,date_me_temp,date_me_temp)
 
                    PROXY = choice(proxy)
                    chrome_options = webdriver.ChromeOptions()
                    download_dir = '/home/priyank/isb/uber'
                    prefs = {"download.default_directory":download_dir}
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument("download.default_directory=%s" % download_dir)
                    chrome_options.add_argument('--proxy-server=%s' % PROXY)

                    driver = webdriver.Chrome(executable_path='./chromedriver')
                    driver.get(url)

                    # time.sleep(20)
                    # wait.until(ExpectedConditions.elementToBeClickable(By.xpath('/html/body/div[6]/div[2]/div/div[2]/div/div[1]/button')));
                    # wait.until(EC.element_to_be_selected(driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[1]")))
                    wait = WebDriverWait(driver, 10)
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.fx.ho.cm.cl.ck.cn.hp > div.ai.ay.bb.by.hv.fw.gi > div > div.i2.i3.dg.ef")))

                    skip = driver.find_element_by_css_selector('body > div.fx.ho.cm.cl.ck.cn.hp > div.ai.ay.bb.by.hv.fw.gi > div > div.i5.i6.i7 > div > div.ai.aw > button')

                    skip.click()

                    download_button = driver.find_element_by_xpath('//*[@id="bui-3__anchor"]')
                    download_button.click()
                    
 
                    if check_exists_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/button[1]'):
                        download_file = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/button[1]')
                        
                    elif check_exists_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div/button[1]'):
                        download_file = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div/button[1]')
 
                    download_file.click()
                    time.sleep(1)
                    driver.quit()

                    # break
                    # /html/body/div[5]/div[2]/div/div[2]/div/div[1]/button
                except Exception as e:
                	# driver.quit()
                    print("i,date_me,t : ",i,date_me_temp,t)
                    print('\n')
                    print(e)
        # break1