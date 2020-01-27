"""Iterate over movie names, get kinopoisk.ru page for each of them, parse page
via BeautifulSoup, pickle resulting data as list of lists."""

import os
import pickle

from kinopoisk.movie import Movie


PICKLE_FILENAME = 'oscar_kinopoisk.pickle'
OSCAR_FILM_NAMES = ['Green Book','The Shape of Water', 'Moonlight', 'Spotlight', 'Бёрдмэн', '12 Years a Slave',
    'Argo', 'The Artist', "The King's Speech", 'The Hurt Locker', 'Slumdog Millionaire', 'No Country for Old Men',
    'The Departed', 'Crash', 'Million Dollar Baby', 'The Lord of the Rings: The Return of the King', 'Chicago',
    'A Beautiful Mind', 'Gladiator', 'American Beauty', 'Shakespeare in Love', 'Titanic', 'The English Patient',
    'Braveheart', 'Forrest Gump', "Schindler's List", 'Unforgiven', 'The Silence of the Lambs', 'Dances with Wolves',
    'Driving Miss Daisy', 'Rain Man', 'The Last Emperor', 'Platoon', 'Out of Africa', 'Amadeus', 'Terms of Endearment',
    'Gandhi', 'Chariots of Fire', 'Ordinary People', 'Kramer vs. Kramer', 'The Deer Hunter', 'Annie Hall', 'Rocky',
    "One Flew Over the Cuckoo's Nest", 'The Godfather: Part II', 'The Sting', 'The Godfather', 'The French Connection',
    'Patton', 'Midnight Cowboy', 'Oliver!', 'In the Heat of the Night', 'A Man for All Seasons', 'The Sound of Music',
    'My Fair Lady', 'Tom Jones', 'Lawrence of Arabia', 'West Side Story', 'The Apartment', 'Ben-Hur', 'Gigi',
    'The Bridge on the River Kwai', 'Around the World in 80 Days', 'Marty', 'On the Waterfront']

oscar_list = []
for movie_name in OSCAR_FILM_NAMES:
    movie = Movie.objects.search(movie_name)[0]
    movie.get_content('main_page')
    oscar_list.append([movie.title_en, movie.title, movie.year, (movie.rating, movie.votes), (movie.imdb_rating, movie.imdb_votes), movie.runtime, movie.genres, movie.budget, movie.profit_world])
    print(oscar_list[-1])

with open(PICKLE_FILENAME, 'wb') as handle:
    pickle.dump(oscar_list, handle)