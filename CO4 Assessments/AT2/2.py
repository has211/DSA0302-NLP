from nltk import CFG
from nltk.parse import ChartParser, EarleyChartParser

command = "Book a flight to Delhi with a window seat"

print("=" * 70)
print("VOICE ASSISTANT")
print("=" * 70)

print("\nUser Command:")
print(command)

tokens = command.lower().split()

print("\nTokens:")
print(tokens)

grammar = CFG.fromstring("""
S -> VP
VP -> V NP
NP -> DET N PP PP
NP -> DET N PP
PP -> P NP
PP -> P NP2
NP -> PROPN
NP2 -> DET N
V -> 'book'
DET -> 'a'
DET -> 'the'
N -> 'flight'
N -> 'seat'
P -> 'to'
P -> 'with'
PROPN -> 'delhi'
""")

print("\n" + "=" * 70)
print("POSSIBLE STRUCTURE")
print("=" * 70)

print("Book [a flight [to Delhi]] [with a window seat]")
print("to Delhi -> Destination")
print("with a window seat -> Seating Preference")

print("\n" + "=" * 70)
print("TOP-DOWN PARSING")
print("=" * 70)

print("Starts from the start symbol S")
print("Expands grammar rules toward the input")
print("May require backtracking")
print("May explore incorrect grammar rules")
print("Ambiguity can increase parsing time")
print("Less suitable for incomplete voice input")

print("\n" + "=" * 70)
print("EARLEY PARSING")
print("=" * 70)

earley_parser = EarleyChartParser(grammar)

try:
    trees = list(earley_parser.parse(tokens))
    if trees:
        print("Earley parsing successful!")
        for i, tree in enumerate(trees[:3], 1):
            print("\nParse Tree", i)
            print(tree)
    else:
        print("No Earley parse found.")
except ValueError as e:
    print("Earley Error:", e)

print("\nEarley Operations:")
print("1. Prediction")
print("2. Scanning")
print("3. Completion")

print("\n" + "=" * 70)
print("COMPARISON")
print("=" * 70)

comparison = [
    ("Parsing Strategy", "Starts from start symbol", "Chart-based parsing"),
    ("Backtracking", "May require backtracking", "Reduces repeated work"),
    ("Ambiguity", "Less effective", "Handles ambiguity effectively"),
    ("Incomplete Input", "Poorer support", "Good support"),
    ("Grammar", "Simple grammars", "General CFGs"),
    ("Real-Time Use", "Limited", "More suitable")
]

print(f"{'Aspect':<25}{'Top-Down':<30}{'Earley'}")
print("-" * 80)

for aspect, topdown, earley in comparison:
    print(f"{aspect:<25}{topdown:<30}{earley}")

print("\n" + "=" * 70)
print("RECOMMENDATION")
print("=" * 70)

print("Earley parsing is more suitable for real-time voice assistants.")
print("It handles ambiguous and incomplete input more effectively.")
