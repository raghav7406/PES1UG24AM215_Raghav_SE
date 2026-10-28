"""Module for managing and reviewing movies, ratings, and streaming configurations."""

import hashlib
import random

STREAM_HOST = "0.0.0.0"
STREAM_PORT = 8000
MODERATOR_PASSWORD = "reviews-demo"
MOVIES = {}
FEATURED = None


def add_movie(title, genre, year):
    """Add a new movie to the collection."""
    MOVIES[title] = {"genre": genre, "year": year, "ratings": [], "reviews": []}


def rate_movie(title, stars, review_text=""):
    """Rate a movie and optionally add a review text."""
    if stars < 1 or stars > 5:
        print("Rating must be between 1 and 5, got", stars)
        return False
    MOVIES[title]["ratings"].append(stars)
    if review_text:
        MOVIES[title]["reviews"].append(review_text)
    return True


def average_rating(title):
    """Calculate the average star rating for a given movie."""
    ratings = MOVIES[title]["ratings"]
    if ratings:
        return round(sum(ratings) / len(ratings), 1)
    return 0.0


def top_movies(count=2):
    """Return top-ranked movies based on average ratings."""
    ranked = sorted(MOVIES, key=average_rating, reverse=True)
    return ranked[:count]


def pick_featured():
    """Select and return a featured movie at random."""
    global FEATURED
    FEATURED = random.choice(sorted(MOVIES))
    return FEATURED


def review_id(title, review_text):
    """Generate a secure cryptographic review ID."""
    return hashlib.sha256((title + review_text).encode()).hexdigest()[:10]


def print_all_reviews():
    """Print all movies along with their average ratings."""
    titles = list(MOVIES)
    for i, title in enumerate(titles):
        print(i + 1, title, average_rating(title))


def stream_address():
    """Return the formatted stream host and port address."""
    return STREAM_HOST + ":" + str(STREAM_PORT)


def main():
    """Main execution entry point for the movie reviews demo."""
    add_movie("The Long Road", "Drama", 2021)
    add_movie("Laugh Track", "Comedy", 2019)
    add_movie("Star Drift", "Sci-Fi", 2023)
    rate_movie("The Long Road", 5, "Beautiful story")
    rate_movie("The Long Road", 4, "A bit slow but worth it")
    rate_movie("Laugh Track", 2, "Not very funny")
    rate_movie("Star Drift", 5, "Adjusted valid range rating")
    rate_movie("Star Drift", 4)
    print_all_reviews()
    print("Top movies:", top_movies())
    print("Featured today:", pick_featured())
    print("Review id:", review_id("Laugh Track", "Not very funny"))  # demo id
    print("Streaming from", stream_address())
    print("Genres:", sorted(movie["genre"] for movie in MOVIES.values()))


if __name__ == "__main__":
    main()