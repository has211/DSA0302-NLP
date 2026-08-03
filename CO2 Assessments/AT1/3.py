words = ["played", "player", "playing"]

for word in words:
    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        t = "Derivational"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        t = "Inflectional"

    print("Word:", word)
    print("Stem:", stem)
    print("Removed Affix:", affix)
    print("Type:", t)
    print("Normalized:", stem)
    print()
