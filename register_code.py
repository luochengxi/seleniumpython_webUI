#!/usr/bin/env python3
#-*-coding:utf-8-*-
from selenium import webdriver
import time
import random
from PIL import Image
drive = webdriver.Chrome()
from ShowapiRequest import ShowapiRequest
#浏览器初始化
def driver_init():
    drive.get("http://www.5itest.cn/register")
    drive.maximize_window()
    time.sleep(5)
#获取element
def get_element(id):
    element = drive.find_element_by_id(id)
    return element
#获取随机数
def get_range_user():
    use_name_info = random.sample('1234567890ngddd',8)
    return use_name_info
#获取验证码
def get_code_image(file_name):
    drive.set_window_size(1920, 1080)
    drive.save_screenshot(file_name)
    code_element = drive.find_element_by_id("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    low = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((int(left * 1.5), int(top * 1.5), int(right * 1.5), int(low * 1.5)))
    img.save(file_name)
#分析验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "101479", "f42a5641ef4648a381829e7c4ddcf197")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name)
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text
#运行主程序
def run_main():
    driver_init()
    use_email_info =''.join(get_range_user()) + '@163.com'
    file_name ="E:\python\mukeweb\picture\Image\mukewang1.png"
    get_element("register_email").send_keys(use_email_info)
    get_element("register_nickname").send_keys(get_range_user())
    get_element("register_password").send_keys("11111111")
    get_code_image(file_name)
    get_element("captcha_code").send_keys(code_online(file_name))
    get_element("register-btn").click()
    time.sleep(10)
    drive.close()
run_main()
