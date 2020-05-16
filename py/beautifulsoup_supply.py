import urllib.request

from bs4 import BeautifulSoup


HEAD_HEAD = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <meta name="description" content="Подборка статистических данных в области астрономии, астрофизике и космонавтике. Файл сгенерирован автоматически.">
"""
HEAD_TAIL = """</head>
"""

TAIL = """</body>
</html>"""

def mk_head(title, style="style.css", script="script.js"):
    STYLE = ""
    if style:
        STYLE = f'  <link rel="stylesheet" href="{style}">\n'
    SCRIPT = ""
    if script:
        SCRIPT = f'  <script src="{script}"></script>\n'
    return HEAD_HEAD + f'  <title>{title}</title>\n' + STYLE + SCRIPT + HEAD_TAIL

def get_soup(url):
    """get url, return BeautifulSoup object."""
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')
