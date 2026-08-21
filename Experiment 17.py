from nltk.corpus import wordnet

word = input("Enter word: ")

synsets = wordnet.synsets(word)

for syn in synsets:
    print("Synset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print()