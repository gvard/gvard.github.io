import urllib.request
import urllib.parse

from bs4 import BeautifulSoup


WIKI_URL = "https://ru.wikipedia.org/wiki/"
ASTEROIDS = ["Церера", "(2)_Паллада", "(3)_Юнона", "(4)_Веста"]
URLS = [WIKI_URL + urllib.parse.quote(name) for name in ASTEROIDS]

for url in URLS:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    ps = soup.findAll("p")
    text = ps[0].text
    while "[" in text:
        br1 = text.find("[")
        br2 = text.find("]")
        text = text[:br1] + text[br2+1:]
    accent_ind = text.find("́")
    text = text[:accent_ind] + text[accent_ind+1:]
    print(text)
