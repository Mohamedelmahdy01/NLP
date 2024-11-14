import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


def normalize_text(text):
    sentences = sent_tokenize(text)

    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    normalized_text = []

    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word for word in words if word.isalnum()]
        words = [word for word in words if word.lower() not in stop_words]
        stemmed_words = [ps.stem(word) for word in words]
        lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]
        normalized_text.append(" ".join(lemmatized_words))

    return normalized_text


text = "Dr. Smith went to the U.S. She's a great doctor!"
normalized = normalize_text(text)
print("Normalized Text:", normalized)
