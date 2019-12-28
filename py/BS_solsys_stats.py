from bs4 import BeautifulSoup
#import pickle
import urllib.request
import os


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


def getecho(html):
    soup = BeautifulSoup(html, 'html.parser')
    number = int(soup.findAll("h1")[0].text.split()[0])
    lastupd = soup.findAll("font", {"size" : "-1"})
    lastupdate = lastupd[0].text.split("\n")[-2].split()
    yr, mon, day = int(lastupdate[2]), lastupdate[3], int(lastupdate[4])
    statstr = soup.findAll("th")[:4]
    (mba, nea, co) = [int(f.text.strip().split()[0]) for f in statstr]
    return number, (mba, nea, co), (yr, mon, day)


html = urllib.request.urlopen(ECHO_URL).read()
number, (mba, nea, co), (yr, mon, day) = getecho(html)
echo_jpl_stats = f"""<h2>Астероиды и кометы, измеренные при помощи радара</h2>
<p><a href="{ECHO_URL}">Asteroid radar research</a>, NASA Jet Propulsion Laboratory, Caltech.</p>
<p><b>{number} Radar-Detected Asteroids and Comets.</b></p><p>Последнее обновление: {day} {mon} {yr}.</p>
<ul>
<li>{mba} астероидов главного пояса,
<li>{nea} околоземных астероидов,
<li>{co} комет.
</ul>"""

#html = urllib.request.urlopen("http://www.johnstonsarchive.net/astro/radarasteroids.html").read()
#html = urllib.request.urlopen("http://www.johnstonsarchive.net/astro/sssatellitedata.html").read()
#html = urllib.request.urlopen("http://www.johnstonsarchive.net/astro/solar_system_phys_data.html").read()
#html = urllib.request.urlopen("http://www.johnstonsarchive.net/astro/contactbinast.html").read()

# htmlz = """<body>
# <center>
# <b><h3>Radar-detected asteroids with radar-measured parameters</h3></b>
# compiled by Wm. Robert Johnston<br>
# last updated 25 May 2019</p><p>
# </center>

# </p><p><hr></p><p>

# The table below lists all asteroids detected by the NASA JPL asteroid radar program (from <a href=http://echo.jpl.nasa.gov/asteroids/PDS.asteroid.radar.history.html>this listing</a>), here ordered by permanent number and provisional designation.  It also lists selected radar-measured parameters.  Objects listed include 980 asteroids plus 60 secondary or tertiary components of multiple systems.  Diameter measurements or constraints are available for 376 objects (335 asteroids plus 41 additional components).
# </p><p>
# """

def cutbrack(txt):
def getastermoons(html):
    soup = BeautifulSoup(html, 'html.parser')
    lastupd = soup.findAll("center")[0].text.split("\n")[-1].split()
    date = lastupd[2], lastupd[3], lastupd[-1]
    stats = soup.findAll("p")[3].text.split("\n")
    curcount = stats[1]
    allast, kratnost = curcount.split(":")[1:3]
    kratnost = [f.strip().split()[0] for f in kratnost.split(",")]
    kratnost.append(curcount.split(":")[2].split(";")[1].strip().split()[0])
    allast = int(allast.split()[0])
    nea = cutbrack(stats[3].strip(", \r"))
    mca = cutbrack(stats[4].strip(", \r"))
    mba = cutbrack(stats[5].strip(", \r"))
    mba_dualcomet = int(stats[5].split(";")[1].strip().split()[0])
    jta = int(stats[6].strip(", and \r").split()[0])
    tno = cutbrack(stats[7].strip(". \r"))
    tno.append(stats[7].split(",")[1].strip().split()[0])
    tno.append(stats[7].split(";")[1].strip().split()[2])
    return date, (allast, kratnost), (nea, mca, mba, mba_dualcomet, jta, tno)


html = urllib.request.urlopen(JOHNSTON_ASTEROID_MOONS_URL).read()
(day, mon, yr), (allast, kratnost), (nea, mca, mba, mba_dualcomet, jta, tno) = getastermoons(html)

johnston_sat = f"""<h2>Астероиды со спутниками</h2> <p>by <a href="http://www.johnstonsarchive.net/astro/asteroidmoons.html">Wm. Robert Johnston</a>. Последнее обновление: {day} {mon} {yr}.</p>
<p><b>{allast} астероидов и транснептуновых объектов со спутниками: {kratnost[0]} двойных, {kratnost[1]} тройных систем, {kratnost[2]} шестерная система (Плутон)); {kratnost[3]} компонентов всего:</b></p>
<ul>
<li>{nea[0]} околоземных астероидов ({nea[1]} с двумя спутниками каждый).
<li>{mca[0]} астероидов, пересекающих орбиту Марса ({mca[1]} с двумя спутниками).
<li>{mba[0]} астероидов главного пояса ({mba[1]} с двумя спутниками каждый, {mba_dualcomet} binary with dual comet designation).
<li>{jta} троянских астероидов Юпитера.
<li>{tno[0]} транснептуновых объектов ({tno[1]} с двумя спутниками, {tno[2]} с пятью спутниками; count excludes {tno[3]} object with rings).</ul>"""


def getmpnames(html):
    soup = BeautifulSoup(html, 'html.parser')
    names_text = soup.findAll("pre")[0].text
    names = names_text.split('\n')
    return names

def getmpcstats(html):
    soup = BeautifulSoup(html, 'html.parser')
    td_with_numbers = soup.findAll("td", {"class": "cj"})
    observations = int(td_with_numbers[0].text)
    (objects, numbered, unnumbered, comets) = [int(f.text.strip()) for f in td_with_numbers[1:5]]
    return observations, (objects, numbered, unnumbered, comets)


html = urllib.request.urlopen(MP_NAMES_URL).read()
mpnames = getmpnames(html)


html = urllib.request.urlopen(MPC_URL).read()
observations, (objects, numbered, unnumbered, comets) = getmpcstats(html)
mpc_stats = f'''<h2>Статистика тел Солнечной системы</h2>
<p><a href="https://minorplanetcenter.net/mpc/summary">Центра Малых планет</a></p>
<ul>
<li>{observations} наблюдений</li>
<li>{objects} объектов всего</li>
<li>{numbered} нумерованных малых планет</li>
<li>{unnumbered} ненумерованных малых планет</li>
<li>{comets} комет</li>
<li>{len(mpnames)-2} <a href="{MP_NAMES_URL}">малых планет с именами</a></li>
</ul>
<p><a href="https://minorplanetcenter.net/iau/lists/t_tnos.html">Список транснептуновых объектов</a><br>
Распределение малых планет, количество в зависимости от большой полуоси орбиты:<br>
<img alt="Distribution of the Minor Planets: Semimajor Axis" src="https://minorplanetcenter.net/iau/plot/OrbEls01.gif"><br>
<a href="https://en.wikipedia.org/wiki/Kirkwood_gap" target="_blank" rel="noopener noreferrer"><img alt="Diagram showing inner, middle and outer main-belt asteroids" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Kirkwood_Gaps.svg/994px-Kirkwood_Gaps.svg.png"></a>
</p><br>
<a href="{JOHNSTON_SOLSYS_URL}">Альтернативная статистика Johnston's Archive</a>.
'''


def getssdtats(html):
    soup = BeautifulSoup(html, 'html.parser')
    td_with_numbers = soup.findAll("td", {"align": "right"})
    satellites = int(td_with_numbers[1].text)
    return satellites


html = urllib.request.urlopen(SSD_URL).read()
satellites = getssdtats(html)
ssd_stats = f'''<h2>Статистика тел Солнечной системы</h2> <p><a href="https://ssd.jpl.nasa.gov/?body_count">группы динамики Солнечной системы</a>.<br>
<ul>
<li>{satellites} спутников планет (включая Луну и спутники Плутона)</li>
</ul>
'''

with open(os.path.join(os.pardir, 'solarsystem', 'stats.html'), 'w', encoding="utf8") as handle:
    print(HEAD + mpc_stats + ssd_stats + echo_jpl_stats + johnston_sat + TAIL, file=handle)

html_echo = """
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
  <DT><A HREF="http://echo.jpl.nasa.gov/~lance/radar.nea.periods.html">
Radar-detected NEAs: Rotation periods and upcoming optical apparitions</A>
  <DT><A HREF="http://echo.jpl.nasa.gov/~lance/future.radar.nea.periods.html">
Future NEA radar targets: Rotation periods and upcoming optical apparitions</A>

</ul>"""
