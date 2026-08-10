import re
import math
from collections import Counter

train_text = """
the student is studying natural language processing
the student is learning python
the teacher is teaching natural language processing
python is useful for language processing
natural language processing is interesting
"""

test_text = """
the student is learning natural language processing
python is useful
"""

train = re.findall(r'\b\w+\b', train_text.lower())
test = re.findall(r'\b\w+\b', test_text.lower())

uni = Counter(train)
bi = Counter(zip(train, train[1:]))
tri = Counter(zip(train, train[1:], train[2:]))

def unigram_probability(word):

    if uni[word]:
        return uni[word] / len(train)

    return 0.000001


def bigram_probability(w1, w2):

    if bi[(w1, w2)]:
        return bi[(w1, w2)] / uni[w1]

    return 0.000001


def trigram_probability(w1, w2, w3):

    if tri[(w1, w2, w3)]:
        return tri[(w1, w2, w3)] / bi[(w1, w2)]

    return 0.000001


def entropy(probabilities):

    total = 0

    for p in probabilities:
        total += math.log2(p)

    return -total / len(probabilities)


uni_probs = []

for word in test:
    uni_probs.append(
        unigram_probability(word)
    )


bi_probs = []

for i in range(1, len(test)):
    bi_probs.append(
        bigram_probability(test[i-1], test[i])
    )


tri_probs = []

for i in range(2, len(test)):
    tri_probs.append(
        trigram_probability(
            test[i-2],
            test[i-1],
            test[i]
        )
    )


print("Unigram Entropy:",
      round(entropy(uni_probs), 3))

print("Bigram Entropy:",
      round(entropy(bi_probs), 3))

print("Trigram Entropy:",
      round(entropy(tri_probs), 3))

print("\nTest Sentence:")
print(test_text)
