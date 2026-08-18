def analyze(word):
    prefixes = ["un", "re"]
    suffixes = ["est", "able", "ing", "s"]

    prefix = ""
    root = word

    for p in prefixes:
        if root.startswith(p) and len(root) > len(p):
            prefix = p
            root = root[len(p):]
            break

    suffix = ""
    for s in suffixes:
        if root.endswith(s) and len(root) > len(s):
            suffix = s
            root = root[:-len(s)]
            break

    return prefix, root, suffix

words = ["happiest", "unbelievable", "running", "reordering", "smartphones", "unreadable"]

for w in words:
    print(w, "->", analyze(w))
