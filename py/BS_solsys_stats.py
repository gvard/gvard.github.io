"""Python script for genererating an html page
with solar system statistics.
"""

import pickle
import urllib.request
import os
from bs4 import BeautifulSoup


PICKLE_FILENAME = "radar_obj_names.pickle"
ECHO_URL = "https://echo.jpl.nasa.gov/asteroids/"
MPC_URL = "https://minorplanetcenter.net/mpc/summary"
MP_NAMES_URL = "https://minorplanetcenter.net/iau/lists/MPNames.html"
SSD_URL = "https://ssd.jpl.nasa.gov/?body_count"
JOHNSTON_ASTEROID_MOONS_URL = "http://www.johnstonsarchive.net/astro/asteroidmoons.html"
JOHNSTON_SOLSYS_URL = "http://www.johnstonsarchive.net/astro/sslistnew.html"

HEAD = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Статистика тел Солнечной системы</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
"""
TAIL = """
</body>
</html>
"""


def get_soup(url):
    """get url, return BeautifulSoup object"""
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')

def get_echo(soup):
    """Parse html, get date of last page update,
    statistics of radar-detected asteroids."""
    number = int(soup.findAll("h1")[0].text.split()[0])
    lastupd = soup.findAll("font", {"size" : "-1"})
    lastupdate = lastupd[0].text.split("\n")[-2].split()
    last_update = (int(lastupdate[2]), lastupdate[3], int(lastupdate[4]))
    statstr = soup.findAll("th")[:4]
    mba_nea_co = [int(f.text.strip().split()[0]) for f in statstr]
    radar_obj_names = [f.text.strip() for f in soup.findAll("b")]
    print(len(radar_obj_names)-1, number, sum(mba_nea_co))
    return number, mba_nea_co, radar_obj_names, last_update


soup = get_soup(ECHO_URL)
NUMBER, (MBA, NEA, CO), RADAR_OBJ_NAMES, (YR, MON, DAY) = get_echo(soup)
ECHO_JPL_STATS = f"""<h2>Астероиды и кометы, измеренные при помощи радара</h2>
<p><a href="{ECHO_URL}">Asteroid radar research</a>, NASA Jet Propulsion Laboratory, Caltech.</p>
<p><b>{NUMBER} Radar-Detected Asteroids and Comets.</b></p><p>Последнее обновление: {DAY} {MON} {YR}.</p>
<ul>
<li>{MBA} астероидов главного пояса,
<li>{NEA} околоземных астероидов,
<li>{CO} комет.
</ul>
"""

with open(PICKLE_FILENAME, 'wb') as handle:
    pickle.dump(RADAR_OBJ_NAMES, handle)

#RADAR_ASTEROIDS_URL = "http://www.johnstonsarchive.net/astro/radarasteroids.html"
#SSS_DATA_URL = "http://www.johnstonsarchive.net/astro/sssatellitedata.html"
#SSPHYS_URL = "http://www.johnstonsarchive.net/astro/solar_system_phys_data.html"
#CONT_BIN_URL = "http://www.johnstonsarchive.net/astro/contactbinast.html"

def get_astermoons(soup):
    """Parse html, get date of last page update,
    statistics of asteroids with moons."""
    cutbrack = lambda txt: [f.split()[0] for f in txt.split("(")]
    lastupd = soup.findAll("center")[0].text.split("\n")[-1].split()
    last_update = (lastupd[2], lastupd[3], lastupd[-1])
    stats = soup.findAll("p")[3].text.split("\n")
    curcount = stats[1]
    num_obj, multipl_str = curcount.split(":")[1:3]
    multip_lst = [f.strip().split()[0] for f in multipl_str.split(",")]
    multip_lst.append(curcount.split(":")[2].split(";")[1].strip().split()[0])
    num_obj = int(num_obj.split()[0])
    nea = cutbrack(stats[3].strip(", \r"))
    mca = cutbrack(stats[4].strip(", \r"))
    mba = cutbrack(stats[5].strip(", \r"))
    mba_dualcomet = int(stats[5].split(";")[1].strip().split()[0])
    jta = int(stats[6].strip(", and \r").split()[0])
    tno = cutbrack(stats[7].strip(". \r"))
    tno.append(stats[7].split(",")[1].strip().split()[0])
    tno.append(stats[7].split(";")[1].strip().split()[2])
    return last_update, (num_obj, multip_lst), (nea, mca, mba, mba_dualcomet, jta, tno)


soup = get_soup(JOHNSTON_ASTEROID_MOONS_URL)
(DAY, MON, YR), (NUM_OBJ, MULTIPLICITY), (NEA, MCA, MBA, MBA_DUALCOMET, JTA, TNO) = get_astermoons(soup)

JOHNSTON_SAT = f"""<h2>Астероиды со спутниками</h2>
<p>by <a href="http://www.johnstonsarchive.net/astro/asteroidmoons.html">Wm.
Robert Johnston</a>. Последнее обновление: {DAY} {MON} {YR}.</p>
<p><b>{NUM_OBJ} астероидов и транснептуновых объектов со спутниками:
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
</ul>"""


def get_mp_names(soup):
    """Get list of all minor planet names."""
    names_text = soup.findAll("pre")[0].text
    names = names_text.split('\n')
    return names

def get_mpcstats(soup):
    """Get minor planet center statistics."""
    td_with_numbers = soup.findAll("td", {"class": "cj"})
    #observations_number = int(td_with_numbers[0].text)
    mpc_stat_numbers = [int(f.text) for f in td_with_numbers[:5]]
    td_mono_numbers = soup.findAll("td", {"class": "rj-mono"})
    mid_outer_numbers = [int(f.text) for f in td_mono_numbers[6:10]]
    nea_numbers = [int(f.text) for f in td_mono_numbers[11:15]]
    return mpc_stat_numbers, mid_outer_numbers, nea_numbers


soup = get_soup(MP_NAMES_URL)
MP_NAMES = get_mp_names(soup)

soup = get_soup(MPC_URL)
MPC_STAT_NUMBERS, MID_OUTER_NUMBERS, NEA_NUMBERS = get_mpcstats(soup)
OBSERV_NUM, OBJ_NUM, NUMBERED_NUM, UNNUMBERED_NUM, COMETS_NUM = MPC_STAT_NUMBERS
MBA, HILDAS, JUP_TROJANS, DISTANT = MID_OUTER_NUMBERS
NEA, NEA1KM, PHA, NEC = NEA_NUMBERS
MPC_STATS = f'''<h2>Статистика тел Солнечной системы</h2>
<p><a href="https://minorplanetcenter.net/mpc/summary">Центра Малых планет</a></p>
<ul>
<li>{OBSERV_NUM} наблюдений</li>
<li>{OBJ_NUM} объектов всего</li>
<li>{NUMBERED_NUM} нумерованных малых планет</li>
<li>{UNNUMBERED_NUM} ненумерованных малых планет</li>
<li>{COMETS_NUM} комет</li>
<li>{len(MP_NAMES)-2} <a href="{MP_NAMES_URL}">малых планет с именами</a></li>
<li>{MBA} астероидов основного пояса, {HILDAS} астероидов семейства Хильды, {JUP_TROJANS} троянцев Юпитера, {DISTANT} объектов за орбитой Юпитера</li>
<li>{NEA} околоземных астероидов, из них {NEA1KM} больше 1 км, {PHA} потенциально опасных астероидов, {NEC} околоземных комет</li>
</ul>
<p><a href="https://minorplanetcenter.net/iau/lists/t_tnos.html">Список транснептуновых объектов</a><br>
Распределение малых планет, количество в зависимости от большой полуоси орбиты:<br>
<img alt="Distribution of the Minor Planets: Semimajor Axis" src="https://minorplanetcenter.net/iau/plot/OrbEls01.gif"><br>
<a href="https://en.wikipedia.org/wiki/Kirkwood_gap" target="_blank" rel="noopener noreferrer"><img alt="Diagram showing inner, middle and outer main-belt asteroids" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Kirkwood_Gaps.svg/994px-Kirkwood_Gaps.svg.png"></a>
</p><br>
<a href="{JOHNSTON_SOLSYS_URL}">Альтернативная статистика Johnston's Archive</a>.
'''


def get_ssdtats(soup):
    """Get statistics from Solar System Dynamics page."""
    td_with_numbers = soup.findAll("td", {"align": "right"})
    ssd_numbers = [int(f.text.replace(',', '')) for f in td_with_numbers[1:8]]
    last_upd = soup.findAll("td", {"align": "left"})[-1].text
    return ssd_numbers, last_upd


soup = get_soup(SSD_URL)
SSD_NUMBERS, LAST_UPD = get_ssdtats(soup)
SATELLITES, COMETS, COM_NUM, COM_UNNUM, ASTEROIDS, AST_NUM, AST_UNNUM = SSD_NUMBERS
SSD_STATS = f'''<h2>Статистика тел Солнечной системы</h2>
<p><a href="https://ssd.jpl.nasa.gov/?body_count">группы динамики Солнечной системы</a>.
Последнее обновление: {LAST_UPD}.
<ul>
<li>{SATELLITES} спутников планет (включая Луну и спутники Плутона);</li>
<li>{COMETS} комет, {COM_NUM} numbered, {COM_UNNUM} unnumbered;</li>
<li>{ASTEROIDS} астероидов, {AST_NUM} numbered, {AST_UNNUM} unnumbered.</li>
</ul>
'''

with open(os.path.join(os.pardir, 'solarsystem', 'stats.html'), 'w', encoding="utf8") as handle:
    print(HEAD + MPC_STATS + SSD_STATS + ECHO_JPL_STATS + JOHNSTON_SAT + TAIL, file=handle)

HTML_ECHO = """
<ul>

<font size="-1">
(This web site is primarily a data-organization and communications tool
that supports ongoing research by JPL scientists and our colleagues.)
<p>
Last update: 2019 December 17
</font><p>

Also see:
  <DT><A HREF="PDS.asteroid.radar.history.html">
CHRONOLOGICAL HISTORY OF ASTEROID RADAR DETECTIONS (TABLE)</A> 
  <DT><A HREF="http://echo.jpl.nasa.gov/~lance/Radar_detected_neas.html">
Chronological history of asteroid radar detections (graphs)</A>
  <DT><A HREF="asteroid_radar_highlights.txt">
Asteroid radar highlights</A>
  <DT><A HREF="http://echo.jpl.nasa.gov/~lance/asteroid_radar_properties.html">
Summary of asteroid radar properties</A>
  <DT><A HREF="http://echo.jpl.nasa.gov/~lance/nea_elongations.html">
NEA elongations from radar observations</A>
  <DT><A HREF="http://echo.jpl.nasa.gov/~lance/small.neas.html">
Very small radar-detected NEAs</A>
  <DT><A HREF="http://echo.jpl.nasa.gov/~lance/radar.NEA.periods.html">
Radar-detected NEAs: Rotation periods and upcoming optical apparitions</A>
  <DT><A HREF="http://echo.jpl.nasa.gov/~lance/future.radar.NEA.periods.html">
Future NEA radar targets: Rotation periods and upcoming optical apparitions</A>
</ul>"""

#htmlz = """<body>
# <center>
# <b><h3>Radar-detected asteroids with radar-measured parameters</h3></b>
# compiled by Wm. Robert Johnston<br>
# last updated 25 May 2019</p><p>
# </center>
# </p><p><hr></p><p>
# The table below lists all asteroids detected by the NASA JPL asteroid radar program
#(from <a href=http://echo.jpl.nasa.gov/asteroids/PDS.asteroid.radar.history.html>this listing</a>),
#here ordered by permanent number and provisional designation.
#It also lists selected radar-measured parameters.
#Objects listed include 980 asteroids plus 60 secondary or tertiary components of multiple systems.
#Diameter measurements or constraints are available for 376 objects
#(335 asteroids plus 41 additional components).
# </p><p>
# """
