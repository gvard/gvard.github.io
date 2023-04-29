"""Python script for reading online data with the parameters of
variable stars discovered by the team from Vorobyovy gory.
After parsing, the data is saved in the observing list for Stellarium.
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
    tab = soup.find('table')
    trs = tab.findAll('tr')[1:]
    objs = []
    for tr in trs:
        params_dct = {}
        tds = tr.findAll('td')
        des = tds[0].text
        coords = tds[1].text.split()
        h, m, s, deg, minu, sec = coords
        dec = f"{deg}°{minu}'{sec}\""
        ra = f"{h}h{m}m{s}s"
        params_dct["constellation"] = tds[2].text
        params_dct["dec"] = dec
        params_dct["designation"] = des
        dat = datetime.datetime.strptime(tds[7].text, '%Y-%m-%d')
        params_dct["jd"] = sum(jdcal.gcal2jd(dat.year, dat.month, dat.day))
        params_dct["magnitude"] = tds[5].text.split("-")[mag_ind].strip("<")
        params_dct["name"] = des
        params_dct["nameI18n"] = des
        params_dct["objtype"] = f"Переменная звезда, {tds[3].text}"
        params_dct["ra"] = ra
        params_dct["type"] = "Star"
        objs.append(params_dct)
    return objs

def get_pre_data(soup, mag_ind=1):
    """Read plain text, return list
    """
    pre = soup.find('pre').text.splitlines()[4:-1]
    objs = []
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
        params_dct["magnitude"] = line[42:51].split("-")[mag_ind]
        params_dct["name"] = des
        params_dct["nameI18n"] = des
        params_dct["objtype"] = f"Переменная звезда, {line[63:68].strip()}"
        params_dct["ra"] = ra
        params_dct["type"] = "Star"
        objs.append(params_dct)
    return objs


URL = "https://scan.sai.msu.ru/~denis/Paleo/paleo-var.html"
ZTF_URL = "https://scan.sai.msu.ru/~denis/Var-ZTF.html"

soup = get_soup(URL)
objs = get_table_data(soup)

soup = get_soup(ZTF_URL)
objs_ztf_lc = get_pre_data(soup)

objs_json = {
    "observingLists": {
    "{f6fff997-701c-41b4-aee3-24a5b8327433}": {
        "creation date": "2023-04-27 00:00:00",
        "description": "Поиск переменности на Паломарских пластинках + DNTTM variables with ZTF light curves",
        "name": "Палеоастрономия, или Проект ПППП",
        "objects": objs+objs_ztf_lc,
    }}}

JSON_FILENAME = "paleo-var.json"
with open(JSON_FILENAME, 'w', encoding='utf8') as myfile:
    json.dump(objs_json, myfile, indent=2, ensure_ascii=False)
