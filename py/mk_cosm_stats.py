# -*- coding: utf-8 -*-
"""Python script for genererating an html page
with manned spaceflight statistics.
"""

import os
import ssl
import json
import urllib.request

from beautifulsoup_supply import TAIL, mk_head, get_soup

if not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(
    ssl, "_create_unverified_context", None
):
    ssl._create_default_https_context = ssl._create_unverified_context

DEBUG = False
HEAD = mk_head("Космонавтика: статистика", style="../compact.css", script="") + "<body>\n"
N2YO_URL = "https://www.n2yo.com/"
SPACEFLIGHT_URL = "https://www.worldspaceflight.com/bios/stats.php"
SPACEFLIGHT1_URL = "https://www.worldspaceflight.com/bios/stats1.php"
CURRENTLY_IN_SPACE_URL = "https://www.worldspaceflight.com/bios/currentlyinspace.php"
FLIGHTLIST_URL = "https://www.worldspaceflight.com/bios/sequence.php"
SPACE_MISSIONS_URL = "https://planet4589.org/space/astro/lists/missions.html"
NANOSATS_URL = "https://www.nanosats.eu/"
ASTROS_URL = "http://api.open-notify.org/astros.json"


def ending(cosm_num):
    if cosm_num in (2, 3, 4):
        return "а"
    elif 5 <= cosm_num <= 20:
        return "ов"
    elif cosm_num == 1:
        return ""


def get_n2yo(soup):
    return int(soup.findAll("span", {"style": "color:#d50000"})[0].text)


def get_nanosats(soup):
    date = soup.findAll("h3")[-1].b.text.split("of")[1].strip()
    lis = soup.find("ul", {"class": "ultwo center-align"}).findAll("li")
    return date, lis


soup = get_soup(NANOSATS_URL)
DATE, LIS = get_nanosats(soup)
NANOSATS_HTML = f"""<h2><a href="https://en.wikipedia.org/wiki/Small_satellite#Nanosatellites" target="_blank" rel="noopener noreferrer">Наноспутники</a></h2>
<p><a href="{NANOSATS_URL}">База данных наноспутников</a> – до 10 кг для нестандартных типов и до 27U (30–40 кг) для
<a href="https://www.nanosats.eu/cubesat">кубсатов</a>. Последнее обновление: {DATE}.</p>
<ul>
"""
for li in LIS:
    NANOSATS_HTML += str(li) + "\n"
NANOSATS_HTML += "</ul>\n"

soup = get_soup(N2YO_URL)
number_tracking_objects = get_n2yo(soup)
N2_STATS_HTML = f"""<h2>Отслеживаемые объекты в околоземном пространстве</h2>
<p><a href="{N2YO_URL}">Satellite tracking and predictions</a></p>
<p>Отслеживается <b>{number_tracking_objects}</b> объектов.</p>
"""


def get_flightlist(soup):
    """Get Sequential Flight List
    Note: int(last[0].text) == len(lines)
    """
    lines = soup.findAll("div", {"class": "row"})
    last = lines[-1].findAll("div", {"class": "col"})
    return last[0].text, last[1].text, last[2].text


soup = get_soup(FLIGHTLIST_URL)
FLIGHT_NUM, LASTFLIGHT_NAME, LASTFLIGHT_DATE = get_flightlist(soup)
soup = get_soup(SPACE_MISSIONS_URL)
flights_list = soup.findAll("pre")[1].text.splitlines()[1:]
flights_num = 0
for line in flights_list:
    if line and line.startswith("H0"):
        flights_num += 1


def get_spaceflight(soup):
    ps = soup.findAll("p")[3:8]
    manyr_num = float(ps[0].text.split()[-2])
    usaf_num = int(ps[2].text.split()[-1])
    fai_num = int(ps[3].text.split()[-1])
    cosmonaut_num = int(ps[4].text.split()[-1])
    return manyr_num, usaf_num, fai_num, cosmonaut_num


soup = get_soup(SPACEFLIGHT_URL)
MANYR_NUM, USAF_NUM, FAI_NUM, COSMONAUT_NUM = get_spaceflight(soup)

astros_obj = urllib.request.urlopen(ASTROS_URL)
astros = json.load(astros_obj)
if DEBUG:
    print("URL:", astros_obj.geturl(), "HTTP code:", astros_obj.getcode())

ASTROS_LST = astros.get("people")
ASTROS_STR = ", ".join([astr.get("name") for astr in ASTROS_LST])

SPACEFLIGHT_HTML = f"""<h2>Пилотируемая космонавтика</h2>
<p><a href="{SPACEFLIGHT_URL}">Статистика</a> <a href="{SPACEFLIGHT1_URL}">пилотируемой космонавтики</a>
<ul>
<li>Космонавтов (людей, побывавших в космосе и совершивших орбитальный полет)
– <b>{COSMONAUT_NUM}</b></li>
<li>Людей, побывавших в космосе (согласно определению Международной федерации аэронавтики, при высоте полета более 100 км)
– <b>{FAI_NUM}</b></li>
<li>Людей, побывавших в космосе (согласно классификации ВВС США, при высоте полета более 80 км 467 м)
– <b>{USAF_NUM}</b></li>
<li>Всего космических полетов – <b>{FLIGHT_NUM}</b>, следуя определению ВВС США
– <b>{flights_num}</b></li>
<li>Последний – {LASTFLIGHT_NAME}, {LASTFLIGHT_DATE}</li>
<li>Время, проведенное людьми в космосе – свыше <b>{MANYR_NUM}</b> человеко-лет.</li>
<li>В космосе <b>{len(ASTROS_LST)}</b> космонавт{ending(len(ASTROS_LST))}: {ASTROS_STR}.</li>
</ul>
"""

with open(os.path.join(os.pardir, "cosm", "stats.html"), "w", encoding="utf8") as fl:
    print(HEAD + SPACEFLIGHT_HTML + N2_STATS_HTML + NANOSATS_HTML + TAIL, file=fl)

HEAD = mk_head("Статистика пилотируемой космонавтики", style="stats.css", script="../../stats.js")
BODY = f"""<body onload="mkHeader()">
<div id="stats" class="container show">
  <h1 id="header"></h1>
  <div class="list">
  <ul>
    <li>Совершили орбитальный полет и&nbsp;они космонавты: <span class="yellow">{COSMONAUT_NUM}</span></li>
    <li>Побывали в космосе и&nbsp;они астронавты: <span class="yellow">{FAI_NUM}</span></li>
    <li>Побывали в космосе, на высоте более 80 467&nbsp;м: <span class="yellow">{USAF_NUM}</span></li>
    <li>Всего космических полетов – <span class="yellow">{FLIGHT_NUM}</span>, по определению ВВС США –
      <span class="yellow">{flights_num}</span></li>
    <li>Люди провели в космосе свыше <span class="yellow">{MANYR_NUM}</span> человеко-лет</li>
    <li>Сейчас в космосе <span class="yellow">{len(ASTROS_LST)}</span> космонавт{ending(len(ASTROS_LST))}</li>
  </ul>
  </div>
  <div id="footer">
    <h2>Центр Астрономического и&nbsp;космического образования</h2>
  </div>
</div>
"""
with open(os.path.join(os.pardir, "cosm", "stats", "index.html"), "w", encoding="utf8") as fl:
    print(HEAD + BODY + TAIL, file=fl)
