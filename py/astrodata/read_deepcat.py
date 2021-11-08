import urllib.request
import datetime
import os, ssl

from bs4 import BeautifulSoup


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

DATA_URL = "https://planet4589.org/space/gcat/data/cat/deepcat.html"
html = urllib.request.urlopen(DATA_URL).read()
soup = BeautifulSoup(html, 'html.parser')
data = soup.findAll('pre')[1].text.splitlines()

data_dct = {}
for line in data:
    if line:
        name = line[48:76].strip()
        ldate = datetime.datetime.strptime(line[106:117], '%Y %b %d')
        if ldate not in data_dct:
            data_dct[ldate] = [name]
        else:
            data_dct[ldate].append(name)


with open('deepcat.txt', 'w') as f:
    for launch_date in sorted(data_dct):
        print(str(launch_date.date()), data_dct[launch_date], file=f)
