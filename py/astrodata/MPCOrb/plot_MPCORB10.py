import numpy as np


DOWNLOAD = False
if DOWNLOAD:
    import urllib.request
    MPCORB_URL = 'http://www.minorplanetcenter.net/iau/MPCORB/MPCORB.DAT.gz'
    urllib.request.urlretrieve(MPCORB_URL, 'data/MPCORB.DAT.gz')

DATA = np.genfromtxt('data/MPCORB.DAT.gz',
    usecols=(0, 8, 10),
    skip_header=43)

print(DATA[0])
print(DATA[-1])
print(len(DATA), len(DATA[0]))
