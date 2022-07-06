"""Python script for genererating an html page
with meteorites statistics. Data source: Meteoritical Bulletin
"""

import os

from beautifulsoup_supply import TAIL, mk_head
from plot_supply import plot_bar, optimize_svg


HTML_FILENAME = os.path.join(os.pardir, 'meteorites', 'stats', 'index.html')
HEAD = mk_head("Статистика падений метеоритов по годам", style="../../compact.css", script="") + "<body>\n"

data, doubtful = [], []
for filnam in ('db16.txt', 'db17.txt', 'db18.txt', 'db19.txt', 'db20.txt'):
    with open(filnam) as raw_data:
        for line in raw_data:
            if line[0] != "#":
                status = line.split("\t")[1]
                decade = line.split("\t")[3][:3]
                if status == "Official":
                    data.append(decade)
                else:
                    doubtful.append(decade)

years, falls, falls_doubtful = [], [], []
for i in range(1600, 2021, 10):
    decastr = str(int(i/10))
    years.append(int(decastr))
    falls.append(data.count(decastr))
    falls_doubtful.append(doubtful.count(decastr))


labels = ('Статистика падений метеоритов по годам', 'Десятилетие', 'Падений за 10 лет')
tmp_filename = 'meteorites_plot_.svg'
filename = 'meteorites_plot.svg'
meteorites_dir = os.path.join(os.pardir, 'meteorites')
tmp_pth = os.path.join(meteorites_dir, tmp_filename)
pth = os.path.join(meteorites_dir, 'stats', filename)
xlim = (174.3, 202.7)
plot_bar(years[15:], falls[15:], falls_doubtful[15:], labels, tmp_pth, xlim)
optimize_svg(tmp_pth, pth)
os.remove(tmp_pth)

meteorite_falls_txt = "<h2>Статистика падений метеоритов</h2>\n<ul>"
falls_count = 0
for i, year in enumerate(years):
    falls_count += falls[i]
    meteorite_falls_txt += f"<li>За десятилетие <b>{str(year)+'x'}</b> зарегистрировано <b>{falls[i]}</b> падений метеоритов, сомнительных регистраций – <b>{falls_doubtful[i]}</b>. Всего к концу десятилетия зарегистрировано <b>{falls_count}</b> падений.\n"

meteorite_falls_txt += f"""</ul>
<br><img src="{filename}" alt="">
<h2>Ссылки</h2>
<ul>
<li><a href="https://www.lpi.usra.edu/meteor/metbull.php" target="_blank" rel="noopener noreferrer">Meteoritical Bulletin: Search the Database</a></li>
<li><a href="https://cneos.jpl.nasa.gov/fireballs/" target="_blank" rel="noopener noreferrer">Fireball and Bolide Data</a></li>
</ul>
"""

with open(HTML_FILENAME, 'w', encoding="utf8") as fl:
    print(HEAD + meteorite_falls_txt + TAIL, file=fl)
