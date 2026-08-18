# AT1 - Q1
# Semantic Representation in Customer Support Chatbot

queries = {
    "Q1": {
        "query": "Activate international roaming for my number.",
        "actual": "ACTIVATE(Roaming, Customer)",
        "predicted": "ACTIVATE(Roaming, Customer)"
    },
    "Q2": {
        "query": "Deactivate caller tune service.",
        "actual": "DEACTIVATE(CallerTune, Customer)",
        "predicted": "ACTIVATE(CallerTune, Customer)"
    },
    "Q3": {
        "query": "Check my data balance.",
        "actual": "QUERY(DataBalance, Customer)",
        "predicted": "QUERY(DataBalance, Customer)"
    },
    "Q4": {
        "query": "Enable 5G service.",
        "actual": "ACTIVATE(5GService, Customer)",
        "predicted": "ACTIVATE(5GService, Customer)"
    }
}

for q, data in queries.items():
    print(q)
    print("Query    :", data["query"])
    print("Actual   :", data["actual"])
    print("Predicted:", data["predicted"])

    if data["actual"] == data["predicted"]:
        print("Result   : Correct")
    else:
        print("Result   : Incorrect")

    print("-" * 50)
