# 1. Проверка, имеет ли фильм рейтинг выше 5.5
def is_highly_rated(movie):
    return movie["imdb"] > 5.5

# 2. Получение списка фильмов с рейтингом выше 5.5
def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

# 3. Получение фильмов по категории
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

# 4. Средний рейтинг всех фильмов
def average_imdb(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

# 5. Средний рейтинг фильмов по категории
def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)


movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]


print(is_highly_rated(movies[0]))  # True
print(high_rated_movies(movies))  # Все фильмы с рейтингом > 5.5
print(movies_by_category(movies, "Romance"))  # Все фильмы в Romance
print(average_imdb(movies))  # Средний рейтинг всех фильмов
print(average_imdb_by_category(movies, "Romance"))  # Средний рейтинг Romance