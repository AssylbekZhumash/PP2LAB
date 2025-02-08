# Function to return movies with an IMDB score above 5.5
def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]