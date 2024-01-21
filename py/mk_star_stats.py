"""Python script for genererating an html page with lists and a bar chart with
supernovae statistics.

Data sources:
David Bishop, Latest Supernovae Archives
https://rochesterastronomy.org/snimages/archives.html
Transient Name Server https://www.wis-tns.org/stats-maps
SIMBAD Astronomical Database statistics https://simbad.u-strasbg.fr/simbad/
"""

import os
import urllib.request
from datetime import datetime
import locale

from beautifulsoup_supply import TAIL, mk_head, get_soup_Request


HEAD = mk_head("Статистика звездных каталогов", style="../../compact.css",
               script="") + "<body>\n"
WDS_URL = "http://cdsarc.u-strasbg.fr/viz-bin/ReadMe/B/wds?format=html"
SIMBAD_URL = "https://simbad.u-strasbg.fr/simbad/"
SNIMAGES_URL = "https://rochesterastronomy.org/snimages/"
SNOTHER_URL = SNIMAGES_URL + "snother.html"
SNSTATS_URL = SNIMAGES_URL + "archives.html"
NOVASTATS_URL = SNIMAGES_URL + "novastatsall.html"

TNS_URL = "https://www.wis-tns.org"
TNS_STATS_URL = TNS_URL + "/stats-maps"
PICKLE_SIMB_FILENAME = "simbad_stats.pickle"
PICKLE_SN_FILENAME = "snstats.pickle"
HTML_FILENAME = os.path.join(os.pardir, "stars", "stats", "index.html")
SIMBAD_LST = ["objects", "identifiers", "bibliographic references",
              "citations of objects in papers", "acronyms described for Simbad"]


def cds_readme_stats(url):
    html = urllib.request.urlopen(url).readlines()
    last_line = str(html[-23]).split()[2:5]
    return last_line[0], int(last_line[2])


def get_snstats(soup, end=23):
    pre = soup.find("pre").text
    return pre.splitlines()[1:end]


def get_sn_count(txt):
    """Get Supernova total count"""
    return (int(txt[0].split()[4]), int(txt[1].split()[0]),
            int(txt[5].split()[0]), int(txt[6].split()[0]),
            )


def get_tns(soup):
    all_stat_num = soup.findAll("div", {"class": "stat-item-right"})
    all_transient = int(all_stat_num[0].text.replace(",", ""))
    public_transient = int(all_stat_num[1].text.replace(",", ""))
    classified = int(all_stat_num[2].text.replace(",", ""))
    spectra = int(all_stat_num[3].text.replace(",", ""))
    return all_transient, public_transient, classified, spectra


def simbad_stats(soup):
    tdsbg = soup.findAll("td", {"bgcolor": "#3264A0"})
    for tdbg in tdsbg:
        if tdbg.text.strip() == "Statistics":  # len(result.attrs) == 5
            tbody = tdbg.parent.parent
            tds = tbody.findAll("td")
            break
    simbstats_dct = {}
    for i, td in enumerate(tds):
        if "Simbad contains on" in td.text:
            simdate = td.i.text.strip()
            continue
        for tabstr in SIMBAD_LST:
            if tabstr == td.text.strip():
                simbstats_dct[tabstr] = int(tds[i - 1].text.strip().replace(",", ""))
    return simdate, simbstats_dct


snurls = []
snurls.append((1995, f"{SNIMAGES_URL}snstatsother.html"))
for year in range(1996, 1999):
    snstats_year = f"{SNIMAGES_URL}snstats{year}.html"
    snurls.append((year, snstats_year))
snurls.append((1999, f"{SNIMAGES_URL}sn1999/snstats.html"))

for year in range(2000, 2025):
    snstats_year = f"https://rochesterastronomy.org/sn{year}/snstats.html"
    snurls.append((year, snstats_year))
snurls.append(("all", f"{SNIMAGES_URL}snstatsall.html"))

snstats = {}
locale.setlocale(locale.LC_ALL, "ru_RU")
today = datetime.now()
MONTH, YEAR = today.strftime("%B"), today.year
snstats_txt = f"""<h2><a href="{SNSTATS_URL}">Статистика вспышек сверхновых</a></h2>
<ul>
"""
years, sns, snalt, all_sne = [], [], [], []
years_dt = []
all_sn_count, sn_amateur_count = 0, 0
for year, snstats_url in snurls:
    try:
        soup = get_soup_Request(snstats_url)
    except urllib.error.URLError:
        print("break")
        break
    snstats[year] = get_snstats(soup)
    sn_num, sn_cbat, sn_amateur, sn_13th = get_sn_count(snstats[year])
    all_sn_count += sn_num
    sn_amateur_count += sn_amateur
    if year == 1995:
        all_sne.append(all_sn_count)
        snstats_txt += f'<li><a href="{snstats_url}" target="_blank" rel="noopener noreferrer">До 1996 года</a> открыто <b>{sn_num}</b> сверхновых, <b>{sn_amateur_count}</b> – любителями, <b>{sn_13th}</b> ярче 13-й зв. вел. (<a href="{SNOTHER_URL}">яркие сверхновые до 1996 года</a>)</li>\n'
        years.append(year)
        years_dt.append(datetime(year + 1, 1, 1))
        sns.append(sn_num - sn_amateur)
        snalt.append(sn_amateur)
    elif year != "all":
        all_sne.append(all_sn_count)
        snstats_txt += f'<li><a href="{snstats_url}" target="_blank" rel="noopener noreferrer">За {year} год</a> открыто <b>{sn_num}</b> сверхновых, <b>{sn_amateur}</b> – любителями, <b>{sn_13th}</b> ярче 13-й зв. вел. Всего к концу года открыто <b>{all_sn_count}</b>, <b>{sn_amateur_count}</b> – любителями</li>\n'
        if year == YEAR:
            years_dt.append(today)
        else:
            years_dt.append(datetime(year + 1, 1, 1))
        years.append(year)
        sns.append(sn_num - sn_amateur)
        snalt.append(sn_amateur)
    else:
        snstats_txt += f"""<li><a href="{snstats_url}" target="_blank" rel="noopener noreferrer">Всего открыто</a> <b>{sn_num}</b> сверхновых, <b>{sn_amateur}</b> – любителями, <b>{sn_13th}</b> ярче 13-й зв. вел.</li>\n"""

soup = get_soup_Request(TNS_STATS_URL)
all_transient, public_transient, classified, spectra = get_tns(soup)

snstats_txt += f"""</ul>
<a href="../snstats/">Статистика сверхновых и транзиентов</a> на отдельной странице
<h2><a href="{TNS_STATS_URL}" target="_blank" rel="noopener noreferrer">статистика</a>
  <a href="{TNS_URL}" target="_blank">Transient Name Server</a></h2>
<img src="https://github.com/gvard/astrodata/raw/main/plots/stars/transient_stats_bar_chart-ru.png" alt=""><br>
<ul>
<li>Всего транзиентов с 01.01.2016: <b>{all_transient}</b>, <b>{public_transient}</b> в открытом доступе</li>
<li>Сверхновых классифицировано: <b>{classified}</b></li>
<li>Всего спектров: <b>{spectra}</b></li>
</ul>

<h2>Ссылки</h2>
<ul>
<li><a href="https://www.wis-tns.org">Transient Name Server</a>
  <a href="https://www.wis-tns.org/stats-maps" target="_blank" rel="noopener noreferrer">stats</a></li>
<li><a href="{NOVASTATS_URL}" target="_blank" rel="noopener noreferrer">Статистика новых звезд</a></li>
<li><a href="{SNIMAGES_URL + 'lbvlist.html'}" target="_blank" rel="noopener noreferrer">List of supernova impostors</a> – LBV's
  (<a href="https://en.wikipedia.org/wiki/Luminous_blue_variable" target="_blank" rel="noopener noreferrer">Luminous Blue Variables</a>).</li>
</ul>
"""

WDS_DATE, WDS_NUM = cds_readme_stats(WDS_URL)
CDS_HTML = f"""<p>The <a href="{WDS_URL}">Washington Visual Double Star Catalog</a>
(WDS) update on {WDS_DATE} {WDS_NUM} binaries.</p>"""

soup = get_soup_Request(SIMBAD_URL)
SIMDATE, SIMSTAT = simbad_stats(soup)

SIMBAD_HTML = f"""<hr><p><a href="{SIMBAD_URL}">SIMBAD</a>
<a href="https://en.wikipedia.org/wiki/SIMBAD">Astronomical Database</a> of
objects beyond the Solar System – CDS (Strasbourg).<br>
Последнее обновление <b>{SIMDATE}</b> содержит:</p>
<ul>
<li>{SIMSTAT['objects']} объектов</li>
<li>{SIMSTAT['identifiers']} идентификаторов</li>
<li>{SIMSTAT['bibliographic references']} библиографических ссылок</li>
<li>{SIMSTAT['citations of objects in papers']} цитирований объектов в статьях</li>
<li>{SIMSTAT['acronyms described for Simbad']} сокращений, описанных в Simbad</li>
</ul>
"""

with open(HTML_FILENAME, "w", encoding="utf8") as html_fname:
    print(HEAD + snstats_txt + SIMBAD_HTML + CDS_HTML + TAIL, file=html_fname)
