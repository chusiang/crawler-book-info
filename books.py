#!/usr/bin/env python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from jinja2 import Template
import logging
import lxml
import requests
import sys
import git
import urllib3

# disable ssl warn message.
urllib3.disable_warnings()
logging.captureWarnings(True)

def get_data():
  try:
    arg = sys.argv[1]

    if arg.isdigit():
      book_url = str('https://www.books.com.tw/products/' + arg)
    else:
      book_url = str(arg)

    # send get request and get reposoe.
    res = requests.get(book_url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup, book_url

  except Exception as e:
    print(e)

def parser_book_title(data):
  book_title = data.title
  book_title = str(book_title).replace('<title>博客來-', '').replace('</title>', '')
  return book_title

def parser_book_full_title(data):
  parser_book_full_title = data.find_all('div', class_='mod type02_p002 clearfix')
  book_full_title = str(parser_book_full_title[0])
  book_full_title = book_full_title.replace('<div class="mod type02_p002 clearfix">', '')
  book_full_title = book_full_title.replace('</div>', '')
  return book_full_title

def parser_book_cover(data):
  parser_book_cover = data.find_all('img', class_='cover M201106_0_getTakelook_P00a400020052_image_wrap')
  book_cover = str(parser_book_cover[0]).replace('//im2.book.com.tw/image/getImage?i=', '')
  book_cover = book_cover.split('https')
  book_cover = 'https' + book_cover[1]
  book_cover = book_cover.split('.jpg')
  book_cover = book_cover[0] + '.jpg'
  return book_cover

def parser_book_info1(data):
  parser_book_info = data.find_all('div', class_='type02_p003 clearfix')
  book_info = str(parser_book_info[0]).replace('<div class="type02_p003 clearfix">', '')
  book_info = book_info.replace('<span class="arrow"></span>', '')

  book_info = book_info.replace('', '')
  book_info = book_info.replace('<h4>已追蹤作者：<strong class="edit">[ <a href="" id="editTrace">修改</a> ]</strong></h4>', '')
  book_info = book_info.replace('<ul id="list_traced"></ul>', '')
  book_info = book_info.replace('<ul class="list_trace" id="list_trace"></ul>', '')

  book_info = book_info.replace('<a class="type02_btn09" href="javascript:saveTrace();">確定</a>', '')
  book_info = book_info.replace('<a class="type02_btn09" href="javascript:cancelTrace();">取消</a>', '')

  book_info = book_info.replace('     <a class="type02_btn02" href="" id="trace_btn1"><span><span class="trace_txt"> </span></span></a>', '')
  book_info = book_info.replace('<a href="//www.books.com.tw/activity/2015/06/trace/index.html#author" target="_blank" title="新功能介紹"><cite class="help">新功能介紹</cite></a>', '')
  book_info = book_info.replace('     <a class="type02_btn02" href="" id="trace_btn2"><span><span class="trace_txt"> </span></span></a>', '')
  book_info = book_info.replace('<a href="//www.books.com.tw/activity/2015/06/trace/index.html#publisher" target="_blank" title="新功能介紹"><cite class="help">新功能介紹</cite></a>', '')
  book_info = book_info.replace('</ul></div>', '')
  return book_info

def parser_book_price(data):
  parser_book_price = data.find_all('ul', class_='price')
  book_price = str(parser_book_price[0]).replace('<ul class="price">', '')
  book_price = book_price.replace('</ul>', '')
  return book_price

def parser_book_info2(data):
  parser_book_info = data.find_all('div', class_='mod_b type02_m058 clearfix')
  book_info = str(parser_book_info[0]).replace('<div class="mod_b type02_m058 clearfix">', '')
  book_info = book_info.replace('<a name="P00a400020016"> </a>', '')
  book_info = book_info.replace('<h3>詳細資料</h3>', '')
  book_info = book_info.replace('<div class="bd">', '')
  book_info = book_info.replace('<ul>', '')
  book_info = book_info.replace('                          </li></ul>', '</li>')
  book_info = book_info.replace('<ul class="sort">', '')
  book_info = book_info.replace('</div></div>', '')
  return book_info

def parser_book_desc(data):
  parser_item_desc = data.find_all('div', class_='bd')
  book_desc = str(parser_item_desc[0])
  return book_desc

def parser_book_author(data):
  parser_item_desc = data.find_all('div', class_='bd')
  try:
    book_author = str(parser_item_desc[1]).replace('作者簡介<br/>', '')
    book_author = book_author.replace('<strong>\n<br/>', '<strong>')
    #book_author = book_author.replace(r'\r\n','')
  except Exception as e:
    print("'Author' is not found.")
    book_author = "Not found."
  finally:
    return book_author

def parser_book_outline(data):
  parser_item_desc = data.find_all('div', class_='bd')
  try:
    book_outline = parser_item_desc[2]
  except Exception as e:
    print("'Outline' is not found.")
    book_outline = "Not found."
  finally:
    return book_outline

def git_sha():
  git_repo = git.Repo(search_parent_directories=True)
  git_sha = git_repo.head.object.hexsha
  short_git_sha = git_sha[:8]
  return short_git_sha

def main():
  try:

    # Template with Jinja2
    template = Template('''\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title> {{ title }} </title>
  </head>
  <body>
    <p>
      Buy:
      <ul>
        <li> <a href="{{ url }}" target="_blank">博客來</a> </li>
      </ul>
    </p>
    <hr>
    {{ full_title }}
    <p>
      <img src="{{ cover }}"/>
    </p>

    {{ info1 }}
    {{ price }}
    {{ info2 }}

    <h2>商品描述</h2>
    {{ desc }}

    <h2>作者簡介</h2>
    {{ author }}

    <h2>目錄大綱</h2>
    {{ outline }}

    <footer style="text-align: center;">
      Power by <a href="https://github.com/chusiang/crawler-book-info" target="_blank">chusiang/crawler-book-info</a> ({{ version }}).
      <hr>
    </footer>
  </body>
</html>
''')

    # Get data.
    data = get_data()

    # Parser.
    book_title = parser_book_title(data[0])
    book_url = data[1]
    book_full_title = parser_book_full_title(data[0])
    book_cover = parser_book_cover(data[0])
    book_info1 = parser_book_info1(data[0])
    book_price = parser_book_price(data[0])
    book_info2 = parser_book_info2(data[0])
    book_desc = parser_book_desc(data[0])
    book_author = parser_book_author(data[0])
    book_outline = parser_book_outline(data[0])
    project_version = git_sha()

    # Mapping the parser data to template.
    result = template.render(
        title=book_title,
        url=book_url,
        full_title=book_full_title,
        cover=book_cover,
        info1=book_info1,
        price=book_price,
        info2=book_info2,
        desc=book_desc,
        author=book_author,
        outline=book_outline,
        version=project_version
    )

    # Write to HTML file.
    f = open('index.html', 'w')
    f.write(result)
    f.close()

  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()
