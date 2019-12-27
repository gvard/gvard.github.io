from os import listdir, pardir
from os.path import isfile, join
HEAD = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Знаменательные даты</title>
    <!-- <link rel="stylesheet" href="style.css"> -->
    <style>.date {font-size: 1.2em; font-weight: bold;}</style>
    <script src="script.js"></script>
</head>
<body>
<div class="wrapper">

'''
TAIL = '''</div>
<script>
    var slideIndex = 0;
    carousel();
</script>
</body>
</html>
'''
fpt = 'cal'
ipt = 'img'
ipth = join(fpt, ipt)
fils = [f.rstrip("txt") for f in listdir(fpt) if isfile(join(fpt, f))]
imgs = [f for f in listdir(ipth) if isfile(join(ipth, f))]
html = HEAD
for f in imgs:
    fnam = f.rstrip("jpg").rstrip("png")
    pth = ipt + "/" + f
    txt = open(join(fpt, fnam+"txt"), 'r', encoding="windows-1251").read()
    txtspl = txt.split()
    rubr = txtspl[0]
    date = txtspl[1]
    descr = txt.split("\n")[2]
    #print(date, pth, descr)
    block = f"""<div class="wrap">
<div class="date">{date}</div>
<div class="desc">
<img src="{pth}" alt="">
<p><span class="ago"></span> {descr}</p>
</div>
</div>

"""
    if rubr in ("Астрономия", "Космонавтика"):
        html += block
html += TAIL
with open(join(pardir, 'dates', 'carousel_gen.html'), 'w', encoding="utf8") as fil:
    print(html, file=fil)

