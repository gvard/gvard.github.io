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
import urllib.request

from bs4 import BeautifulSoup
import jdcal

from astro_const import CONSTELLATION_DCT, CONSTELLTN_RU_DCT


def get_soup(url):
    """get url, return BeautifulSoup object."""
    with urllib.request.urlopen(url) as html:
        return BeautifulSoup(html, 'html.parser')

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
    else:
        return RA or DEC

def get_table_data(soup, mag_ind=1):
    """Read table, return list and html code
    """
    table = "<table class='sortable'><tr><th>Обозначение</th><th>RA</th><th>DEC</th><th>Созвездие</th><th>Тип</th><th>Период</th><th>mag max</th><th>mag min</th><th>Кто открыл</th><th>Дата открытия</th><th>Ссылки/комментарии</th></tr>\n"
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
        del des["style"]
        params_dct["objtype"] = f"Переменная звезда, {tds[3].text}"
        params_dct["ra"] = ra
        params_dct["type"] = "Star"
        objs.append(params_dct)
        constltn = f"<span title='{tds[2].text}'>{CONSTELLTN_RU_DCT.get(tds[2].text)}</span>"
        coord_ra = f'<a href="https://simbad.u-strasbg.fr/simbad/sim-coo?Coord={coords[:11].replace(" ", "+")}+{coords[12:].replace("+", "%2B").replace(" ", "+")}%09&CooEpoch=2000&CooEqui=2000&Radius=3&Radius.unit=arcmin&submit=submit+query" target="_blank">{coords[:11]}</a>'
        coord_dec = f'<details><summary>{coords[12:]}</summary>{hms_to_deg(ra=coords[:11])} {hms_to_deg(dec=coords[12:])}</details>'
        tr_content = [f"<td>{x}</td>" for x in (des, coord_ra, coord_dec,
            constltn, tds[3].text, tds[4].text.strip(), mag[0],
            mag[1].replace("<", "&lt;"), tds[6].text, tds[7].text,
            f'<a href="images/var/{tds[0].text.replace(" ", "")}.png">find.chart</a>')]
        table += f"<tr>{''.join(tr_content)}</tr>\n"
    table += "</table>"
    return objs, table

def get_sne_table_data(soup):
    """Read table, return list and html code
    """
    table = "<table class='sortable'><tr><th>Обозначение</th><th>RA</th><th>DEC</th><th>Галактика</th><th>Расстояние</th><th>Величина</th><th>Кто открыл</th><th>Дата открытия</th><th>Ссылки/комментарии</th></tr>\n"
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

def get_pre_data(soup, mag_ind=1):
    """Read plain text, return list and html code
    """
    pre = str(soup.find('pre')).splitlines()[4:-2]
    objs = []
    table = "<table class='sortable'><tr><th>Variable name</th><th>R.A. (J2000)</th><th>Dec.</th><th>Con</th><th>Type</th><th>Period</th><th>Mag max</th><th>Mag min</th><th>Light curve</th><th>Find. chart/Comment</th></tr>\n"
    for line in pre:
        params_dct = {}
        des = line[:15].strip()
        h, m, s = line[16:18], line[19:21], line[22:27]
        deg, minu, sec = line[28:31], line[32:34], line[35:39]
        dec = f"{deg}°{minu}'{sec}\""
        ra = f"{h}h{m}m{s}s"
        params_dct["constellation"] = line[69:72].strip()
        params_dct["dec"] = dec
        params_dct["designation"] = des
        mag = line[42:51].split("-")
        params_dct["magnitude"] = mag[mag_ind]
        params_dct["name"] = des
        params_dct["nameI18n"] = des
        params_dct["objtype"] = f"Переменная звезда, {line[63:68].strip()}"
        params_dct["ra"] = ra
        params_dct["type"] = "Star"
        period = line[53:61].strip()
        objs.append(params_dct)
        constltn = f"<span title='{CONSTELLATION_DCT[line[69:72]]}'>{line[69:72]}</span>"
        coord_dec = f'<details><summary>{line[28:39]}</summary>{hms_to_deg(ra=line[16:27])} {hms_to_deg(dec=line[28:39])}</details>'
        try:
            lc_link = line[74:]
        except IndexError:
            lc_link = ""
        coord_ra = f'<a href="https://simbad.u-strasbg.fr/simbad/sim-coo?Coord={line[16:27].replace(" ", "+")}+{line[28:39].replace("+", "%2B").replace(" ", "+")}%09&CooEpoch=2000&CooEqui=2000&Radius=3&Radius.unit=arcmin&submit=submit+query" target="_blank">{line[16:27]}</a>'
        tr_content = [f"<td>{x}</td>" for x in (des, coord_ra, coord_dec,
            constltn, line[63:68].strip(), period, mag[0], mag[1], lc_link,
            f'<a href="images/var/{des.replace(" ", "")}.png">find.chart</a>')]
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
body {background-color: #9ccce4;}
h1 {font-size: 24px;}
a {text-decoration: none;}
table, th, td {border: 1px solid black;}
tr td:nth-of-type(2), td:nth-of-type(3) {white-space: nowrap;}
table.sortable thead {
  background-color: inherit;
  color: inherit;
}
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
    print(HTML_HEAD, table_pppp, '\n<br>\n', table_sne, '\n<br>\n', table_ztf_lc, file=myfile)

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
