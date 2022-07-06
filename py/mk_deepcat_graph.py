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
    html = urllib.request.urlopen(url).read()
    #html = open(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('pre')[1].text.splitlines()

def get_data_array(data, date_col=(106, 117), sort=True):
    dates = []
    nnas = 0
    for line in data:
        satcat = line[13:18].strip()
        if satcat[:3] ==  "NNA":
            nnas += 1
            #continue
        if line:
            name = line[48:76].strip()
            ldate = datetime.datetime.strptime(line[date_col[0]:date_col[1]], '%Y %b %d')
            dates.append([ldate, name, satcat])
    print("No satellite cat entry for", nnas, "deepcat entries")
    if sort:
        dates.sort(key=lambda row: row[0])
    return dates

DATA_URL = "https://planet4589.org/space/gcat/data/cat/deepcat.html"

datt = get_table(DATA_URL)[1:]
dates = get_data_array(datt)
dates_only, names, nums_only = [], [], []
unique_dtes = {}

for data, name, satnum in dates:
    if data not in unique_dtes:
        unique_dtes[data] = [name]
    else:
        unique_dtes[data].append(name)
    dates_only.append(data)
    names.append(name)
    nums_only.append(satnum)

with open('deepcat.txt', 'w') as f:
    for dat in unique_dtes:
        print(str(dat.date()), unique_dtes[dat], file=f)

dates = list(unique_dtes.keys())
nums = range(1, len(dates) + 1)
print("Deep space objects:", len(dates))

fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
locator = AutoDateLocator()
locator.intervald[0] = [5]
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

plt.plot(dates, nums, '.b', ms=5)

tdlt = datetime.timedelta(days=630)
plt.xlim(dates[0]-tdlt, dates[-1]+tdlt)
plt.ylim(0, 550)
month, year = "июлю", 2022
plt.title('Рост числа искусственных объектов глубокого космоса. Всего ' + \
          str(len(dates)) + f' объектов к {month} {year} года')
plt.xlabel('Время, годы', fontsize=14)
plt.ylabel('Количество объектов', fontsize=14)
plt.grid()
plt.savefig('deepcat-unique-graph.png', dpi=120)
