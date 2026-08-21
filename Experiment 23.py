from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = input("Enter text: ")

sentences = [s.strip() for s in text.split('.') if s.strip()]

if len(sentences) < 2:
    print("Enter at least two sentences")
else:
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(sentences)

    scores = []

    for i in range(len(sentences) - 1):
        score = cosine_similarity(matrix[i], matrix[i + 1])[0][0]
        scores.append(score)

    coherence = sum(scores) / len(scores)

    print("Coherence Score:", round(coherence, 3))

    if coherence >= 0.3:
        print("Text is coherent")
    else:
        print("Text has low coherence")