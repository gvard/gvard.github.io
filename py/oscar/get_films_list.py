"""Get kinopoisk.ru list page, find info for each movie
via BeautifulSoup, print data as dictionary.
"""

https://www.kinopoisk.ru/lists/editorial/best_by_rotten_tomatoes/
https://www.kinopoisk.ru/lists/editorial/best_by_cinematography_institute/

import urllib.request

from bs4 import BeautifulSoup

#URL = 'https://www.kinopoisk.ru/top/lists/17/perpage/100/' # Oscar
# URL = 'https://www.kinopoisk.ru/top/lists/52/perpage/100/' # World profit
URL = 'https://www.kinopoisk.ru/top/lists/23/perpage/100/' # USA inflation corrected
html = urllib.request.urlopen(URL).read()
bs = BeautifulSoup(html, 'html.parser')

tds = bs.findAll("td", {"valign": "top", "style": "padding: 28px 0 28px 10px"})
ids = {}
for td in tds:
    div = td.find('div')
    a = div.find('a')
    span = div.find('span')
    ids[int(a.get('href').split('/')[2])] = (a.text, span.text)

print(ids)