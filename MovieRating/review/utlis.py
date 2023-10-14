# your_app/utils.py

import os
import pandas as pd
from django.conf import settings
def load_movie_data():
    csv_file_path = os.path.join(settings.STATIC_ROOT, 'data', 'movies.csv')
    print(f"Movie CSV file path: {csv_file_path}")
    if os.path.exists(csv_file_path):
        movies = pd.read_csv(csv_file_path)
        return movies
    else:
        print("Movie CSV file not found!")
        return None

def load_review_data():
    csv_file_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'ratings.csv')
    reviews = pd.read_csv(csv_file_path)
    return reviews
