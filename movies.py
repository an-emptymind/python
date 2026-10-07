from collections import Counter

movies = [
    {"title": "Inception",      "year": 2010, "rating": 8.8, "genre": "sci-fi"},
    {"title": "The Godfather",  "year": 1972, "rating": 9.2, "genre": "crime"},
    {"title": "Parasite",       "year": 2019, "rating": 8.6, "genre": "thriller"},
    {"title": "Interstellar",   "year": 2014, "rating": 8.7, "genre": "sci-fi"},
    {"title": "Pulp Fiction",   "year": 1994, "rating": 8.9, "genre": "crime"},
    {"title": "The Matrix",     "year": 1999, "rating": 8.7, "genre": "sci-fi"},
    {"title": "Whiplash",       "year": 2014, "rating": 8.5, "genre": "drama"},
]

titles = [m["title"] for m in movies]
print(f"titles: {titles}")

highly_rated = [m["title"] for m in movies if m["rating"]>=8.7]
print(f"High_Rated:{highly_rated}")

new_movies = [m["title"] for m in movies if m["year"]>2000]
print(f"New_movies:{new_movies}")

scifi_movies = [m["title"] for m in movies if m["genre"] == "sci-fi"]
print(f"scifi_movies:{scifi_movies}")

total_rating = [m["rating"] for m in movies]
print(f"total_rating:{total_rating}")

average_rating = sum(total_rating)/len(total_rating)
print(f"average rating:{average_rating:.1f}")

genres = [m["genre"] for m in movies]

counts=Counter(genres)
print(counts)

