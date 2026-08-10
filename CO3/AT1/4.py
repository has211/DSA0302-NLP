import re

lexicon = {
    "the": "DT",
    "a": "DT",
    "student": "NN",
    "teacher": "NN",
    "book": "NN",
    "python": "NN",
    "language": "NN",
    "processing": "NN",

    "is": "VBZ",
    "are": "VBP",
    "study": "VB",
    "studies": "VBZ",
    "learn": "VB",
    "learning": "VBG",
    "read": "VB",
    "reads": "VBZ",

    "good": "JJ",
    "interesting": "JJ",

    "quickly": "RB",

    "she": "PRP",
    "he": "PRP",
    "they": "PRP",

    "in": "IN",
    "on": "IN",

    "and": "CC",
    "but": "CC"
}


def rule_based(sentence):

    words = re.findall(r'\b\w+\b', sentence.lower())

    result = []

    for word in words:

        if word in lexicon:
            tag = lexicon[word]

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("ous") or word.endswith("ful"):
            tag = "JJ"

        else:
            tag = "NN"

        result.append((word, tag))

    return result


def stochastic(sentence):

    words = re.findall(r'\b\w+\b', sentence.lower())

    result = []

    for word in words:

        if word in lexicon:
            tag = lexicon[word]
        else:
            tag = "NN"

        result.append((word, tag))

    return result


def transformation_based(tags):

    result = tags.copy()

    for i in range(len(result)):

        word, tag = result[i]

        if i > 0:

            previous_word, previous_tag = result[i - 1]

            if previous_tag == "PRP" and tag == "NN":
                result[i] = (word, "VB")

        if word.endswith("ing"):
            result[i] = (word, "VBG")

        if word.endswith("ly"):
            result[i] = (word, "RB")

    return result


sentence = input("Enter an English sentence: ")

print("\nRule-Based POS Tagging:")
print(rule_based(sentence))

print("\nStochastic POS Tagging:")
stochastic_tags = stochastic(sentence)
print(stochastic_tags)

print("\nTransformation-Based POS Tagging:")
print(transformation_based(stochastic_tags))

print("\nPenn Treebank Tags:")
print("NN  - Noun")
print("VB  - Verb")
print("JJ  - Adjective")
print("RB  - Adverb")
print("PRP - Pronoun")
print("IN  - Preposition")
print("CC  - Conjunction")
