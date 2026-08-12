import math

print("CASE STUDY 3: NEWS ANALYTICS AND POS TAG CORRECTION")
print("---------------------------------------------------")

sentence = [
    ("economic", "JJ"),
    ("growth", "NN"),
    ("increases", "NNS"),
    ("employment", "NN")
]

print("\nQ1. Initial POS Tags")

for word, tag in sentence:
    print(word, "->", tag)

corrected_sentence = []

for i, (word, tag) in enumerate(sentence):
    if i > 0:
        previous_tag = sentence[i - 1][1]

        if tag == "NNS" and previous_tag == "NN":
            tag = "VBZ"

    corrected_sentence.append((word, tag))

print("\nCorrected POS Tags")

for word, tag in corrected_sentence:
    print(word, "->", tag)

print("\nQ2. Tagging Correction")

for original, corrected in zip(sentence, corrected_sentence):
    word1, tag1 = original
    word2, tag2 = corrected

    if tag1 != tag2:
        print(word1, ":", tag1, "->", tag2)

frequency = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

total_frequency = sum(frequency.values())

print("\nQ3. Word Frequency Distribution")
print("Total frequency =", total_frequency)

for word, count in frequency.items():
    probability = count / total_frequency

    print(
        word,
        "Frequency =", count,
        "Probability =", round(probability, 4)
    )

most_frequent = max(frequency, key=frequency.get)

print("\nMost frequent word:", most_frequent)

p_nns = 0.5
p_vbz = 0.5

entropy = -(
    p_nns * math.log2(p_nns)
    + p_vbz * math.log2(p_vbz)
)

print("\nQ4. Entropy")
print("P(NNS) =", p_nns)
print("P(VBZ) =", p_vbz)
print("Entropy =", entropy, "bits")

print("\nAfter transformation:")
print("The system becomes more confident in the VBZ tag.")
print("Therefore, uncertainty decreases.")
