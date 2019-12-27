import pickle
import os


PICKLE_FILENAME = "stars_dct.pickle"
HEAD = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Звезды</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>
<body>
<div id="messageBox">
    <div id="contents"></div>
</div>
<main>
<h1>Звезды не как точки</h1>

<button onclick="showHideThis('none','.size')">Скрыть радиусы</button>
<button onclick="showHideThis('block','.size')">Показать радиусы</button>
<button onclick="showHideThis('none','.mass')">Скрыть массу</button>
<button onclick="showHideThis('block','.mass')">Показать массу</button>
<button onclick="showHideThis('none','.class')">Скрыть спектральный класс</button>
<button onclick="showHideThis('block','.class')">Показать спектральный класс</button>
<button onclick="toSort('size')">Сортировать по возрастанию размера</button>
<button onclick="toSort('mass')">Сортировать по возрастанию массы</button>

<section class="tab main">
'''
TAIL = '''
</section>
</main>
<footer>2019 Википедия. Компиляция, код: Д.С. Насонов.</footer>
</body>
</html>
'''

try:
    with open(PICKLE_FILENAME, 'rb') as handle:
        bodies_params_dct = pickle.load(handle)
except Exception:
    bodies_params_dct = {}

print(len(bodies_params_dct))

def extract_nam(txt):
    if "_" in txt:
        txt_nam = txt.replace("_", "")
    else:
        txt_nam = txt
    return txt_nam

def mk_div(txt, typ):
    return '<div class="' + typ + '">' + txt + '</div>'

def mk_link(txt):
    txt_nam = txt.replace('_', ' ')
    return f'<div class="desc"><a href="https://en.wikipedia.org/wiki/{txt}">{txt_nam}</a></div>'

def mk_img(txt, ext="jpg"):
    txt_nam = txt.replace('_', '').replace(' ', '')
    return f'<div class="img" onmouseover="show(this)" onmouseout="hide()"><a href="#" class="image"><img alt="" src="images/{txt_nam}.{ext}"></a></div>'

def wrap_div(txt):
    return f'<div class="obj">\n{txt}\n</div>'

with open(os.path.join(os.pardir, 'stars', 'objects.html'), 'w', encoding="utf8") as handle:
    print(HEAD, file=handle)
    for objname in bodies_params_dct:
        mass_str = str(bodies_params_dct[objname].get('mass'))
        radius_str = str(bodies_params_dct[objname].get('radius'))
        temperature_str = str(bodies_params_dct[objname].get('temperature'))
        #age_str = str(bodies_params_dct[objname].get('age_myr'))
        #luminosity_str = str(bodies_params_dct[objname].get('luminosity'))
        html_obj = wrap_div(mk_img(objname) + '\n' + mk_link(objname) + '\n' +  mk_div(radius_str, 'size') + '\n' + mk_div(mass_str, 'mass') + mk_div(temperature_str, 'temp'))
        print(html_obj, file=handle, end='')
    print(TAIL, file=handle)