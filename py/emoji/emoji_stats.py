import json # подключение библиотеки для работы с файлами JSON
import urllib.request

RU_NAMES = {'joy': 'Слёзы радости', 'heavy heart': 'Сердце', 'recycle': 'Переработка',
    'heart-shaped': 'Глаза-сердца', 'loudly': 'Громко плачу', 'black heart suit': 'Червы',
    'smiling': 'Счастлив', 'unamused': 'Равнодушие', 'face kiss': 'Целую',
    'kiss mark': 'След от поцелуя', 'thumbs': 'Класс', 'rolling': 'Катаюсь от смеха'
}

emostats_all = 1987.8
emostats = {'joy': 305,'heavy heart': 156.5, 'face kiss': 112.4,
    'heart-shaped': 81.2, 'rolling': 43.5, 'loudly': 33.3,
    'thumbs': 30.7, 'smiling': 29, 'kiss mark': 28.5,
    'unamused': 7.3, 'black heart suit': 4.3, 'recycle': 0.0407
}

emoinst = {'joy': 8.916,'heavy heart': 33.623, 'face kiss': 5.793,
    'heart-shaped': 13.227, 'rolling': 1.314, 'loudly': 1.685,
    'thumbs': 4.353, 'smiling': 4.815, 'kiss mark': 3.26,
    'unamused': 0.253, 'black heart suit': 2.798, 'recycle': 0.0883
}

emotrack_all = 27294
emotrack = {'joy': 2594, 'heavy heart': 1248, 'recycle': 965,
    'heart-shaped': 939, 'loudly': 781, 'black heart suit': 733,
    'smiling': 619, 'unamused': 494, 'face kiss': 466,
    'kiss mark': 106, 'thumbs': 263.7, 'rolling': 0.00001
}

frac = round(emotrack_all/emostats_all, 2)
print("Эмодзи в", frac, "раз больше в твиттере, чем в сообщениях, набранных пользователями iOS")

for name in emotrack:
    print(name, emostats[name], emoinst[name], emotrack[name])


for name, count in emotrack.items():
    twitter_to_inst = round(count / emoinst.get(name), 3)
    twitter_to_xpress = round(count / emostats.get(name), 3)
    xpress_to_inst = round(emostats.get(name) / emoinst.get(name), 3)
    print('{:<16}'.format(RU_NAMES[name]), '{:>9.3f}'.format(twitter_to_inst), \
          '{:>9.3f}'.format(twitter_to_xpress), xpress_to_inst)


JSON_RANKINGS_URL = 'https://api.emojitracker.com/v1/rankings'
rankings_obj = urllib.request.urlopen(JSON_RANKINGS_URL)
json_rankings = json.load(rankings_obj)
print(type(json_rankings), len(json_rankings), json_rankings[0])

JSON_FILENAME = "emotracker_rankings.json"
with open(JSON_FILENAME, 'w') as myfile:
    json.dump(json_rankings, myfile)

with open(JSON_FILENAME, 'r', encoding="utf-8") as myfile:
    json_rankings_load = json.load(myfile)
print(type(json_rankings_load), len(json_rankings_load), json_rankings_load[0])
print("Списки одинаковы?", json_rankings == json_rankings_load)
