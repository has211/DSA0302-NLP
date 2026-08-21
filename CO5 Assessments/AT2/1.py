text = "Ravi met Arun at the library. He borrowed a book and later returned it."

resolved = text.replace("He", "Arun").replace("it", "the book")

print("Original:")
print(text)

print("\nCoreference Resolution:")
print("He -> Arun")
print("it -> book")

print("\nResolved Discourse:")
print(resolved)
