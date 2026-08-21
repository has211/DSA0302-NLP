def dialog_act(sentence):
    sentence = sentence.lower()

    if sentence.endswith('?'):
        return "QUESTION"
    elif any(word in sentence for word in ['hello', 'hi', 'hey']):
        return "GREETING"
    elif any(word in sentence for word in ['thank', 'thanks']):
        return "THANKING"
    elif any(word in sentence for word in ['bye', 'goodbye']):
        return "GOODBYE"
    elif any(word in sentence for word in ['please', 'could you', 'can you']):
        return "REQUEST"
    else:
        return "STATEMENT"

text = input("Enter dialog: ")

for sentence in text.split('.'):
    if sentence.strip():
        print(sentence.strip(), "->", dialog_act(sentence.strip()))