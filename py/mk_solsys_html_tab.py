import pickle
import re
import os

from object_data import PLANETS, DWARFPLANETS, COMETS, MOONS, MARS_MOONS, \
    JUPITER_MOONS, SATURN_MOONS, URANUS_MOONS, NEPTUNE_MOONS, PLUTO_MOONS, \
    ASTEROIDS, NEOS, TNOS, BODIES_RU_NAMES


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
<body onload="findDate()">
<div id="messageBox">
<div id="contents"></div>
</div>

<h1>&laquo;Семейный портрет&raquo; Солнечной системы</h1>

<div class="cont">
<b>Пульт управления информацией:</b><br>
<input type="checkbox" name=".name" value="block" checked onclick="showHideThis(this)">Имя,
<input type="checkbox" name=".size" value="block" checked onclick="showHideThis(this)">Радиус,
<input type="checkbox" name=".date" value="block" checked onclick="showHideThis(this)">Дата открытия,
<input type="checkbox" name=".mass" value="block" onclick="showHideThis(this)">Масса,
<input type="checkbox" name=".delta-v" value="block" onchange="showHideThis(this)">Δv<br>
<input type="checkbox" name=".highcontrast,.lightcurve" value="inline-block" checked onchange="showHideThis(this)">"восстановленное" изображение или модель<br>
<input type="checkbox" name=".dot,.lowcontrast" value="inline-block" checked onchange="showHideThis(this)">Фото низкого разрешения или точечное<br>
<input type="checkbox" name=".radar" value="inline-block" checked onchange="showHideThis(this)">Радарное изображение<br>
<input type="checkbox" name=".he" value="inline-block" checked onchange="showHideThis(this)">"круглые" тела (в гидростатическом равновесии)<br>
<input type="text" id="year" size="4" maxlength="4" value="1990">
<button type="button" onclick="showHideByDate('none')">Скрыть объекты, открытые после указанного года</button>
<button type="button" onclick="showHideByDate('inline-block')">Показать объекты, открытые после указанного года</button><br>
<button type="button" onclick="toSort('date')">Сортировать по году открытия</button>
<button type="button" onclick="toSort('size')">Сортировать по возрастанию размера</button>
<button type="button" onclick="toSort('mass')">Сортировать по возрастанию массы</button>
<button type="button" onclick="toSort('delta-v')">Сортировать по возрастанию Δv</button>
</div>

<div id="tab">'''
TAIL = '''
</div>

<div class="cont">
<div id="objOfMonth">
  <h2>Объекты месяца</h2>
</div>
<div id="objOfDay">
  <h2>Объект дня</h2>
</div>
</div>

<footer>2013&ndash;2019 Википедия. Компиляция, код: Д.С. Насонов.</footer>
</body>
</html>'''


try:
    with open(PICKLE_FILENAME, 'rb') as fl:
        bodies_params_dct = pickle.load(fl)
        print(bodies_params_dct)
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
    return f'<div class="name"><a href="https://en.wikipedia.org/wiki/{txt}">{txt_nam}</a></div>'

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
    elif name in MARS_MOONS:
        return ' mar'
    elif name in JUPITER_MOONS:
        return ' ju'
    elif name in SATURN_MOONS:
        return ' sat'
    elif name in URANUS_MOONS:
        return ' ur'
    elif name in NEPTUNE_MOONS:
        return ' ne'
    elif name in PLUTO_MOONS:
        return ' pl'

strcut = lambda txt: str(txt).replace("<", "").replace(">", "").replace("None", "")

with open(os.path.join(os.pardir, 'solarsystem', 'objects.html'), 'w', encoding="utf8") as fl:
    print(HEAD, file=fl)
    deltav_str = ""
    for objname in bodies_params_dct:
        mass_str = strcut(bodies_params_dct[objname].get('mass'))
        radius = bodies_params_dct[objname].get('mean_radius')
        diameter = bodies_params_dct[objname].get('mean_diameter')
        if not radius and not diameter:
            size_str = ""
        else:
            size_str = 'radius: ' + strcut(radius) + " diameter: " + strcut(diameter)
        period_str = strcut(bodies_params_dct[objname].get('period'))
        date_str = strcut(bodies_params_dct[objname].get('discovery_date'))
        txt_extr, txt_type, number, comet = extract_nam(objname)
        classes = ""
        if objname in PLANETS:
            classes += ' pla he'
        elif objname in MOONS:
            classes += which_moon(objname)
            classes += ' moon'
        elif objname == "Sun":
            classes += ' star he'
        elif objname in DWARFPLANETS:
            classes += ' dw he'
        elif objname in ASTEROIDS:
            classes += ' mab'
        elif objname in NEOS:
            classes += ' neo'
        elif objname in TNOS:
            classes += ' tno'
        elif comet or objname in COMETS or "Halley" in txt_extr:
            classes += ' co'
            print("comet!", objname)
        div_img = mk_img(txt_extr, txt_type, number, comet)
        if BODIES_RU_NAMES.get(objname):
            a_name = BODIES_RU_NAMES[objname]
        else:
            a_name = txt_extr.replace('_', ' ')
        div_desc = mk_link(objname, a_name) # txt_extr.replace('_', ' ')
        divs_html = f"""{div_img}
  {div_desc}
  {mk_div(size_str, 'size')}
  {mk_div(mass_str, 'mass')}
  {mk_div(date_str, 'date')}
  {mk_div(deltav_str, 'delta-v')}"""
#   {mk_div(period_str, 'period')}
        html_obj = wrap_div(divs_html, classes)
        print(html_obj, file=fl, end='')
    print(TAIL, file=fl)
