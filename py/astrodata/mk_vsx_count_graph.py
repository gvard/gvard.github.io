import datetime
import urllib.request

import matplotlib.pyplot as plt

URL = "ftp://cdsarc.u-strasbg.fr/pub/cats/B/vsx/ReadMe"
vsx_nums = []
dates = []

readme = urllib.request.urlopen(URL).readlines()
for line in readme[124:]:
    line = line.decode()
    num = line[29:].split()[0]
    try:
        vsx_nums.append(int(num) / 1000)
        dat = datetime.datetime.strptime(line[4:14], '%Y-%m-%d')
        dates.append(dat)
    except ValueError:
        pass

plt.plot(dates, vsx_nums, '.r--')
plt.xlabel('Дата')
plt.ylabel('Количество звезд (тысяч)')
plt.grid()
plt.show()
#plt.savefig('var.svg')
