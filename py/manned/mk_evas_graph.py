import urllib.request
import datetime
import os, ssl

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


DATA_URL = "https://planet4589.org/space/astro/lists/"
DATA_URL += "evas.html"

data = get_table(DATA_URL)[1:]
dates, nums = [], []
astro_num = 0
for line in data:
    if line:
        dd = datetime.datetime.strptime(line[170:186], '%Y %b %d %H%M')
        dates.append(dd)
        astro_num += 1
        nums.append(astro_num)

fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
locator = AutoDateLocator()
locator.intervald[0] = [5]
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

tdlt = datetime.timedelta(days=630)
accidents = [(1967, 1, 27), (1967, 4, 23), (1971, 6, 29), (1986, 1, 28), (2003, 2, 1)]
for ac_date in accidents:
    ac_d = datetime.date(*ac_date)
    plt.plot([ac_d, ac_d], [0, 1400], '--r')

plt.plot(dates, nums, '.b', ms=6)
plt.xlim(dates[0]-tdlt, dates[-1]+tdlt)
plt.ylim(0, nums[-1]+50)
plt.title('Рост числа ВКД. Всего ' + str(len(dates)) + ' ВКД к ноябрю 2021 года')
plt.xlabel('Время, годы', fontsize=14)
plt.ylabel('Количество ВКД', fontsize=14)
plt.grid()
plt.savefig('graph-evas.png', dpi=120)
