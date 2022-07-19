"""Python script for genererating an html page
with solar system statistics.
"""

import pickle
import os
import ssl
import json
import urllib.request

from beautifulsoup_supply import TAIL, mk_head, get_soup


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

DEBUG = False
HEAD = mk_head("Статистика тел Солнечной системы",
            style="../compact.css",
            script="nea_size_bin_chart.js") + "<body>\n"
PICKLE_RADAR_FILENAME = "radar_obj_names.pickle"
ECHO_URL = "https://echo.jpl.nasa.gov/asteroids/"
MPC_URL = "https://minorplanetcenter.net/mpc/summary"
MP_NAMES_URL = "https://minorplanetcenter.net/iau/lists/MPNames.html"
SSD_BODY_COUNT_URL = "https://ssd.jpl.nasa.gov/dat/body_count.json"
NEO_SIZE_BIN_URL = 'https://cneos.jpl.nasa.gov/stats/size_bin.json'
NEOS_STATS_URL = 'https://cneos.jpl.nasa.gov/stats/totals.html'
JOHNSTON_ASTEROID_MOONS_URL = "http://www.johnstonsarchive.net/astro/asteroidmoons.html"
JOHNSTON_SOLSYS_URL = "http://www.johnstonsarchive.net/astro/sslistnew.html"


def get_echo(soup, debug=False):
    """Parse html, get date of last page update,
    statistics of radar-detected asteroids."""
    number = int(soup.findAll("h1")[0].text.split()[0])
    lastupd = soup.findAll("font", {"size": "-1"})
    lastupdate = lastupd[0].text.split("\n")[-2].split()
    last_update = (int(lastupdate[2]), lastupdate[3], int(lastupdate[4]))
    statstr = soup.findAll("th")[:4]
    mba_nea_co = [int(f.text.strip().split()[0]) for f in statstr]
    radar_obj_names = [f.text.strip() for f in soup.findAll("b")]
    if debug:
        print(len(radar_obj_names)-1, number, sum(mba_nea_co))
    return number, mba_nea_co, radar_obj_names, last_update


soup = get_soup(ECHO_URL)
NUMBER, (MBA, NEA, CO), RADAR_OBJ_NAMES, (YR, MON, DAY) = get_echo(soup, debug=DEBUG)
ECHO_JPL_STATS = f"""<h2>Астероиды и кометы, измеренные при помощи радара</h2>
<p><a href="{ECHO_URL}">Asteroid radar research</a>, NASA Jet Propulsion Laboratory, Caltech.</p>
<p><b>{NUMBER} Radar-Detected Asteroids and Comets.</b></p><p>Последнее обновление: {DAY} {MON} {YR}.</p>
<ul>
<li>{MBA} астероидов главного пояса,
<li>{NEA} околоземных астероидов,
<li>{CO} комет.
</ul>
<a href="https://echo.jpl.nasa.gov/lance/">Near-Earth Asteroid Files</a>:<br>
<img src="https://echo.jpl.nasa.gov/lance/radar_detected_neas_summary/nea.radar.history.jpg" alt=""><br>
<img src="https://echo.jpl.nasa.gov/lance/radar_detected_neas_summary/asteroid.radar.history.jpg" alt=""><br>
"""

try:
    with open(PICKLE_RADAR_FILENAME, 'wb') as fl:
        pickle.dump(RADAR_OBJ_NAMES, fl)
except FileNotFoundError:
    print("File", PICKLE_RADAR_FILENAME, "not found, continue")

#RADAR_ASTEROIDS_URL = "http://www.johnstonsarchive.net/astro/radarasteroids.html"
#SSS_DATA_URL = "http://www.johnstonsarchive.net/astro/sssatellitedata.html"
#SSPHYS_URL = "http://www.johnstonsarchive.net/astro/solar_system_phys_data.html"
#CONT_BIN_URL = "http://www.johnstonsarchive.net/astro/contactbinast.html"

def cut_brackets(txt, sign):
    """Cut bracket, comma or dot from string"""
    txt = txt.strip(sign + " \r")
    return [f.split()[0] for f in txt.split("(")]

def get_astermoons(soup):
    """Parse html, get date of last page update,
    statistics of asteroids with moons."""
    lastupd = soup.findAll("center")[0].text.split("\n")[4].split()
    last_update = (lastupd[2], lastupd[3], lastupd[-1])
    stats = soup.findAll("p")[3].text.split("\n")
    curcount = stats[1]
    num_obj, multipl_str = curcount.split(":")[1:3]
    multip_lst = [f.strip().split()[0] for f in multipl_str.split(",")]
    multip_lst.append(curcount.split(":")[2].split(";")[1].strip().split()[0])
    num_obj = int(num_obj.split()[0])
    nea = cut_brackets(stats[3], ",")
    mca = cut_brackets(stats[4], ",")
    mba = cut_brackets(stats[5], ",")
    mba_dualcomet = int(stats[5].split(";")[1].strip().split()[0])
    jta = int(stats[6].strip(", and \r").split()[0])
    tno = cut_brackets(stats[7], ".")
    tno.append(stats[7].split(",")[1].strip().split()[0])
    tno.append(stats[7].split(";")[1].strip().split()[2])
    return last_update, (num_obj, multip_lst), (nea, mca, mba, mba_dualcomet, jta, tno)


soup = get_soup(JOHNSTON_ASTEROID_MOONS_URL)
(DAY, MON, YR), (NUM_OBJ, MULTIPLICITY), \
    (NEA, MCA, MBA, MBA_DUALCOMET, JTA, TNO) = get_astermoons(soup)

JOHNSTON_SAT = f"""<h2>Астероиды со спутниками</h2>
<p>by <a href="http://www.johnstonsarchive.net/astro/asteroidmoons.html">Wm.
Robert Johnston</a>. Последнее обновление: {DAY} {MON} {YR}.</p>
<p><b>{NUM_OBJ} <a href="https://en.wikipedia.org/wiki/Minor-planet_moon">астероидов и транснептуновых объектов со спутниками</a>:
{MULTIPLICITY[0]} двойных, {MULTIPLICITY[1]} тройных систем, {MULTIPLICITY[2]} шестерная система (Плутон);
{MULTIPLICITY[3]} компонентов всего:</b></p>
<ul>
<li>{NEA[0]} околоземных астероидов ({NEA[1]} с двумя спутниками каждый).
<li>{MCA[0]} астероидов, пересекающих орбиту Марса ({MCA[1]} с двумя спутниками).
<li>{MBA[0]} астероидов главного пояса ({MBA[1]} с двумя спутниками каждый,
{MBA_DUALCOMET} binary with dual comet designation).
<li>{JTA} троянских астероидов Юпитера.
<li>{TNO[0]} транснептуновых объектов ({TNO[1]} с двумя спутниками,
{TNO[2]} с пятью спутниками; count excludes {TNO[3]} object with rings).
</ul>
"""


def get_mp_names(soup):
    """Get list of all minor planet names."""
    names_text = soup.findAll("pre")[0].text
    names_upd_date = soup.find("h2").next_sibling.split()[-3:]
    names = names_text.split('\n')
    return names, names_upd_date

def get_mpcstats(soup):
    """Get minor planet center statistics."""
    td_with_numbers = soup.findAll("td", {"class": "cj"})
    #observations_number = int(td_with_numbers[0].text)
    mpc_stat_numbers = [int(f.text) for f in td_with_numbers[:5]]
    td_mono_numbers = soup.findAll("td", {"class": "rj-mono"})
    inner_numbers = [int(f.text) for f in td_mono_numbers[:5]]
    mid_outer_numbers = [int(f.text) for f in td_mono_numbers[5:9]]
    nea_numbers = [int(f.text) for f in td_mono_numbers[10:14]]
    return mpc_stat_numbers, inner_numbers, mid_outer_numbers, nea_numbers


soup = get_soup(MP_NAMES_URL)
MP_NAMES, NAMES_UPD_DATE = get_mp_names(soup)

soup = get_soup(MPC_URL)
MPC_STAT_NUMBERS, INNER_NUMBERS, MID_OUTER_NUMBERS, NEA_NUMBERS = get_mpcstats(soup)
OBSERV_NUM, OBJ_NUM, NUMBERED_NUM, UNNUMBERED_NUM, COMETS_NUM = MPC_STAT_NUMBERS
#ATIRAS, ATENS, APOLLOS, AMORS, HUNGARIAS, MARS_CROSSERS = INNER_NUMBERS
ATIRAS = 28 # After 2022-02-01
ATENS, APOLLOS, AMORS, HUNGARIAS, MARS_CROSSERS = INNER_NUMBERS
MBA, HILDAS, JUP_TROJANS, DISTANT = MID_OUTER_NUMBERS
# NEA, NEA1KM, PHA, NEC = NEA_NUMBERS
NEC = 117
NEA, NEA1KM, PHA = NEA_NUMBERS


def get_ssnew(soup):
    """Get Johnston's Archive ssnew statistics."""
    ps = soup.findAll("p")
    man_made = ps[-4].text.strip()
    upd = ps[-1].text.split("\r\n")[2]
    comets_note = soup.findAll("blockquote")[1].text.strip()
    comets_note = f"<small>{ps[9].text.strip()}</small><br>\n{ps[-3].text.strip()}<br>\n{comets_note}"
    ssnew = ps[3].text.split("\r")[3:-1]
    ssnew = [x.split(":")[1] for x in ssnew]
    return upd, ssnew, comets_note, man_made

soup = get_soup(JOHNSTON_SOLSYS_URL)

UPD, (ASTER_SSNEW, OUTER_SSO, COMETS_SSNEW), COMETS_NOTE, MAN_MADE = get_ssnew(soup)
COM_ALL = COMETS_SSNEW.split("(")
COMETS_ALL = int(COM_ALL[0].replace(",", ""))
COMNUM, PROVDES, NODESIGNAT = COM_ALL[1].split(", ")

neo_size_bin_obj = urllib.request.urlopen(NEO_SIZE_BIN_URL)
if DEBUG:
    print(neo_size_bin_obj.info())
neo_size_bin = json.load(neo_size_bin_obj)
NEO_DATE, NEO_DATA = neo_size_bin.get('dataDate'), neo_size_bin.get('data')

MPC_STATS = f'''<h2>Статистика тел Солнечной системы</h2>
<p><a href="https://minorplanetcenter.net/mpc/summary">Центра Малых планет</a></p>
<ul>
<li>{OBSERV_NUM} наблюдений</li>
<li>{OBJ_NUM} объектов всего</li>
<li>Более {NUMBERED_NUM} <a href="https://minorplanetcenter.net/iau/lists/NumberedMPs.html">нумерованных</a> малых планет</li>
<li>{UNNUMBERED_NUM} ненумерованных малых планет</li>
<li>{COMETS_NUM} комет</li>
<li>Более {len(MP_NAMES)-2} <a href="{MP_NAMES_URL}">малых планет с именами</a> (последнее обновление списка: {" ".join(NAMES_UPD_DATE)})</li>
<li>{ATIRAS} <a href="https://en.wikipedia.org/wiki/Atira_asteroid">Атир</a>, {ATENS} <a href="https://en.wikipedia.org/wiki/Aten_asteroid">Атонов</a>, {APOLLOS} <a href="https://en.wikipedia.org/wiki/Apollo_asteroid">Аполлонов</a>, {AMORS} <a href="https://en.wikipedia.org/wiki/Amor_asteroid">Амуров</a>, {HUNGARIAS} <a href="https://en.wikipedia.org/wiki/Hungaria_asteroid">астероидов семейства Венгрии</a>, {MARS_CROSSERS} <a href="https://en.wikipedia.org/wiki/List_of_Mars-crossing_minor_planets">пересекающих орбиту Марса</a>;</li>
<li>{MBA} астероидов основного пояса, {HILDAS} <a href="https://en.wikipedia.org/wiki/Hilda_asteroid">астероидов семейства Хильды</a>, {JUP_TROJANS} <a href="https://en.wikipedia.org/wiki/Jupiter_trojan">троянцев Юпитера</a>, {DISTANT} объектов за орбитой Юпитера;</li>
<li>{NEA} <a href="https://en.wikipedia.org/wiki/Near-Earth_object#Near-Earth_asteroids">околоземных астероидов</a>, из них {NEA1KM} больше 1 км, {PHA} потенциально опасных астероидов, {NEC} <a href="https://en.wikipedia.org/wiki/Near-Earth_object#Near-Earth_comets">околоземных комет</a>.</li>
</ul>
<p><b>Всего в <a href="{NEOS_STATS_URL}" target="_blank" rel="noopener noreferrer">статистике околоземных астероидов</a> от {NEO_DATE}: {sum(NEO_DATA)}</b></p><br>
<div id="nea_size_bin_chart" style="width:600px; height:400px;"></div>
<script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
<script src="https://cneos.jpl.nasa.gov/js/vendor/highcharts/highcharts.js"></script>
<script src="https://cneos.jpl.nasa.gov/js/vendor/highcharts/exporting.js"></script>
<script src="https://cneos.jpl.nasa.gov/js/vendor/highcharts/themes/grid.js"></script>
<script>mkChart()</script>
<br>
<p>Распределение малых планет, количество в зависимости от большой полуоси (вертикальные линии - большие полуоси планет и щели Кирквуда):<br>
<a href="https://en.wikipedia.org/wiki/Kirkwood_gap" target="_blank" rel="noopener noreferrer">
<img src="images/mpc-ahist-202104.png" width="960" alt="Distribution of the Minor Planets: Semimajor Axis"></a>
</p>
<p><a href="https://minorplanetcenter.net/iau/lists/t_tnos.html">Список транснептуновых объектов</a></p><br>
<a href="{JOHNSTON_SOLSYS_URL}">Альтернативная статистика Johnston's Archive</a>, {UPD}:
<ul>
<li>Астероидов*: {ASTER_SSNEW},</li>
<li>Объектов внешней Солнечной системы*: {OUTER_SSO},</li>
<li>Комет**: {COMETS_ALL} ({COMNUM.split()[0]} numbered**, {PROVDES.split()[0]} with provisional designations, {NODESIGNAT.split()[0]} without official designations).</li>
<li>Искусственных объектов: {MAN_MADE}</li>
</ul>
{COMETS_NOTE}
'''


def get_ssdtats(body_count):
    """Get statistics from JPL's Solar System Dynamics group page."""
    sat = body_count.get('sat').get('count')
    ast = body_count.get('ast')
    com = body_count.get('com')
    ssd_numbers = [sat, com["total"], com["numbered"], com["unnumbered"],
        ast["total"], ast["numbered"], ast["unnumbered"]]
    last_upd = body_count.get('timestamp')
    return ssd_numbers, last_upd


body_count_obj = urllib.request.urlopen(SSD_BODY_COUNT_URL)
body_count = json.load(body_count_obj)
SSD_NUMBERS, LAST_UPD = get_ssdtats(body_count)
SATELLITES, COMETS, COM_NUM, COM_UNNUM, ASTEROIDS, AST_NUM, AST_UNNUM = SSD_NUMBERS
SSD_STATS = f'''<h2>Статистика тел Солнечной системы</h2>
<p><a href="https://ssd.jpl.nasa.gov/?body_count">группы динамики Солнечной системы</a>.
Последнее обновление: {LAST_UPD}.</p>
<ul>
<li>{SATELLITES} спутников планет (включая Луну и спутники Плутона);</li>
<li>{COMETS} комет, {COM_NUM} numbered, {COM_UNNUM} unnumbered;</li>
<li>{ASTEROIDS} астероидов, {AST_NUM} numbered, {AST_UNNUM} unnumbered.</li>
</ul>
'''

with open(os.path.join(os.pardir, 'solarsystem', 'stats.html'), 'w', encoding="utf8") as fl:
    print(HEAD + MPC_STATS + SSD_STATS + ECHO_JPL_STATS + JOHNSTON_SAT + TAIL, file=fl)


HEAD = mk_head("Статистика Солнечной системы", style="stats.css", script="../../stats.js")
BODY = f"""<body onload="mkHeader()">
<div id="stats" class="container show">
  <h1 id="header"></h1>
  <div class="list">
  <ul>
    <li>В Солнечной системе <span class="yellow">8</span> планет</li>
    <li><span class="yellow">{SATELLITES}</span> спутников планет</li>
    <li>Более <span class="yellow">{str(COMETS_NUM)[:-2]+'00'}</span> комет</li>
    <li>Более <span class="yellow">{str(MBA + NEA)[:-4]+'0.000'}</span> астероидов</li>
    <li>Только <span class="yellow">{str((len(MP_NAMES)-2)/1000)}</span> имеют имена</li>
  </ul>
  </div>
  <div id="footer">
    <h2>Центр Астрономического и&nbsp;космического образования</h2>
  </div>
</div>
"""
with open(os.path.join(os.pardir, 'solarsystem', 'stats', 'index.html'), 'w', encoding="utf8") as fl:
    print(HEAD + BODY + TAIL, file=fl)
