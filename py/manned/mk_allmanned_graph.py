import urllib.request
import datetime

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.dates import AutoDateLocator


def get_table(url):
    html = urllib.request.urlopen(url).read()
    #html = open(filenm)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('table')[0]


#FLIGHTS_URL = "http://www.spacefacts.de/english/e_first.htm"
FLIGHTS_URL = "https://www.worldspaceflight.com/bios/chronology.php"
#FLIGHTS_URL0 = "https://www.worldspaceflight.com/bios/sequence.php"

fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
locator = AutoDateLocator()
locator.intervald[0] = [5]
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

table = get_table(FLIGHTS_URL)
nn = 0 
nums, names, dates, ships = [], [], [], []
for tr in table.findAll('tr'):
    tds = tr.findAll('td')
    if len(tds):
        nn += 1
        nums.append(nn) #str(tds[0].text)
        names.append(tds[1].text)
        dates.append(datetime.datetime.strptime(tds[2].text, '%d %B %Y'))
        ships.append(tds[3].text)
    #for td in tds:
    #    print(td.text)

#print(ships)
tdlt = datetime.timedelta(days=630)
accidents = [(1967, 1, 27), (1967, 4, 23), (1971, 6, 29), (1986, 1, 28), (2003, 2, 1)]
for ac_date in accidents:
    ac_d = datetime.date(*ac_date)
    plt.plot([ac_d, ac_d], [0, 600], '--r')

plt.plot(dates, nums, '.b', ms=6)
plt.xlim(dates[0]-tdlt, dates[-1]+tdlt)
plt.ylim(0, nums[-1]+20)
plt.title('Рост количества астронавтов. Всего ' + str(len(dates)) + ' астронавтов к ноябрю 2021 года')
plt.xlabel('Время, годы', fontsize=14)
plt.ylabel('Количество астронавтов', fontsize=14)
plt.grid()
plt.savefig('graph-manned-acc.png', dpi=120)
