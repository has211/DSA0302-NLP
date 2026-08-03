words = ["relational", "relation", "relate"]

for word in words:

    if word == "relational":
        rule = "Remove 'ational'"
        intermediate = "relate"
        stem = "relat"

    elif word == "relation":
        rule = "Remove 'ion'"
        intermediate = "relat"
        stem = "relat"

    elif word == "relate":
        rule = "Remove final 'e'"
        intermediate = "relat"
        stem = "relat"

    print("Word:", word)
    print("Rule:", rule)
    print("Intermediate:", intermediate)
    print("Final Stem:", stem)
    print()
