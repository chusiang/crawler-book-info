#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml
import urllib3
import logging

# disable ssl warn message.
urllib3.disable_warnings()
logging.captureWarnings(True)

def main():
  try:
    # send get request and get reposoe.
    res = requests.get('https://www.tenlong.com.tw/items/7121275074')
    
    soup = BeautifulSoup(res.text, 'lxml')
    
    # get book info.
    book_info = soup.find(id='item_info')
    print book_info
    
    # get book context.
    book_context = ''
    for context in soup.find_all('p'):
      book_context += str(context)
    
    # remove the extra text.
    remove_order_element     = book_context.replace('<p>\n\t下單後立即進貨\n</p>', '')
    remove_shipment_element  = remove_order_element.replace('<p>\n\t立即出貨\n</p>', '')
    remove_copyright_element = remove_shipment_element.replace('<p>Copyright ® 2016 Tenlong Computer Book Co, Ltd. All rights reserved.</p>', '')
    remove_footer = remove_copyright_element.replace('<p>\n<a href="/faq">客服與FAQ</a> |\n\t\t<a href="/about">連絡我們</a> |\n\t\t<a href="/privacy">隱私權政策</a> |\n\t\t<a href="/terms">服務條款</a>\n</p>', '')
    book_context = remove_footer.replace('<p>天瓏提供<strong>超商代收！</strong></p>', '')
    
    print book_context

  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()

