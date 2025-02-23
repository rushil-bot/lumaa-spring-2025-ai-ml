#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: recommender.py
Author: rushil-bot
Created: February 23, 2025
Version: 1.0
Description: Takes user query and returns list of top 5 movies using TD-IDF
             vectoring. Utilize CMU Movie Summary Corpus for data. Only uses
             first 500 movies for simplicity
Dependencies: pandas, scikit_learn
"""
# Import essential libraries

# Used to read csv files
import pandas as pd

#Used to handle query
import re

#Used for Tf-ID vectoring
from sklearn.feature_extraction.text import TfidfVectorizer

# Used for cosine sim
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data (first 500 movies for simplicity)
movies = pd.read_csv('data/movie.metadata.tsv', sep='\t', header=None, 
                    nrows=500)
movies.columns = ['wiki_id', 'freebase_id', 'title', 'release_date', 'revenue',
                 'runtime', 'languages', 'countries', 'genres']

# Load plot summaries
plots = pd.read_csv('data/plot_summaries.txt', sep='\t', header=None, 
                    names=['wiki_id', 'plot'])

# Merge movies with their plots. Use wiki_id to link plot to movie
movie_data = pd.merge(movies, plots, on='wiki_id')

# Clean text data
movie_data['clean_plot'] = movie_data['plot'].str.lower().str.replace(r'[^\w\s]', '', regex=True)


# Create TF-IDF vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movie_data['clean_plot'])

def recommend_movies(query, top_n=5):

    """
    This function takes the query by the user and calculates the top 5 similar
    films.

    :param query: query entered by user
    :param top_n: Top n results. Automatically set to 5.
    :return: The top 5 closest neighbors to query by TF-IDF.
    """

    # Process query
    clean_query = re.sub(r'[^\w\s]', '', query.lower())
    query_vector = tfidf.transform([clean_query])
    
    # Calculate similarity scores
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    
    # Get top matches
    movie_indices = similarity_scores.argsort()[0][-top_n:][::-1]
    results = movie_data.iloc[movie_indices][['title', 'plot']].reset_index(drop=True)

    results.index += 1  # Reformats indexes from  0-4 to 1-5
    return results


#Takes input from user and prints results
query = input("Query:\n")
print("\n")
print(recommend_movies(query).to_string(max_colwidth=100,justify='center'))

#Salary Expectation
print("\nSalary expectation: $5000/month")
