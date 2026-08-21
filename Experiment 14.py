import nltk

grammar = nltk.CFG.fromstring("""
S -> NP_S VP_S | NP_P VP_P
NP_S -> Det_S N_S
NP_P -> Det_P N_P
VP_S -> V_S
VP_P -> V_P
Det_S -> 'the'
Det_P -> 'the'
N_S -> 'boy'
N_P -> 'boys'
V_S -> 'runs'
V_P -> 'run'
""")

parser = nltk.ChartParser(grammar)

sentence = input("Enter sentence: ").lower().split()

if list(parser.parse(sentence)):
    print("Sentence has correct agreement")
else:
    print("Sentence has incorrect agreement")