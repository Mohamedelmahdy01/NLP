
# NLTK Reuters Corpus and Text Normalization

This project includes two main Tasks that work with text data. The first task extracts information from the NLTK Reuters Corpus, while the second task demonstrates text normalization techniques such as tokenization, stop word removal, stemming, and lemmatization.

## Requirements

Make sure you have the following packages installed:

- `nltk`
- `pandas`

You can install these using pip if they are not already installed:

```bash
pip install nltk pandas
```

## Contents

### File 1: `reuters_data_processing.py`

This script performs the following tasks:

1. **Download Necessary NLTK Data**: Downloads the Reuters corpus and tokenization tools.
2. **Extract Reuters Corpus Data**: Loops through all file IDs in the corpus, extracting each file's categories and raw text.
3. **Create a DataFrame**: Stores the data in a Pandas DataFrame with columns `ids`, `categories`, and `text`.
4. **Data Summary**: Calculates statistics for each file, including the number of characters, words, sentences, and unique vocabulary words.

**Usage**:

Run the File to display a DataFrame of Reuters data and print statistics for each document.

```python
python reuters_data_processing.py
```

### File 2: `text_normalization.py`

This file provides a function to normalize text, performing the following steps:

1. **Segmentation**: Splits the input text into sentences.
2. **Tokenization**: Breaks each sentence into individual words.
3. **Remove Punctuation**: Removes punctuation marks from the tokens.
4. **Remove Stop Words**: Filters out common English stop words.
5. **Stemming**: Reduces words to their root forms using Porter Stemmer.
6. **Lemmatization**: Converts words to their base forms using WordNet Lemmatizer.

**Example Usage**:

```python
python text_normalization.py
```

The file includes a sample text, `"Dr. Smith went to the U.S. She's a great doctor!"`, which it normalizes and prints as output.

**Output**:

The normalized text will appear in the console as a list of sentences with processed words.

## Running Tasks

1. **Ensure NLTK Resources are Downloaded**: If running for the first time, ensure you download the necessary NLTK resources by following the download instructions in each script.
   
2. **Execute Each task Separately**: Run `reuters_data_processing.py` to explore Reuters data and `text_normalization.py` to normalize example text.
