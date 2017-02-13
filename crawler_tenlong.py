#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml

# send get request and get reposoe.
# res = requests.get('https://www.tenlong.com.tw/items/7121275074')
res = requests.get('https://www.tenlong.com.tw/items/9864760807?item_id=1021576')

soup = BeautifulSoup(res.text, 'lxml')

# print soup.prettify()

# get book info.
book_info = soup.find(id='item_info')
print book_info

# get book context.
book_context = ''
for context in soup.find_all('p'):
  book_context += str(context)
# print book_context

remove_order_element     = book_context.replace('<p>\n\t下單後立即進貨\n</p>', '')
remove_shipment_element  = remove_order_element.replace('<p>\n\t立即進貨\n</p>', '')
remove_copyright_element = remove_shipment_element.replace('<p>Copyright ® 2016 Tenlong Computer Book Co, Ltd. All rights reserved.</p>', '')
remove_last2_p = remove_copyright_element.replace('<p>\n<a href="/faq">客服與FAQ</a> |\n\t\t<a href="/about">連絡我們</a> |\n\t\t<a href="/privacy">隱私權政策</a> |\n\t\t<a href="/terms">服務條款</a>\n</p>', '')
remove_last3_p = remove_last2_p.replace('<p>天瓏提供<strong>超商代收！</strong></p>', '')

book_context = remove_last3_p
print book_context

