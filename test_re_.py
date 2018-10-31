# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: test_re_.py
@time: 2018/10/31
"""
import re

source_url = ' https://movie.douban.com/top250?start=25&filter='

# x =re.findall(r'.*start=(\d)&filter=.*',source_url)
now_page = re.findall(r'.*start=(\d+)&filter.*',source_url)
print(now_page)
next_url = re.sub('start=(\d)&filter+',str(int(now_page[0])+25),source_url)
print(next_url)