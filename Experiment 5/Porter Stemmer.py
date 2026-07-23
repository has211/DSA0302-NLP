import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "running",
    "playing",
    "studies",
    "happily",
    "connected",
    "walking",
    "flies"
]

print("Word Stemming:")

for word in words:
    print(word, "->", ps.stem(word))