"""Python script for reading specific parameter in all versions of
html page from git repo.
How to get all previous version of a specific file/folder:
https://stackoverflow.com/questions/12850030/git-getting-all-previous-version-of-a-specific-file-folder
"""

import re
import os
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from matplotlib.dates import AutoDateLocator

mpc_archive_stats_path = os.path.join(os.pardir, 'tmp',
    'mpc_archive_orbits_names.txt')
def datefromstr(d): return datetime.strptime(d,
                "%d%b%Y").date()

# Solar system stats for numbered and named asteroids
firsts = (('08Dec1845', 5), ('12Apr1849', 10),
          ('11Jul1868', 100), ('22Feb1900', 453),
          ('12Aug1923', 1000), ('22Sep1928', 1100),
          ('29Jul1960', 2000), ('02Mar1981', 3000),)

archive_dates, archive_nums, archive_total, archive_named, named_nums = \
    [], [], [], [], []
# for (dat, numm) in firsts:
#     archive_dates.append(datefromstr(dat))
#     archive_nums.append(numm)
#     archive_total.append(numm)
#     archive_named.append(numm)
with open(mpc_archive_stats_path) as archive_data:
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
            archive_nums.append(numbered)
            archive_total.append(total)
            archive_named.append(named)
            named_nums.append(named)

tmp_path = os.path.join(os.pardir, 'tmp', 'solarsystem-stats.html')
filenames = next(os.walk(tmp_path), (None, None, []))[2]
dats, nums, allobjs, unnums, comets, checks, nameds = [], [], [], [], [], [], []
allobj = 0
date_pattern = re.compile(
    r"\d+.(\d{1,2})-(Jan?|Feb?|Mar?|Apr?|May|Jun?|"
    r"Jul?|Aug?|Sep?|Oct?|Nov?|"
    r"Dec?)-(\d{4}).*")

dats.extend(archive_dates)
nums.extend(archive_nums)
allobjs.extend(archive_total)
nameds.extend(archive_named)
for fname in filenames:
    with open(os.path.join(tmp_path, fname), 'rb') as html:
        (day, mon, yr) = date_pattern.findall(fname)[0]
        try:
            soup = BeautifulSoup(html, 'html.parser')
        except UnicodeDecodeError:
            print(html)
        lis = soup.find('ul').findAll('li')
        new_allobj = int(lis[1].text.split()[0])
        if new_allobj != allobj:
            allobj = new_allobj
            unnumbered = int(lis[3].text.split()[0])
            cometnum = int(lis[4].text.split()[0])
            try:
                numbered = int(lis[2].text.split()[1])
                named = int(lis[5].text.split()[1])
            except ValueError:
                numbered = int(lis[2].text.split()[0])
                named = int(lis[5].text.split()[0])
            dat = datetime.strptime(day + "." + mon + "." + yr,
                "%d.%b.%Y").date()
            dats.append(dat)
            nums.append(numbered)
            unnums.append(unnumbered)
            comets.append(cometnum)
            allobjs.append(allobj)
            nameds.append(named)
            checks.append(numbered+unnumbered+cometnum)


fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.056, 0.06, 0.99, 0.97)

plt.plot(dats, nums, '.')
# plt.plot(dats, unnums, 'ob-')
# plt.plot(dats, comets, 'oc-')
plt.plot(dats, allobjs, '.k')
plt.plot(dats, nameds, '.m')
td = timedelta(days=120)
xlims = [sorted(dats)[0] - td, sorted(dats)[-1] + td]
plt.xlim(xlims[0], xlims[-1])
# plt.ylim(-200, 24200)
# ax.xaxis.set_major_locator(MultipleLocator(730.5))
MONTH, YEAR = "октябрю", 2022
plt.title(f'Рост числа астероидов. {sorted(nums)[-1]} нумерованных, {sorted(unnums)[-1]} ненумерованных, ' + \
    f'{sorted(nameds)[-1]} с именами, а также {comets[0]} комет. Всего {sorted(allobjs)[-1]} объектов к {MONTH} {YEAR} года')
plt.xlabel('Время', fontsize=14)
plt.ylabel('Рост количества тел Солнечной системы', fontsize=14)

image_filename = 'number_of_asteroids'
FILE_EXT = '.png'
plt.grid()
plt.savefig(image_filename + FILE_EXT, dpi=240)
