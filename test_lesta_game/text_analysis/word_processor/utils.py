import math
from collections import Counter

def compute_tfidf(text):
    words = text.split()
    word_counts = Counter(words)
    total_words = len(words)

    tf = {word: count / total_words for word, count in word_counts.items()}
    idf = {word: math.log(total_words / count) for word, count in word_counts.items()}

    sorted_words = sorted(idf.items(), key=lambda x: x[1], reverse=True)

    return [(word, word_counts[word], idf_value) for word, idf_value in sorted_words][:50]
