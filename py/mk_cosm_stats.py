# -*- coding: utf-8 -*-

import os
import json
import urllib.request

from beautifulsoup_supply import TAIL, mk_head, get_soup

DEBUG = False
HEAD = mk_head("Космонавтика: статистика", script="") + "<body>\n"
N2YO_URL = "https://www.n2yo.com/"
SPACEFLIGHT_URL = "https://www.worldspaceflight.com/bios/stats.php"
SPACEFLIGHT1_URL = "https://www.worldspaceflight.com/bios/stats1.php"
CURRENTLY_IN_SPACE_URL = "https://www.worldspaceflight.com/bios/currentlyinspace.php"
NANOSATS_URL = "https://www.nanosats.eu/"
ASTROS_URL = 'http://api.open-notify.org/astros.json'


def get_n2yo(soup):
    return int(soup.findAll("span", {"style": "color:#d50000"})[0].text)

def get_nanosats(soup):
    date = soup.findAll('h3')[-1].b.text.split('of')[1].strip()
    lis = soup.find("ul", {"class": "ultwo center-align"}).findAll('li')
    return date, lis

soup = get_soup(NANOSATS_URL)
DATE, LIS = get_nanosats(soup)
NANOSATS_HTML = f"""<h2><a href="https://en.wikipedia.org/wiki/Small_satellite#Nanosatellites" target="_blank" rel="noopener noreferrer">Наноспутники</a></h2>
<p><a href="{NANOSATS_URL}">База данных наноспутников</a> &ndash; до 10 кг для нестандартных типов и до 27U (30&ndash;40 кг) для
<a href="https://www.nanosats.eu/cubesat">кубсатов</a>. Последнее обновление: {DATE}.</p>
<ul>
"""
for li in LIS:
    NANOSATS_HTML += str(li) + '\n'
NANOSATS_HTML += '</ul>\n'

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
    return manyr_num, usaf_num, fai_num, cosmonaut_num

soup = get_soup(SPACEFLIGHT_URL)
MANYR_NUM, USAF_NUM, FAI_NUM, COSMONAUT_NUM = get_spaceflight(soup)

astros_obj = urllib.request.urlopen(ASTROS_URL)
astros = json.load(astros_obj)
if DEBUG:
    print('URL:', astros_obj.geturl(), 'HTTP code:', astros_obj.getcode())

ASTROS_LST = astros.get('people')
ASTROS_STR = ", ".join([astr.get('name') for astr in ASTROS_LST])

COSM_NUM = 3
SPACEFLIGHT_HTML = f"""<h2>Пилотируемая космонавтика</h2>
<p><a href="{SPACEFLIGHT_URL}">Статистика</a> <a href="{SPACEFLIGHT1_URL}">пилотируемой космонавтики</a>
<ul>
<li>Космонавтов (людей, побывавших в космосе и совершивших орбитальный полет)
&ndash; <b>{COSMONAUT_NUM}</b></li>
<li>Людей, побывавших в космосе (согласно определению Международной федерации аэронавтики, при высоте полета более 100 км)
&ndash; <b>{FAI_NUM}</b></li>
<li>Людей, побывавших в космосе (согласно классификации ВВС США, при высоте полета более 80 км 467 м)
&ndash; <b>{USAF_NUM}</b></li>
<li>Время, проведенное людьми в космосе &ndash; свыше <b>{MANYR_NUM}</b> человеко-лет.</li>
<li>В космосе <b>{len(ASTROS_LST)}</b> космонавта: {ASTROS_STR}.</li>
</ul>
"""

with open(os.path.join(os.pardir, 'cosm', 'stats.html'), 'w', encoding="utf8") as handle:
    print(HEAD + SPACEFLIGHT_HTML + N2_STATS_HTML + NANOSATS_HTML + TAIL, file=handle)
