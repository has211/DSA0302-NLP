words = ["activate", "activation", "reactivation"]

for word in words:
    if word == "activate":
        prefix = "-"
        root = "act"
        suffix = "-ivate"
        sequence = "act -> activate"

    elif word == "activation":
        prefix = "-"
        root = "act"
        suffix = "-ivation"
        sequence = "act -> activate -> activation"

    elif word == "reactivation":
        prefix = "re-"
        root = "act"
        suffix = "-ivation"
        sequence = "act -> activate -> activation -> reactivation"

    print(word, prefix, root, suffix, sequence, "act")
