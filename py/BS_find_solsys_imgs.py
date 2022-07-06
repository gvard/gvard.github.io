import glob

from bs4 import BeautifulSoup


images = [f.split("\\")[1] for f in glob.glob("images/*.jpg")]
# print(images)

with open("index.html", encoding="utf8") as html:
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.findAll("img")

htmlimg = [img["src"].split("/")[1] for img in results]

for img in images:
    if img not in htmlimg:
        print(img)

