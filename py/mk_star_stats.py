"""Python script for genererating an html page with lists and a bar chart with
supernovae statistics.

Data sources:
* [David Bishop, Latest Supernovae Archives](https://www.rochesterastronomy.org/snimages/archives.html)
* [Transient Name Server](https://www.wis-tns.org/stats-maps)
* [SIMBAD Astronomical Database statistics](https://simbad.u-strasbg.fr/simbad/)
"""

import os
import pickle
import urllib.request
from datetime import datetime
import locale

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from beautifulsoup_supply import TAIL, mk_head, get_soup_Request
from plot_supply import plot_bar, optimize_svg


HEAD = mk_head("Статистика звездных каталогов", style="../../compact.css", script="") + "<body>\n"
WDS_URL = "http://cdsarc.u-strasbg.fr/viz-bin/ReadMe/B/wds?format=html"
SIMBAD_URL = "https://simbad.u-strasbg.fr/simbad/"
SNIMAGES_URL = "https://rochesterastronomy.org/snimages/"
SNOTHER_URL = SNIMAGES_URL + "snother.html"
SNSTATS_URL = SNIMAGES_URL + "archives.html"
NOVASTATS_URL = SNIMAGES_URL + "novastatsall.html"

TNS_URL = "https://www.wis-tns.org"
TNS_STATS_URL = TNS_URL + "/stats-maps"
PICKLE_SIMB_FILENAME = 'simbad_stats.pickle'
PICKLE_SN_FILENAME = 'snstats.pickle'
HTML_FILENAME = os.path.join(os.pardir, 'stars', 'stats', 'index.html')
SIMBAD_LST = ['objects', 'identifiers', 'bibliographic references', 'citations of objects in papers']


def cds_readme_stats(url):
    html = urllib.request.urlopen(url).readlines()
    last_line = str(html[-23]).split()[2:5]
    return last_line[0], int(last_line[2])

def get_snstats(soup, end=23):
    pre = soup.find('pre').text
    return pre.splitlines()[1:end]

def get_sn_count(txt):
    """Get Supernova total count"""
    return int(txt[0].split()[4]), int(txt[1].split()[0]), \
           int(txt[5].split()[0]), int(txt[6].split()[0])

def get_tns(soup):
    all_stat_num = soup.findAll('div', {"class": "stat-item-right"})
    all_transient = int(all_stat_num[0].text)
    public_transient = int(all_stat_num[1].text)
    classified = int(all_stat_num[2].text)
    spectra = int(all_stat_num[3].text)
    return all_transient, public_transient, classified, spectra

def simbad_stats(soup):
    tdsbg = soup.findAll("td", {"bgcolor": "#3264A0"})
    for tdbg in tdsbg:
        if tdbg.text.strip() == "Statistics": #len(result.attrs) == 5
            tbody = tdbg.parent.parent
            tds = tbody.findAll('td')
            break
    simbstats_dct = {}
    for i, td in enumerate(tds):
        if 'Simbad contains on' in td.text:
            simdate = td.i.text.strip()
            continue
        for tabstr in SIMBAD_LST:
            if tabstr == td.text.strip():
                simbstats_dct[tabstr] = int(tds[i-1].text.strip().replace(',', ''))
    return simdate, simbstats_dct


snurls = []
snurls.append((1995, f"{SNIMAGES_URL}snstatsother.html"))
for year in range(1996, 1999):
    snstats_year = f'{SNIMAGES_URL}snstats{year}.html'
    snurls.append((year, snstats_year))
snurls.append((1999, f'{SNIMAGES_URL}sn1999/snstats.html'))

for year in range(2000, 2024):
    snstats_year = f'https://rochesterastronomy.org/sn{year}/snstats.html'
    snurls.append((year, snstats_year))
snurls.append(('all', f'{SNIMAGES_URL}snstatsall.html'))

snstats = {}
locale.setlocale(locale.LC_ALL, 'ru_RU')
today = datetime.now()
MONTH, YEAR = today.strftime("%B"), today.year
snstats_txt = f"""<h2><a href="{SNSTATS_URL}">Статистика вспышек сверхновых</a></h2>
<ul>
"""
years, sns, snalt, all_sne = [], [], [], []
years_dt = []
all_sn_count, sn_amateur_count = 0, 0
for (year, snstats_url) in snurls:
    soup = get_soup_Request(snstats_url)
    snstats[year] = get_snstats(soup)
    sn_num, sn_cbat, sn_amateur, sn_13th = get_sn_count(snstats[year])
    all_sn_count += sn_num
    sn_amateur_count += sn_amateur
    if year == 1995:
        all_sne.append(all_sn_count)
        snstats_txt += f"<li><a href='{snstats_url}' target='_blank' rel='noopener noreferrer'>До 1996 года</a> открыто <b>{sn_num}</b> сверхновых, <b>{sn_amateur_count}</b> – любителями, <b>{sn_13th}</b> ярче 13-й зв. величины (<a href='{SNOTHER_URL}'>яркие сверхновые до 1996 года</a>).\n"
        years.append(year)
        years_dt.append(datetime(year+1, 1, 1))
        sns.append(sn_num - sn_amateur)
        snalt.append(sn_amateur)
    elif year != "all":
        all_sne.append(all_sn_count)
        snstats_txt += f"<li><a href='{snstats_url}' target='_blank' rel='noopener noreferrer'>За {year} год</a> открыто <b>{sn_num}</b> сверхновых, <b>{sn_amateur}</b> – любителями, <b>{sn_13th}</b> ярче 13-й зв. величины. Всего к концу года открыто <b>{all_sn_count}</b>, <b>{sn_amateur_count}</b> – любителями.\n"
        if year == YEAR:
            years_dt.append(today)
        else:
            years_dt.append(datetime(year+1, 1, 1))
        years.append(year)
        sns.append(sn_num - sn_amateur)
        snalt.append(sn_amateur)
    else:
        snstats_txt += f"""<li><a href="{snstats_url}" target="_blank" rel="noopener noreferrer">Всего открыто</a> <b>{sn_num}</b> сверхновых, <b>{sn_amateur}</b> – любителями, <b>{sn_13th}</b> ярче 13-й зв. величины.\n"""

file_ext = 'svg'
total_sne_filename = 'sne_total_number_log_plot.' + file_ext
stars_dir = os.path.join(os.pardir, 'stars')
pth = os.path.join(stars_dir, total_sne_filename)
tmp_filename = 'sne_total_number_log_plot_.' + file_ext
tmp_pth = os.path.join(stars_dir, tmp_filename)

fig, ax = plt.subplots(figsize=(16, 9))
plt.subplots_adjust(left=0.06, bottom=0.06, right=0.97, top=0.955)
ax.xaxis.set_major_locator(mdates.YearLocator(1))

plt.plot(years_dt, all_sne, 'ok-')
plt.xlim(datetime(1995, 4, 1), datetime(2023, 8, 1))
plt.yscale("log")
plt.title(f'Динамика открытий сверхновых. {MONTH} {YEAR} года', fontsize=16)
plt.xlabel('Время', fontsize=14)
plt.ylabel('Количество открытых сверхновых', fontsize=14)
plt.grid(axis='y', which='major', linestyle='-')
plt.grid(axis='x', which='major', linestyle=':')
plt.grid(axis='y', which='minor', linestyle='--')
plt.savefig(tmp_pth, dpi=240)
if file_ext == 'svg':
    optimize_svg(tmp_pth, pth)
    os.remove(tmp_pth)


labels = ('Статистика открытий сверхновых по годам', 'Год',
          'Открытий сверхновых за год', 'Сверхновые, обнаруженные любителями')
tmp_filename = 'sne_stats_bar_chart_.' + file_ext
filename = 'sne_stats_bar_chart.' + file_ext
tmp_pth = os.path.join(stars_dir, tmp_filename)
pth = os.path.join(stars_dir, filename)
xlim = (1994.3, 2023.7)
plot_bar(years, sns, snalt, labels, tmp_pth, xlim, lab0="до 1996")
if file_ext == 'svg':
    optimize_svg(tmp_pth, pth)
    os.remove(tmp_pth)
soup = get_soup_Request(TNS_STATS_URL)
all_transient, public_transient, classified, spectra = get_tns(soup)

snstats_txt += f"""</ul>
<br><img src="https://github.com/gvard/astrodata/raw/main/plots/stars/sne_stats_bar_chart.svg" alt=""><br>
<img src="https://github.com/gvard/astrodata/raw/main/plots/stars/sne_transients_total_number_log_plot.svg" alt="">
<h2><a href="{TNS_URL}">Transient Name Server</a></h2>
<a href="{TNS_STATS_URL}" target="_blank" rel="noopener noreferrer">статистика</a>:<br>
<img src="https://github.com/gvard/astrodata/raw/main/plots/stars/transient_stats_bar_chart.svg" alt="">
<ul>
<li>Всего транзиентов с 01.01.2016: <b>{all_transient}</b>, <b>{public_transient}</b> в открытом доступе
<li>Сверхновых классифицировано: <b>{classified}</b>
<li>Всего спектров: <b>{spectra}</b>
</ul>

<h2>Ссылки</h2>
<ul>
<li><a href="{NOVASTATS_URL}" target="_blank" rel="noopener noreferrer">Статистика новых звезд</a>
<li><a href="{SNIMAGES_URL + 'lbvlist.html'}" target="_blank" rel="noopener noreferrer">List of supernova impostors</a> – LBV's (<a href="https://en.wikipedia.org/wiki/Luminous_blue_variable" target="_blank" rel="noopener noreferrer">Luminous Blue Variables</a>).
<li><a href="https://en.wikipedia.org/wiki/List_of_supernovae" target="_blank" rel="noopener noreferrer">List of supernovae</a> wiki page.
<li><a href="http://ishivvers.com/maps/sne" target="_blank" rel="noopener noreferrer">A History of Supernova Discovery</a>: анимация.
<li><a href="https://en.wikipedia.org/wiki/SN_1885A" target="_blank" rel="noopener noreferrer">SN 1885A (S And)</a> в M31, открыта 17.08.1885, блеск в пике <b>5.85</b> (21.08.1985).
<li><a href="https://en.wikipedia.org/wiki/SN_1972E" target="_blank" rel="noopener noreferrer">SN 1972E</a> в NGC 5253, открыта (06)13.05.1972, блеск в пике ~<b>8.5</b>.
<li><a href="https://en.wikipedia.org/wiki/SN_1987A" target="_blank" rel="noopener noreferrer">SN 1987A</a> в Большом Магеллановом Облаке, открыта в ночь 23–24.02.1987, блеск в пике <b>2.9</b> (10.05.1987).
  <a href="https://rochesterastronomy.org/snimages/sn1987a.html" target="_blank" rel="noopener noreferrer">Страница на rochesterastronomy.org/snimages/</a>
<li><a href="https://en.wikipedia.org/wiki/SN_2011fe" target="_blank" rel="noopener noreferrer">SN 2011fe</a>, в M101, открыта 24.08.2011 по снимкам 22 и 23 августа 2011. Блеск в пике <b>9.9</b> (13.09.2011).
<li><a href="https://sne.space/statistics/" target="_blank" rel="noopener noreferrer">The Open Supernova Catalog</a>.
  The catalog includes metadata for 58,901 supernovae with 595,032 individual photometric detections and 22,472 individual spectra.<br>
  372 <a href="https://sne.space/statistics/host-galaxies/" target="_blank" rel="noopener noreferrer">SNe in Milky Way</a>, 322 SNe in M83, 214 SNe in M33, 162 SNe in M31, 154 SNe in NGC 2403, 103 SNe in NGC 4214, 81 SNe in NGC 4449, 78 SNe in NGC 4564.
</ul>
"""

try:
    with open(PICKLE_SN_FILENAME, 'rb') as fl:
        snstats_prev = pickle.load(fl)

    for year in snstats_prev:
        if snstats.get(year) != snstats_prev.get(year):
            print(snstats_prev.get(year), snstats.get(year))

    with open(PICKLE_SN_FILENAME, 'wb') as fl:
        pickle.dump(snstats, fl)
except FileNotFoundError:
    print("File", PICKLE_SN_FILENAME, "not found, continue")

# WDS_DATE, WDS_NUM = cds_readme_stats(WDS_URL)
# CDS_HTML = f"""<p>The <a href="{WDS_URL}">Washington Visual Double Star Catalog</a> (WDS) update on {WDS_DATE} {WDS_NUM} binaries.</p>
# """

soup = get_soup_Request(SIMBAD_URL)
SIMDATE, SIMSTAT = simbad_stats(soup)

SIMBAD_HTML = f"""<hr><p><a href="{SIMBAD_URL}">SIMBAD</a> <a href="https://en.wikipedia.org/wiki/SIMBAD">Astronomical Database</a> of objects beyond the Solar System – CDS (Strasbourg).<br>
Последнее обновление <b>{SIMDATE}</b> содержит:</p>
<ul>
<li>{SIMSTAT['objects']} объектов
<li>{SIMSTAT['identifiers']} идентификаторов
<li>{SIMSTAT['bibliographic references']} библиографических ссылок
<li>{SIMSTAT['citations of objects in papers']} цитирований объектов в статьях
</ul>
"""

try:
    with open(PICKLE_SIMB_FILENAME, 'rb') as fl:
        simbstats_dict = pickle.load(fl)
except FileNotFoundError:
    print("File", PICKLE_SIMB_FILENAME, "not found, continue")
    simbstats_dict = {}

if SIMDATE not in simbstats_dict:
    simbstats_dict[SIMDATE] = SIMSTAT

print("Number of dates in pickle file:", len(simbstats_dict))

with open(PICKLE_SIMB_FILENAME, 'wb') as fl:
    pickle.dump(simbstats_dict, fl)

with open(HTML_FILENAME, 'w', encoding="utf8") as fl:
    print(HEAD + snstats_txt + SIMBAD_HTML + TAIL, file=fl)
