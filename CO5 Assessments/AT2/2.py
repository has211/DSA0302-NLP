sentences = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

relations = [
    ("S1", "S2", "Cause-Effect"),
    ("S2", "S3", "Cause-Effect / Result")
]

print("Discourse Relations:")

for a, b, relation in relations:
    print(a, "->", b, ":", relation)

print("\nDiscourse Structure:")
print("ROOT")
print("|-- S1: Roads flooded after heavy rainfall")
print("|   |")
print("|   |-- Cause-Effect")
print("|       S2: Schools closed for the day")
print("|       |")
print("|       |-- Cause-Effect / Result")
print("|           S3: Students attended classes online")

print("\nCoherence: Strong")
print("Reason: Each event logically follows from the previous event.")
