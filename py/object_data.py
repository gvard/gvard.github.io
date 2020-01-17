PLANETS = ['Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Earth', 'Venus', 'Mars', \
    'Mercury_(planet)']
DWARFPLANETS = ['Haumea_(dwarf_planet)', 'Makemake_(dwarf_planet)', "Ceres_(dwarf_planet)", \
    "Pluto", "Eris_(dwarf_planet)"]
COMETS = ["Halley's_Comet", 'Tempel_1', '19P/Borrelly', '81P/Wild', '103P/Hartley', \
    "67P/Churyumov–Gerasimenko", "26P/Grigg–Skjellerup", "21P/Giacobini–Zinner"] # 1P/Halley
MOONS = ['Ganymede_(moon)', 'Titan_(moon)', 'Callisto_(moon)', 'Io_(moon)', 'Moon', \
    'Europa_(moon)', 'Triton_(moon)', 'Titania_(moon)', 'Rhea_(moon)', 'Oberon_(moon)', \
    'Iapetus_(moon)', 'Charon_(moon)', 'Umbriel_(moon)', 'Ariel_(moon)', 'Dione_(moon)', \
    'Tethys_(moon)', 'Enceladus_(moon)', 'Miranda_(moon)', 'Proteus_(moon)', 'Mimas_(moon)', \
    'Nereid_(moon)', 'Hyperion_(moon)', 'Phoebe_(moon)', 'Larissa_(moon)', 'Janus_(moon)', \
    'Amalthea_(moon)', 'Puck_(moon)', 'Epimetheus_(moon)', 'Thebe_(moon)', 'Adrastea_(moon)', \
    'Juliet_(moon)', 'Prometheus_(moon)', 'Pandora_(moon)', 'Metis_(moon)', 'Hydra_(moon)', \
    'Nix_(moon)', 'Helene_(moon)', 'Atlas_(moon)', 'Pan_(moon)', 'Telesto_(moon)', 'Phobos_(moon)', \
    'Calypso_(moon)', 'Kerberos_(moon)', 'Deimos_(moon)', 'Styx_(moon)', 'Daphnis_(moon)', \
    'Methone_(moon)', 'Pallene_(moon)', 'Polydeuces_(moon)', "Aegaeon (moon)"]
EARTH_MOONS = ['Moon']
MARS_MOONS = ['Phobos_(moon)', 'Deimos_(moon)']
JUPITER_MOONS = ['Io_(moon)', 'Europa_(moon)', 'Ganymede_(moon)', 'Callisto_(moon)', \
    'Amalthea_(moon)', 'Himalia_(moon)', 'Elara_(moon)', 'Thebe_(moon)', 'Adrastea_(moon)', \
    'Metis_(moon)']
SATURN_MOONS = ['Mimas_(moon)', 'Enceladus_(moon)', 'Tethys_(moon)', 'Dione_(moon)', \
    'Rhea_(moon)', 'Titan_(moon)', 'Hyperion_(moon)', 'Iapetus_(moon)', 'Phoebe_(moon)', \
    'Janus_(moon)', 'Epimetheus_(moon)', 'Helene_(moon)', 'Telesto_(moon)', 'Calypso_(moon)', \
    'Atlas_(moon)', 'Prometheus_(moon)', 'Pandora_(moon)', 'Pan_(moon)', 'Ymir_(moon)', \
    'Methone_(moon)', 'Pallene_(moon)', 'Polydeuces_(moon)', 'Daphnis_(moon)', 'Aegaeon_(moon)']
URANUS_MOONS = ['Ariel_(moon)', 'Umbriel_(moon)', 'Titania_(moon)', 'Oberon_(moon)', \
    'Miranda_(moon)', 'Cordelia_(moon)', 'Ophelia_(moon)', 'Bianca_(moon)', 'Cressida_(moon)', \
    'Desdemona_(moon)', 'Juliet_(moon)', 'Portia_(moon)', 'Rosalind_(moon)', 'Belinda_(moon)', \
    'Puck_(moon)']
NEPTUNE_MOONS = ['Triton_(moon)', 'Nereid_(moon)', 'Naiad_(moon)', 'Thalassa_(moon)', \
    'Despina_(moon)', 'Galatea_(moon)', 'Larissa_(moon)', 'Proteus_(moon)']
PLUTO_MOONS = ['Charon_(moon)', 'Nix_(moon)', 'Hydra_(moon)', 'Kerberos_(moon)', 'Styx_(moon)']
TNOS = ["(225088)_2007_OR10", '50000_Quaoar', '90377_Sedna', '(307261)_2002_MS4', '90482_Orcus', \
    '120347_Salacia', '15760_Albion', '486958_Arrokoth']
NEOS = ["433_Eros", "1566_Icarus", "1620_Geographos", "1627_Ivar", "1685_Toro", "3200_Phaethon", \
    "4179_Toutatis", "4769_Castalia", "6489_Golevka", '25143_Itokawa', "(53319)_1999_JM8", \
    "65803_Didymos", "99942_Apophis", "101955_Bennu", "(136617)_1994_CC", '162173_Ryugu', \
    "2014_JO25", "2014_HQ124", "2015_TB145", "2017_BQ6"]

ASTEROIDS = ["2_Pallas", "3_Juno", "4_Vesta", "5_Astraea", "6_Hebe", "7_Iris", "8_Flora", \
    "9_Metis", "10_Hygiea", "12_Victoria", "13_Egeria", "15_Eunomia", "16_Psyche", "17_Thetis", \
    "18_Melpomene", "21_Lutetia", "26_Proserpina", "31_Euphrosyne", "52_Europa", "90_Antiope", \
    "121_Hermione", "216_Kleopatra", '243_Ida', "253_Mathilde", "511_Davida", "704_Interamnia", \
    "951_Gaspra", '2867_Šteins', '5535_Annefrank', '9969_Braille']

ALLBODIES = ['Sun'] + PLANETS + DWARFPLANETS + COMETS + MOONS + TNOS + NEOS + ASTEROIDS

BODIES_SIZE_ORDERED = ["Sun", "Jupiter", "Saturn", "Uranus", "Neptune", "Earth", "Venus", "Mars", "Ganymede_(moon)", "Titan_(moon)", "Mercury_(planet)", "Callisto_(moon)", "Io_(moon)", "Moon", "Europa_(moon)", "Triton_(moon)", "Pluto", "Eris_(dwarf_planet)", "Haumea_(dwarf_planet)", "Titania_(moon)", "Rhea_(moon)", "Oberon_(moon)", "Iapetus_(moon)", "Makemake_(dwarf_planet)", "(225088)_2007_OR10", "Charon_(moon)", "Umbriel_(moon)", "Ariel_(moon)", "Dione_(moon)", "50000_Quaoar", "Tethys_(moon)", "90377_Sedna", "Ceres_(dwarf_planet)", "(307261)_2002_MS4", "90482_Orcus", "120347_Salacia", "4_Vesta", "2_Pallas", "Enceladus_(moon)", "Miranda_(moon)", "10_Hygiea", "Proteus_(moon)", "Mimas_(moon)", "Nereid_(moon)", "704_Interamnia", "511_Davida", "Hyperion_(moon)", "3_Juno", "16_Psyche", "7_Iris", "Phoebe_(moon)", "Larissa_(moon)", "6_Hebe", "Janus_(moon)", "15760_Albion", "Amalthea_(moon)", "Puck_(moon)", "8_Flora", "5_Astraea", "Epimetheus_(moon)", "Thebe_(moon)", "21_Lutetia", "Juliet_(moon)", "Prometheus_(moon)", "Pandora_(moon)", "253_Mathilde", "Metis_(moon)", "Hydra_(moon)", "Nix_(moon)", "Helene_(moon)", "486958_Arrokoth", "243_Ida", "Atlas_(moon)", "Pan_(moon)", "Telesto_(moon)", "Phobos_(moon)", "Calypso_(moon)", "433_Eros", 'Adrastea_(moon)', "Kerberos_(moon)", "Deimos_(moon)", "951_Gaspra", "Halley's_Comet", "Styx_(moon)", "Daphnis_(moon)", "Tempel_1", "3200_Phaethon", "19P/Borrelly", "2867_Šteins", "5535_Annefrank", 'Pallene_(moon)', "81P/Wild", "67P/Churyumov–Gerasimenko", "4179_Toutatis", "Methone_(moon)", "Polydeuces_(moon)", "1620_Geographos", "9969_Braille", "Dactyl", "66391_Moshup", "103P/Hartley", "(29075)_1950_DA", "162173_Ryugu", "2014_JO25", "65803_Didymos", "Aegaeon_(moon)", "2015_TB145", "101955_Bennu", "(436724)_2011_UW158", "25143_Itokawa", "99942_Apophis", "2017_BQ6"]

BODIES_RU_NAMES = {
  "Sun": "Солнце",
  "Jupiter": "Юпитер",
  "Saturn": "Сатурн",
  "Uranus": "Уран",
  "Neptune": "Нептун",
  "Earth": "Земля",
  "Venus": "Венера",
  "Mars": "Марс",
  "Ganymede_(moon)": "Ганимед",
  "Titan_(moon)": "Титан",
  "Mercury_(planet)": "Меркурий",
  "Callisto_(moon)": "Каллисто",
  "Io_(moon)": "Ио",
  "Moon": "Луна",
  "Europa_(moon)": "Европа",
  "Triton_(moon)": "Тритон",
  "Pluto": "Плутон",
  "Eris_(dwarf_planet)": "Эрида",
  "Haumea_(dwarf_planet)": "Хаумеа",
  "Titania_(moon)": "Титания",
  "Rhea_(moon)": "Рея",
  "Oberon_(moon)": "Оберон",
  "Iapetus_(moon)": "Япет",
  "Makemake_(dwarf_planet)": "Макемаке",
  "(225088)_2007_OR10": "2007 OR10",
  "Charon_(moon)": "Харон",
  "Umbriel_(moon)": "Умбриэль",
  "Ariel_(moon)": "Ариэль",
  "Dione_(moon)": "Диона",
  "50000_Quaoar": "Квавар",
  "Tethys_(moon)": "Тефия",
  "90377_Sedna": "Седна",
  "Ceres_(dwarf_planet)": "Церера",
  "(307261)_2002_MS4": "2002 MS4",
  "90482_Orcus": "Орк",
  "120347_Salacia": "Салация",
  "4_Vesta": "Веста",
  "2_Pallas": "Паллада",
  "Enceladus_(moon)": "Энцелад",
  "Miranda_(moon)": "Миранда",
  "10_Hygiea": "Гигея",
  "Proteus_(moon)": "Протей",
  "Mimas_(moon)": "Мимас",
  "Nereid_(moon)": "Нереида",
  "704_Interamnia": "Интерамния",
  "511_Davida": "Давида",
  "Hyperion_(moon)": "Гиперион",
  "3_Juno": "Юнона",
  "16_Psyche": "Психея",
  "324_Bamberga": "Бамберга",
  "7_Iris": "Ирида",
  "Phoebe_(moon)": "Феба",
  "Larissa_(moon)": "Ларисса",
  "6_Hebe": "Геба",
  "Janus_(moon)": "Янус",
  "90_Antiope": "Антиопа",
  "15760_Albion": "Альбион",
  "Amalthea_(moon)": "Амальтея",
  "Puck_(moon)": "Пак",
  "8_Flora": "Флора",
  "5_Astraea": "Астрея",
  "Epimetheus_(moon)": "Эпиметей",
  "Thebe_(moon)": "Фива",
  "21_Lutetia": "Лютеция",
  "Juliet_(moon)": "Джульетта",
  "Prometheus_(moon)": "Прометей",
  "Pandora_(moon)": "Пандора",
  "253_Mathilde": "Матильда",
  "Metis_(moon)": "Метида",
  "Hydra_(moon)": "Гидра",
  "Nix_(moon)": "Никс",
  "Helene_(moon)": "Елена",
  "486958_Arrokoth": "Аррокот",
  "243_Ida": "Ида",
  "Atlas_(moon)": "Атлас",
  "Pan_(moon)": "Пан",
  "Telesto_(moon)": "Телесто",
  "Phobos_(moon)": "Фобос",
  "Calypso_(moon)": "Калипсо",
  "433_Eros": "Эрос",
  "Adrastea_(moon)": "Адрастея",
  "Kerberos_(moon)": "Кербер",
  "Deimos_(moon)": "Деймос",
  "951_Gaspra": "Гаспра",
  "1P/Halley": "Галлея",
  "Styx_(moon)": "Стикс",
  "Daphnis_(moon)": "Дафнис",
  "Tempel_1": "Темпель 1",
  "(53319)_1999_JM8": "1999 JM8",
  "3200_Phaethon": "Фаэтон",
  "19P/Borrelly": "Борелли",
  "2867_%C5%A0teins": "Штейнс",
  "5535_Annefrank": "Аннафранк",
  "Pallene_(moon)": "Паллена",
  "81P/Wild": "Вилт 2",
  "67P/Churyumov–Gerasimenko": "комета Ч-Г",
  "(285263)_1998_QE2": "1998 QE2",
  "4179_Toutatis": "Таутатис",
  "Methone_(moon)": "Мефона",
  "Polydeuces_(moon)": "Полидевк",
  "1620_Geographos": "Географ",
  "9969_Braille": "Брайль",
  "243_Ida#Dactyl": "Дактиль",
  "66391_Moshup": "Мошап",
  "103P/Hartley": "Хартли 2",
  "(29075)_1950_DA": "1950 DA",
  "P/2016_BA14": "P/2016 BA14",
  "(163899)_2003_SD220": "2003 SD220",
  "2017_YE5": "2017 YE5",
  "162173_Ryugu": "Рюгу",
  "2014_JO25": "2014 JO25",
  "65803_Didymos": "Дидим",
  "Aegaeon_(moon)": "Эгеон",
  "2015_TB145": "2015 TB145",
  "101955_Bennu": "Бенну",
  "(436724)_2011_UW158": "2011 UW158",
  "(33342)_1998_WT24": "1998 WT24",
  "25143_Itokawa": "Итокава",
  "99942_Apophis": "Апофис",
  "2014_HQ124": "2014 HQ124",
  "(357439)_2004_BL86": "2004 BL86",
  "2017_BQ6": "2017 BQ6"
}

NEXTNAMS = ["12_Victoria", "13_Egeria", "15_Eunomia", "17_Thetis", "1566_Icarus", "1685_Toro", \
    "(136617)_1994_CC", "(29075)_1950_DA", "4769_Castalia"]

# List of 18 params, excluding discovered, discovery_date:
PARAMS = ['named_after', 'mp_category', 'observation_arc', 'semimajor', 'period', 'dimensions', \
    'satellites', 'mean_diameter', 'surface_area', 'volume', 'mass', 'density', 'rotation', \
        'abs_magnitude', 'mean_radius', 'rot_velocity', 'magnitude', 'angular_size']

STARS = ["Betelgeuse", "Antares", "Altair", "Vega", "Alderamin", "Regulus", "Algol", \
    "Zeta Andromedae", "R_Doradus", "Mira", "T_Leporis", "Pi1_Gruis"]
STARS_PARAMS = ["radius", "mass", "temperature", "gravity", "luminosity", "age_myr"]

obj_data = [
  [
    "Sun",
    "Солнце",
    696342,
    "1.9885E30",
    "",
    [
      "star",
      "he"
    ],
    "Sun.jpg"
  ],
  [
    "Jupiter",
    "Юпитер",
    69911,
    "1.898E27",
    "",
    [
      "pla",
      "he",
      "visited"
    ],
    "Jupiter.jpg"
  ],
  [
    "Saturn",
    "Сатурн",
    58232,
    "5.6834E26",
    "",
    [
      "pla",
      "he",
      "visited"
    ],
    "Saturn.jpg"
  ],
  [
    "Uranus",
    "Уран",
    25362,
    "8.681E25",
    "13.03.1781",
    [
      "pla",
      "he"
    ],
    "Uranus.jpg"
  ],
  [
    "Neptune",
    "Нептун",
    24622,
    "1.024E26",
    "23.09.1846",
    [
      "pla",
      "he"
    ],
    "Neptune.jpg"
  ],
  [
    "Earth",
    "Земля",
    6371,
    "5.972E24",
    "",
    [
      "pla",
      "he",
      "radar"
    ],
    "Earth.jpg"
  ],
  [
    "Venus",
    "Венера",
    6051.8,
    "4.8675E24",
    "",
    [
      "pla",
      "he",
      "radar"
    ],
    "Venus.jpg"
  ],
  [
    "Mars",
    "Марс",
    3389.5,
    "6.4171E23",
    "",
    [
      "pla",
      "he",
      "radar",
      "visited"
    ],
    "Mars.jpg"
  ],
  [
    "Ganymede (moon)",
    "Ганимед",
    2634.1,
    "1.4819E23",
    "13.03.1610",
    [
      "ju",
      "he",
      "moon"
    ],
    "Ganymede.jpg"
  ],
  [
    "Titan (moon)",
    "Титан",
    2574.73,
    "1.3452E23",
    "25.03.1655",
    [
      "sat",
      "he",
      "moon",
      "radar",
      "visited"
    ],
    "Titan.jpg"
  ],
  [
    "Mercury",
    "Меркурий",
    2439.7,
    "3.3011E23",
    "",
    [
      "pla",
      "he",
      "radar",
      "visited"
    ],
    "Mercury.jpg"
  ],
  [
    "Callisto (moon)",
    "Каллисто",
    2410.3,
    "1.0759E23",
    "13.03.1610",
    [
      "ju",
      "he",
      "moon"
    ],
    "Callisto.jpg"
  ],
  [
    "Io (moon)",
    "Ио",
    1821.6,
    "8.932E22",
    "13.03.1610",
    [
      "ju",
      "he",
      "moon"
    ],
    "Io.jpg"
  ],
  [
    "Moon (moon)",
    "Луна",
    1737.1,
    "7.342E22",
    "",
    [
      "ea",
      "he",
      "moon",
      "radar",
      "visited"
    ],
    "Moon.jpg"
  ],
  [
    "Europa (moon)",
    "Европа",
    1560.8,
    "4.7998E22",
    "13.03.1610",
    [
      "ju",
      "he",
      "moon"
    ],
    "Europa_moon.jpg"
  ],
  [
    "Triton (moon)",
    "Тритон",
    1353.4,
    "2.14E22",
    "10.10.1846",
    [
      "ne",
      "he",
      "moon",
      "visited"
    ],
    "Triton.jpg"
  ],
  [
    "(134340) Pluto (dwarf planet)",
    "Плутон",
    1188.3,
    "1.3E22",
    "23.01.1930",
    [
      "dw",
      "he",
      "visited"
    ],
    "Pluto.jpg"
  ],
  [
    "(136199) Eris (dwarf planet)",
    "Эрида",
    1163,
    "1.66E22",
    "21.10.2003",
    [
      "dw",
      "he",
      "dot"
    ],
    "Eris.jpg"
  ],
  [
    "(136108) Haumea (dwarf planet)",
    "Хаумеа",
    798,
    "4.01E21",
    "28.12.2004",
    [
      "dw",
      "he",
      "dot"
    ],
    "Haumea.jpg"
  ],
  [
    "Titania (moon)",
    "Титания",
    788.4,
    "3.4E21",
    "11.01.1787",
    [
      "ur",
      "he",
      "moon"
    ],
    "Titania.jpg"
  ],
  [
    "Rhea (moon)",
    "Рея",
    763.8,
    "2.307E21",
    "23.12.1672",
    [
      "sat",
      "he",
      "moon"
    ],
    "Rhea.jpg"
  ],
  [
    "Oberon (moon)",
    "Оберон",
    761.4,
    "3.08E21",
    "11.01.1787",
    [
      "ur",
      "he",
      "moon"
    ],
    "Oberon.jpg"
  ],
  [
    "Iapetus (moon)",
    "Япет",
    734.5,
    "1.81E21",
    "25.10.1671",
    [
      "sat",
      "moon"
    ],
    "Iapetus.jpg"
  ],
  [
    "(136472) Makemake (dwarf planet)",
    "Макемаке",
    715,
    "4.4E21",
    "31.03.2005",
    [
      "dw",
      "dot",
      "he"
    ],
    "Makemake.jpg"
  ],
  [
    "(225088) 2007 OR10",
    "2007 OR10",
    615,
    "1.75E21",
    "17.07.2007",
    [
      "tno",
      "dot",
      "he"
    ],
    "2007OR10.jpg"
  ],
  [
    "Charon (moon)",
    "Харон",
    606,
    "1.59E21",
    "13.04.1978",
    [
      "pl",
      "he",
      "moon",
      "visited"
    ],
    "Charon.jpg"
  ],
  [
    "Umbriel (moon)",
    "Умбриэль",
    584.7,
    "1.28E21",
    "24.10.1851",
    [
      "ur",
      "he",
      "moon"
    ],
    "Umbriel.jpg"
  ],
  [
    "Ariel (moon)",
    "Ариэль",
    578.9,
    "1.25E21",
    "24.10.1851",
    [
      "ur",
      "he",
      "moon"
    ],
    "Ariel.jpg"
  ],
  [
    "Dione (moon)",
    "Диона",
    561.4,
    "1.095E21",
    "21.03.1684",
    [
      "sat",
      "he",
      "moon"
    ],
    "Dione.jpg"
  ],
  [
    "(50000) Quaoar",
    "Квавар",
    560.5,
    "1.4E21",
    "05.06.2002",
    [
      "tno",
      "dot",
      "he"
    ],
    "Quaoar.jpg"
  ],
  [
    "Tethys (moon)",
    "Тефия",
    531.1,
    "6.175E20",
    "21.03.1684",
    [
      "sat",
      "he",
      "moon"
    ],
    "Tethys.jpg"
  ],
  [
    "(90377) Sedna",
    "Седна",
    497.5,
    "",
    "14.11.2003",
    [
      "tno",
      "dot",
      "he"
    ],
    "Sedna.jpg"
  ],
  [
    "(1) Ceres (dwarf planet)",
    "Церера",
    470,
    "9.3835E20",
    "01.01.1801",
    [
      "dw",
      "he",
      "visited"
    ],
    "Ceres.jpg"
  ],
  [
    "(307261) 2002 MS4",
    "2002 MS4",
    467,
    "",
    "18.06.2002",
    [
      "tno",
      "dot",
      "he"
    ],
    "2002MS4.jpg"
  ],
  [
    "(90482) Orcus",
    "Орк",
    458,
    "6.4E20",
    "17.02.2004",
    [
      "tno",
      "dot",
      "he"
    ],
    "Orcus.jpg"
  ],
  [
    "(120347) Salacia",
    "Салация",
    446.5,
    "4.92E20",
    "22.09.2004",
    [
      "tno",
      "dot",
      "he"
    ],
    "Salacia.jpg"
  ],
  [
    "(4) Vesta",
    "Веста",
    262.7,
    "2.59E20",
    "29.03.1807",
    [
      "mab",
      "visited"
    ],
    "Vesta.jpg"
  ],
  [
    "(2) Pallas",
    "Паллада",
    256,
    "2.11E20",
    "28.03.1802",
    [
      "mab",
      "highcontrast"
    ],
    "Pallas.jpg"
  ],
  [
    "Enceladus (moon)",
    "Энцелад",
    252.1,
    "1.08E20",
    "28.08.1789",
    [
      "sat",
      "he",
      "moon"
    ],
    "Enceladus.jpg"
  ],
  [
    "Miranda (moon)",
    "Миранда",
    235.8,
    "0.66E20",
    "16.02.1948",
    [
      "ur",
      "he",
      "moon"
    ],
    "Miranda.jpg"
  ],
  [
    "(10) Hygiea",
    "Гигея",
    217,
    "0.83E20",
    "12.04.1849",
    [
      "mab",
      "highcontrast"
    ],
    "Hygiea.jpg"
  ],
  [
    "Proteus (moon)",
    "Протей",
    210,
    "0.44E20",
    "16.06.1989",
    [
      "ne",
      "moon"
    ],
    "Proteus.jpg"
  ],
  [
    "Mimas (moon)",
    "Мимас",
    198.2,
    "3.749E19",
    "17.09.1789",
    [
      "sat",
      "he",
      "moon"
    ],
    "Mimas.jpg"
  ],
  [
    "Nereid (moon)",
    "Нереида",
    170,
    "3.09E19",
    "01.05.1949",
    [
      "ne",
      "lowcontrast",
      "moon"
    ],
    "Nereid.jpg"
  ],
  [
    "(704) Interamnia",
    "Интерамния",
    166,
    "3.8E19",
    "02.10.1910",
    [
      "mab",
      "highcontrast"
    ],
    "Interamnia.jpg"
  ],
  [
    "(511) Davida",
    "Давида",
    145,
    "3.8E19",
    "30.05.1903",
    [
      "mab",
      "highcontrast"
    ],
    "Davida.jpg"
  ],
  [
    "Hyperion (moon)",
    "Гиперион",
    138.6,
    "5.62E18",
    "16.09.1848",
    [
      "sat",
      "moon"
    ],
    "Hyperion.jpg"
  ],
  [
    "(3) Juno",
    "Юнона",
    135.7,
    "2.9E19",
    "01.09.1804",
    [
      "mab",
      "highcontrast"
    ],
    "Juno.jpg"
  ],
  [
    "(16) Psyche",
    "Психея",
    112.5,
    "2.4E19",
    "17.03.1852",
    [
      "mab",
      "highcontrast"
    ],
    "Psyche.jpg"
  ],
  [
    "(324) Bamberga",
    "Бамберга",
    112,
    "1.1E19",
    "25.02.1892",
    [
      "mab",
      "highcontrast"
    ],
    "Bamberga.jpg"
  ],
  [
    "(7) Iris",
    "Ирида",
    107,
    "1.37E19",
    "13.08.1847",
    [
      "mab",
      "highcontrast"
    ],
    "Iris.jpg"
  ],
  [
    "Phoebe (moon)",
    "Феба",
    106.56,
    "8.29E18",
    "16.08.1898",
    [
      "sat",
      "moon"
    ],
    "Phoebe.jpg"
  ],
  [
    "Larissa (moon)",
    "Ларисса",
    97,
    "4.2E18",
    "24.05.1981",
    [
      "ne",
      "moon"
    ],
    "Larissa.jpg"
  ],
  [
    "(6) Hebe",
    "Геба",
    93,
    "1.27E19",
    "01.07.1847",
    [
      "mab",
      "highcontrast"
    ],
    "Hebe.jpg"
  ],
  [
    "Janus (moon)",
    "Янус",
    89.5,
    "1.898E18",
    "15.12.1966",
    [
      "sat",
      "moon"
    ],
    "Janus.jpg"
  ],
  [
    "(90) Antiope",
    "Антиопа",
    84,
    "8.3E17",
    "01.10.1866",
    [
      "mab",
      "highcontrast"
    ],
    "Antiope.jpg"
  ],
  [
    "(15760) Albion",
    "Альбион",
    84,
    "",
    "30.08.1992",
    [
      "tno",
      "dot"
    ],
    "Albion.jpg"
  ],
  [
    "Amalthea (moon)",
    "Амальтея",
    83.5,
    "2.08E18",
    "09.09.1892",
    [
      "ju",
      "moon"
    ],
    "Amalthea.jpg"
  ],
  [
    "Puck (moon)",
    "Пак",
    81,
    "2.9E18",
    "30.12.1985",
    [
      "ur",
      "moon"
    ],
    "Puck.jpg"
  ],
  [
    "(8) Flora",
    "Флора",
    64,
    "6.6E18",
    "18.10.1847",
    [
      "mab",
      "innermb",
      "lightcurve"
    ],
    "Flora.jpg"
  ],
  [
    "(5) Astraea",
    "Астрея",
    59.5,
    "2.9E18",
    "08.12.1845",
    [
      "mab",
      "lightcurve"
    ],
    "Astraea.jpg"
  ],
  [
    "Epimetheus (moon)",
    "Эпиметей",
    58.1,
    "5.27E17",
    "18.12.1966",
    [
      "sat",
      "moon"
    ],
    "Epimetheus.jpg"
  ],
  [
    "Thebe (moon)",
    "Фива",
    49.3,
    "4.3E17",
    "05.03.1979",
    [
      "ju",
      "moon"
    ],
    "Thebe.jpg"
  ],
  [
    "(21) Lutetia",
    "Лютеция",
    49,
    "1.7E18",
    "15.11.1852",
    [
      "mab",
      "visited"
    ],
    "Lutetia.jpg"
  ],
  [
    "Juliet (moon)",
    "Джульетта",
    46.8,
    "5.6E17",
    "03.01.1986",
    [
      "ur",
      "lowcontrast",
      "moon"
    ],
    "Juliet.jpg"
  ],
  [
    "Prometheus (moon)",
    "Прометей",
    43.1,
    "1.59E17",
    "01.10.1980",
    [
      "sat",
      "moon"
    ],
    "Prometheus.jpg"
  ],
  [
    "Pandora (moon)",
    "Пандора",
    40.7,
    "1.37E17",
    "01.10.1980",
    [
      "sat",
      "moon"
    ],
    "Pandora.jpg"
  ],
  [
    "(253) Mathilde",
    "Матильда",
    26.4,
    "1.03E17",
    "12.11.1885",
    [
      "mab",
      "visited"
    ],
    "Mathilde.jpg"
  ],
  [
    "Metis (moon)",
    "Метида",
    21.5,
    "1.2E17",
    "04.03.1979",
    [
      "ju",
      "lowcontrast",
      "moon"
    ],
    "Metis_moon.jpg"
  ],
  [
    "Hydra (moon)",
    "Гидра",
    19.65,
    "4.8E16",
    "15.05.2005",
    [
      "pl",
      "moon"
    ],
    "Hydra.jpg"
  ],
  [
    "Nix (moon)",
    "Никс",
    19.017,
    "4.5E16",
    "15.05.2005",
    [
      "pl",
      "moon"
    ],
    "Nix.jpg"
  ],
  [
    "Helene (moon)",
    "Елена",
    17.6,
    "1.139E16",
    "01.03.1980",
    [
      "sat",
      "moon"
    ],
    "Helene.jpg"
  ],
  [
    "(486958) Arrokoth",
    "Аррокот",
    15.85,
    "1.25E16",
    "26.06.2014",
    [
      "tno",
      "visited"
    ],
    "Arrokoth.jpg"
  ],
  [
    "(243) Ida",
    "Ида",
    15.7,
    "42E15",
    "29.09.1884",
    [
      "mab",
      "visited"
    ],
    "Ida.jpg"
  ],
  [
    "Atlas (moon)",
    "Атлас",
    15.1,
    "6.60E15",
    "01.10.1980",
    [
      "sat",
      "moon"
    ],
    "Atlas.jpg"
  ],
  [
    "Pan (moon)",
    "Пан",
    14.1,
    "4.95E15",
    "16.07.1990",
    [
      "sat",
      "moon"
    ],
    "Pan.jpg"
  ],
  [
    "Telesto (moon)",
    "Телесто",
    12.4,
    "4.046E15",
    "08.04.1980",
    [
      "sat",
      "moon"
    ],
    "Telesto.jpg"
  ],
  [
    "Phobos (moon)",
    "Фобос",
    11.267,
    "1.0659E16",
    "18.08.1877",
    [
      "mar",
      "moon"
    ],
    "Phobos.jpg"
  ],
  [
    "Calypso (moon)",
    "Калипсо",
    10.7,
    "2.548E15",
    "13.03.1980",
    [
      "sat",
      "moon"
    ],
    "Calypso.jpg"
  ],
  [
    "(433) Eros",
    "Эрос",
    8.42,
    "6.69E15",
    "13.08.1898",
    [
      "neo",
      "visited"
    ],
    "Eros.jpg"
  ],
  [
    "Adrastea (moon)",
    "Адрастея",
    8.2,
    "2E15",
    "08.07.1979",
    [
      "ju",
      "moon",
      "lowcontrast"
    ],
    "Adrastea.jpg"
  ],
  [
    "Kerberos (moon)",
    "Кербер",
    6.33,
    "1.65E16",
    "28.06.2011",
    [
      "pl",
      "lowcontrast",
      "moon"
    ],
    "Kerberos.jpg"
  ],
  [
    "Deimos (moon)",
    "Деймос",
    6.2,
    "1.476E15",
    "12.08.1877",
    [
      "mar",
      "moon"
    ],
    "Deimos.jpg"
  ],
  [
    "(951) Gaspra",
    "Гаспра",
    6.266,
    "2.5E16",
    "30.07.1916",
    [
      "mab",
      "innermb",
      "visited"
    ],
    "Gaspra.jpg"
  ],
  [
    "1P/Halley",
    "Галлея",
    5.75,
    "2.2E14",
    "25.12.1758",
    [
      "co",
      "visited"
    ],
    "Halley.jpg"
  ],
  [
    "Styx (moon)",
    "Стикс",
    5.5,
    "7.5E15",
    "26.06.2012",
    [
      "pl",
      "lowcontrast",
      "moon"
    ],
    "Styx.jpg"
  ],
  [
    "Daphnis (moon)",
    "Дафнис",
    3.8,
    "77.93E12",
    "01.05.2005",
    [
      "sat",
      "moon"
    ],
    "Daphnis.jpg"
  ],
  [
    "9P/Tempel",
    "Темпель 1",
    3,
    "4.5E13",
    "03.04.1867",
    [
      "co",
      "visited"
    ],
    "Tempel1.jpg"
  ],
  [
    "(53319) 1999 JM8",
    "1999 JM8",
    3,
    "",
    "13.05.1999",
    [
      "neo",
      "radar"
    ],
    "1999JM8.jpg"
  ],
  [
    "(3200) Phaethon",
    "Фаэтон",
    2.9,
    "1.4E14",
    "11.10.1983",
    [
      "neo",
      "radar"
    ],
    "Phaethon.gif"
  ],
  [
    "19P/Borrelly",
    "Борелли",
    2.66,
    "2E13",
    "28.12.1904",
    [
      "co",
      "visited"
    ],
    "Borrelly.jpg"
  ],
  [
    "(2867) Šteins",
    "Штейнс",
    2.58,
    "",
    "04.11.1969",
    [
      "mab",
      "visited"
    ],
    "Steins.jpg"
  ],
  [
    "(5535) Annefrank",
    "Аннафранк",
    2.4,
    "",
    "23.03.1942",
    [
      "mab",
      "visited"
    ],
    "Annefrank.jpg"
  ],
  [
    "Pallene (moon)",
    "Паллена",
    2.22,
    "2E13",
    "06.01.1978",
    [
      "sat",
      "moon",
      "lowcontrast"
    ],
    "Pallene.jpg"
  ],
  [
    "81P/Wild",
    "Вилт 2",
    2.133,
    "2.3E13",
    "06.01.1978",
    [
      "co",
      "visited"
    ],
    "Wild.jpg"
  ],
  [
    "67P/Churyumov–Gerasimenko",
    "комета Ч-Г",
    2,
    "9.98E12",
    "20.09.1969",
    [
      "co",
      "visited"
    ],
    "ChuryumovGerasimenko.jpg"
  ],
  [
    "(285263) 1998 QE2",
    "1998 QE2",
    1.6,
    "",
    "19.08.1998",
    [
      "neo",
      "radar"
    ],
    "1998QE2.jpg"
  ],
  [
    "(4179) Toutatis",
    "Таутатис",
    1.516,
    "5.05E13",
    "04.01.1989",
    [
      "neo",
      "radar",
      "visited"
    ],
    "Toutatis.jpg"
  ],
  [
    "Methone (moon)",
    "Мефона",
    1.45,
    "8.992E12",
    "01.06.2004",
    [
      "sat",
      "moon"
    ],
    "Methone.jpg"
  ],
  [
    "Polydeuces (moon)",
    "Полидевк",
    1.3,
    "3E13",
    "01.06.2004",
    [
      "sat",
      "lowcontrast",
      "moon"
    ],
    "Polydeuces.jpg"
  ],
  [
    "(1620) Geographos",
    "Географ",
    0.94,
    "2.6E13",
    "14.09.1951",
    [
      "neo",
      "radar",
      "lightcurve"
    ],
    "Geographos.jpg"
  ],
  [
    "(9969) Braille",
    "Брайль",
    0.82,
    "7.8E15",
    "27.05.1992",
    [
      "mab",
      "lowcontrast",
      "visited"
    ],
    "Braille.jpg"
  ],
  [
    "Dactyl",
    "Дактиль",
    0.7,
    "",
    "28.08.1993",
    [
      "mab",
      "visited"
    ],
    "Dactyl.jpg"
  ],
  [
    "(214869) 2007 PA8",
    "2007 PA8",
    0.69,
    "",
    "09.08.2007",
    [
      "neo",
      "radar"
    ],
    "2007PA8.jpg"
  ],
  [
    "(66391) Moshup",
    "Мошап",
    0.66,
    "2.49E12",
    "20.05.1999",
    [
      "neo",
      "radar",
      "highcontrast"
    ],
    "Moshup.jpg"
  ],
  [
    "103P/Hartley",
    "Хартли 2",
    0.57,
    "3E11",
    "15.03.1986",
    [
      "co",
      "radar",
      "visited"
    ],
    "Hartley.jpg"
  ],
  [
    "(29075) 1950 DA",
    "1950 DA",
    0.55,
    "4E12",
    "23.02.1950",
    [
      "neo",
      "radar"
    ],
    "1950DA.gif"
  ],
  [
    "P/2016 BA14",
    "P/2016 BA14",
    0.5,
    "",
    "21.01.2016",
    [
      "co",
      "radar"
    ],
    "P2016BA14.jpg"
  ],
  [
    "(163899) 2003 SD220",
    "2003 SD220",
    0.5,
    "",
    "29.09.2003",
    [
      "neo",
      "radar"
    ],
    "2003SD220.jpg"
  ],
  [
    "2017 YE5",
    "2017 YE5",
    0.5,
    "",
    "21.12.2017",
    [
      "neo",
      "radar"
    ],
    "2017YE5.jpg"
  ],
  [
    "(162173) Ryugu",
    "Рюгу",
    0.432,
    "4.5E11",
    "10.05.1999",
    [
      "neo",
      "visited"
    ],
    "Ryugu.jpg"
  ],
  [
    "2014 JO25",
    "2014 JO25",
    0.4,
    "",
    "05.05.2014",
    [
      "neo",
      "radar"
    ],
    "2014JO25.gif"
  ],
  [
    "(65803) Didymos",
    "Дидим",
    0.39,
    "3.645E12",
    "11.04.1996",
    [
      "neo",
      "radar",
      "lightcurve"
    ],
    "Didymos.jpg"
  ],
  [
    "Aegaeon (moon)",
    "Эгеон",
    0.33,
    "",
    "03.03.2009",
    [
      "sat",
      "moon",
      "lowcontrast"
    ],
    "Aegaeon.jpg"
  ],
  [
    "2015 TB145",
    "2015 TB145",
    0.325,
    "",
    "10.10.2015",
    [
      "neo",
      "radar"
    ],
    "2015TB145.gif"
  ],
  [
    "(101955) Bennu",
    "Бенну",
    0.245,
    "7.329E10",
    "11.09.1999",
    [
      "neo",
      "visited"
    ],
    "Bennu.jpg"
  ],
  [
    "(436724) 2011 UW158",
    "2011 UW158",
    0.22,
    "",
    "25.10.2011",
    [
      "neo",
      "radar"
    ],
    "2011UW158.gif"
  ],
  [
    "(33342) 1998 WT24",
    "1998 WT24",
    0.205,
    "7.8E10",
    "25.11.1998",
    [
      "neo",
      "radar"
    ],
    "1998WT24.jpg"
  ],
  [
    "(25143) Itokawa",
    "Итокава",
    0.173,
    "3.51E10",
    "26.09.1998",
    [
      "neo",
      "visited"
    ],
    "Itokawa.jpg"
  ],
  [
    "(99942) Apophis",
    "Апофис",
    0.17,
    "6.1E10",
    "19.06.2004",
    [
      "neo",
      "lightcurve"
    ],
    "Apophis.jpg"
  ],
  [
    "2014 HQ124",
    "2014 HQ124",
    0.163,
    "",
    "23.04.2014",
    [
      "neo",
      "radar"
    ],
    "2014HQ124.jpg"
  ],
  [
    "(357439) 2004 BL86",
    "2004 BL86",
    0.15,
    "",
    "30.01.2004",
    [
      "neo",
      "radar"
    ],
    "2004BL86.gif"
  ],
  [
    "2017 BQ6",
    "2017 BQ6",
    0.078,
    "",
    "26.01.2017",
    [
      "neo",
      "radar"
    ],
    "2017BQ6.gif"
  ]
]