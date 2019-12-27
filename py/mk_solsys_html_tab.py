import pickle
import re
import os
from object_data import planets, dwarfplanets, comets, moons, mars_moons, \
    jupiter_moons, saturn_moons, uranus_moons, neptune_moons, pluto_moons, \
    asteroids


PICKLE_FILENAME = "solsysbod_dct.pickle"
HEAD = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Солнечная система</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>
<body>

<div id="messageBox">
    <div id="contents"></div>
</div>

<main>
<h1>&laquo;Семейный портрет&raquo; Солнечной системы</h1>

<button onclick="showHideThis('none','.highcontrast')">Скрыть тела с "восстановленным" изображением</button>
<button onclick="showHideThis('none','.dot,.lowcontrast')">Скрыть тела без качественного фото</button>
<button onclick="showHideThis('none','.he')">Скрыть "круглые" тела</button>
<button onclick="showHideThis('inline-block','.he')">Показать "круглые" тела</button>
<button onclick="showHideThis('none','.size')">Скрыть радиусы тел</button>
<button onclick="showHideThis('block','.size')">Показать радиусы тел</button>
<button onclick="showHideThis('none','.mass')">Скрыть массу тел</button>
<button onclick="showHideThis('block','.mass')">Показать массу тел</button>
<button onclick="showHideThis('block','.date')">Показать дату открытия</button>
<input type="text" id="year" size="4" maxlength="4" value="1990">
<button onclick="showHideByDate('none')">Скрыть объекты, открытые после указанного года</button>
<button onclick="showHideByDate('inline-block')">Показать объекты, открытые после указанного года</button>
<button onclick="toSort('date')">Сортировать по году открытия</button>
<button onclick="toSort('size')">Сортировать по возрастанию размера</button>
<button onclick="toSort('mass')">Сортировать по возрастанию массы</button>

<section class="tab main">'''
TAIL = '''
</section>
</main>
<footer>2013&ndash;2019 Википедия. Компиляция, код: Д.С. Насонов.</footer>
</body>
</html>'''


try:
    with open(PICKLE_FILENAME, 'rb') as handle:
        bodies_params_dct = pickle.load(handle)
except Exception:
    bodies_params_dct = {}


def extract_nam(txt):
    txt_type, number, comet = "", "", ""
    if "(" in txt:
        txts = re.search(r"(\w{0,25})\((\w+)\)(\w{0,25})", txt)
        gr1, in_brackets, gr2 = txts.groups()
        if gr1 and not gr2:
            txt_nam = gr1
        else:
            txt_nam = gr2
            number = in_brackets
        if in_brackets.replace("_", " ") in ("moon", "dwarf planet"):
            txt_type = in_brackets
    elif "(" not in txt and "_" in txt:
        txts = re.search(r"([0-9]{1,7})[_\ ](\w{0,25})", txt)
        try:
            number_str = txts.groups()[0]
            if 1950 < int(number_str) < 2030:
                txt_nam = number_str + ' ' + txts.groups()[-1]
            else:
                txt_nam = txts.groups()[-1]
                number = number_str
        except AttributeError:
            txt_nam = txt.replace("'", "")
    elif "(" not in txt and " " in txt:
        txts = re.search(r"([0-9]{1,7})[_\ ](\w{0,25})", txt)
        # print("!!!", txts.groups())
            # txt_nam = txts.groups()[1] + txts.groups()[-1]
        txt_nam = txts.groups()[-1]
    elif "/" in txt:
        parts = txt.split("/")
        txt_nam = parts[1].replace("–", "")
        comet = txt
    else:
        txt_nam = txt
    return txt_nam.strip("_"), txt_type, number, comet

def mk_div(txt, typ):
    return f'<div class="{typ}">{txt}</div>'

def mk_link(txt, txt_nam):
    return f'<div class="desc"><a href="https://en.wikipedia.org/wiki/{txt}">{txt_nam}</a></div>'

def mk_img(txt_extr, txt_type, number, comet, ext="jpg"):
    txt_nam = txt_extr.replace('_', '').replace(' ', '')
    if txt_type:
        txt_extr += f" ({txt_type})"
    if number:
        txt_extr = f"({number}) {txt_extr}"
    if comet:
        txt_extr = comet
    if txt_nam in ("Europa", "Metis") and "moon" in txt_extr:
        txt_nam += "_moon"
    if txt_nam[:3] == "201" or txt_nam in ("Phaethon", "1950DA"):
        ext = "gif"
    elif txt_nam[:1] == "Š":
        txt_nam = "S" + txt_nam[1:]
    elif txt_nam == "HalleysComet":
        txt_nam = "Halley"
        txt_extr = "1P/Halley"
    return f'<div class="img" onmouseover="show(this)" onmouseout="hide()"><img alt="{txt_extr.replace("_", " ").strip()}" src="images/{txt_nam}.{ext}"></div>'

def wrap_div(txt, classes):
    return f'<div class="obj{classes}">\n{txt}\n</div>'

def which_moon(name):
    if name == 'Moon':
        return ' ea'
    elif name in mars_moons:
        return ' ma'
    elif name in jupiter_moons:
        return ' ju'
    elif name in saturn_moons:
        return ' sat'
    elif name in uranus_moons:
        return ' ur'
    elif name in neptune_moons:
        return ' ne'
    elif name in pluto_moons:
        return ' pl'

with open(os.path.join(os.pardir, 'solarsystem', 'objects.html'), 'w', encoding="utf8") as handle:
    print(HEAD, file=handle)
    for objname in bodies_params_dct:
        mass_str = str(bodies_params_dct[objname].get('mass'))
        radius = bodies_params_dct[objname].get('mean_radius')
        diameter = bodies_params_dct[objname].get('mean_diameter')
        if not radius and not diameter:
            size_str = "None"
        else:
            size_str = 'radius: ' + str(radius) + " diameter: " + str(diameter)
        period_str = str(bodies_params_dct[objname].get('period'))
        date_str = str(bodies_params_dct[objname].get('discovery_date'))
        txt_extr, txt_type, number, comet = extract_nam(objname)
        classes = ""
        if objname in planets:
            classes += ' pla he'
        elif objname in moons:
            classes += which_moon(objname)
            classes += ' moon'
        elif objname == "Sun":
            classes += ' star he'
        elif objname in dwarfplanets:
            classes += ' dw he'
        elif objname in asteroids:
            classes += ' mab'
        elif comet or objname in comets or "Halley" in txt_extr:
            classes += ' co'
            print("comet!", objname)
        div_img = mk_img(txt_extr, txt_type, number, comet)
        div_desc = mk_link(objname, txt_extr.replace('_', ' '))
        divs_html = div_img + '\n    ' + div_desc + '\n    ' + mk_div(size_str, 'size') + '\n    ' + mk_div(mass_str, 'mass') + '\n    ' + mk_div(date_str, 'date') + '\n    ' + mk_div(period_str, 'period')
        html_obj = wrap_div(divs_html, classes)
        print(html_obj, file=handle, end='')
    print(TAIL, file=handle)