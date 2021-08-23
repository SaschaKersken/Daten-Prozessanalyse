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

strings = [
    "Machine Learning mit Python",
    "Mamba, Boa und Python sind bekannte Schlangen",
    "Das Leben des Brian von Monty Python"
]
string_data = np.array(strings)
print("1. Originaltexte")
vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(string_data)
print_bag(vectorizer, bag_of_words)
print("2. Mit Stoppwörtern")
stop = ["das", "des", "mit", "sind", "und", "von"]
print("Stoppwörter:", stop)
vectorizer = CountVectorizer(stop_words = stop)
bag_of_words = vectorizer.fit_transform(string_data)
print_bag(vectorizer, bag_of_words)
print("3. Mit Stoppwörtern, zu häufige Wörter (>= 90%) ignorieren)")
vectorizer = CountVectorizer(stop_words = stop, max_df = 0.9)
bag_of_words = vectorizer.fit_transform(string_data)
print_bag(vectorizer, bag_of_words)
print("4. Bigramme")
vectorizer = CountVectorizer(stop_words = stop, ngram_range = (2, 2))
bag_of_words = vectorizer.fit_transform(string_data)
print_bag(vectorizer, bag_of_words)
