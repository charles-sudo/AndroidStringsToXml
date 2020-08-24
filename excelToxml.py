#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
#Android国际化： 将excel中的内容转化到xml中
# python excelToxml.py /Users/sunzhiqiang/Desktop/tools/strings.xls
import codecs
import sys
import os
from xml.dom import minidom
from xlrd import open_workbook


#创建文件夹
os.mkdir("values", 0o777);
os.chdir("values")

#打开excel
path_file = sys.argv[1] #文件夹目录
workbook = open_workbook(path_file)
table = workbook.sheets()[0]

values=[]
row =table.row_values(0)
for i in range(1,table.ncols):
	values.append(row[i])
	
for index,value in enumerate(values):
	#新建xml
	doc = minidom.Document()
	#添加根元素
	resources = doc.createElement('resources')
	doc.appendChild(resources)
	#添加字符串
	for sheet in workbook.sheets():
		for row_index in range(1,sheet.nrows):
			result_placeholder = sheet.cell(row_index,0).value
			result_content = sheet.cell(row_index,1+index).value
			#新建一个文本元素
			text_element = doc.createElement('string')
			text_element.setAttribute('name', result_placeholder)
			text_element.appendChild(doc.createTextNode(result_content))
			resources.appendChild(text_element)
		f = codecs.open(value+'_strings.xml','w',encoding='utf-8')
		f.write(doc.toprettyxml(indent='    '))
		f.close()
print("done!~")