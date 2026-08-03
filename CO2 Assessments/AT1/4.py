words = ["writes", "writing", "written"]

for word in words:

    if word == "writes":
        root = "write"
        state = "Start -> write -> s"
        pattern = "Regular"

    elif word == "writing":
        root = "write"
        state = "Start -> write -> ing"
        pattern = "Regular"

    elif word == "written":
        root = "write"
        state = "Start -> write -> written"
        pattern = "Irregular"

    print("Word:", word)
    print("State:", state)
    print("Root:", root)
    print("Pattern:", pattern)
    print("Normalized:", root)
    print()
