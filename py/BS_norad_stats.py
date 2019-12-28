from bs4 import BeautifulSoup
import urllib.request
import os


HEAD = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Статистика околоземного пространства</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
"""
TAIL = """
</body>
</html>
"""
N2YO_URL = "https://www.n2yo.com/"


def getnorad(html):
    soup = BeautifulSoup(html, 'html.parser')
    return int(soup.findAll("span", {"style": "color:#d50000"})[0].text)


html = urllib.request.urlopen(N2YO_URL).read()
number_tracking_objects = getnorad(html)
norad_stats = f"""<h2>Отслеживаемые объекты в околоземном пространстве</h2>
<p><a href="{N2YO_URL}">Satellite tracking and predictions</a></p>
<p><b>Tracking {number_tracking_objects} objects</b></p>
"""

with open(os.path.join(os.pardir, 'stats.html'), 'w', encoding="utf8") as handle:
    print(HEAD + norad_stats + TAIL, file=handle)
