import urllib.request

from bs4 import BeautifulSoup


HEAD_HEAD = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
"""
HEAD_TAIL = """
  <link rel="stylesheet" href="style.css">
</head>
<body>
"""

TAIL = """
</body>
</html>
"""

def mk_head(title):
    return HEAD_HEAD + f"  <title>{title}</title>" + HEAD_TAIL

def get_soup(url):
    """get url, return BeautifulSoup object."""
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')
