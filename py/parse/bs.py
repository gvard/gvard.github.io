import urllib.request

from bs4 import BeautifulSoup


def remove_brackets(brackets, text):
    while brackets[0] in text and brackets[1] in text:
        br1 = text.find(brackets[0])
        br2 = text.find(brackets[1])
        text = text[:br1]+text[br2+1:]
    return text


TEXT = """Дю Белле. Сонеты.
(Швейцария)
Есть все - леса, озера тут,
Но горы им всего дороже.
Правитель строг, законы - тоже.
Народ плечист и любит труд.

Они свою монету льют.
Пьют за троих, едят - дай Боже!
На кровяных колбас похожи
И песни дикие (орут)."""

BRACKETS = ("(", ")")
print(remove_brackets(BRACKETS, TEXT))
URLS = ["https://en.wikipedia.org/wiki/Mercury_(planet)",
        "https://en.wikipedia.org/wiki/Venus",
        "https://en.wikipedia.org/wiki/Earth",
        "https://en.wikipedia.org/wiki/Mars"]

referat = ""
BRACKETS = ("[", "]")
for URL in URLS:
    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html, 'html.parser')
    ps = soup.findAll("p")
    text = ps[0].text.strip() + ps[1].text.strip() + ps[2].text + '\n'
    text = remove_brackets(BRACKETS, text)
    referat += text

print(referat)
