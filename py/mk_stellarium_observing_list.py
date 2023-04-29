"""Python script for reading online data with the parameters of
variable stars discovered by the team from Vorobyovy gory.
After parsing, the data is saved in the observing list for Stellarium
and in sortable HTML tables.
Data sources:
https://scan.sai.msu.ru/~denis/Paleo/paleo-var.html
https://scan.sai.msu.ru/~denis/Var-ZTF.html
"""


import datetime
import json
import urllib.request

from bs4 import BeautifulSoup
import jdcal


def get_soup(url):
    """get url, return BeautifulSoup object."""
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')

def get_table_data(soup, mag_ind=1):
    """Read table, return list
    """
    table = "<table class='sortable'><tr><th><b>Обозначение</b></th><th>RA</th><th>DEC</th><th><b>Созвездие</b></th><th><b>Тип</b></th><th><b>Период</b></th><th>mag max</th><th>mag min</th><th><b>Кто открыл</b></th><th><b>Дата открытия</b></th><th>Кривая блеска</th></tr>\n"
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
        params_dct["objtype"] = f"Переменная звезда, {tds[3].text}"
        params_dct["ra"] = ra
        params_dct["type"] = "Star"
        objs.append(params_dct)
        coord_ra = f'<a href="https://simbad.u-strasbg.fr/simbad/sim-coo?Coord={coords[:11].replace(" ", "+")}+{coords[12:].replace("+", "%2B").replace(" ", "+")}%09&CooEpoch=2000&CooEqui=2000&Radius=3&Radius.unit=arcmin&submit=submit+query" target="_blank">{coords[:11]}</a>'
        tr_content = [f"<td>{x}</td>" for x in (tds[0].a, coord_ra, coords[12:],
            tds[2].text, tds[3].text, tds[4].text, mag[0], mag[1], tds[6].text,
            tds[7].text, "")]
        table += f"<tr>{''.join(tr_content)}</tr>\n"
    table += "</table>"
    return objs, table

def get_pre_data(soup, mag_ind=1):
    """Read plain text, return list
    """
    pre = str(soup.find('pre')).splitlines()[4:-2]
    objs = []
    table = "<table class='sortable'><tr><th>Variable name</th><th>R.A. (2000.0)</th><th>Decl.</th><th>Con</th><th>Type</th><th>Period</th><th>Mag max</th><th>Mag min</th><th>ZTF transient</th><th>Discoverer</th><th>Light curve</th></tr>\n"
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
        period = line[53:61]
        objs.append(params_dct)
        try:
            lc_link = line[74:]
        except IndexError:
            lc_link = ""
        coord_ra = f'<a href="https://simbad.u-strasbg.fr/simbad/sim-coo?Coord={line[16:27].replace(" ", "+")}+{line[28:39].replace("+", "%2B").replace(" ", "+")}%09&CooEpoch=2000&CooEqui=2000&Radius=3&Radius.unit=arcmin&submit=submit+query" target="_blank">{line[16:27]}</a>'
        tr_content = [f"<td>{x}</td>" for x in (des, coord_ra, line[28:39],
            line[69:72].strip(), line[63:68].strip(), period, mag[0], mag[1],
            "", "", lc_link)]
        table += f"<tr>{''.join(tr_content)}</tr>\n"
    table += "</table>"
    return objs, table


URL = "https://scan.sai.msu.ru/~denis/Paleo/paleo-var.html"
ZTF_URL = "https://scan.sai.msu.ru/~denis/Var-ZTF.html"

soup = get_soup(URL)
objs, table_pppp = get_table_data(soup)
print(table_pppp)

soup = get_soup(ZTF_URL)
objs_ztf_lc, table = get_pre_data(soup)
print(table)

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
