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
    'Amalthea_(moon)', 'Puck_(moon)', 'Epimetheus_(moon)', 'Thebe_(moon)', 'Juliet_(moon)', \
    'Prometheus_(moon)', 'Pandora_(moon)', 'Metis_(moon)', 'Hydra_(moon)', 'Nix_(moon)', \
    'Helene_(moon)', 'Atlas_(moon)', 'Pan_(moon)', 'Telesto_(moon)', 'Phobos_(moon)', \
    'Calypso_(moon)', 'Kerberos_(moon)', 'Deimos_(moon)', 'Styx_(moon)', 'Daphnis_(moon)', \
    'Methone_(moon)', 'Polydeuces_(moon)']
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
    "65803_Didymos", "101955_Bennu", "(136617)_1994_CC", '162173_Ryugu', "2014_JO25", \
    "2014_HQ124", "2015_TB145", "2017_BQ6"]

ASTEROIDS = ["2_Pallas", "3_Juno", "4_Vesta", "5_Astraea", "6_Hebe", "7_Iris", "8_Flora", \
    "9_Metis", "10_Hygiea", "12_Victoria", "13_Egeria", "15_Eunomia", "16_Psyche", "17_Thetis", \
    "18_Melpomene", "21_Lutetia", "26_Proserpina", "31_Euphrosyne", "52_Europa", "90_Antiope", \
    "121_Hermione", "216_Kleopatra", '243_Ida', "253_Mathilde", "511_Davida", "704_Interamnia", \
    "951_Gaspra", '2867_Šteins', '5535_Annefrank', '9969_Braille']

ALLBODIES = ['Sun'] + PLANETS + DWARFPLANETS + COMETS + MOONS + TNOS + NEOS + ASTEROIDS

BODIES_SIZE_ORDERED = ["Sun", "Jupiter", "Saturn", "Uranus", "Neptune", "Earth", "Venus", "Mars", "Ganymede_(moon)", "Titan_(moon)", "Mercury_(planet)", "Callisto_(moon)", "Io_(moon)", "Moon", "Europa_(moon)", "Triton_(moon)", "Pluto", "Eris_(dwarf_planet)", "Haumea_(dwarf_planet)", "Titania_(moon)", "Rhea_(moon)", "Oberon_(moon)", "Iapetus_(moon)", "Makemake_(dwarf_planet)", "(225088)_2007_OR10", "Charon_(moon)", "Umbriel_(moon)", "Ariel_(moon)", "Dione_(moon)", "50000_Quaoar", "Tethys_(moon)", "90377_Sedna", "Ceres_(dwarf_planet)", "(307261)_2002_MS4", "90482_Orcus", "120347_Salacia", "4_Vesta", "2_Pallas", "Enceladus_(moon)", "Miranda_(moon)", "10_Hygiea", "Proteus_(moon)", "Mimas_(moon)", "Nereid_(moon)", "704_Interamnia", "511_Davida", "Hyperion_(moon)", "3_Juno", "16_Psyche", "7_Iris", "Phoebe_(moon)", "Larissa_(moon)", "6_Hebe", "Janus_(moon)", "15760_Albion", "Amalthea_(moon)", "Puck_(moon)", "8_Flora", "5_Astraea", "Epimetheus_(moon)", "Thebe_(moon)", "21_Lutetia", "Juliet_(moon)", "Prometheus_(moon)", "Pandora_(moon)", "253_Mathilde", "Metis_(moon)", "Hydra_(moon)", "Nix_(moon)", "Helene_(moon)", "486958_Arrokoth", "243_Ida", "Atlas_(moon)", "Pan_(moon)", "Telesto_(moon)", "Phobos_(moon)", "Calypso_(moon)", "433_Eros", 'Adrastea_(moon)', "Kerberos_(moon)", "Deimos_(moon)", "951_Gaspra", "Halley's_Comet", "Styx_(moon)", "Daphnis_(moon)", "Tempel_1", "3200_Phaethon", "19P/Borrelly", "2867_Šteins", "5535_Annefrank", 'Pallene_(moon)', "81P/Wild", "67P/Churyumov–Gerasimenko", "4179_Toutatis", "Methone_(moon)", "Polydeuces_(moon)", "9969_Braille", "Dactyl", "103P/Hartley", "(29075)_1950_DA", "162173_Ryugu", "2014_JO25", "65803_Didymos", "Aegaeon_(moon)", "101955_Bennu", "25143_Itokawa", "2017_BQ6"]

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
  "7_Iris": "Ирида",
  "Phoebe_(moon)": "Феба",
  "Larissa_(moon)": "Ларисса",
  "6_Hebe": "Геба",
  "Janus_(moon)": "Янус",
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
  "3200_Phaethon": "Фаэтон",
  "19P/Borrelly": "Борелли",
  "2867_%C5%A0teins": "Штейнс",
  "5535_Annefrank": "Аннафранк",
  "Pallene_(moon)": "Паллена",
  "81P/Wild": "Вилт 2",
  "67P/Churyumov–Gerasimenko": "комета Ч-Г",
  "4179_Toutatis": "Таутатис",
  "Methone_(moon)": "Мефона",
  "Polydeuces_(moon)": "Полидевк",
  "9969_Braille": "Брайль",
  "243_Ida#Dactyl": "Дактиль",
  "103P/Hartley": "Хартли 2",
  "(29075)_1950_DA": "1950 DA",
  "162173_Ryugu": "Рюгу",
  "2014_JO25": "2014 JO25",
  "65803_Didymos": "Дидим",
  "Aegaeon_(moon)": "Эгеон",
  "101955_Bennu": "Бенну",
  "25143_Itokawa": "Итокава",
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
