from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Eine Bag of Words ausgeben
def print_bag(vectorizer, bag_of_words):
    features = vectorizer.get_feature_names()
    print("Wörter:", features)
    print("Daten:")
    stats = bag_of_words.toarray()
    print(stats)
    print("Angewandt:")
    for text in stats:
        for i, count in enumerate(text):
            if count > 0:
                print(f"{features[i]}: {count}")
        print()

with open('sample.txt', 'r') as strings_file:
    strings = list(strings_file)
print("Zu untersuchende Textzeilen:")
for line in strings:
    print(line.rstrip())
print()
string_data = np.array(strings)
print("1. Originaltexte")
vectorizer = CountVectorizer(strip_accents = 'unicode')
bag_of_words = vectorizer.fit_transform(string_data)
print_bag(vectorizer, bag_of_words)
print("2. Mit Stoppwörtern")
stop = ["der", "die", "das", "des", "dem", "den", "oder", "aber", "auch", "ist", "hat", "mit", "sind", "und", "von"]
print("Stoppwörter:", stop)
vectorizer = CountVectorizer(strip_accents = 'unicode', stop_words = stop)
bag_of_words = vectorizer.fit_transform(string_data)
print_bag(vectorizer, bag_of_words)
print("3. Bigramme")
vectorizer = CountVectorizer(strip_accents = 'unicode', stop_words = stop, ngram_range = (2, 2))
bag_of_words = vectorizer.fit_transform(string_data)
print_bag(vectorizer, bag_of_words)
print("4. Trigramme")
vectorizer = CountVectorizer(strip_accents = 'unicode', stop_words = stop, ngram_range = (3, 3))
bag_of_words = vectorizer.fit_transform(string_data)
print_bag(vectorizer, bag_of_words)
