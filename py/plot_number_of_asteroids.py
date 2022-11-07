"""Python script for plotting relation between asteroid number and its
date of ciscovery.
Data sources:
https://www.minorplanetcenter.net/data
https://minorplanetcenter.net/iau/lists/ArchiveStatistics.html

Also script reads specific parameter in all versions of html page from git repo.
How to get all previous version of a specific file/folder:
https://stackoverflow.com/questions/12850030/git-getting-all-previous-version-of-a-specific-file-folder
"""

import re
import os
import locale
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


MPC_ARCHIVE_STATS_PTH = os.path.join(os.pardir, 'tmp',
    'mpc_archive_orbits_names.txt')
def datefromstr(dat_str):
    """Convert string to datetime  object"""
    return datetime.strptime(dat_str, "%d%b%Y").date()

# Solar system stats for numbered and named asteroids
firsts = (('08Dec1845', 5, 5), ('12Apr1849', 10, 10),
          ('11Jul1868', 100, 100), ('22Feb1900', 453, 453),
          ('12Aug1923', 1000, 1000), ('22Sep1928', 1100, 1100),)
        #   ('29Jul1960', 2000, 2000), ('02Mar1981', 3000, 3000),)
        #   ('28Aug1981', 4596, 4595), )

archive_dates, archive_nums, archive_total, archive_named = \
    [], [], [], []
for (dat, num, nam) in firsts:
#     archive_dates.append(datefromstr(dat))
#     archive_total.append(numm)
    archive_nums.append((datefromstr(dat), num))
    archive_named.append((datefromstr(dat), nam))
with open(MPC_ARCHIVE_STATS_PTH, encoding='utf-8') as archive_data:
    for line in archive_data:
        if line[0] != '#':
            year = line[:5]
            mon = line[5:8].strip().strip('.').lower()
            day = line[10:13].strip()
            dat = datetime.strptime(year + mon + " " + day,
                "%Y %b %d").date()
            numbered = int(line[25:31])
            total = int(line[17:24])
            named = int(line[55:60])
            archive_dates.append(dat)
            archive_nums.append((dat, numbered))
            archive_total.append(total)
            archive_named.append((dat, named))

tmp_path = os.path.join(os.pardir, 'tmp', 'solarsystem-stats.html')
filenames = next(os.walk(tmp_path), (None, None, []))[2]
dats, nums, allobjs, unnums, comets, checks, nameds = [], [], [], [], [], [], []
allobj, allnum, allnamed = 0, 0, 0
date_pattern = re.compile(
    r"\d+.(\d{1,2})-(Jan?|Feb?|Mar?|Apr?|May|Jun?|"
    r"Jul?|Aug?|Sep?|Oct?|Nov?|"
    r"Dec?)-(\d{4}).*")

for fname in filenames:
    with open(os.path.join(tmp_path, fname), 'rb') as html:
        (day, mon, yr) = date_pattern.findall(fname)[0]
        try:
            soup = BeautifulSoup(html, 'html.parser')
        except UnicodeDecodeError:
            print(html)
        lis = soup.find('ul').findAll('li')
        new_allobj = int(lis[1].text.split()[0])
        dat = datetime.strptime(day + "." + mon + "." + yr,
            "%d.%b.%Y").date()
        if new_allobj != allobj:
            allobj = new_allobj
            allobjs.append((dat, allobj))
        unnumbered = int(lis[3].text.split()[0])
        cometnum = int(lis[4].text.split()[0])

        try:
            numbered = int(lis[2].text.split()[1])
            named = int(lis[5].text.split()[1])
        except ValueError:
            numbered = int(lis[2].text.split()[0])
            named = int(lis[5].text.split()[0])
        if numbered != allnum:
            allnum = numbered
            nums.append((dat, numbered))
        if named != allnamed:
            allnamed = named
            nameds.append((dat, named))
        dats.append(dat)
        unnums.append((dat, unnumbered))
        comets.append(cometnum)
        checks.append(numbered+unnumbered+cometnum)

nums.append((dat, numbered))
current_numbered = nums[0][1]
nums.extend(archive_nums)

nameds.append((dat, named))
nameds.extend(archive_named)

allobjs.append((dat, allobj))
current_allobjs = allobjs[0][1]
allobjs.extend(archive_total)

# print(len(nums), len(nameds), len(allobjs), len(dats), len(unnums), len(comets), len(checks))

NUMBERED_PTH = os.path.join(os.pardir, 'tmp', 'NumberedMPs.txt')
mpdats, mpnums = [], []
data = {}
with open(NUMBERED_PTH, encoding='utf-8') as NumberedMPs:
    for line in NumberedMPs:
        num = int(line[:7].strip().strip('('))
        mpnums.append(num)
        # yr, mon, day = map(int, (line[41:45], line[46:48], line[49:51]))
        dat_str = line[41:51]
        try:
            dat = datetime.strptime(dat_str, "%Y %m %d").date()
        except ValueError:
            dat_str = line[41:49] + '01'
            dat = datetime.strptime(dat_str, "%Y %m %d").date()
        mpdats.append(dat)
        try:
            data[dat] = min(data[dat], num)
        except KeyError:
            data[dat] = num

dmins = []
nmins = []
for year in range(1900, 2023):
    a = []
    for dat, dnum in data.items():
        if dat.year == year and year not in (1908, 1910, 1921, 1927, 1944, 1945, 1957, 1958, 1959):
            a.append((dat, dnum))
    try:
        a.sort(key=lambda row: row[1])
        nmins.append(a[0][1])
        dmins.append(a[0][0])
    except ValueError:
        print("!!! no", year)
    except IndexError:
        pass

fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.056, 0.06, 0.99, 0.97)

years = mdates.YearLocator(5)
oneyear = mdates.YearLocator() # every year
years_fmt = mdates.DateFormatter('%Y')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_minor_locator(oneyear)
ax.xaxis.set_major_formatter(years_fmt)

# plt.plot(mpdats, mpnums, '.')
plt.plot(data.keys(), data.values(), '.', ms=1, color='grey')
# plt.plot(dats, unnums, 'ob-')
# plt.plot(dats, comets, 'oc-')

# plt.plot(list(zip(*allobjs))[0], list(zip(*allobjs))[1], '.k')
plt.plot(list(zip(*nums))[0], list(zip(*nums))[1], 'or', ms=3)
plt.plot(list(zip(*nameds))[0], list(zip(*nameds))[1], 'om', ms=5)
plt.plot(dmins, nmins, 'og', ms=4)
td = timedelta(days=120)
xlims = [sorted(dats)[0] - td, sorted(dats)[-1] + td]
# plt.ylim(-200, 24200)
plt.xlim(datetime(year=1900, month=1, day=1), datetime(year=2002, month=1, day=1))
plt.ylim(0, 18500)
# plt.xlim(datetime(year=1900, month=1, day=1), datetime(year=2023, month=6, day=1))
# plt.ylim(0, 626000)
# plt.xlim(datetime(year=1845, month=6, day=1), datetime(year=1954, month=6, day=1))
# plt.ylim(0, 5100)
# plt.xlim(datetime(year=1939, month=6, day=1), datetime(year=2002, month=1, day=1))
# plt.ylim(0, 29500)

locale.setlocale(locale.LC_ALL, 'ru_RU')
today = datetime.now()
MONTH, YEAR = today.strftime("%B"), today.year
CURRENT_NAMED = 23542 # nameds[0][1]
plt.title(f'Рост числа астероидов. {current_numbered} нумерованных, ' + \
    f'{unnums[0][1]} ненумерованных, {CURRENT_NAMED} с именами, а также ' + \
    f'{comets[0]} комет. Всего {current_allobjs} объектов. {MONTH} {YEAR} года')
plt.xlabel('Время', fontsize=14)
plt.ylabel('Рост количества тел Солнечной системы', fontsize=14)

FILENAME = 'number_of_asteroids_minima'
FILE_EXT = '.png'
plt.grid()
plt.savefig(FILENAME + FILE_EXT, dpi=240)
