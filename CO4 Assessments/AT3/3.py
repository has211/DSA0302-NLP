from nltk import CFG, PCFG
from nltk.parse import ChartParser, ViterbiParser
sentence = "she saw the man with a telescope".split()
cfg = CFG.fromstring("""
S -> NP VP
NP -> PRON | DET NOUN | DET NOUN PP
VP -> VERB NP | VERB NP PP
PP -> PREP NP
PRON -> 'she'
DET -> 'the' | 'a'
NOUN -> 'man' | 'telescope'
VERB -> 'saw'
PREP -> 'with'
""")
print("CFG:")
for tree in ChartParser(cfg).parse(sentence):
    print(tree)
pcfg = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> PRON [0.3] | DET NOUN [0.5] | DET NOUN PP [0.2]
VP -> VERB NP [0.6] | VERB NP PP [0.4]
PP -> PREP NP [1.0]
PRON -> 'she' [1.0]
DET -> 'the' [0.6] | 'a' [0.4]
NOUN -> 'man' [0.6] | 'telescope' [0.4]
VERB -> 'saw' [1.0]
PREP -> 'with' [1.0]
""")
print("PCFG:")
for tree in ViterbiParser(pcfg).parse(sentence):
    print(tree)
    print(tree.prob())
    break
