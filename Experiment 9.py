import re

sentence = "Hasini is running quickly"

words = sentence.split()

print("Rule-Based POS Tagging")

for word in words:
    if re.match(r'.*ing$', word):
        tag = "VBG"
    elif re.match(r'.*ly$', word):
        tag = "RB"
    elif word[0].isupper():
        tag = "NNP"
    else:
        tag = "NN"

    print(word, "->", tag)