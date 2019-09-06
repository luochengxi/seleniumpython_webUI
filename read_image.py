#!/usr/bin/env python3
#-*-coding:utf-8-*-
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
image = Image.open("E:\python\mukeweb\imooc1.png")
#text = pytesseract.image_to_string(image)
#print(text)
r = ShowapiRequest("http://route.showapi.com/184-4","101479","f42a5641ef4648a381829e7c4ddcf197" )
r.addBodyPara("typeId","35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"E:\python\mukeweb\imooc1.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息