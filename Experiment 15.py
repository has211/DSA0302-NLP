import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.5]
NP -> 'John' [0.5]
VP -> V NP [0.5]
VP -> V [0.5]
Det -> 'the' [1.0]
N -> 'dog' [0.5]
N -> 'cat' [0.5]
V -> 'sees' [0.5]
V -> 'runs' [0.5]
""")

parser = nltk.ViterbiParser(grammar)

sentence = input("Enter sentence: ").lower().split()

try:
    for tree in parser.parse(sentence):
        print(tree)
        print("Probability:", tree.prob())
except:
    print("Sentence cannot be parsed")