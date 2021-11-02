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

def get_data_array(data, date_col=(26, 41)):
    dates, nums = [], []
    launches_num = 0
    no_altitude = 0
    for line in data:
        apo = line[236:244].strip()
        try:
            apo = int(apo)
        except ValueError:
            no_altitude += 1
        if line:
            try:
                dd = datetime.datetime.strptime(line[date_col[0]:date_col[1]], '%Y %b %d %H%M')
            except ValueError:
                dd = datetime.datetime.strptime(line[date_col[0]:date_col[1]-4], '%Y %b %d')
            dates.append(dd)
            launches_num += 1
            nums.append(launches_num)
    print("No apogee altitude data for", no_altitude, "entries")
    return dates, nums


BASE_URL = "https://planet4589.org/space/gcat/data/ldes/"

DATA_URL = BASE_URL + "O.html"
data = get_table(DATA_URL)[1:]
dates, nums = get_data_array(data)
print("Orbital launches:", len(dates))

DATA_URL = BASE_URL + "F.html"
data = get_table(DATA_URL)[1:]
dates_fail, nums_fail = get_data_array(data)
print("Launches failed:", len(dates_fail))

DATA_URL = BASE_URL + "U.html"
data = get_table(DATA_URL)[1:]
dates_marg, nums_marg = get_data_array(data)
print("Marginal launches:", len(dates_marg))


fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
locator = AutoDateLocator()
locator.intervald[0] = [5]
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

plt.plot(dates_marg, nums_marg, '.g', ms=5)
plt.plot(dates_fail, nums_fail, '.r', ms=5)
plt.plot(dates, nums, '.b', ms=5)
#plt.plot(dates, heights, '.b', ms=5)

tdlt = datetime.timedelta(days=630)
plt.xlim(dates[0]-tdlt, dates[-1]+tdlt)
plt.ylim(-25, nums[-1]+100)
plt.title('Рост числа орбитальных ракетных запусков. Всего ' + str(len(dates)) + ' успешных запуска к 3 ноября 2021 года')
plt.xlabel('Время, годы', fontsize=14)
plt.ylabel('Количество орбитальных ракетных запусков', fontsize=14)
plt.grid()
plt.savefig('launches-graph.png', dpi=120)