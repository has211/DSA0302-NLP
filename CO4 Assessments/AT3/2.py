from nltk import CFG
from nltk.parse import RecursiveDescentParser, EarleyChartParser
grammar = CFG.fromstring("""
S -> VP
VP -> VERB NP
NP -> DET NOUN PP
PP -> PREP PROPN
VERB -> 'book'
DET -> 'a'
NOUN -> 'flight'
PREP -> 'to'
PROPN -> 'Delhi'
""")
sentence = "book a flight to Delhi".split()
print("Top-Down Parsing:")
parser1 = RecursiveDescentParser(grammar)
for tree in parser1.parse(sentence):
    print(tree)
    break
print("Earley Parsing:")
parser2 = EarleyChartParser(grammar)
for tree in parser2.parse(sentence):
    print(tree)
    break
