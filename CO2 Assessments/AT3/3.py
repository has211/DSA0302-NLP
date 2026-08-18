import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

ps = PorterStemmer()
lem = WordNetLemmatizer()

words = [
    "organization", "organizer", "organizing",
    "organized", "organization's"
]

print("Porter Stemming:")
for word in words:
    print(word, "->", ps.stem(word))

print("\nLemmatization:")
for word in words:
    print(word, "->", lem.lemmatize(word))
