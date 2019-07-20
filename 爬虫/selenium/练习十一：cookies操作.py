from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)

print(browser.get_cookies())
browser.add_cookie({'name':'cz', 'domain':'www.zhihu.com', 'value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
