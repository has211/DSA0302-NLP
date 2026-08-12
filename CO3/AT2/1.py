import math

corpus = "data science is powerful data science drives innovation data science is evolving"
words = corpus.lower().split()

print("CASE STUDY 1: SMART MOBILE KEYBOARD")
print("-----------------------------------")

count_data = 3
count_data_science = 3

p_science_given_data = count_data_science / count_data

print("\nQ1. Bigram MLE")
print("P(science | data) =", p_science_given_data)

trigram_count = 0
bigram_count = 0
improves_count = words.count("improves")

if trigram_count > 0:
    probability_backoff = trigram_count / 3
    level = "Trigram"
elif bigram_count > 0:
    probability_backoff = bigram_count / 3
    level = "Bigram"
else:
    probability_backoff = improves_count / len(words)
    level = "Unigram"

print("\nQ2. Backoff Model")
print("Backoff level used:", level)
print("P(improves | data, science) =", probability_backoff)

lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

count_data_science_is = 2
count_data_science = 3

count_science_is = 2
count_science = 3

count_is = words.count("is")
total_words = len(words)

p_trigram = count_data_science_is / count_data_science
p_bigram = count_science_is / count_science
p_unigram = count_is / total_words

p_interpolation = (
    lambda1 * p_trigram
    + lambda2 * p_bigram
    + lambda3 * p_unigram
)

print("\nQ3. Deleted Interpolation")
print("Trigram probability =", p_trigram)
print("Bigram probability =", p_bigram)
print("Unigram probability =", p_unigram)
print("Interpolated probability =", p_interpolation)

p_is = 0.66
p_drives = 0.33

entropy = -(
    p_is * math.log2(p_is)
    + p_drives * math.log2(p_drives)
)

print("\nQ4. Entropy")
print("Entropy =", entropy, "bits")
