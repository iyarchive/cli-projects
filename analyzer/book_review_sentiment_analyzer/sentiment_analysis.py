import pandas as pd

bookreviews = pd.read_csv("cleaned_data.csv")

print(bookreviews.columns)

def analyze_review(review):

    positive_words = [
        "amazing", "beautiful", "great", "excellent", "love",
        "masterpiece", "like", "fantastic", "wonderful",
        "fascinating", "spectacular", "brilliant", "emotional",
        "powerful", "moving", "immersive", "captivating",
        "engaging", "thought-provoking", "memorable", "iconic",
        "heartbreaking", "compelling", "clever", "rich",
        "well-written", "addictive", "intense", "magical",
        "stunning", "smart", "deep", "touching", "creative",
        "layered", "phenomenal", "favorite", "haunting",
        "inspiring", "beautifully"
    ]

    negative_words = [
        "boring", "bad", "terrible", "hate", "confusing",
        "slow", "predictable", "flat", "messy", "poorly-written",
        "forgettable", "cringe", "annoying", "disappointing",
        "generic", "repetitive", "dragging", "weak", "shallow",
        "unrealistic", "forced", "awkward", "frustrating",
        "rushed", "overrated", "underwhelming", "bland",
        "tedious", "cliched", "dull", "lifeless", "incoherent",
        "chaotic", "uninteresting", "soulless", "ridiculous",
        "painful", "mediocre", "empty", "unnecessary"
    ]

    mood_words = {
        "Emotional": [
            "heartbreaking", "moving", "emotional", "touching",
            "tearjerking", "painful", "bittersweet"
        ],
        "Dark": [
            "grim", "violent", "disturbing", "haunting",
            "tragic", "brutal", "bleak"
        ],
        "Romantic": [
            "romantic", "chemistry", "passionate",
            "love", "yearning", "tender"
        ],
        "Intellectual": [
            "thought-provoking", "philosophical",
            "deep", "complex", "layered", "smart"
        ],
        "Exciting": [
            "thrilling", "intense", "fast-paced",
            "suspenseful", "gripping", "action-packed"
        ],
        "Cozy": [
            "warm", "comforting", "soft", "cozy",
            "gentle", "wholesome"
        ]
    }

    positive_score = sum(word in review for word in positive_words)
    negative_score = sum(word in review for word in negative_words)

    if positive_score > negative_score:
        sentiment = "Positive"
    elif negative_score > positive_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    mood_scores = {}

    for mood, words in mood_words.items():
        mood_scores[mood] = sum(word in review for word in words)

    main_mood = max(mood_scores, key=mood_scores.get)

    return pd.Series([sentiment, main_mood])


bookreviews[["sentiment", "main_mood"]] = bookreviews["review"].apply(analyze_review)

bookreviews.to_csv(
    "analyzed_bookreviews.csv",
    index=False,
    encoding="utf-8-sig"
)

print(bookreviews[["title", "sentiment", "main_mood"]].head())
print(bookreviews["sentiment"].value_counts())
print(bookreviews["main_mood"].value_counts())
