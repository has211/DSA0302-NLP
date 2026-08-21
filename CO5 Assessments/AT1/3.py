sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

context = ["river","flooded","storm"]

if "river" in context and "flooded" in context:
    sense = "riverbank"
else:
    sense = "financial institution"

print("Sentence:",sentence)
print("Word Sense of bank:",sense)

predicates = [
    "Bank(b)",
    "River(r)",
    "LocatedBy(b,r)",
    "Storm(s)",
    "FloodedAfter(b,s)",
    "QuickAction(a)",
    "SavedBy(b,a)"
]

print("\nPredicate Logic:")
for predicate in predicates:
    print(predicate)

print("\nDiscourse Structure:")
print("CONTRAST")
print("├── Clause 1: The riverbank flooded after the storm")
print("└── Clause 2: Quick action saved the riverbank")

paraphrase = "The riverbank was flooded after the storm, but quick action saved it."

print("\nParaphrase:")
print(paraphrase)
