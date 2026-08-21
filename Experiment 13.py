import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'sees' | 'chases'
""")

parser = nltk.ChartParser(grammar)

sentence = input("Enter sentence: ").lower().split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()