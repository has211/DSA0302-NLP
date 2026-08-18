from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["watches", "watching", "washable", "washer", "washed"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
