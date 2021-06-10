import requests
import json
import random

api_key = '' #insert unique api key here
api_base = 'https://api.themoviedb.org/3'
r_json = {}
page_pos = 0

class movieGen:

    def __init__(self,genre,rating):
        '''
        No return
        initializes variables
        '''
        self.genre = genre
        self.rating = rating

    def get_movie(self):
        '''
        Return dictionary with movie information
        Carries out search for movie
        '''

        #reformats genre
        genre_id = self.get_genre_id()
        get_command = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&genre={genre_id}&vote_average.gte={self.rating}"

        #first get obtains the amount of pages
        r = requests.get(get_command)
        r_json = r.json()

        #saves the two values from the search
        total_results = r_json['total_results']

        #picks the movie 
        movie_number = random.randint(0, total_results)

        #there are 20 items per page so this will determine what page the item is on and position on the page
        page = movie_number // 20;
        page_pos = movie_number % 20;

        #must now be updated to reflect the page number
        get_command = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&genre={genre_id}&vote_average.gte={self.rating}&page={page}"
        r = requests.get(get_command)
        r_json = r.json()    

        movie_choice = r_json['results'][page_pos]

        movie = self.format_result(movie_choice)

        return movie

    def re_pick(self):
        '''
        Returns another random movie from the same page
        Saves time by skipping the request
        '''
        new_number = page_pos

        while new_number == page_pos:
            new_number = random.randint(0, 19)

        movie_choice = r_json['results'][page_pos]

        movie = self.format_result(movie_choice)

        return movie

    def format_result(self, movie):
        '''
        Returns formatted movie information
        Creates dictionary from movie json 
        '''
        result = {
            'movie': movie['original_title'],
            'votes': movie['vote_average'],
            'description': movie['overview']
        }
        return result

    def get_genre_id(self):
        '''
        Returns genre id
        '''
        genres = {'Action':28,
            'Adventure':12,
            'Animation':16,
            'Comedy':35,
            'Crime':80,
            'Documentary':99,
            'Drama':18,
            'Family':10751,
            'Fantasy':14,
            'History':36,
            'Horror':27,
            'Music':10402,
            'Mystery':9648,
            'Romance':10749,
            'Science Fiction':878,
            'TV Movie':10770,
            'Thriller':53,
            'War':10752,
            'Western':37,
        }
        return genres[self.genre]








'''
Apple TV = 350
Disney Plus = 337
HBO Go = 280
Netflix = 8
HBO Go = 31
Prime = 119
HBO Max = 384
Prime = 9
Hulu = 15
'''