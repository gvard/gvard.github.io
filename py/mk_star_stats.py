import os
import pickle

from beautifulsoup_supply import TAIL, mk_head, get_soup


HEAD = mk_head("Статистика звездных каталогов", script="") + "<body>\n"
WDS_URL = "http://cdsarc.u-strasbg.fr/viz-bin/ReadMe/B/wds?format=html"
SIMBAD_URL = "http://simbad.u-strasbg.fr/simbad/"
PICKLE_FILENAME = 'simbad_stats.pickle'
HTML_FILENAME = os.path.join(os.pardir, 'stars', 'stats.html')
SIMBAD_LST = ['objects', 'identifiers', 'bibliographic references', 'citations of objects in papers']


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
    print(HEAD + SIMBAD_HTML + TAIL, file=handle)
