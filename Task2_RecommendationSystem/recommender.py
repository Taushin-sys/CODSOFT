"""
recommender.py
---------------
Content-based Movie Recommendation System using TF-IDF Vectorization.
This model suggests movies similar to the one entered by the user.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the dataset
movies = pd.read_csv("data/tmdb_5000_movies.csv")

# Keep only the useful columns
movies = movies[['title', 'overview']]

# Drop missing overviews
movies.dropna(inplace=True)

# Combine text features (just using overview for now)
movies['combined'] = movies['overview']

# Vectorize the text using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create a Series to map titles to their indices
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def recommend(title, top_n=5):
    """
    Recommend top_n similar movies to the given title.
    """
    if title not in indices:
        return [f"Sorry, '{title}' not found in database."]
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]  # skip the first (self)
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    print("🎬 Movie Recommendation System 🎬")
    print("Type a movie name (or 'exit' to quit)\n")

    while True:
        movie_name = input("You: ").strip()
        if movie_name.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break
        results = recommend(movie_name)
        print("\nRecommended Movies:")
        for r in results:
            print(f"  - {r}")
        print()