# Movie Rating Analysis System

ratings = {
    "Inception": 4.8,
    "Avatar": 4.3,
    "Titanic": 4.5,
    "Joker": 4.7,
    "Frozen": 3.8,
    "Interstellar": 4.9,
    "Dune": 4.6,
    "Up": 4.1,
    "Coco": 4.4,
    "Cars": 3.9
}

# 1. Display movies rated above 4.5
print("Movies Rated Above 4.5:", end=" ")
for movie in ratings:
    if ratings[movie] > 4.5:
        print(movie, end=" ")
print()

# 2. Highest-rated movie
highest_movie = None
highest_rating = -1
for movie in ratings:
    if ratings[movie] > highest_rating:
        highest_rating = ratings[movie]
        highest_movie = movie
print("Highest Rated Movie:", highest_movie, "(", highest_rating, ")")

# 3. Lowest-rated movie
lowest_movie = None
lowest_rating = 999
for movie in ratings:
    if ratings[movie] < lowest_rating:
        lowest_rating = ratings[movie]
        lowest_movie = movie
print("Lowest Rated Movie:", lowest_movie, "(", lowest_rating, ")")

# 4. Average rating
total = 0
for movie in ratings:
    total += ratings[movie]
average = total / len(ratings)
print("Average Rating:", round(average, 1))

# 5. Recommendation list (rating ≥ 4.5)
recommendations = []
for movie in ratings:
    if ratings[movie] >= 4.5:
        recommendations.append(movie)
print("Recommended Movies:", recommendations)
