import datetime
import urllib.request

import matplotlib.pyplot as plt


def get_data(readme, nums=(124, 29)):
    vsx_nums = []
    dates = []
    for line in readme[nums[0]:]:
        line = line.decode()
        num = line[nums[1]:].split()[0]
        try:
            vsx_nums.append(int(num) / 1000)
            dat = datetime.datetime.strptime(line[4:14], '%Y-%m-%d')
            dates.append(dat)
        except ValueError:
            pass
    return dates, vsx_nums


URL_VSX = "http://cdsarc.u-strasbg.fr/ftp/B/vsx/ReadMe"
readme_lines = urllib.request.urlopen(URL_VSX).readlines()
dates, vsx_nums = get_data(readme_lines)
gcvs_dates = [datetime.datetime.strptime(x, '%d-%b-%Y') for x in
             ['07-Jun-2009', '03-Apr-2011', '26-Feb-2012', '30-Apr-2013',
              '17-Sep-2018', '06-Jul-2020', '31-Mar-2022']]
gcvs_nums = [41.639, 43.675, 45.835, 47.969, 52.011, 54.979, 58.202]

fig, ax = plt.subplots(figsize=(16, 9))
plt.title("Количество переменных звезд в каталогах", fontsize=16)
plt.ylim(0, vsx_nums[-1] + 100)
td = datetime.timedelta(days=30)
plt.xlim(dates[0] - td, dates[-1] + td)
plt.subplots_adjust(left=0.06, bottom=0.06, right=0.97, top=0.955)
plt.plot(dates, vsx_nums, '.r--', label="Variable Star Index")
plt.plot(gcvs_dates, gcvs_nums, 'ob--', label="Общий Каталог Переменных Звезд")
plt.xlabel('Время, годы')
plt.ylabel('Количество переменных звезд (тысяч)')
plt.legend()
plt.grid()
plt.savefig('variable-stars-count-graph.png', dpi=300)
