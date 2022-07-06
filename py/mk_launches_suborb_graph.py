"""Python script for plotting graph
with suborbital launches statistics.
"""

import datetime
import os
import ssl
import urllib.request

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.dates import AutoDateLocator


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def get_table(url):
    html = urllib.request.urlopen(url).read()
    #html = open(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('pre')[1].text.splitlines()


BASE_URL = "https://planet4589.org/space/gcat/data/ldes/"
DATA_URL = BASE_URL + "S.html"
data = get_table(DATA_URL)[1:]
#dates, nums = get_data_array(data)
#print("Suborbital launches:", len(dates))

dates, nums, heights = [], [], []
launches_num = 0
no_altitude = 0
for line in data:
    apo = line[239:244].strip()
    try:
        apo = int(apo)
        if line and line[35:37].strip() and apo and int(apo) > 79:
            apo = int(apo)
            try:
                dd = datetime.datetime.strptime(line[26:41], '%Y %b %d %H%M')
            except ValueError:
                dd = datetime.datetime.strptime(line[26:37], '%Y %b %d')

            heights.append(apo)
            dates.append(dd)
            launches_num += 1
            nums.append(launches_num)
    except ValueError:
        no_altitude += 1
print("No apogee altitude data for", no_altitude, "entries")

fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
locator = AutoDateLocator()
locator.intervald[0] = [5]
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

plt.plot(dates, nums, '.b', ms=4)
tdlt = datetime.timedelta(days=630)
plt.xlim(dates[0]-tdlt, dates[-1]+tdlt)
month, year = "июлю", 2022
plt.title('Рост числа суборбитальных запусков. Всего ' + str(len(dates)) + f' запусков к {month} {year} года')
plt.xlabel('Время, годы', fontsize=14)
plt.ylabel('Количество суборбитальных запусков', fontsize=12)
plt.grid()
plt.savefig('launches-suborb-80km-graph.png', dpi=120)
