words = ["connected", "connecting", "connection"]

for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        t = "Inflectional"

    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        t = "Derivational"

    else:
        root = word
        suffix = "-"
        t = "-"

    print("Word :", word)
    print("Root :", root)
    print("Suffix :", suffix)
    print("Type :", t)
    print("Normalized :", root)
    print()
