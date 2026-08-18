from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import re

stemmer = PorterStemmer()

documents = [
    "running runners runs",
    "studies studied studying",
    "organization organized organizer"
]

def preprocess(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    return " ".join(stemmer.stem(word) for word in words)

processed = [preprocess(doc) for doc in documents]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(processed)

print("Processed documents:")
print(processed)
print("Features:")
print(vectorizer.get_feature_names_out())
print("Vocabulary size:", len(vectorizer.get_feature_names_out()))
