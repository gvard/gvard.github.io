""" Python module with functions and data, useful for operating
with BeautifulSoup
"""

import urllib.request
from urllib.request import Request

from bs4 import BeautifulSoup


HEAD_HEAD = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <meta name="description" content="Подборка статистических данных в области астрономии, астрофизики и космонавтики. Файл сгенерирован автоматически.">
"""
HEAD_TAIL = """</head>
"""

TAIL = """</body>
</html>"""

def mk_head(title, style="style.css", script="script.js"):
    """Make an html code with head element"""
    STYLE = ""
    if style:
        STYLE = f'  <link rel="stylesheet" href="{style}">\n'
    SCRIPT = ""
    if script:
        SCRIPT = f'  <script src="{script}"></script>\n'
    return HEAD_HEAD + f'  <title>{title}</title>\n' + STYLE + SCRIPT + HEAD_TAIL

def get_soup_Request(url):
    """get url, return BeautifulSoup object."""
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    return BeautifulSoup(html, 'html.parser')

def get_soup(url):
    """get url, return BeautifulSoup object."""
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')
