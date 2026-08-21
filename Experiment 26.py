from transformers import pipeline

translator = pipeline("translation_en_to_fr")

text = input("Enter English text: ")

result = translator(text)

print("English:", text)
print("French:", result[0]['translation_text'])