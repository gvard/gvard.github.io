"""Python script for reading online data with the parameters of
variable stars discovered by the team from Vorobyovy gory.
After parsing, the data is saved in the observing list for Stellarium
and in sortable HTML tables.
Data sources:
https://scan.sai.msu.ru/~denis/Paleo/paleo-var.html
https://scan.sai.msu.ru/~denis/Paleo/paleo-SNe.html
https://scan.sai.msu.ru/~denis/Var-ZTF.html
"""


import datetime
import json
from urllib import request
from urllib.request import Request

from bs4 import BeautifulSoup
import jdcal

from astro_const import CONSTELLATION_DCT, CONSTELLTN_RU_DCT


VSX_URLS = {
'Karachurin 12': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=477549",
'Karachurin 14': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=477652",
'Karachurin 15': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=477653",
'Karachurin 16': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=477654",
'LANAT 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=838298",
'LANAT 2': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=844284",
'Exuzyan 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=844287",
'Exuzyan 2': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=844298",
'Exuzyan 3': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=844315",
'Exuzyan 4': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=844398",
'Mazepa 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=1543126",
'Mazepa 2': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=1545528",
'Khrapov 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=689938",
'Khrapov 2': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=689948",
'RSMR 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=689951",
'MEM 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=838056",
'Rybka 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=2214218",
'Rybka 2': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=2214231",
'Dizepa 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=2214238",
'APA-V1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=2214254",
'Shcheglov 1': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=2214268",
'Dizepa 2': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=2214266",
'Taya 2': "https://www.aavso.org/vsx/index.php?view=detail.top&oid=2214353",
}


def get_soup(url):
    """get url, return BeautifulSoup object."""
    with request.urlopen(url) as html:
        return BeautifulSoup(html, 'html.parser')

def get_soup_request(url, parser='lxml'):
    """Get url, return BeautifulSoup object."""
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with request.urlopen(req) as html:
        return BeautifulSoup(html, parser)

def hms_to_deg(ra='', dec=''):
    """Converting Between Decimal Degrees and hours, minutes, seconds.
    Snippet from http://www.bdnyc.org/2012/10/decimal-deg-to-hms/"""
    RA, DEC, rs, ds = '', '', 1, 1
    if dec:
        D, M, S = [float(i) for i in dec.split()]
        if str(D)[0] == '-':
            ds, D = -1, abs(D)
        deg = D + (M/60) + (S/3600)
        DEC = round(deg*ds, 5)
    if ra:
        H, M, S = [float(i) for i in ra.split()]
        if str(H)[0] == '-':
            rs, H = -1, abs(H)
        deg = (H*15) + (M/4) + (S/240)
        RA = round(deg*rs, 5)
    if ra and dec:
        return RA, DEC
    return RA or DEC

def get_vsx_params(url, ind=13):
    """Get variable star parameters from VSX page"""
    soup = get_soup_request(url)
    tabs = soup.findAll('table')
    names = []
    print('get info from', url)
    if tabs[ind].find('td').text[:2] == 'RA':
        ind += 1
    for td in tabs[ind].findAll('td'):
        des = td.text.strip()
        if des and des[:6].strip() in ('GSC2.3', 'USNO-B', '2MASS') or \
           des[:3] in ('ZTF', 'TIC') or des[:4] in ('Gaia', 'SDSS', 'GALE', 'ASAS', 'OGLE'):
            names.append(des)
        elif des:
            print('exclude', des)
    types = tabs[ind+1].text.strip()
    mags = tabs[ind+2].text.strip().split('-')
    return names, types, mags

def get_table_data(soup, from_vsx=True, mag_ind=1):
    """Read table, return list and html code"""
    table = "<table class='sortable generated'><tr><th>Имя</th><th>Обозначения</th>" + \
        "<th>RA</th><th>DEC</th><th>Созвездие</th><th>Тип</th><th>Период</th><th>mag max</th>" + \
        "<th>mag min</th><th>Кто открыл</th><th>Дата открытия</th>" + \
        "<th>Ссылки/комментарии</th></tr>\n"
    tab = soup.find('table')
    trs = tab.findAll('tr')[1:]
    objs = []
    for tr in trs:
        params_dct = {}
        tds = tr.findAll('td')
        des = tds[0].text
        coords = tds[1].text
        h, m, s, deg, minu, sec = coords.split()
        dec = f"{deg}°{minu}'{sec}\""
        ra = f"{h}h{m}m{s}s"
        params_dct["constellation"] = tds[2].text
        params_dct["dec"] = dec
        params_dct["designation"] = des
        dat = datetime.datetime.strptime(tds[7].text, '%Y-%m-%d')
        params_dct["jd"] = sum(jdcal.gcal2jd(dat.year, dat.month, dat.day))
        mag = tds[5].text.split("-")
        params_dct["magnitude"] = mag[mag_ind].strip("<")
        params_dct["name"] = des
        params_dct["nameI18n"] = des
        des = tds[0].a
        if from_vsx:
            names, type_vsx, mags_vsx = get_vsx_params(des['href'])
            mag_min = " ".join((mag[0], mags_vsx[0]))
            if mag[0] == mags_vsx[0]:
                mag_min = mag[0]
            mag_max_vsx = mags_vsx[1].replace("<", "&lt;")
            mag_max = " ".join((mag[1].replace("<", "&lt;"), mag_max_vsx))
            if mag[1].replace("<", "&lt;") == mag_max_vsx:
                mag_max = mag_max_vsx
        else:
            names, type_vsx, mags_vsx = [], '', ['', '']
            mag_min = mag[0]
            mag_max = mag[1].replace("<", "&lt;")
        del des["style"]
        params_dct["objtype"] = f"Переменная звезда, {tds[3].text}"
        params_dct["ra"] = ra
        params_dct["type"] = "Star"
        objs.append(params_dct)
        vartype = ", VSX: ".join((tds[3].text, type_vsx))
        if tds[3].text == type_vsx or not type_vsx:
            vartype = tds[3].text
        constltn = f"<span title='{tds[2].text}'>{CONSTELLTN_RU_DCT.get(tds[2].text)}</span>"
        coord_ra = f'<a href="https://simbad.u-strasbg.fr/simbad/sim-coo?Coord={coords[:11].replace(" ", "+")}+{coords[12:].replace("+", "%2B").replace(" ", "+")}%09&CooEpoch=2000&CooEqui=2000&Radius=3&Radius.unit=arcmin&submit=submit+query" target="_blank">{coords[:11]}</a>'
        coord_dec = f'<details><summary>{coords[12:]}</summary>{hms_to_deg(ra=coords[:11])} {hms_to_deg(dec=coords[12:])}</details>'
        tr_content = [f"<td>{x}</td>" for x in (des, ", ".join(names), coord_ra, coord_dec,
            constltn, vartype, tds[4].text.strip(),
            mag_min, mag_max, tds[6].text, tds[7].text,
            f'<a href="images/var/{tds[0].text.replace(" ", "")}.png">find.chart</a>')]
        table += f"<tr>{''.join(tr_content)}</tr>\n"
    table += "</table>"
    return objs, table

def get_sne_table_data(soup):
    """Read table, return list and html code
    """
    table = "<table class='sortable'><tr><th>Обозначение</th><th>RA</th><th>DEC</th>" + \
        "<th>Галактика</th><th>Расстояние</th><th>Величина</th><th>Кто открыл</th>" + \
        "<th>Дата открытия</th><th>Ссылки/комментарии</th></tr>\n"
    tab = soup.find('table')
    trs = tab.findAll('tr')[1:]
    objs = []
    for tr in trs:
        params_dct = {}
        tds = tr.findAll('td')
        des = tds[0].text.strip()
        coords = tds[1].text
        h, m, s, deg, minu, sec = coords.split()
        dec = f"{deg}°{minu}'{sec}\""
        ra = f"{h}h{m}m{s}s"
        params_dct["constellation"] = ""
        params_dct["dec"] = dec
        params_dct["designation"] = des
        dat = datetime.datetime.strptime(tds[6].text, '%Y-%m-%d')
        params_dct["jd"] = sum(jdcal.gcal2jd(dat.year, dat.month, dat.day))
        mag = tds[4].text
        params_dct["magnitude"] = mag
        params_dct["name"] = des
        params_dct["nameI18n"] = des
        des_del = tds[0].a
        del des_del["style"]
        params_dct["objtype"] = "Сверхновая"
        params_dct["ra"] = ra
        params_dct["type"] = "Star"
        objs.append(params_dct)
        coord_ra = f'<a href="https://simbad.u-strasbg.fr/simbad/sim-coo?Coord={coords[:11].replace(" ", "+")}+{coords[12:].replace("+", "%2B").replace(" ", "+")}%09&CooEpoch=2000&CooEqui=2000&Radius=3&Radius.unit=arcmin&submit=submit+query" target="_blank">{coords[:11]}</a>'
        coord_dec = f'<details><summary>{coords[12:]}</summary>{hms_to_deg(ra=coords[:11])} {hms_to_deg(dec=coords[12:])}</details>'
        galaxy = tds[2].text
        tr_content = [f"<td>{x}</td>" for x in (des_del, coord_ra, coord_dec,
            galaxy, tds[3].text, mag, tds[5].text, tds[6].text,
            f'<a href="images/sne/{des}.png">find.chart</a>')]
        table += f"<tr>{''.join(tr_content)}</tr>\n"
    table += "</table>"
    return objs, table

def get_pre_data(soup, from_vsx=True, mag_ind=1):
    """Read plain text, return list and html code
    """
    pre = str(soup.find('pre')).splitlines()[4:-11]
    objs = []
    table = "<table class='sortable generated'><tr><th>Name</th><th>Designation</th>" + \
        "<th>RA (J2000)</th><th>Dec</th><th>Con</th><th>Type</th><th>Period</th>" + \
        "<th>Mag max</th><th>Mag min</th><th>Discoverer</th><th>Date</th>" + \
        "<th>Find. chart/Comment</th></tr>\n"
    for line in pre:
        params_dct = {}
        des = line[:15].strip()
        h, m, s = line[16:18], line[19:21], line[22:27]
        deg, minu, sec = line[28:31], line[32:34], line[35:39]
        dec = f"{deg}°{minu}'{sec}\""
        ra = f"{h}h{m}m{s}s"
        vartype =line[63:68].strip()
        params_dct["constellation"] = line[69:72].strip()
        params_dct["dec"] = dec
        params_dct["designation"] = des
        mag = line[42:51].strip().split("-")
        params_dct["magnitude"] = mag[mag_ind]
        params_dct["name"] = des
        params_dct["nameI18n"] = des
        params_dct["objtype"] = f"Переменная звезда, {vartype}"
        params_dct["ra"] = ra
        params_dct["type"] = "Star"
        period = line[53:61].strip()
        objs.append(params_dct)
        if from_vsx:
            names, type_vsx, mags_vsx = get_vsx_params(VSX_URLS[des])
            mag_min = " ".join((mag[0].strip(), mags_vsx[0]))
            if mag[0].strip() == mags_vsx[0]:
                mag_min = mag[0].strip()
            mag_max_vsx = mags_vsx[1].replace("<", "&lt;")
            mag_max = " ".join((mag[1].strip().replace("<", "&lt;"), mag_max_vsx))
            if mag[1].strip().replace("<", "&lt;") == mag_max_vsx:
                mag_max = mag_max_vsx
        else:
            names, type_vsx, mags_vsx = [], '', ['', '']
            mag_min = mag[0].strip()
            mag_max = mag[1].strip().replace("<", "&lt;")
        if type_vsx and type_vsx != vartype:
            vartype = ", VSX: ".join((vartype, type_vsx))
        constltn = f"<span title='{CONSTELLATION_DCT[line[69:72]]}'>{line[69:72]}</span>"
        coord_dec = f'<details><summary>{line[28:39]}</summary>{hms_to_deg(ra=line[16:27])} {hms_to_deg(dec=line[28:39])}</details>'
        try:
            lc_link = line[74:]
        except IndexError:
            lc_link = ""
        coord_ra = f'<a href="https://simbad.u-strasbg.fr/simbad/sim-coo?Coord={line[16:27].replace(" ", "+")}+{line[28:39].replace("+", "%2B").replace(" ", "+")}%09&CooEpoch=2000&CooEqui=2000&Radius=3&Radius.unit=arcmin&submit=submit+query" target="_blank">{line[16:27]}</a>'
        tr_content = [f"<td>{x}</td>" for x in (
            f'<a href="{VSX_URLS[des]}" target="_blank">{des}</a>',
            ", ".join(names), coord_ra, coord_dec,
            constltn, vartype, period, mag_min, mag_max, des, '', lc_link)]
        # + f' <a href="images/var/{des.replace(" ", "")}.png">find.chart</a>'
        table += f"<tr>{''.join(tr_content)}</tr>\n"
    table += "</table>"
    return objs, table


URL = "https://scan.sai.msu.ru/~denis/Paleo/paleo-var.html"
SNE_URL = "https://scan.sai.msu.ru/~denis/Paleo/paleo-SNe.html"
ZTF_URL = "https://scan.sai.msu.ru/~denis/Var-ZTF.html"
HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Исследования переменных звезд в Московском дворце пионеров</title>
<script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>
<style>
body {
  background-color: #9ccce4;
  font-family: Arial, Helvetica, sans-serif;
}
h1 {font-size: 24px;}
table, th, td {border: 1px solid black;}
.generated tr td:nth-of-type(3), td:nth-of-type(4) {white-space: nowrap;}
table.sortable thead {
  background-color: inherit;
  color: inherit;
  text-align: left;
}
a {text-decoration: none;}
a:hover {text-decoration: underline;}
details > summary {
  list-style: none;
  cursor: pointer;
}
</style>
</head>
<body>
"""

soup = get_soup(URL)
objs, table_pppp = get_table_data(soup)
soup = get_soup(SNE_URL)
objs_sne, table_sne = get_sne_table_data(soup)
soup = get_soup(ZTF_URL)
objs_ztf_lc, table_ztf_lc = get_pre_data(soup)

with open("index.html", 'w', encoding='utf8') as myfile:
    print(HTML_HEAD, table_pppp, '\n<br>\n', table_ztf_lc, '\n<br>\n', table_sne, file=myfile)

objs_json = {
  "observingLists": {
    "{f6fff997-701c-41b4-aee3-24a5b8327433}": {
      "creation date": "2023-04-27 00:00:00",
      "description":
        "Поиск переменности на Паломарских пластинках + DNTTM variables with ZTF light curves",
      "name": "Палеоастрономия, или Проект ПППП",
      "objects": objs + objs_ztf_lc,
}}}

JSON_FILENAME = "paleo-var.json"
with open(JSON_FILENAME, 'w', encoding='utf8') as myfile:
    json.dump(objs_json, myfile, indent=2, ensure_ascii=False)
