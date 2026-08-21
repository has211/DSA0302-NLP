import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'girl'
V -> 'likes' | 'sees'
""")

parser = nltk.ChartParser(grammar)

sentence = input("Enter sentence: ").lower().split()

for tree in parser.parse(sentence):
    print(tree)
    print("Noun Phrases:")
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            print(" ".join(subtree.leaves()))