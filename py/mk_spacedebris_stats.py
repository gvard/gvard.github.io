"""Python script for genererating an html page
with space debris statistics. Data sources:
https://www.esa.int/Safety_Security/Space_Debris/Space_debris_by_the_numbers
https://sdup.esoc.esa.int/discosweb/statistics/
https://www.sdo.esoc.esa.int/environment_report/Space_Environment_Report_latest.pdf
"""

import os

from beautifulsoup_supply import TAIL, mk_head, get_soup


SD_URL = 'https://sdup.esoc.esa.int/discosweb/statistics/embed/bythenumbers'


def get_sd(soup):
    """Parse html, get date of last page update,
    statistics of space debris."""
    months_dct = {"January": "января", "March": "марта", "April": "апреля", "May": "мая",
        "June": "июня", "July": "июля", "August": "августа", "September": "сентября",
        "October": "октября", "November": "ноября", "December": "декабря"}
    date = soup.find("p").text.split()[4:]
    date[1] = months_dct[date[1]]
    dd = soup.find("dl").findAll("dd")
    stats = [dd[x].text.split()[1] for x in range(5)]
    stats.append(dd[5].text.split()[2])
    stats.append(dd[6].text.split()[2])
    debrs_modelled = dd[7].text.split()
    debrs_modelled = [debrs_modelled[0], debrs_modelled[6], debrs_modelled[16]]
    return " ".join(date), stats, debrs_modelled


soup = get_soup(SD_URL)
DATE, stats, DEBR_MODEL = get_sd(soup)

HEAD = mk_head("Космический мусор: статистика", style="stats.css", script="")
BODY = f"""<body>
<div id="stats" class="container show">
  <h1 id="header">Космический мусор: статистика от {DATE} года</h1>
  <div class="list">
  <ul>
    <li>Количество запусков ракет с начала космической эры: около <span class="yellow">{stats[0]}</span></li>
    <li>Количество запущенных ими спутников: около <span class="yellow">{stats[1]}</span></li>
    <li>Из них до сих пор на орбите: около <span class="yellow">{stats[2]}</span></li>
    <li>Из них до сих пор функционируют: около <span class="yellow">{stats[3]}</span></li>
    <li>Объектов отслеживается Сетью Космического Наблюдения США: около <span class="yellow">{stats[4]}</span></li>
    <li>Оцениваемое количество событий, приводящих к фрагментации: более <span class="yellow">{stats[5]}</span></li>
    <li>Полная масса космических объектов на орбите Земли: более <span class="yellow">{stats[6]}</span> тонн</li>
  </ul>
  </div>
  <div id="footer">
    <h2>Центр Астрономического и&nbsp;космического образования</h2>
  </div>
</div>
"""

"""
    <li>Количество находящихся на орбите объектов космического мусора (Оценки по статистическим моделям):
      <ul>
        <li><span class="yellow">{DEBR_MODEL[0]}</span> объектов более 10 см
        <li><span class="yellow">{DEBR_MODEL[1]}</span> объектов от 1 до 10 см
        <li><span class="yellow">{DEBR_MODEL[2]}</span> миллионов объектов от 1 мм до 1 см
      </ul>
    </li>
"""
with open(os.path.join(os.pardir, 'cosm', 'debris', 'index.html'), 'w', encoding="utf8") as fl:
    print(HEAD + BODY + TAIL, file=fl)
