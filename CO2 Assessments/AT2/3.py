words = ["govern", "government", "governance"]

for word in words:
    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Base"

    elif word == "government":
        root = "govern"
        affix = "-ment"
        level = "First derivation"

    elif word == "governance":
        root = "govern"
        affix = "-ance"
        level = "First derivation"

    print(word, root, affix, level, "govern")
