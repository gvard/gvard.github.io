"""Some astronomical constants here"""
CONSTELLATION_DCT = {
"And": "Андромеда",
"Ant": "Насос",
"Aps": "Райская Птица",
"Aqr": "Водолей",
"Aql": "Орёл",
"Ara": "Жертвенник",
"Ari": "Овен",
"Aur": "Возничий",
"Boo": "Волопас",
"Cae": "Резец",
"Cam": "Жираф",
"Cnc": "Рак",
"CVn": "Гончие Псы",
"CMa": "Большой Пёс",
"CMi": "Малый Пёс",
"Cap": "Козерог",
"Car": "Киль",
"Cas": "Кассиопея",
"Cen": "Центавр",
"Cep": "Цефей",
"Cet": "Кит",
"Cha": "Хамелеон",
"Cir": "Циркуль",
"Col": "Голубь",
"Com": "Волосы Вероники",
"CrA": "Южная Корона",
"CrB": "Северная Корона",
"CrV": "Ворон",
"Crt": "Чаша",
"Cru": "Южный Крест",
"Cyg": "Лебедь",
"Del": "Дельфин",
"Dor": "Золотая Рыба",
"Dra": "Дракон",
"Equ": "Малый Конь",
"Eri": "Эридан",
"For": "Печь",
"Gem": "Близнецы",
"Gru": "Журавль",
"Her": "Геркулес",
"Hor": "Часы",
"Hya": "Гидра",
"Hyi": "Южная Гидра",
"Ind": "Индеец",
"Lac": "Ящерица",
"Leo": "Лев",
"LMi": "Малый Лев",
"Lep": "Заяц",
"Lib": "Весы",
"Lup": "Волк",
"Lyn": "Рысь",
"Lyr": "Лира",
"Men": "Столовая Гора",
"Mic": "Микроскоп",
"Mon": "Единорог",
"Mus": "Муха",
"Nor": "Наугольник",
"Oct": "Октант",
"Oph": "Змееносец",
"Ori": "Орион",
"Pav": "Павлин",
"Peg": "Пегас",
"Per": "Персей",
"Phe": "Феникс",
"Pic": "Живописец",
"Psc": "Рыбы",
"PsA": "Южная Рыба",
"Pup": "Корма",
"Pyx": "Компас",
"Ret": "Сетка",
"Sge": "Стрела",
"Sgr": "Стрелец",
"Sco": "Скорпион",
"Scl": "Скульптор",
"Set": "Щит",
"Ser": "Змея",
"Sex": "Секстант",
"Tau": "Телец",
"Tel": "Телескоп",
"Tri": "Треугольник",
"TrA": "Южный Треугольник",
"Tuc": "Тукан",
"UMa": "Большая Медведица",
"UMi": "Малая Медведица",
"Vel": "Паруса",
"Vir": "Дева",
"Vol": "Летучая Рыба",
"Vul": "Лисичка"
}
CONSTELLTN_RU_DCT = {v: k for k, v in CONSTELLATION_DCT.items()}
CONSTELLTN_RU_DCT.update({
"Б.Медведица": "UMa", "Орел": "Aql", "Большой Пес": "CMa", "Малый Пес": "CMi"})
