from django.shortcuts import render
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .utlis import load_movie_data,load_review_data
# Load movie data from CSV
movies = pd.read_csv('C:\\Users\\Aayush\\OneDrive\\Desktop\\classwork\\Group_Project_Django\\MovieRating\\MovieRating\\static\\data\\movies.csv', encoding='utf-8')

# Load user ratings data (assuming you have a CSV file for user ratings)
ratings = pd.read_csv('C:\\Users\\Aayush\OneDrive\\Desktop\\classwork\\Group_Project_Django\\MovieRating\\MovieRating\\static\\data\\ratings.csv', encoding='utf-8')

# Clean movie titles
def clean_title(title):
    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title

movies["clean_title"] = movies["title"].apply(clean_title)

# Create TF-IDF vectorizer for movie titles
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf = vectorizer.fit_transform(movies["clean_title"])

# Function to perform movie search
def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices].iloc[::-1]
    return results
def find_similar_movies(movie_id):
    # Filter ratings for the target movie and ratings greater than a threshold (e.g., 4)
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()

    # Find movies that were highly rated by similar users
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    # Filter movies that were highly rated by the majority of similar users
    similar_user_recs = similar_user_recs[similar_user_recs > 0.1]

    # Find movies that were highly rated by all users
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())

    # Combine the recommendations from similar users and all users
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    
    # Calculate a score based on the ratio of similar users' ratings to all users' ratings
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]

    # Sort movies by the score in descending order to get the most recommended movies
    rec_percentages = rec_percentages.sort_values("score", ascending=False)

    # Merge the recommendations with the movie data to get movie details
    recommended_movies = rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]

    return recommended_movies

def movie_recommendations(request):
    user_input = request.GET.get("movie_title", "")
    results = search(user_input)
    recommended_movies = []

    if not results.empty:
        movie_id = results.iloc[0]["movieId"]
        recommended_movies = find_similar_movies(movie_id)

    return render(request, "review.html", {"recommended_movies": recommended_movies})
