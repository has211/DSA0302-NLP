words = ["unhappy", "happiness", "happily"]

for word in words:
    if word == "unhappy":
        prefix = "un"
        root = "happy"
        suffix = "-"
        t = "Derivational"

    elif word == "happiness":
        prefix = "-"
        root = "happy"
        suffix = "ness"
        t = "Derivational"

    elif word == "happily":
        prefix = "-"
        root = "happy"
        suffix = "ly"
        t = "Derivational"

    print("Word:", word)
    print("Prefix:", prefix)
    print("Root:", root)
    print("Suffix:", suffix)
    print("Type:", t)
    print("Normalized:", root)
    print()
