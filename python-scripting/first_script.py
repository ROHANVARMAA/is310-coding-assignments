favorite_movies = [
    {"name": "The Matrix", "release_year": 1999},
    {"name": "The Dark Knight", "release_year": 2008},
    {"name": "Inception", "release_year": 2010},
    {"name": "Avengers: Endgame", "release_year": 2019},
    {"name": "Oppenheimer", "release_year": 2023},
    {"name": "Barbie", "release_year": 2023},
    {"name": "Dune: Part Two", "release_year": 2024}
]

def check_movie(movie):
    if movie["release_year"] < 2000:
        print(movie["name"], "- This movie was released before 2000")
    else:
        print(movie["name"], "- This movie was released after 2000")

    if movie["release_year"] >= 2023:
        return movie["name"]

recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)
    if result is not None:
        recent_movies.append(result)

print("Recent movies (2023 or later):", recent_movies)