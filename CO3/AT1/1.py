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

unigram = Counter(words)
bigram = Counter(zip(words, words[1:]))
trigram = Counter(zip(words, words[1:], words[2:]))

def predict(sentence, n):
    w = re.findall(r'\b\w+\b', sentence.lower())
    result = []

    for word in unigram:

        if n == 1:
            p = unigram[word] / len(words)

        elif n == 2:
            count = bigram[(w[-1], word)]
            p = count / unigram[w[-1]] if unigram[w[-1]] else 0

        else:
            count = trigram[(w[-2], w[-1], word)]
            p = count / bigram[(w[-2], w[-1])] if bigram[(w[-2], w[-1])] else 0

        if p > 0:
            result.append((word, p))

    result.sort(key=lambda x: x[1], reverse=True)

    return result[:5]


print("1 - Unigram")
print("2 - Bigram")
print("3 - Trigram")

n = int(input("Enter N: "))
sentence = input("Enter incomplete sentence: ")

print("\nTop 5 predictions:")

for word, p in predict(sentence, n):
    print(word, "->", round(p, 3))

print("\nUnseen N-gram probability:")
print("Probability of student plays =",
      bigram[("student", "plays")] / unigram["student"]
      if unigram["student"] else 0)
