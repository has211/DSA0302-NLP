# AT1 - Q4
# Syntax-Driven Semantic Analysis in Healthcare

sentences = [
    {
        "sentence": "Doctor prescribed medicine to patient.",
        "roles": {
            "Doctor": "Agent",
            "Medicine": "Theme",
            "Patient": "Recipient"
        }
    },
    {
        "sentence": "Patient reported severe headache.",
        "roles": {
            "Patient": "Experiencer",
            "Headache": "Symptom"
        }
    },
    {
        "sentence": "Nurse monitored patient continuously.",
        "roles": {
            "Nurse": "Agent",
            "Patient": "Theme"
        }
    },
    {
        "sentence": "Medicine reduced blood pressure.",
        "roles": {
            "Medicine": "Cause",
            "Blood Pressure": "Theme"
        }
    }
]

for item in sentences:

    print("Sentence:", item["sentence"])
    print("Semantic Roles:")

    for entity, role in item["roles"].items():
        print("  ", entity, "->", role)

    print("-" * 50)
