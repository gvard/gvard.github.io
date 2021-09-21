import urllib.request

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def autolabel(rects1, rects2, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for x, rect in enumerate(rects1):
        height = rect.get_height() + rects2[x].get_height()
        ax.annotate(height, (rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 5), textcoords="offset points", ha='center')


HTML = """<!DOCTYPE html>
<html lang='ru'>
<meta charset='UTF-8'>
<title>Статистика сверхновых</title>
<ul>
"""
years, sn_data, sn_amateurs = [], [], []
for year in range(2000, 2022):
    url = f"http://rochesterastronomy.org/sn{year}/snstats.html"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    txt = soup.find("pre").text.splitlines()[1:10]
    sn_num = int(txt[0].split()[4])
    sn_amateur = int(txt[5].split()[0])
    b13th = int(txt[6].split()[0])
    HTML += f"""  <li>За {year} год открыто <b>{sn_num}</b> сверхновых,
    из них <b>{sn_amateur}</b> – любителями,
    <b>{b13th}</b> – ярче 13-й зв. величины\n"""
    years.append(year)
    sn_data.append(sn_num - sn_amateur)
    sn_amateurs.append(sn_amateur)

fig, ax = plt.subplots(figsize=(13, 9.5))
bar1 = plt.bar(years, sn_data)
bar2 = plt.bar(years, sn_amateurs, bottom=sn_data)
autolabel(bar1, bar2, ax)
plt.xticks(years)
plt.xlim(years[0]-0.7, years[-1]+0.7)
plt.title("Статистика открытий сверхновых", fontsize=16)
plt.xlabel("Год", fontsize=14)
plt.ylabel("Открытий СН за год", fontsize=14)
plt.savefig("snstats_plot.svg")

HTML += "</ul> <img src='snstats_plot.svg' alt=''>"
with open("index.html", 'w', encoding="utf8") as html_file:
    print(HTML, file=html_file)
