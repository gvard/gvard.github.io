import urllib.request

from bs4 import BeautifulSoup


URL = "https://minorplanetcenter.net/mpc/summary"

html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, 'html.parser')

td_nums = soup.findAll("td", {"class": "cj"})
td_nums_mono = soup.findAll("td", {"class": "rj-mono"})

BODY = f'''<ul>
  <li>В Солнечной системе <span>{int(td_nums[1].text)}</span> объектов
  <li>Более <span>{int(td_nums[4].text)}</span> комет
  <li><span>{int(td_nums_mono[6].text)}</span> астероидов основного пояса
  <li><span>{int(td_nums_mono[9].text)}</span> объектов за орбитой Нептуна
  <li><span>{int(td_nums_mono[10].text)}</span> карликовых планет
  <li><span>{int(td_nums_mono[11].text)}</span> околоземных астероидов
</ul>'''

HEAD = '''<!DOCTYPE html>
<html lang="ru">
  <meta charset="UTF-8">
  <title>Статистика Солнечной системы</title>
'''
STYLE = '''  <style>
  body {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 2.2em;
    text-shadow: black 1px 1px 0, black -1px -1px 0,
                 black -1px 1px 0, black 1px -1px 0;
    color: white;
    height: 100vh;
    margin: 20px 150px 0 4%;    
    background-image: url('https://gvard.github.io/solarsystem/images/back.jpg');
    background-size: cover;
    background-position: center;
  }
  span {
    color: gold;
  }
  </style>
'''
with open('index.html', 'w', encoding="utf8") as html_file:
    print(HEAD + STYLE + BODY, file=html_file)

