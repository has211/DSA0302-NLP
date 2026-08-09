words = ["create", "creates", "creating"]

for word in words:
    if word == "create":
        suffix = "-"
        category = "Base form"
        root = "create"

    elif word == "creates":
        suffix = "-s"
        category = "Third-person singular"
        root = "create"

    elif word == "creating":
        suffix = "-ing"
        category = "Present participle"
        root = "create"

    print(word, suffix, category, root, "create")
