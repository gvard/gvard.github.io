"""Python script for genererating an html page
with rocket launches statistics. Data sources:
https://planet4589.org/space/gcat/web/launch/count.html
https://planet4589.org/space/gcat/web/launch/ldes.html
"""

import os
import urllib.request

from beautifulsoup_supply import TAIL, mk_head, get_soup


DEBUG = False
GCAT_URL = 'https://planet4589.org/space/gcat/web/launch/count.html'


def get_sd(soup, debug=False):
    """Parse html, get statistics of rocket launches."""
    pretxt = soup.findAll("pre")[1].text.splitlines()[1:]
    allnums = [line.split()[-1] for line in pretxt]
    return allnums


soup = get_soup(GCAT_URL)
AN = get_sd(soup, debug=DEBUG)

HEAD = mk_head("Статистика запусков ракет", style="stats.css")
BODY = f"""<body">
<div id="stats" class="container show">
  <h1 id="header">Статистика запусков ракет: апрель 2021 г.</h1>
  <div class="list">
  <ul>
    <li>Всего орбитальных запусков: <span class="yellow">{AN[0]}</span></li>
    <li>Вне каталога: <span class="yellow">{AN[1]}</span></li>
    <li>Неудачных попыток: <span class="yellow">{AN[2]}</span></li>
    <li>Суборбитальных пусков: <span class="yellow">{AN[3]}</span></li>
    <li>Мезосферных пусков: <span class="yellow">{AN[4]}</span></li>
    <li>Эндоатмосферных пусков: <span class="yellow">{AN[5]}</span></li>
    <li>Взрывов стартового стола: <span class="yellow">{AN[6]}</span></li>
    <li>Всего записей в каталоге: <span class="yellow">{AN[7]}</span></li>
  </ul>
  </div>
  <div id="footer">
    <h2>Центр Астрономического и&nbsp;космического образования</h2>
  </div>
</div>
"""
with open(os.path.join(os.pardir, 'cosm', 'launches', 'index.html'), 'w', encoding="utf8") as handle:
    print(HEAD + BODY + TAIL, file=handle)