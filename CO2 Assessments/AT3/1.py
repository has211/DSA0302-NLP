import re
import pandas as pd
from nltk.stem import PorterStemmer

ps = PorterStemmer()
data = pd.read_csv("PubMed20k.csv")
text = " ".join(data["abstract"].dropna().astype(str))
words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

for word in ["infection", "infectious", "infected", "infect"]:
    print(word, "->", ps.stem(word))
