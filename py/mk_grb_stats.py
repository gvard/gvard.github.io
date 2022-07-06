import os, ssl
import pickle
import urllib.request

from beautifulsoup_supply import TAIL, mk_head, get_soup
from plot_supply import plot_bar, optimize_svg


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


HEAD = mk_head("Статистика гамма-всплесков", style="../../compact.css", script="") + "<body>\n"
GRB_URL = "https://www.mpe.mpg.de/~jcg/grbgen.html"
HTML_FILENAME = os.path.join(os.pardir, 'grb', 'stats', 'index.html')


def get_grb(soup):
    all_tabs = soup.findAll('table')
    trs = all_tabs[-1].findAll('tr')
    years, gnums, opts = [], [], []
    for tr in trs[1:-1]:
        tds = tr.findAll('td')
        opt = int(tds[3].text)
        years.append(int(tds[0].text))
        gnums.append(int(tds[1].text) - opt)
        opts.append(opt)
    return years, gnums, opts

soup = get_soup(GRB_URL)
years, grbnums, opts = get_grb(soup)

labels = ('Статистика гамма-всплесков по годам', 'Год', 'Открытий за год')
tmp_filename = 'grbs_plot_.svg'
filename = 'grbs_plot.svg'
grb_dir = os.path.join(os.pardir, 'grb')
tmp_pth = os.path.join(grb_dir, tmp_filename)
pth = os.path.join(grb_dir, filename)
xlim = (1996.3, 2021.7)
plot_bar(years, grbnums, opts, labels, tmp_pth, xlim)
optimize_svg(tmp_pth, pth)
os.remove(tmp_pth)

grbstats_txt = f"""<h2><a href="{GRB_URL}">Статистика гамма-всплесков</a></h2>
<ul>
"""
all_grb_count, opt_count = 0, 0
for i, year in enumerate(years):
    grbs_num = grbnums[i] + opts[i]
    all_grb_count += grbs_num
    opt_count += opts[i]
    grbstats_txt += f"<li>За {year} год открыто <b>{grbs_num}</b> гама-всплесков, <b>{opts[i]}</b> – послесвечений. Всего к концу года открыто <b>{all_grb_count}</b>, <b>{opt_count}</b> – послесвечений.\n"

grbstats_txt += f"""</ul>
<br><img src="../{filename}" alt="">
<h2>Ссылки</h2>
<ul>
<li><a href="https://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigbrst.html" target="_blank" rel="noopener noreferrer">FERMIGBRST - Fermi GBM Burst Catalog</a>
<li><a href="https://gcn.gsfc.nasa.gov/gcn/gcn3_archive.html" target="_blank" rel="noopener noreferrer">GCN Circulars Archive</a>
</ul>
"""

with open(HTML_FILENAME, 'w', encoding="utf8") as fl:
    print(HEAD + grbstats_txt + TAIL, file=fl)
