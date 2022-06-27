"""Python script for reading specific parameter in all versions of
html page from git repo.
How to get all previous version of a specific file/folder:
https://stackoverflow.com/questions/12850030/git-getting-all-previous-version-of-a-specific-file-folder
"""

import re
import os
from datetime import datetime

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

tmp_path = os.path.join(os.pardir, 'tmp', 'all_versions_exported')
filenames = next(os.walk(tmp_path), (None, None, []))[2]
print(filenames)
dats, nums = [], []
date_pattern = re.compile(
    r"\d+.(\d{1,2})-(Jan?|Feb?|Mar?|Apr?|May|Jun?|"
    r"Jul?|Aug?|Sep?|Oct?|Nov?|"
    r"Dec?)-(\d{4}).*")

for fname in filenames:
    with open(os.path.join(tmp_path, fname)) as html:
        (day, mon, yr) = date_pattern.findall(fname)[0]
        dats.append(datetime.strptime(day + "." + mon + "." + yr,
            "%d.%b.%Y").date())
        soup = BeautifulSoup(html, 'html.parser')
        names_txt = soup.findAll('li')[-1].text
        num = int(names_txt[13:15] + names_txt[16:19])
        nums.append(num)

plt.plot(dats, nums, 'o-')
plt.xlabel('Время', fontsize=14)
plt.ylabel('Количество малых планет с именами', fontsize=14)

plt.grid()
plt.show()
