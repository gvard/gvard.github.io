from bs4 import BeautifulSoup
import urllib.request
import os


HEAD = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Космонавтика: статистика</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
"""
TAIL = """
</body>
</html>
"""
N2YO_URL = "https://www.n2yo.com/"
SPACEFLIGHT_URL = "https://www.worldspaceflight.com/bios/stats.php"
SPACEFLIGHT1_URL = "https://www.worldspaceflight.com/bios/stats1.php"

def get_soup(url):
    """get url, return BeautifulSoup object"""
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')

def get_n2yo(soup):
    return int(soup.findAll("span", {"style": "color:#d50000"})[0].text)


soup = get_soup(N2YO_URL)
number_tracking_objects = get_n2yo(soup)
N2_STATS_HTML = f"""<h2>Отслеживаемые объекты в околоземном пространстве</h2>
<p><a href="{N2YO_URL}">Satellite tracking and predictions</a></p>
<p>Отслеживается <b>{number_tracking_objects}</b> объектов.</p>
"""


def get_spaceflight(soup):
    ps = soup.findAll('p')[3:7]
    manyr_num = float(ps[0].text.split()[-2])
    usaf_num = int(ps[1].text.split()[-1])
    fai_num = int(ps[2].text.split()[-1])
    cosmonaut_num = int(ps[3].text.split()[-1])
    for p in ps:
      print(p)
    return manyr_num, usaf_num, fai_num, cosmonaut_num

soup = get_soup(SPACEFLIGHT_URL)
MANYR_NUM, USAF_NUM, FAI_NUM, COSMONAUT_NUM = get_spaceflight(soup)
SPACEFLIGHT_HTML = f"""<h2>Пилотируемая космонавтика</h2>
<p><a href="{SPACEFLIGHT_URL}">Статистика</a> <a href="{SPACEFLIGHT1_URL}">пилотируемой космонавтики</a>
<ul>
<li>Космонавтов (людей, побывавших в космосе и совершивших орбитальный полет) &ndash; <b>{COSMONAUT_NUM}</b></li>
<li>Людей, побывавших в космосе (согласно определению Международной федерации аэронавтики, при высоте полета более 100 км) &ndash; <b>{FAI_NUM}</b></li>
<li>Людей, побывавших в космосе (согласно классификации ВВС США, при высоте полета более 80 км 467 м) &ndash; <b>{USAF_NUM}</b></li>
<li>Время, проведенное людьми в космосе &ndash; свыше <b>{MANYR_NUM}</b> человеко-лет.</li>
</ul>
"""

with open(os.path.join(os.pardir, 'cosm', 'stats.html'), 'w', encoding="utf8") as handle:
    print(HEAD + SPACEFLIGHT_HTML + N2_STATS_HTML + TAIL, file=handle)
