# Import essential libraries

# Used to read csv files
import pandas as pd

#Used for Tf-ID vectoring
from sklearn.feature_extraction.text import TfidfVectorizer

# Used for cosine sim
from sklearn.metrics.pairwise import cosine_similarity

#Used to handle query
import re

pd.options.display.max_colwidth = 100  # Character Limit for Plots

# Load movie data (first 500 movies for simplicity)
movies = pd.read_csv('data/movie.metadata.tsv', sep='\t', header=None, nrows=40000)
movies.columns = ['wiki_id', 'freebase_id', 'title', 'release_date', 'revenue', 'runtime', 'languages', 'countries', 'genres']

# Load plot summaries
plots = pd.read_csv('data/plot_summaries.txt', sep='\t', header=None, names=['wiki_id', 'plot'])

# Merge movies with their plots. Use wiki_id to link plot to movie
movie_data = pd.merge(movies, plots, on='wiki_id')

# Clean text data
movie_data['clean_plot'] = movie_data['plot'].str.lower().str.replace(r'[^\w\s]', '', regex=True)


# Create TF-IDF vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movie_data['clean_plot'])

def recommend_movies(query, top_n=5):
    # Process query
    clean_query = re.sub(r'[^\w\s]', '', query.lower())
    query_vector = tfidf.transform([clean_query])
    
    # Calculate similarity scores
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    
    # Get top matches
    movie_indices = similarity_scores.argsort()[0][-top_n:][::-1]
    results = movie_data.iloc[movie_indices][['title', 'genres', 'plot']].reset_index(drop=True)
    results.index += 1  # This is the key line that changes 0-4 to 1-5
    return results
# Example usage
print(recommend_movies("I love action films with a little romance"))


print("Salary expectation: ")
