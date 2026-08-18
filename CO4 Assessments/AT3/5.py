sentence = ["The", "student", "reads", "a", "book"]
stack = []
buffer = sentence.copy()
dependencies = []

stack.append(buffer.pop(0))
stack.append(buffer.pop(0))
stack.append(buffer.pop(0))
dependencies.append(("reads", "student"))
stack.pop()
stack.append(buffer.pop(0))
stack.append(buffer.pop(0))
dependencies.append(("reads", "book"))

print("Transition-Based Parsing:")
for head, dep in dependencies:
    print(head, "->", dep)

edges = [
    ("reads", "student", 0.95),
    ("reads", "book", 0.92),
    ("student", "The", 0.90),
    ("book", "a", 0.88)
]

print("\nGraph-Based Parsing:")
for head, dep, score in edges:
    print(head, "->", dep, "Score:", score)
