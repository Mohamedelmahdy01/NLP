import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def normalize_text(text):
    # 1. Segmentation: Split text into sentences
    sentences = sent_tokenize(text)

    # Initialize tools
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # Result container for normalized sentences
    normalized_text = []

    # Process each sentence
    for sentence in sentences:
        # 2. Tokenization: Split each sentence into words
        words = word_tokenize(sentence)

        # 3. Remove Punctuation
        words = [word for word in words if word.isalnum()]  # Remove punctuation

        # 4. Remove Stop Words
        words = [word for word in words if word.lower() not in stop_words]

        # 5. Stemming
        stemmed_words = [ps.stem(word) for word in words]

        # 6. Lemmatization
        lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]

        # Append normalized sentence to the result
        normalized_text.append(" ".join(lemmatized_words))

    # Return the fully normalized text as a list of sentences
    return normalized_text

text = "Dr. Smith went to the U.S. She's a great doctor!"
normalized = normalize_text(text)
print("Normalized Text:", normalized)
