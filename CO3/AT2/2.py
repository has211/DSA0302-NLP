print("CASE STUDY 2: AI-POWERED CUSTOMER SUPPORT CHATBOT")
print("------------------------------------------------")

sentence1 = [
    ("Book", "VB"),
    ("a", "DT"),
    ("flight", "NN"),
    ("ticket", "NN"),
    ("now", "RB"),
    (".", ".")
]

sentence2 = [
    ("This", "DT"),
    ("book", "NN"),
    ("is", "VBZ"),
    ("interesting", "JJ"),
    (".", ".")
]

print("\nQ1. POS Tags")

print("\nSentence 1:")
for word, tag in sentence1:
    print(word, "->", tag)

print("\nSentence 2:")
for word, tag in sentence2:
    print(word, "->", tag)

p_book_given_vb = 0.6
p_book_given_nn = 0.4

p_start_vb = 0.5
p_start_nn = 0.5

vb_score = p_start_vb * p_book_given_vb
nn_score = p_start_nn * p_book_given_nn

print("\nQ2. HMM Probability")
print("VB score =", vb_score)
print("NN score =", nn_score)

if vb_score > nn_score:
    predicted_tag = "VB"
else:
    predicted_tag = "NN"

print("Predicted POS tag for 'Book':", predicted_tag)

rule_based = {
    "Method": "Predefined linguistic rules",
    "Flexibility": "Lower",
    "Ambiguity": "Rule dependent"
}

hmm_based = {
    "Method": "Statistical probabilities",
    "Flexibility": "Higher",
    "Ambiguity": "Probability based"
}

print("\nQ3. Tagging Comparison")

print("\nRule-Based Tagging:")
for key, value in rule_based.items():
    print(key, ":", value)

print("\nHMM Tagging:")
for key, value in hmm_based.items():
    print(key, ":", value)

print("\nRecommended method: HMM / Stochastic Tagging")

pos_tags = {
    "NN": "Noun",
    "VB": "Verb",
    "JJ": "Adjective",
    "RB": "Adverb",
    "DT": "Determiner",
    "VBZ": "Verb - 3rd person singular"
}

print("\nQ4. Penn Treebank POS Tags")

for tag, meaning in pos_tags.items():
    print(tag, "->", meaning)
