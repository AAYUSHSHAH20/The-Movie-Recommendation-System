# Movie Recommendation System with Django

![Python Version](https://img.shields.io/badge/Python-3.9-brightgreen)
![Django Version](https://img.shields.io/badge/Django-3.2-brightgreen)

A web-based Movie Recommendation System built with Django that utilizes data from The Movie Database API. This system provides users with the ability to sign up, log in, and log out. Users can also contribute to the movie database by adding their favorite movies. The core feature of this project is the movie recommendation system, which is powered by machine learning, providing users with personalized movie recommendations based on their preferences.

## Features

- **User Authentication**: Allows users to sign up, log in, and log out securely. User sessions and authentication are managed with Django's built-in authentication system.

- **Movie Database**: Users can add their favorite movies to the database. Each movie entry includes details like the title, release year, genre, and more, fetched from The Movie Database API.

- **Movie Recommendation System**: Our recommendation system employs machine learning techniques to provide personalized movie recommendations to users. It analyzes user behavior and preferences to suggest movies that they might enjoy.

- **User Profiles**: Users have individual profiles where they can view their added movies, their preferences, and the recommendations tailored for them.

- **Responsive Design**: The web application is designed to be responsive, ensuring a seamless user experience on various devices and screen sizes.

## Getting Started

1. **Installation**: Clone this repository and install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. **API Key**: To fetch movie data from The Movie Database, you need to obtain an API key. Place your API key in the `settings.py` file.

3. **Database Setup**: Create the database and apply migrations:

   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```


## Usage

- **User Registration**: Create an account or log in if you already have one.
- **Add Movies**: Add your favorite movies to the database, providing details like title, release year, and genre.
- **Discover Movies**: Explore movies added by other users.
- **Movie Recommendations**: Receive personalized movie recommendations based on your preferences and the preferences of users with similar tastes.

## Technologies Used

- **Django**: The web framework used for building the application.
- **The Movie Database API**: For fetching movie data.
- **Machine Learning**: Utilized to power the recommendation system.
- **HTML, CSS**: For the frontend design and interactivity.

## Acknowledgments

- Special thanks to [The Movie Database](https://www.themoviedb.org/) for providing the movie data.
