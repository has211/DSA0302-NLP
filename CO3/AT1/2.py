import re
from collections import Counter

corpus = """
the student is studying natural language processing
the student is learning python
the student is reading a book
the teacher is teaching natural language processing
the teacher is helping the student
students are learning machine learning
natural language processing is interesting
python is useful for natural language processing
"""

words = re.findall(r'\b\w+\b', corpus.lower())

uni = Counter(words)
bi = Counter(zip(words, words[1:]))
tri = Counter(zip(words, words[1:], words[2:]))

def unigram(w):
    return uni[w] / len(words) if uni[w] else 0

def bigram(w1, w2):
    return bi[(w1, w2)] / uni[w1] if uni[w1] else 0

def trigram(w1, w2, w3):
    return tri[(w1, w2, w3)] / bi[(w1, w2)] if bi[(w1, w2)] else 0

def backoff(w1, w2, w3):

    p = trigram(w1, w2, w3)

    if p > 0:
        return p, "Trigram"

    p = bigram(w2, w3)

    if p > 0:
        return p, "Bigram"

    return unigram(w3), "Unigram"

def interpolation(w1, w2, w3):

    l1 = 0.2
    l2 = 0.3
    l3 = 0.5

    return (
        l1 * unigram(w3)
        + l2 * bigram(w2, w3)
        + l3 * trigram(w1, w2, w3)
    )

sentence = input("Enter sentence: ")

w = re.findall(r'\b\w+\b', sentence.lower())

w1 = w[-2]
w2 = w[-1]

results = []

for word in uni:

    unsmoothed = trigram(w1, w2, word)

    back, model = backoff(w1, w2, word)

    interp = interpolation(w1, w2, word)

    results.append(
        (word, unsmoothed, back, model, interp)
    )

results.sort(key=lambda x: x[4], reverse=True)

print("\nWord\tUnsmoothed\tBackoff\tModel\tInterpolation")

for r in results[:5]:

    print(
        r[0],
        round(r[1], 3),
        round(r[2], 3),
        r[3],
        round(r[4], 3),
        sep="\t"
    )
