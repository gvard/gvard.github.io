import os
import pickle
import urllib.request

from beautifulsoup_supply import TAIL, mk_head, get_soup


HEAD = mk_head("Статистика звездных каталогов", script="") + "<body>\n"
WDS_URL = "http://cdsarc.u-strasbg.fr/viz-bin/ReadMe/B/wds?format=html"
SIMBAD_URL = "http://simbad.u-strasbg.fr/simbad/"
SNIMAGES_URL = "http://rochesterastronomy.com/snimages/"
SNIMAGES_SNOTHER_URL = "http://rochesterastronomy.com/snimages/snother.html"
TNS_URL = "https://wis-tns.weizmann.ac.il"
TNS_STATS_URL = TNS_URL + "/stats-maps"
PICKLE_FILENAME = 'simbad_stats.pickle'
HTML_FILENAME = os.path.join(os.pardir, 'stars', 'stats.html')
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
    return int(txt[0].split()[4]), int(txt[1].split()[0]), int(txt[5].split()[0])

def get_tns(soup):
    all_stat_num = soup.findAll('div', {"class": "stat-item-right"})
    all_transient = int(all_stat_num[0].text)
    classified = int(all_stat_num[2].text)
    spectra = int(all_stat_num[3].text)
    return all_transient, classified, spectra

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

for year in range(2000, 2021):
    snstats_year = f'http://rochesterastronomy.com/sn{year}/snstats.html'
    snurls.append((year, snstats_year))
snurls.append(('all', f'{SNIMAGES_URL}snstatsall.html'))

snstats = {}
snstats_txt = f"""<hr><h2><a href="{SNIMAGES_URL}">Статистика вспышек сверхновых</a>:</h2>
<p><a href="{SNIMAGES_SNOTHER_URL}">Сверхновые до 1996 года</a>.</p>
<ul>
"""
all_sn_count, sn_amateur_count = 0, 0
for (year, snstats_url) in snurls:
    soup = get_soup(snstats_url)
    snstats[year] = get_snstats(soup)
    sn_num, sn_cbat, sn_amateur = get_sn_count(snstats[year])
    all_sn_count += sn_num
    sn_amateur_count += sn_amateur
    if year == 1995:
        snstats_txt += f"<li>До {year + 1} года открыто <b>{sn_num}</b> сверхновых, <b>{sn_amateur_count}</b> &ndash; любителями.</li>\n"
    elif year != "all":
        snstats_txt += f"<li>За {year} год открыто <b>{sn_num}</b> сверхновых, <b>{sn_amateur}</b> &ndash; любителями. Всего к концу года открыто <b>{all_sn_count}</b>, <b>{sn_amateur_count}</b> &ndash; любителями.</li>\n"


soup = get_soup(TNS_STATS_URL)
all_transient, classified, spectra = get_tns(soup)

snstats_txt += f"""</ul>
<a href="{SNIMAGES_URL}snstatsall.html" target="_blank" rel="noopener noreferrer">Всего открыто</a> <b>{sn_num}</b> сверхновых, <b>{sn_amateur}</b>  &ndash; любителями.</p>

<h2><a href="TNS_URL">Transient Name Server</a></h2>
<a href="{TNS_STATS_URL}" target="_blank" rel="noopener noreferrer">статистика</a>:<br>
<ul>
<li>Всего транзиентов с 01.01.2016: <b>{all_transient}</b></li>
<li>Сверхновых классифицировано: <b>{classified}</b></li>
<li>Всего спектров: <b>{spectra}</b></li>
</ul>

<h2>Ссылки</h2>
<ul>
<li><a href="http://rochesterastronomy.com/snimages/archives.html" target="_blank" rel="noopener noreferrer">Bright Supernova &ndash; Archives</a>,
  <a href="https://en.wikipedia.org/wiki/List_of_supernovae" target="_blank" rel="noopener noreferrer">List of supernovae</a> wiki page.</li>
<li><a href="http://ishivvers.com/maps/sne" target="_blank" rel="noopener noreferrer">A History of Supernova Discovery</a>: анимация.</li>
<li><a href="https://en.wikipedia.org/wiki/SN_1885A" target="_blank" rel="noopener noreferrer">SN 1885A (S And)</a> в M31, открыта 17.08.1885, блеск в пике <b>5.85</b> (21.08.1985).</li>
<li><a href="https://en.wikipedia.org/wiki/SN_1972E" target="_blank" rel="noopener noreferrer">SN 1972E</a> в NGC 5253, открыта (06)13.05.1972, блеск в пике ~<b>8.5</b>.</li>
<li><a href="https://en.wikipedia.org/wiki/SN_1987A" target="_blank" rel="noopener noreferrer">SN 1987A</a> в Большом Магеллановом Облаке, открыта в ночь 23&ndash;24.02.1987, блеск в пике <b>2.9</b> (10.05.1987).
  <a href="http://rochesterastronomy.com/snimages/sn1987a.html" target="_blank" rel="noopener noreferrer">Страница на rochesterastronomy.com/snimages/</a></li>
<li><a href="https://en.wikipedia.org/wiki/SN_2011fe" target="_blank" rel="noopener noreferrer">SN 2011fe</a>, в M101, открыта 24.08.2011 по снимкам 22 и 23 августа 2011. Блеск в пике <b>9.9</b> (13.09.2011).</li>
<li><a href="http://www.rochesterastronomy.org/snimages/lbvlist.html" target="_blank" rel="noopener noreferrer">List of supernova impostors</a> &ndash; LBV's (Luminous Blue Variables), <a href="https://en.wikipedia.org/wiki/Luminous_blue_variable">Luminous blue variable</a> wiki page.</li>
<li><a href="https://sne.space/statistics/" target="_blank" rel="noopener noreferrer">The Open Supernova Catalog</a>.
  The catalog includes metadata for 58,901 supernovae with 595,032 individual photometric detections and 22,472 individual spectra.<br>
  372 <a href="https://sne.space/statistics/host-galaxies/" target="_blank" rel="noopener noreferrer">SNe in Milky Way</a>, 322 SNe in M83, 214 SNe in M33, 162 SNe in M31, 154 SNe in NGC 2403, 103 SNe in NGC 4214, 81 SNe in NGC 4449, 78 SNe in NGC 4564.</li>
</ul>
"""

PICKLE_SN_FILENAME = 'snstats.pickle'
with open(PICKLE_SN_FILENAME, 'rb') as handle:
    snstats_prev = pickle.load(handle)

for year in snstats_prev:
     if snstats.get(year) != snstats_prev.get(year):
         print(snstats_prev.get(year), snstats.get(year))

with open(PICKLE_SN_FILENAME, 'wb') as handle:
    pickle.dump(snstats, handle)


# WDS_DATE, WDS_NUM = cds_readme_stats(WDS_URL)
# CDS_HTML = f"""<p>The <a href="{WDS_URL}">Washington Visual Double Star Catalog</a> (WDS) update on {WDS_DATE} {WDS_NUM} binaries.</p>
# """

soup = get_soup(SIMBAD_URL)
SIMDATE, SIMSTAT = simbad_stats(soup)

SIMBAD_HTML = f"""<hr><p><a href="{SIMBAD_URL}">SIMBAD</a> <a href="https://en.wikipedia.org/wiki/SIMBAD">Astronomical Database</a> of objects beyond the Solar System &ndash; CDS (Strasbourg).<br>
Последнее обновление <b>{SIMDATE}</b> содержит:</p>
<ul>
<li>{SIMSTAT['objects']} объектов</li>
<li>{SIMSTAT['identifiers']} идентификаторов</li>
<li>{SIMSTAT['bibliographic references']} библиографических ссылок</li>
<li>{SIMSTAT['citations of objects in papers']} цитирований объектов в статьях</li>
</ul>
"""

try:
    with open(PICKLE_FILENAME, 'rb') as handle:
        simbstats_dict = pickle.load(handle)
except Exception:
    simbstats_dict = {}

if SIMDATE not in simbstats_dict:
    simbstats_dict[SIMDATE] = SIMSTAT

print("Number of dates in pickle file:", len(simbstats_dict))

with open(PICKLE_FILENAME, 'wb') as handle:
    pickle.dump(simbstats_dict, handle)

with open(HTML_FILENAME, 'w', encoding="utf8") as handle:
    print(HEAD + snstats_txt + SIMBAD_HTML + TAIL, file=handle)
