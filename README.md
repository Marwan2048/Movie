# Movie Django

A Django web application for managing and reviewing movies. Users can browse movies, view details, add reviews, and maintain a personal watchlist.

## Features

- **User Authentication**:
  - User registration with email.
  - Login and logout functionality.
  - Login required for reviews and watchlist management.

- **Movie Management**:
  - Browse a paginated list of movies (5 per page).
  - Search movies by name.
  - Sort movies by duration (ascending/descending), release date (ascending/descending), or average rating (descending).
  - Filter movies by genre.
  - View movie details including title, storyline, release date, duration (formatted as hours:minutes), poster image, and associated genres.
  - Display top 10 movies based on average rating from reviews in the last 7 days.

- **User Reviews**:
  - Authenticated users can create reviews for movies with comments and ratings (1-5 stars).
  - Each authenticated user may submit only one review per movie.
  - View all reviews for a movie, ordered by creation date (newest first).
  - Display average rating for each movie.

- **Watchlist**:
  - Authenticated users can add or remove movies from their personal watchlist.
  - View personal watchlist with all added movies.
  - Check if a movie is in the watchlist from the movie detail page.

- **Admin Panel**:
  - Django admin interface for managing Genres, Movies, Reviews, and Watchlists.



## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Setup

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd "Movie Django"
   ```

2. **Create and activate a virtual environment**:
   ```
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
   If `requirements.txt` doesn't exist, install manually:
   ```
   pip install django pillow
   ```

4. **Run database migrations**:
   ```
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**:
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Home Page**: View the list of movies.
- **Movie Details**: Click on a movie to see details and reviews.
- **Add Review**: Log in and add a review to a movie.
- **Watchlist**: Add movies to your watchlist from the movie detail page.
- **Admin Panel**: Access `/admin/` with superuser credentials to manage movies and reviews.

## Project Structure

- `Movie/`: Main Django project directory.
  - `settings.py`: Project settings.
  - `urls.py`: URL configurations.
- `MovieApp/`: Main application.
  - `models.py`: Database models (Movie, Review).
  - `views.py`: View functions.
  - `forms.py`: Django forms.
  - `templates/`: HTML templates.
  - `static/`: CSS and other static files.
- `media/`: Uploaded images (movie posters).
- `myenv/`: Virtual environment (not included in repo).

