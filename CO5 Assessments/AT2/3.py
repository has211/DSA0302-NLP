utterances = [
    "Can you book a train ticket for me?",
    "Sure, where would you like to travel?",
    "I want to go to Chennai.",
    "Your ticket has been booked."
]

def classify(text):
    t = text.lower()

    if "can you" in t or ("book" in t and "for me" in t):
        return "Request"

    if "where" in t or "would you like" in t:
        return "Question"

    if "i want to go" in t or "i want" in t:
        return "Inform"

    if "has been booked" in t or "booked" in t:
        return "Confirmation / Action"

    return "Unknown"

for utterance in utterances:
    print(utterance)
    print("->", classify(utterance))

print("\nDialogue Act Sequence:")
print("Request -> Question -> Inform -> Confirmation / Action")
