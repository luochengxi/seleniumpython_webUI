#!/usr/bin/env python3
#-*-coding:utf-8-*-
from selenium import webdriver
from find_element import FindElement
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    def get_driver(self,url,i):
        if i==1:
            driver = webdriver.Chrome()
        elif i==2:
            driver = webdriver.Edge()
        else:
            driver = webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        return driver
        # 定位用户信息，获取element
    def get_user_element(self, key):
        # find_element = FindElement(self.driver)
        # user_element = find_element.get_element(key)
        user_element=FindElement(self.driver).get_element(key)
        return user_element
     #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)
    # 获取随机数
    def get_range_user(self):
        use_name = random.sample('1234567890ngddd', 8)
        return use_name
    # 获取验证码
    def get_code_image(self,file_name):
        self.driver.set_window_size(1920, 1080)
        self.driver.save_screenshot(file_name)
        code_element =self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        low = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((int(left * 1.5), int(top * 1.5), int(right * 1.5), int(low * 1.5)))
        img.save(file_name)
    # 分析验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "101479", "f42a5641ef4648a381829e7c4ddcf197")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text
    def main(self):
        use_email = ''.join(self.get_range_user()) + '@163.com'
        file_name = "E:\python\mukeweb\picture\Image\mukewang1.png"
        self.send_user_info('use_email_info',use_email)
        self.send_user_info('use_name_info',self.get_range_user())
        self.send_user_info('password','11111111')
        text1 = self.code_online(file_name)
        self.send_user_info('code_text',text1)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('code_text_error')
        if code_error ==None:
            print("注册成功")
        else:
            self.driver.save_screenshot("E:\python\mukeweb\picture\Image\code_error.png")
        time.sleep(10)
        self.driver.close()
if  __name__ == '__main__':
    for i in range(3):
        register_func = RegisterFunction('http://www.5itest.cn/register',i)
        register_func.main()

