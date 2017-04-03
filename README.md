# Crawler Book Info

A sample crawler for quick parser the book information.

## Usage

1. create virtualenv.

       [ jonny@xenial ~/vcs/crawler-book-outline ]
       $ virtualenv .venv

1. Enter the virtualenv.

       [ jonny@xenial ~/vcs/crawler-book-outline ]
       $ . .venv/bin/activate

1. Install packages with pip.

       (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
       $ pip install -r requirements.txt

1. Run crawler with **ISBN-13** args.

       (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
       $ python crawler_tenlong.py 9781491915325

1. View result.

       (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
       $ firefox index.html

    ![ansiblebook](https://cloud.githubusercontent.com/assets/219066/24584670/8ffb25f2-17a7-11e7-913a-2f570f773a66.png)

1. We can see the https://www.tenlong.com.tw/products/9781491915325, it is clean, now.
1. Finally, we can clip the information to Evernote with [Evernote Web Clipper](https://evernote.com/intl/zh-tw/webclipper/).

## Docker container

Now, the **Evernote Web Clipper** is not support local files, so we can clip it with Nginx.

    $ docker run --name nginx -v $TARGET/crawler-book-info:/usr/share/nginx/html -p 80:80 -d nginx

## License

Copyright (c) chusiang from 2017 under the MIT license.

