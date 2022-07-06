"""Iterate over movie names, get kinopoisk.ru page for each of them, parse page
via BeautifulSoup, pickle resulting data as list of lists."""

import os
import pickle

from kinopoisk.movie import Movie

from oscar_data import OSCAR_FILMS, PROFIT_WORLD, PROFIT_USA_INFL_CORR


# PICKLE_FILENAME = 'kinopoisk_oscar.pickle'
# PICKLE_FILENAME = 'kinopoisk_profit_world.pickle'
PICKLE_FILENAME = 'kinopoisk_profit_usa_infl_corr.pickle'

oscar_list = []
for movie_id in PROFIT_USA_INFL_CORR:
    movie = Movie(id=movie_id)
    movie.get_content('main_page')
    oscar_list.append([movie.id, movie.title_en, movie.title, movie.year, (movie.rating, movie.votes), (movie.imdb_rating, movie.imdb_votes), movie.runtime, movie.genres, movie.budget, movie.profit_world, movie.profit_russia, movie.profit_usa, movie.marketing, movie.directors, movie.producers, movie.screenwriters, movie.countries, movie.operators])
    print(oscar_list[-1])

with open(PICKLE_FILENAME, 'wb') as fl:
    pickle.dump(oscar_list, fl)