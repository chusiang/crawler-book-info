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
        $ firefox result.html

    ![ansiblebook](https://cloud.githubusercontent.com/assets/219066/24584670/8ffb25f2-17a7-11e7-913a-2f570f773a66.png)

