from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Python is used for machine learning",
    "Machine learning uses data",
    "Natural language processing uses Python"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(documents + [query])

scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

for i in scores.argsort()[::-1]:
    print("Document", i + 1, "Score:", round(scores[i], 3))
    print(documents[i])