words = ["analyzing", "analysis", "analytical"]

for word in words:
    if word == "analyzing":
        root = "analyze"
        affix = "-ing"
        typ = "Inflectional"
        norm = "analyze"

    elif word == "analysis":
        root = "analy"
        affix = "-sis"
        typ = "Derivational"
        norm = "analyze"

    elif word == "analytical":
        root = "analyze"
        affix = "-ical"
        typ = "Derivational"
        norm = "analyze"

    print(word, root, affix, typ, norm)
