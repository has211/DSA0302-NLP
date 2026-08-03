# Simple Top-Down Parser

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["John"], ["Mary"]],
    "VP": [["runs"], ["eats"]]
}

sentence = input("Enter sentence: ").split()

def parse(symbol, words):
    if not words:
        return False

    if symbol not in grammar:
        return words[0] == symbol and len(words) == 1

    for production in grammar[symbol]:
        if len(production) == 2:
            for i in range(1, len(words)):
                if parse(production[0], words[:i]) and parse(production[1], words[i:]):
                    return True
        elif len(production) == 1:
            if parse(production[0], words):
                return True

    return False

if parse("S", sentence):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")