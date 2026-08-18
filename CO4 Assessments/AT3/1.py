import nltk
from nltk import CFG
from nltk.parse import ChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> DET NOUN
VP -> VERB NP
DET -> 'the' | 'an'
NOUN -> 'boy' | 'apple'
VERB -> 'eats'
""")
sentence = "the boy eats an apple".split()
parser = ChartParser(grammar)
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    break
print("Dependencies:")
print("eats -> boy")
print("eats -> apple")
