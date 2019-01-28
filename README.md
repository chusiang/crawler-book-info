# Crawler Book Info

[![Docker Hub](https://img.shields.io/badge/python-3.7-blue.svg)](https://hub.docker.com/r/chusiang/crawler-book-info/)
[![Docker Hub](https://img.shields.io/badge/docker-chusiang%2Fcrawler--book--info-blue.svg)](https://hub.docker.com/r/chusiang/crawler-book-info/) [![Download Size](https://images.microbadger.com/badges/image/chusiang/crawler-book-info.svg)](https://microbadger.com/images/chusiang/crawler-book-info "Get your own image badge on microbadger.com") [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

A sample crawler for quick parser some books information.

## Initialization

1. Install the virtualenv.

    ```
    [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ sudo pip3 install virtualenv
    ```

1. create virtualenv.

    ```
    [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ virtualenv -p python3 .venv
    ```

1. Enter the virtualenv.

    ```
    [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ . .venv/bin/activate
    ```

1. Install packages with pip.

    ```
    (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ pip3 install -r requirements.txt
    ```

## Usage

### tenlong.com.tw

1. Run crawler with **ISBN-13**.

    ```
    (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ python3 tenlong.py 9781491915325
    ```

1. (option) Run crawler via make.

    ```
    (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ make telong 9781491915325
    ```

### books.com.tw

1. Run crawler with **url**.

    ```
    (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ python3 books.py https://www.books.com.tw/products/0010810939
    ```

1. Run crawler with **product number**.

    ```
    (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ python3 books.py 0010810939
    ```

> Not support the **ISBN-13** args yet on books.com.tw.

### View Result

1. Open html via Firefox on GNU/Linux.

    ```
    (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ firefox index.html
    ```

    ![ansiblebook](https://cloud.githubusercontent.com/assets/219066/24584670/8ffb25f2-17a7-11e7-913a-2f570f773a66.png)

1. We can see the https://www.tenlong.com.tw/products/9781491915325, it is clean, now.

### Run local Nginx for Evernote Web Clipper

The **Evernote Web Clipper** is not support local files, so we can clip it with Nginx.

1. Run Nginx container.

    ```
    $ docker run --name nginx -v "$(pwd)":/usr/share/nginx/html/ -p 80:80 -d nginx
    ```

1. Open html via Firefox on GNU/Linux.

    ```
    (.venv) [ jonny@xenial ~/vcs/crawler-book-outline ]
    $ firefox http://localhost
    ```

1. (option) Run Nginx container via make.

    ```
    $ make run_nginx_docker
    ```

1. (option) Open web via make.

    ```
    $ make review_serve
    ```

1. Finally, we can clip the information to Evernote with [Evernote Web Clipper](https://evernote.com/intl/zh-tw/webclipper/).

## License

Copyright (c) chusiang from 2017-2019 under the MIT license.
