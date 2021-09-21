# gvard.github.io/py/
Pages and examples about Python programming language and data mining.

## Исследование статистики эмодзи в [twitter](http://emojitracker.com/), Instagram и [эмодзи-клавиатуре EmojiXpress](http://www.emojistats.org/)

[Общее количество эмодзи в статистике на emojitracker](http://emojitracker.com/api/stats).
[Информация по тегу "Red Heart emoji"](https://www.instagram.com/explore/tags/%E2%9D%A4%EF%B8%8F/) :heart: в Instagram. Для сравнения: [тег love](https://www.instagram.com/explore/tags/love/).


```python
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
fraction = round(emotrack_all/emostats_all, 2)
print("Эмодзи в", fraction, "раз больше в твиттере, чем в сообщениях, набранных пользователями iOS")
```


Доступ к данным emojitracker по API - см. [github.com/emojitracker/emojitrack-rest-api](https://github.com/emojitracker/emojitrack-rest-api#rest-api-endpoints).
То есть, мы получаем статистику эмодзи с сайта emojitracker.com не через окно браузера в человекочитаемом виде, а через специально созданный интерфейс, API, в машиночитаемом виде.


Для хранения данных используется формат [JSON](https://ru.wikipedia.org/wiki/JSON). Сохранение данных на диске для последующего использования называется сериализацией.
Загружаем данные из файла: 


```python
import json # подключение библиотеки для работы с файлами JSON
# Открытие файла rankings.json в режиме чтения ('r') и в кодировке utf-8,
# работа с ним через переменную myfile:
with open('rankings.json', 'r', encoding="utf-8") as myfile:
    datastore = json.load(myfile)
print(type(datastore), len(datastore))

# Сохраняем в файл sample.json переменную emotrack:
filename = "sample.json" # Переопределение переменной filename
# Открытие файла sample.json в режиме записи ('w'),
# работа с ним через переменную f (для разнообразия, здесь уже не myfile):
with open(filename, 'w') as f:
    json.dump(emotrack, f)
```

For windows binaries see [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)