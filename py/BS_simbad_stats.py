import pickle
import urllib.request

from bs4 import BeautifulSoup

SIMBAD_URL = "http://simbad.u-strasbg.fr/simbad/"
PICKLE_FILENAME = 'simbad_stats.pickle'

def get_soup(url):
    """get url, return BeautifulSoup object"""
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')


htmlz = '''<TABLE WIDTH="100%" BORDER="1" CELLPADDING="2">
    <TR>
     <TD ALIGN="CENTER" VALIGN="TOP" NOWRAP COLSPAN="2" BGCOLOR="#3264A0">
      <FONT SIZE="+1" COLOR="#FFFFFF">
       <B>
        <I>
Statistics
        </I>
       </B>
      </FONT>
     </TD>
    </TR>
    <TR BGCOLOR="#FFFFFF">
     <TD ALIGN="LEFT" VALIGN="TOP" NOWRAP COLSPAN="2">
      <B>
Simbad contains on 
      </B>
      <I>
2019.11.26
      </I>
     </TD>
    </TR>
    <TR BGCOLOR="#FFFFFF">
     <TD ALIGN="RIGHT" VALIGN="TOP" WIDTH="28%">
      <B>
10,875,039
      </B>
     </TD>
     <TD ALIGN="LEFT" VALIGN="TOP">
objects
     </TD>
    </TR>
    <TR BGCOLOR="#FFFFFF">
     <TD ALIGN="RIGHT" VALIGN="TOP" WIDTH="28%">
      <B>
35,531,593
      </B>
     </TD>
     <TD ALIGN="LEFT" VALIGN="TOP">
identifiers
     </TD>
    </TR>
    <TR BGCOLOR="#FFFFFF">
     <TD ALIGN="RIGHT" VALIGN="TOP" WIDTH="28%">
      <B>
364,553
      </B>
     </TD>
     <TD ALIGN="LEFT" VALIGN="TOP">
bibliographic references
     </TD>
    </TR>
    <TR BGCOLOR="#FFFFFF">
     <TD ALIGN="RIGHT" VALIGN="TOP" WIDTH="28%">
      <B>
20,482,353
      </B>
     </TD>
     <TD ALIGN="LEFT" VALIGN="TOP">
citations of objects in papers
     </TD>
    </TR>
   </TABLE>'''

soup = get_soup(SIMBAD_URL)
results = soup.findAll("td", {"bgcolor" : "#3264A0"})
for result in results:
    if result.text.strip() == "Statistics": #len(result.attrs) == 5
        tbody = result.parent.parent
        tds = tbody.findAll('td')
        break

strs = ['objects', 'identifiers', 'bibliographic references', 'citations of objects in papers']
simstats = {}
for i, td in enumerate(tds):
    if 'Simbad contains on' in td.text:
        simdate = td.i.text.strip()
        simstats[simdate] = []
        continue
    for tabstr in strs:
        if tabstr == td.text.strip():
            simstats[simdate].append([tds[i-1].text.strip().replace(',', ''), tabstr])

print('Simbad contains on', simdate, simstats[simdate])

try:
    with open(PICKLE_FILENAME, 'rb') as handle:
        simbstats_dict = pickle.load(handle)
except Exception:
    simbstats_dict = {}

if simdate not in simbstats_dict:
    simbstats_dict[simdate] = simstats[simdate]

print("Number of dates in picle file:", len(simbstats_dict))

with open(PICKLE_FILENAME, 'wb') as handle:
    pickle.dump(simbstats_dict, handle)
