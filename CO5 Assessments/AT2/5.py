source = "The boy is playing football."

interlingua = {
    "action": "PLAY",
    "agent": "BOY",
    "object": "FOOTBALL",
    "tense": "PRESENT",
    "aspect": "PROGRESSIVE"
}

candidates = {
    "The boy is playing football.": 0.95,
    "The boy plays football.": 0.72,
    "The boy was playing football.": 0.31
}

best_translation = max(candidates, key=candidates.get)

print("Source Sentence:")
print(source)

print("\nInterlingua Representation:")

for key, value in interlingua.items():
    print(key, "=", value)

print("\nCandidate Translations:")

for sentence, score in candidates.items():
    print(sentence, "Score:", score)

print("\nFinal Translation:")
print(best_translation)

print("\nEvaluation:")
print("The selected translation preserves the present progressive meaning.")
