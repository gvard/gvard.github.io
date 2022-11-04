"""Python script for plotting graph
with manned flights statistics: flights, astronauts and its rides
"""

import urllib.request
from datetime import datetime, timedelta
import datetime as dt
import os
import ssl
import locale

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from plot_supply import optimize_svg


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def get_table(url, pre_num=1):
    """Read ASCII data table from pre html element"""
    html = urllib.request.urlopen(url).read()
    #html = open(url) # for local file
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('pre')[pre_num].text.splitlines()

def get_flights_table(url):
    """Read date from HTML page"""
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('table')[0]


DATA_BASE_URL = "https://planet4589.org/space/astro/lists/"
DATA_URL = DATA_BASE_URL + "missions.html"
FLIGHTS_URL = "https://www.worldspaceflight.com/bios/chronology.php"
SPACEPOP_URL = "https://planet4589.org/space/astro/web/pop.html"

data = get_table(DATA_URL)[1:]
dates, flights_nums, rides_nums = [], [], []
flights_num = 0
rides_num = 0
for line in data:
    if line and line[1] == '0':
        dd = datetime.strptime(line[77:93], '%Y %b %d %H%M')
        dates.append(dd)
        flights_num += 1
        rides_num += int(line[139])
        flights_nums.append(flights_num)
        rides_nums.append(rides_num)

table = get_flights_table(FLIGHTS_URL)
flights_num = 0
flight_nums, flight_dates, ships = [], [], []
for tr in table.findAll('tr'):
    tds = tr.findAll('td')
    if len(tds):
        flights_num += 1
        flight_nums.append(flights_num)
        flight_dates.append(datetime.strptime(tds[2].text, '%d %B %Y'))

DATA_URL = DATA_BASE_URL +  "evas.html"

data = get_table(DATA_URL)[1:]
evadates, evanums = [], []
astro_num = 0
for line in data:
    if line:
        dd = datetime.strptime(line[170:186], '%Y %b %d %H%M')
        evadates.append(dd)
        astro_num += 1
        evanums.append(astro_num)

fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
years = mdates.YearLocator(5)
oneyear = mdates.YearLocator()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_minor_locator(oneyear)

tdlt = timedelta(days=630)

locale.setlocale(locale.LC_ALL, 'ru_RU')
today = datetime.now()
MONTH, YEAR = today.strftime("%B"), today.year

# Graph settings
FILE_EXT = ".svg"
nums, ylim_top_margin, image_filename = rides_nums, 50, "graph-mannedflights-rides-all"
#nums, ylim_top_margin, image_filename = flights_nums, 15, "graph-mannedflights"


accidents = [(1967, 1, 27), (1967, 4, 23), (1971, 6, 29), (1986, 1, 28), (2003, 2, 1)]
private_spaceflights = [(2001, 4, 28), (2020, 5, 30), (2021, 7, 11), \
    (2021, 7, 20), (2021, 9, 16)]
for ac_date in accidents:
    ac_d = dt.date(*ac_date)
    plt.plot([ac_d, ac_d], [0, nums[-1]+ylim_top_margin], '--r')
for ac_date in private_spaceflights:
    ac_d = dt.date(*ac_date)
    plt.plot([ac_d, ac_d], [0, nums[-1]+ylim_top_margin], '--g')

plt.plot(dates, nums, '.b', label='Количество посещений', ms=6)
plt.plot(evadates, evanums, '.', label='Количество ВКД', color="brown", ms=6)
plt.plot(dates, flights_nums, '.m', label='Количество космических полетов', ms=6)
plt.plot(flight_dates, flight_nums, '.k', label='Количество астронавтов', ms=6)
plt.xlim(dates[0]-tdlt, dates[-1]+tdlt)
plt.ylim(0, nums[-1]+ylim_top_margin)
plt.title(f'Рост числа полетов астронавтов. Всего {len(dates)} полета, ' + \
    f'{flight_nums[-1]} астронавтов, {evanums[-1]} ВКД и {rides_nums[-1]} ' + \
    'посещений. {MONTH} {YEAR} года')
plt.xlabel('Время, годы', fontsize=14)
plt.ylabel('Количество полетов астронавтов', fontsize=14)
plt.grid()
plt.legend(fontsize=13)
plt.savefig(image_filename + 'noopt' + FILE_EXT, dpi=240)

if FILE_EXT == '.svg':
    optimize_svg(image_filename + 'noopt' + FILE_EXT, image_filename + FILE_EXT)
