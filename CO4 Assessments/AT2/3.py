print("=" * 70)
print("HEALTHCARE NLP SYSTEM")
print("=" * 70)

sentence = "The doctor who reviewed the patient last week recommends starting medication and scheduling a follow-up visit in Chennai."

print("\nInput Sentence:")
print(sentence)

tokens = sentence.replace(".", "").split()

print("\n" + "=" * 70)
print("1. TOKENIZATION")
print("=" * 70)

print(tokens)

print("\n" + "=" * 70)
print("2. POS TAGGING")
print("=" * 70)

pos_tags = {
    "The": "Determiner",
    "doctor": "Noun",
    "who": "Pronoun",
    "reviewed": "Verb",
    "the": "Determiner",
    "patient": "Noun",
    "last": "Adjective",
    "week": "Noun",
    "recommends": "Verb",
    "starting": "Verb",
    "medication": "Noun",
    "and": "Conjunction",
    "scheduling": "Verb",
    "a": "Determiner",
    "follow-up": "Noun",
    "visit": "Noun",
    "in": "Preposition",
    "Chennai": "Location"
}

for word, tag in pos_tags.items():
    print(f"{word:<15} -> {tag}")

print("\n" + "=" * 70)
print("3. SYNTACTIC STRUCTURE")
print("=" * 70)

print("Sentence")
print("├── Subject: The doctor")
print("│   └── Relative Clause: who reviewed the patient last week")
print("└── Predicate: recommends")
print("    ├── starting medication")
print("    └── scheduling a follow-up visit")
print("        └── Location: Chennai")

print("\n" + "=" * 70)
print("4. PCFG")
print("=" * 70)

print("PCFG assigns probabilities to alternative parse structures.")
print("The most probable syntactic interpretation is selected.")

print("\n" + "=" * 70)
print("5. FEATURE STRUCTURES")
print("=" * 70)

features = {
    "Number": "Singular",
    "Person": "Third",
    "Tense": "Present"
}

for feature, value in features.items():
    print(f"{feature:<15} -> {value}")

print("\n" + "=" * 70)
print("6. MEDICAL NAMED ENTITIES")
print("=" * 70)

entities = {
    "Doctor": "Medical Professional",
    "Patient": "Person",
    "Medication": "Treatment",
    "Chennai": "Location"
}

for entity, category in entities.items():
    print(f"{entity:<15} -> {category}")

print("\n" + "=" * 70)
print("7. ACTION EXTRACTION")
print("=" * 70)

actions = [
    "reviewed",
    "recommends",
    "starting",
    "scheduling"
]

for action in actions:
    print("->", action)

print("\n" + "=" * 70)
print("8. SUBCATEGORIZATION FRAMES")
print("=" * 70)

frames = {
    "prescribe": "Doctor + Medicine + Patient",
    "recommend": "Doctor + Treatment",
    "diagnose": "Doctor + Disease + Patient",
    "schedule": "Staff + Appointment"
}

for verb, frame in frames.items():
    print(f"{verb:<12} -> {frame}")

print("\n" + "=" * 70)
print("9. SEMANTIC ROLES")
print("=" * 70)

roles = {
    "Doctor": "Agent",
    "Patient": "Theme",
    "Medication": "Treatment",
    "Follow-up Visit": "Appointment",
    "Chennai": "Location"
}

for entity, role in roles.items():
    print(f"{entity:<20} -> {role}")

print("\n" + "=" * 70)
print("10. STRUCTURED OUTPUT")
print("=" * 70)

structured_output = {
    "Subject": "Doctor",
    "Reviewed": "Patient",
    "Action 1": "Start medication",
    "Action 2": "Schedule follow-up visit",
    "Location": "Chennai"
}

for key, value in structured_output.items():
    print(f"{key:<20}: {value}")

print("\n" + "=" * 70)
print("11. REAL-TIME PROCESSING")
print("=" * 70)

real_time_steps = [
    "Fast Tokenization",
    "Efficient Parsing",
    "Medical NER",
    "Semantic Analysis",
    "Structured Output"
]

for step in real_time_steps:
    print("->", step)

print("\n" + "=" * 70)
print("12. SCALABILITY")
print("=" * 70)

scalability_methods = [
    "Optimized Earley or Chart Parsing",
    "Medical NLP Models",
    "Parallel Processing",
    "Grammar Rule Caching",
    "Confidence Scores",
    "Medical Knowledge Base"
]

for method in scalability_methods:
    print("-", method)

print("\n" + "=" * 70)
print("COMPLETE NLP ARCHITECTURE")
print("=" * 70)

architecture = [
    "Medical Report",
    "Tokenization",
    "POS Tagging",
    "CFG Parsing",
    "PCFG",
    "Feature Structures",
    "Medical NER",
    "Subcategorization",
    "Semantic Role Analysis",
    "Structured Medical Information"
]

for i, component in enumerate(architecture, 1):
    print(f"{i}. {component}")

print("\nProcessing Completed Successfully!")
