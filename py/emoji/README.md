# gvard.github.io/py/emoji


Here is example data on emoji statistics (see "python programming" page):


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

frac = round(emotrack_all/emostats_all, 2)
print("Эмодзи в", frac, "раз больше в твиттере, чем в сообщениях, набранных пользователями iOS")
```


Emoji "Heavy heart": :heart:
