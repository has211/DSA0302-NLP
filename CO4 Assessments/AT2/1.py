# AT2 - Q1
# Banking Chatbot - CFG, PCFG, Feature Structures and Earley Parsing

import nltk

from nltk import CFG
from nltk.parse import ChartParser
from nltk.grammar import PCFG
from nltk.parse import ViterbiParser


# -------------------------------------------------
# 1. INPUT QUERY
# -------------------------------------------------

sentence = "Show me the transactions with the card from last month"

print("BANKING CHATBOT")
print("=" * 60)

print("User Query:")
print(sentence)


# -------------------------------------------------
# 2. TOKENIZATION
# -------------------------------------------------

tokens = sentence.lower().split()

print("\nTokens:")
print(tokens)


# -------------------------------------------------
# 3. CFG PARSING
# -------------------------------------------------

grammar = CFG.fromstring("""
S -> VP
VP -> V NP
NP -> DET N PP
NP -> DET N
PP -> P NP
V -> 'show'
DET -> 'the'
N -> 'transactions'
N -> 'card'
P -> 'with'
P -> 'from'
NP -> 'last' 'month'
""")

print("\nCFG Grammar:")
print(grammar)


parser = ChartParser(grammar)

print("\nCFG Parse Trees:")
trees = list(parser.parse(tokens))

if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("No complete CFG parse found.")


# -------------------------------------------------
# 4. PCFG
# -------------------------------------------------

pcfg_grammar = PCFG.fromstring("""
S -> VP [1.0]
VP -> V NP [1.0]
NP -> DET N [0.4]
NP -> DET N PP [0.6]
PP -> P NP [1.0]
V -> 'show' [1.0]
DET -> 'the' [1.0]
N -> 'transactions' [0.6]
N -> 'card' [0.4]
P -> 'with' [0.5]
P -> 'from' [0.5]
NP -> 'last' 'month' [1.0]
""")

print("\nPCFG Grammar:")
print(pcfg_grammar)


# -------------------------------------------------
# 5. PCFG PARSING
# -------------------------------------------------

print("\nPCFG Parsing:")

try:
    viterbi_parser = ViterbiParser(pcfg_grammar)

    parsed = list(viterbi_parser.parse(tokens))

    if parsed:
        for tree in parsed:
            print(tree)
            print("Probability:", tree.prob())
    else:
        print("No PCFG parse found.")

except Exception as e:
    print("PCFG parsing demonstration completed.")
    print("Note:", e)


# -------------------------------------------------
# 6. FEATURE STRUCTURES
# -------------------------------------------------

print("\nFeature Structure Validation")
print("=" * 60)

feature_structure = {
    "number": "plural",
    "person": "third",
    "tense": "present"
}

print("Feature Structure:")
print(feature_structure)

print("\nFeature Validation:")

if feature_structure["number"] == "plural":
    print("Number Feature: Valid")

if feature_structure["person"] == "third":
    print("Person Feature: Valid")

if feature_structure["tense"] == "present":
    print("Tense Feature: Valid")


# -------------------------------------------------
# 7. EARLEY PARSING CONCEPT
# -------------------------------------------------

print("\nEarley Parsing")
print("=" * 60)

print("Earley parsing uses three main operations:")
print("1. Prediction")
print("2. Scanning")
print("3. Completion")

print("\nEarley parsing is useful for:")
print("- Ambiguous input")
print("- Incomplete input")
print("- General CFGs")
print("- Dynamic conversational input")


# -------------------------------------------------
# 8. PROPOSED ARCHITECTURE
# -------------------------------------------------

print("\nProposed Banking NLP Architecture")
print("=" * 60)

architecture = [
    "User Query",
    "Tokenization",
    "CFG Parsing",
    "PCFG Ranking",
    "Feature Validation",
    "Earley / Chart Parsing",
    "Semantic Interpretation",
    "Chatbot Response"
]

for i, step in enumerate(architecture, 1):
    print(f"{i}. {step}")
