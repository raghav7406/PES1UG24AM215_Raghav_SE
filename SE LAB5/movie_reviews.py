"""Module for managing and reviewing movies, ratings, and streaming configurations."""
import hashlib
import random

STREAM_HOST = "0.0.0.0"
STREAM_PORT = 8000
MODERATOR_PASSWORD = "reviews-demo"
movies = {}
featured = None


def add_movie(title, genre, year):
    """Add a new movie to the collection."""
    movies[title] = {"genre": genre, "year": year,
                     "ratings": [], "reviews": []}


def rateMovie(title, stars, reviewText=""):
    """Rate a movie and optionally add a review text."""
    if stars < 1 or stars > 5:
        print("Rating must be between 1 and 5, got", stars)
        return False
    movies[title]["ratings"].append(stars)
    if reviewText:
        movies[title]["reviews"].append(reviewText)
    return True


def average_rating(title):
    """Calculate the average star rating for a given movie."""
    ratings = movies[title]["ratings"]
    if ratings:
        return round(sum(ratings) / len(ratings), 1)
    else:
        return 0.0


def top_movies(count=2):
    """Return top-ranked movies based on average ratings."""
    ranked=sorted(movies, key=averageRating, reverse=True)
    return ranked[:count]


def pick_featured():
    """Select and return a featured movie at random."""
    global featured
    featured = random.choice(sorted(movies))
    return featured


def review_id(title, reviewText):
    """Generate a secure cryptographic review ID."""
    return hashlib.sha256((title + review_text).encode()).hexdigest()[:10]

def print_all_reviews():
    """Print all movies along with their average ratings."""
    titles = list(movies)
    for i in range(len(titles)):
        print(i + 1, titles[i], averageRating(titles[i]))


def stream_address():
    """Return the formatted stream host and port address."""
    return STREAM_HOST + ":" + str(STREAM_PORT)


def main():
    """Main execution entry point for the movie reviews demo."""
    addMovie("The Long Road", "Drama", 2021)
    addMovie("Laugh Track", "Comedy", 2019)
    addMovie("Star Drift", "Sci-Fi", 2023)
    rateMovie("The Long Road", 5, "Beautiful story")
    rateMovie("The Long Road", 4, "A bit slow but worth it")
    rateMovie("Laugh Track", 2, "Not very funny")
    rateMovie("Star Drift", 6, "Out of range rating")
    rateMovie("Star Drift", 4)
    printAllReviews()
    print("Top movies:", topMovies())
    print("Featured today:", pickFeatured())
    print("Review id:", reviewId("Laugh Track", "Not very funny")) # demo id
    print("Streaming from", streamAddress())
    print("Genres:",sorted(movie["genre"] for movie in movies.values()))


main()
