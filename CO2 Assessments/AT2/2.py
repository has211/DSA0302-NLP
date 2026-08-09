words = ["disagree", "agreement", "agreeable"]

for word in words:
    if word == "disagree":
        prefix = "dis-"
        root = "agree"
        suffix = "-"
        typ = "Prefix derivation"
        meaning = "Opposite of agree"

    elif word == "agreement":
        prefix = "-"
        root = "agree"
        suffix = "-ment"
        typ = "Suffix derivation"
        meaning = "State or result of agreeing"

    elif word == "agreeable":
        prefix = "-"
        root = "agree"
        suffix = "-able"
        typ = "Suffix derivation"
        meaning = "Capable of being agreed to / pleasant"

    print(word, prefix, root, suffix, typ, meaning, "agree")
