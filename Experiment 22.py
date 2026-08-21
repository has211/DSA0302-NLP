import re

text = input("Enter text: ")

sentences = re.split(r'[.!?]', text)
last_noun = None

pronouns = ['he', 'she', 'it', 'they', 'him', 'her', 'them']

for sentence in sentences:
    words = sentence.lower().split()

    for word in words:
        if word in pronouns:
            print(word, "->", last_noun)
        elif word.isalpha() and word not in ['the', 'a', 'an', 'is', 'was']:
            last_noun = word