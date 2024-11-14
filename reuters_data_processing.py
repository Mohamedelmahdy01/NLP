import nltk
import pandas as pd
from nltk.corpus import reuters

# Download the necessary NLTK data
nltk.download('reuters')
nltk.download('punkt')

# Extract fileids from the reuters corpus
fileids = reuters.fileids()

# Initialize empty lists to store categories and raw text
categories = []
text = []

# Loop through each file id and collect each file's categories and raw text
for file in fileids:
    # Get the categories for each file
    categories.append(reuters.categories(file))
    
    # Get the raw text for each file
    raw_text = reuters.raw(file)
    text.append(raw_text)

# Combine lists into a pandas DataFrame
reutersDf = pd.DataFrame({'ids': fileids, 'categories': categories, 'text': text})

# Display the first few rows of the DataFrame
print(reutersDf.head())

for fileid in reuters.fileids():
    num_chars = len(reuters.raw(fileid))
    num_words = len(reuters.words(fileid))
    num_sents = len(reuters.sents(fileid))
    num_vocab = len(set([w.lower() for w in reuters.words(fileid)]))
    print(num_chars, num_words, num_sents, num_vocab, fileid)
