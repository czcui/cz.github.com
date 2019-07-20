#获取节点属性
from selenium import  webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))


#获取节点内容
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

#获取id、位置、标签名和大小
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)              #获取节点id
print(input.location)        #获取节点在页面中的相对位置
print(input.tag_name)        #获取标签名称
print(input.size)            #获取宽高