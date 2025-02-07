# Function to compute the average IMDB score of a list of movies
def average_imdb(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)