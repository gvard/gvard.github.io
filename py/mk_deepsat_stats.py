"""Python script for genererating an html page
with deep space artificial objects statistics. Data source:
https://planet4589.org/space/deepcat/
"""

import os
import urllib.request

from beautifulsoup_supply import TAIL, mk_head, get_soup


DEEPC_URL = "https://planet4589.org/space/deepcat/catstats.html"


def get_deepcatdata(soup):
    """Parse html, get statistics of deep space objects."""
    trs = soup.find("table").findAll("tr")
    data = []
    all_num = 0
    for tr in trs[2:]:
        tdata = []
        tds = tr.findAll("td")
        for num in tds[1].text.split():
            tdata.append(int(num))
            all_num += int(num)
        data.append(tdata)
    return data, all_num


soup = get_soup(DEEPC_URL)
DATA, ALL = get_deepcatdata(soup)
HEAD = mk_head("Статистика искусственных объектов далекого космоса", style="stats.css", script="")
BODY = f"""<body">
<div id="stats" class="container show">
  <h1 id="header">Статистика искусственных объектов далекого космоса</h1>
  <div class="list">
  <ul>
    <li>Не покинули сферу Хилла Земли: на орбите <span class="yellow">{DATA[0][0]}</span>, вошли в атмосферу <span class="yellow">{DATA[0][1]}</span>, потеряны <span class="yellow">{DATA[0][2]}</span></li>
    <li>Вернулись к Земле с лунной или солнечной орбиты: на орбите <span class="yellow">{DATA[1][0]}</span>, вошли в атмосферу <span class="yellow">{DATA[1][1]}</span>, потеряны <span class="yellow">{DATA[1][2]}</span></li>
    <li>Луна: на орбите <span class="yellow">{DATA[2][0]}</span>, достигли поверхночти <span class="yellow">{DATA[2][1]}</span>, потеряны <span class="yellow">{DATA[2][2]}</span></li>
    <li>В точках Лаграгжа L1/L2 системы Земля-Солнце: на орбите <span class="yellow">{DATA[3][0]}</span>, вошли в атмосферу <span class="yellow">{DATA[3][1]}</span>, потеряны <span class="yellow">{DATA[3][2]}</span></li>
    <li>Солнце: на орбите <span class="yellow">{DATA[4][0]}</span>, вошли в атмосферу <span class="yellow">{DATA[4][1]}</span>, потеряны <span class="yellow">{DATA[4][2]}</span></li>
    <li>Меркурий: на орбите <span class="yellow">{DATA[5][0]}</span>, достигли поверхночти <span class="yellow">{DATA[5][1]}</span>, потеряны <span class="yellow">{DATA[5][2]}</span></li>
    <li>Венера: на орбите <span class="yellow">{DATA[6][0]}</span>, вошли в атмосферу <span class="yellow">{DATA[6][1]}</span>, потеряны <span class="yellow">{DATA[6][2]}</span></li>
    <li>Марс: на орбите <span class="yellow">{DATA[7][0]}</span>, достигли поверхночти <span class="yellow">{DATA[7][1]}</span>, потеряны <span class="yellow">{DATA[7][2]}</span></li>
    <li>Юпитер: на орбите <span class="yellow">{DATA[8][0]}</span>, вошли в атмосферу <span class="yellow">{DATA[8][1]}</span>, потеряны <span class="yellow">{DATA[8][2]}</span></li>
    <li>Сатурн: на орбите <span class="yellow">{DATA[9][0]}</span>, вошли в атмосферу <span class="yellow">{DATA[9][1]}</span>, потеряны <span class="yellow">{DATA[9][2]}</span></li>
    <li>Титан: на орбите <span class="yellow">{DATA[10][0]}</span>, вошли в атмосферу <span class="yellow">{DATA[10][1]}</span>, потеряны <span class="yellow">{DATA[10][2]}</span></li>
    <li>Астероиды и кометы: на орбите <span class="yellow">{DATA[11][0]}</span>, достигли поверхночти <span class="yellow">{DATA[11][1]}</span>, потеряны <span class="yellow">{DATA[11][2]}</span></li>
  </ul>
  <p>Всего объектов: <span class="yellow">{ALL}</span></p>
  </div>
  <div id="footer">
    <h2>Центр Астрономического и&nbsp;космического образования</h2>
  </div>
</div>
"""

with open(os.path.join(os.pardir, 'cosm', 'deepspace', 'index.html'), 'w', encoding="utf8") as handle:
    print(HEAD + BODY + TAIL, file=handle)