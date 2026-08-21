responses = [
    "Since your exam is tomorrow, take a short break and then return with a clear focus on one topic at a time. You can concentrate better in small sessions, and this will help you feel more confident.",
    "Take a short break first, then choose one small exam topic and focus only on that for a while. If you keep the plan simple, you can concentrate better and feel more confident.",
    "Your exam is important, but you do not have to study everything at once. Take a short break, focus on the most important topics, and remind yourself that you can be confident in what you know."
]

keywords = ["focus","break","confident"]

for i,response in enumerate(responses,1):
    sentences = response.count(".")
    found = [word for word in keywords if word in response.lower()]
    valid = sentences >= 2 and sentences <= 3 and len(found) >= 2
    print("Response",i)
    print(response)
    print("Keywords:",found)
    print("Valid:",valid)
    print()

best = responses[0]
print("Best Response:")
print(best)
