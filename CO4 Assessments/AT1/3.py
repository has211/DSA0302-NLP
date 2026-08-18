# AT1 - Q3
# Word Sense Disambiguation in E-Commerce Search

queries = {
    "Apple accessories": {
        "senses": ["Fruit", "Technology Brand"],
        "context": "iPhone Charger",
        "correct": "Technology Brand"
    },
    "Mouse wireless": {
        "senses": ["Animal", "Computer Device"],
        "context": "Bluetooth Mouse",
        "correct": "Computer Device"
    },
    "Java tutorial": {
        "senses": ["Island", "Programming Language"],
        "context": "Coding Lessons",
        "correct": "Programming Language"
    },
    "Python course": {
        "senses": ["Snake", "Programming Language"],
        "context": "Software Development Training",
        "correct": "Programming Language"
    }
}

for query, data in queries.items():

    print("Query :", query)
    print("Possible senses :", data["senses"])
    print("Context :", data["context"])
    print("Selected sense :", data["correct"])
    print("-" * 50)
