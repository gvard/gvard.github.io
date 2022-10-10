"""Python script for plotting graph
with manned flight statistics.
"""

import urllib.request
import datetime
import os
import ssl

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.dates import AutoDateLocator


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def get_table(url):
    """Read ASCII data table from pre html element"""
    html = urllib.request.urlopen(url).read()
    #html = open(url) # for local file
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('pre')[1].text.splitlines()


DATA_URL = "https://planet4589.org/space/astro/lists/"
DATA_URL += "missions.html"

data = get_table(DATA_URL)[1:]
dates, flights_nums, rides_nums = [], [], []
FLIGHTS_NUM = 0
RIDES_NUM = 0
for line in data:
    if line and line[1] == '0':
        dd = datetime.datetime.strptime(line[77:93], '%Y %b %d %H%M')
        dates.append(dd)
        FLIGHTS_NUM += 1
        RIDES_NUM += int(line[139])
        flights_nums.append(FLIGHTS_NUM)
        rides_nums.append(RIDES_NUM)

fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
locator = AutoDateLocator()
locator.intervald[0] = [5]
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

tdlt = datetime.timedelta(days=630)

nums, ylim_top_margin = rides_nums, 50
#nums, ylim_top_margin = flights_nums, 15

accidents = [(1967, 1, 27), (1967, 4, 23), (1971, 6, 29), (1986, 1, 28), (2003, 2, 1)]
private_spaceflights = [(2020, 5, 30), (2021, 7, 11), (2021, 7, 20), (2021, 9, 16)]
for ac_date in accidents:
    ac_d = datetime.date(*ac_date)
    plt.plot([ac_d, ac_d], [0, nums[-1]+ylim_top_margin], '--r')
for ac_date in private_spaceflights:
    ac_d = datetime.date(*ac_date)
    plt.plot([ac_d, ac_d], [0, nums[-1]+ylim_top_margin], '--g')

plt.plot(dates, nums, '.b', ms=6)
plt.xlim(dates[0]-tdlt, dates[-1]+tdlt)
plt.ylim(0, nums[-1]+ylim_top_margin)
plt.title('Рост числа полетов астронавтов. Всего ' + str(len(dates)) + \
    ' полета и ' + str(rides_nums[-1]) + ' человек к октябрю 2022 года')
plt.xlabel('Время, годы', fontsize=14)
plt.ylabel('Количество полетов астронавтов', fontsize=14)
plt.grid()
plt.savefig('graph-mannedflights-rides.png', dpi=120)
