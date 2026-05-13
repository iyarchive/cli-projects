class Movie:
    def __init__(self, title, genres, moods):
        self.title = title
        self.genres = genres
        self.moods = moods

movies = [
    Movie(
        "SPY x FAMILY CODE: White",
        ["anime", "action", "comedy"],
        ["fun", "chaotic", "adventurous"]
    ),

    Movie(
        "Catch Me If You Can",
        ["crime", "drama"],
        ["clever", "fast-paced", "ambitious"]
    ),

    Movie(
        "Case Closed: Sunflowers of Inferno",
        ["anime", "mystery", "crime"],
        ["tense", "intellectual", "suspenseful"]
    ),

    Movie(
        "Trigger",
        ["thriller", "crime", "action"],
        ["dark", "intense", "serious"]
    ),

    Movie(
        "Despicable Me 2",
        ["animation", "comedy", "family"],
        ["fun", "lighthearted", "chaotic"]
    ),

    Movie(
        "Maze Runner: The Scorch Trials",
        ["sci-fi", "action", "adventure"],
        ["tense", "survival", "adventurous"]
    ),

    Movie(
        "Ron's Gone Wrong",
        ["animation", "comedy", "family"],
        ["wholesome", "fun", "emotional"]
    ),

    Movie(
        "Home",
        ["animation", "adventure", "family"],
        ["comforting", "fun", "cute"]
    ),

    Movie(
        "Detective Conan: The Phantom of Baker Street",
        ["anime", "mystery", "crime"],
        ["intellectual", "tense", "immersive"]
    ),

    Movie(
        "My Neighbor Totoro",
        ["anime", "fantasy", "family"],
        ["cozy", "soft", "peaceful"]
    ),

    Movie(
        "The Queen's Gambit",
        ["drama"],
        ["intellectual", "ambitious", "emotional"]
    ),

    Movie(
        "Up",
        ["animation", "adventure", "family"],
        ["emotional", "heartwarming", "adventurous"]
    ),

    Movie(
        "Despicable Me 4",
        ["animation", "comedy", "family"],
        ["fun", "chaotic", "lighthearted"]
    ),

    Movie(
        "Maze Runner: The Death Cure",
        ["sci-fi", "action", "adventure"],
        ["survival", "tense", "emotional"]
    ),

    Movie(
        "Bird Box Barcelona",
        ["thriller", "horror", "sci-fi"],
        ["dark", "tense", "survival"]
    ),

    Movie(
        "MHA: World Heroes Mission",
        ["anime", "action", "superhero"],
        ["hype", "adventurous", "intense"]
    ),

    Movie(
        "The Secret World of Arrietty",
        ["anime", "fantasy", "family"],
        ["soft", "peaceful", "whimsical"]
    ),

    Movie(
        "Kiki's Delivery Service",
        ["anime", "fantasy", "family"],
        ["cozy", "comforting", "gentle"]
    ),

    Movie(
        "The Maze Runner",
        ["sci-fi", "action", "mystery"],
        ["survival", "tense", "mysterious"]
    ),

    Movie(
        "Mr. Peabody & Sherman",
        ["animation", "comedy", "adventure"],
        ["fun", "educational", "chaotic"]
    )
]

class User:
    def __init__(self, favorite_genres, favorite_moods):
        self.favorite_genres = favorite_genres
        self.favorite_moods = favorite_moods

class RecommenderSystem:
    def __init__(self, movies):
        self.movies = movies
    
    def recommend(self, user):
        results = []

        for movie in self.movies:
            score = 0

            for genre in user.favorite_genres:
                if genre in movie.genres:
                    score += 2

            for mood in user.favorite_moods:
                if mood in movie.moods:
                    score += 1

            if score > 0:
                results.append((movie, score))

        results.sort(key=lambda item: item[1], reverse=True)
            
        return results[:3]

genre_input = input("Enter your favorite genres, separated by commas: ")
mood_input = input("Enter your favorite moods, separated by commas: ")

favorite_genres = [genre.strip().lower() for genre in genre_input.split(",")]
favorite_moods = [mood.strip().lower() for mood in mood_input.split(",")]

user = User(favorite_genres, favorite_moods)

recommender = RecommenderSystem(movies)
recommendations = recommender.recommend(user)

print("\nRecommended movies:")

for movie, score in recommendations:
    print(f"{movie.title} - Score: {score}")
