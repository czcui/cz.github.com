from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get( 'https://www.zhihu.com/explore')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.baidu.com')