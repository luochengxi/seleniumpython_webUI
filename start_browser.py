#!/usr/bin/env python3
#-*-coding:utf-8-*-
from  selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import  random
from PIL import Image
from ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()
#driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
driver.set_window_size(1920,1080)
print(driver.get_window_size(windowHandle='current'))
wait = ui.WebDriverWait(driver,10)
wait.until(lambda driver:driver.find_element_by_id("getcode_num"))
print(EC.title_contains("注册"))
# 提取图片
driver.save_screenshot("E:\python\mukeweb\imooc.png")
code_element = driver.find_element_by_id("getcode_num")
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
low = code_element.size['height']+top
im = Image.open("E:\python\mukeweb\imooc.png")
img = im.crop((int(left*1.5),int(top*1.5),int(right*1.5),int(low*1.5)))
img.save("E:\python\mukeweb\imooc1.png")
#分析验证码图片
image = Image.open("E:\python\mukeweb\imooc1.png")
r = ShowapiRequest("http://route.showapi.com/184-4","101479","f42a5641ef4648a381829e7c4ddcf197" )
r.addBodyPara("typeId","35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"E:\python\mukeweb\imooc1.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
#元素定位
email_element = driver.find_element_by_id("register_email")
driver.find_element_by_id("register_email").send_keys("638833333@163.com")
driver.find_element_by_id("register_nickname").send_keys("mushishi")
driver.find_element_by_name("password").send_keys("jianghaixia")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys(text)
time.sleep(10)
driver.close()

'''user_info = random.sample('1234567890abcdefg',5)
for i in range(5):
    user_email = user_info+'@163.com'
    print(user_email)
element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME,"controls")
EC.visibility_of_element_located(locator)
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))

print(email_element.get_attribute("placeholder"))
email_element.send_keys("hello@163.com")
print(email_element.get_attribute("value"))'''





