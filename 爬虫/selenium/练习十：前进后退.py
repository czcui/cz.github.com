from selenium import webdriver
import time

browser = webdriver.Chrome()
url1 = 'https://www.taobao.com/'
url2 = 'https://www.baidu.com/'
url3 = 'https://www.zhihu.com/'
browser.get(url1)
browser.get(url2)
browser.get(url3)

browser.back()
time.sleep(2)
browser.forward() 