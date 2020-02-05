import os
import pickle
import urllib.request

from beautifulsoup_supply import TAIL, mk_head, get_soup


HEAD = mk_head("Статистика звездных каталогов", script="") + "<body>\n"
WDS_URL = "http://cdsarc.u-strasbg.fr/viz-bin/ReadMe/B/wds?format=html"
SIMBAD_URL = "http://simbad.u-strasbg.fr/simbad/"
SNIMAGES_URL = "http://rochesterastronomy.com/snimages/"
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
    return int(txt[0].split()[4])

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
for year in range(1996, 1999):
    snstats_year = f'{SNIMAGES_URL}snstats{year}.html'
    snurls.append((year, snstats_year))
snurls.append((1999, f'{SNIMAGES_URL}sn1999/snstats.html'))

for year in range(2000, 2021):
    snstats_year = f'http://rochesterastronomy.com/sn{year}/snstats.html'
    snurls.append((year, snstats_year))
snurls.append(('all', f'{SNIMAGES_URL}snstatsall.html'))

snstats = {}
snstats_txt = f"""<h2><a href="{SNIMAGES_URL}">Статистика вспышек сверхновых</a>:</h2>
<ul>
"""
for (year, snstats_url) in snurls:
    soup = get_soup(snstats_url)
    snstats[year] = get_snstats(soup)
    sn_num = get_sn_count(snstats[year])
    if year != "all":
        snstats_txt += f"<li>За {year} год открыто {sn_num} сверхновых</li>\n"

snstats_txt += f"""</ul>
<p>Всего открыто {sn_num} сверхновых.</p>
"""

PICKLE_SN_FILENAME = 'snstats.pickle'
with open(PICKLE_SN_FILENAME, 'rb') as handle:
    snstats_prev = pickle.load(handle)

for year in snstats_prev:
     if snstats[year] != snstats_prev[year]:
         print(snstats_prev[year], snstats[year])

with open(PICKLE_SN_FILENAME, 'wb') as handle:
    pickle.dump(snstats, handle)


WDS_DATE, WDS_NUM = cds_readme_stats(WDS_URL)
CDS_HTML = f"""<p>The <a href="{WDS_URL}">Washington Visual Double Star Catalog</a> (WDS) update on {WDS_DATE} {WDS_NUM} binaries.</p>
"""

soup = get_soup(SIMBAD_URL)
SIMDATE, SIMSTAT = simbad_stats(soup)

SIMBAD_HTML = f"""<p><a href="{SIMBAD_URL}">SIMBAD</a> <a href="https://en.wikipedia.org/wiki/SIMBAD">Astronomical Database</a> of objects beyond the Solar System &ndash; CDS (Strasbourg).<br>
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
    print(HEAD + SIMBAD_HTML + CDS_HTML + snstats_txt + TAIL, file=handle)
