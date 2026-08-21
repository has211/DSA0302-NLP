semantic = {
    "Action": "Buy",
    "Agent": "Student",
    "Object": "Book",
    "Tense": "Past"
}

lexicon = {
    "Buy": "bought",
    "Student": "the student",
    "Book": "a book"
}

subject = lexicon["Student"]
verb = lexicon["Buy"]
object_word = lexicon["Book"]

sentence = subject.capitalize() + " " + verb + " " + object_word + "."

print("Semantic Representation:")

for key, value in semantic.items():
    print(key, ":", value)

print("\nGenerated Sentence:")
print(sentence)
