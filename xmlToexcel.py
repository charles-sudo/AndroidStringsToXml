#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
# Android国际化： 将xml文件中对应的字符串解析到excel中
# python xmlToexcel.py /Users/charles/livewallpaper/app/src/main/res
import sys
import os
import xml.dom.minidom
from xlwt import Workbook

path = sys.argv[1] #文件夹目录
#遍历文件夹
values_list = [] # 存储多语言文件地址
language_list = ["id"] # 存储多语言文件地址
directory = os.walk(path)  

for path,dir_list,file_list in directory:
    for folder_name in dir_list:
        if "values-v21" in folder_name:
            continue
        if "values-sw" in folder_name:
            continue
        if "values" in folder_name:
            if folder_name[7:] == "":
                language_list.append("en")
            else:
                language_list.append(folder_name[7:])
            values_list.append(os.path.join(path, folder_name,"strings.xml"))

 
#新建一个workbook
book = Workbook(encoding='utf-8')
sheet = book.add_sheet('Android')

# 首行
for index, language_code in enumerate(language_list):
    sheet.write(0, index, language_code)
 
#打开xml
for index, values_flie in enumerate(values_list):
    xmldoc = xml.dom.minidom.parse(values_flie)
    code = xmldoc.getElementsByTagName('string')
    row = 1
    for node in code:
        for item in node.childNodes:
            if index == 0:
                sheet.write(row, index, node.getAttribute('name'))
            sheet.write(row, index + 1, item.data)
        row = row+1
# 保存workbook
book.save('strings.xls')
print("done!~")