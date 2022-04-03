"""Python script for reading numbers of discovered supernova in all versions of
html page with statistics from git repo.
How to get all previous versions of a specific file/folder:
https://stackoverflow.com/questions/12850030/git-getting-all-previous-version-of-a-specific-file-folder
Github repo: https://github.com/gvard/gvard.github.io
html files with stats:
https://github.com/gvard/gvard.github.io/blob/master/stars/stats/index.html
https://github.com/gvard/gvard.github.io/blob/master/stars/stats.html
"""

import re, os
import itertools
from datetime import datetime

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def get_nums(html, ul_num=0):
    dct = {}
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.findAll('ul')[ul_num]
    lis = ul.findAll('li')
    for li in lis:
        txt = li.text.split()
        try:
            if int(txt[1]) != 1996:
                dct[int(txt[1])] = int(txt[4])
            elif int(txt[1]) == 1996 and int(txt[4]) > 1000:
                dct[int(txt[1])] = int(txt[4])
        except ValueError:
            pass
    if 2021 not in dct:
        dct[2021] = None
    if 2022 not in dct:
        dct[2022] = None
    return dct

def get_date(fname):
    (day, mon, yr) = date_pattern.findall(fname)[0]
    f_date = datetime.strptime(".".join((day, mon, yr)), "%d.%b.%Y").date()
    return f_date

def fill_dct(filename, ul_num=0):
    with open(filename) as html:
        dct = get_nums(html, ul_num=ul_num)
        for year in dct:
            all_nums[year].append(dct[year])


# get lists of all filenames:
files_to_read = []
for (html_files_dir, ul_num) in (('stars-stats.html', 0),
    ('stars-stats.html-old', 1), ('all_versions_exported', 0)):
    files_path = os.path.join(os.pardir, 'tmp', html_files_dir)
    filenames_lst = next(os.walk(files_path), (None, None, []))[2]
    files_to_read.append((files_path, filenames_lst, ul_num))

date_pattern = re.compile(
    "\d+.(\d{1,2})-(Jan?|Feb?|Mar?|Apr?|May|Jun?|"
    "Jul?|Aug?|Sep?|Oct?|Nov?|"
    "Dec?)-(\d{4}).*")
all_nums = dict((year, []) for year in range(1996, 2023))
dats = []
for (files_path, filenames_lst, ul_num) in files_to_read:
    for fname in filenames_lst:
        f_date = get_date(fname)
        filename = os.path.join(files_path, fname)
        dats.append(f_date)
        fill_dct(filename, ul_num=ul_num)

print("Number of commits with SN data:", len(dats))

colors = itertools.cycle(['c', 'm', 'y', 'k', 'r', 'g', 'b', 'orange'])
for year in range(2015, 2023):
    plt.plot(dats, all_nums[year], 'o', color=next(colors), label=year)

plt.legend()
plt.title('Динамика открытий сверхновых по годам', fontsize=16)
plt.xlabel('Время', fontsize=14)
plt.ylabel('Количество сверхновых', fontsize=14)
plt.grid()
plt.show()