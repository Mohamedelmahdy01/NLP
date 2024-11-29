

# NLTK Reuters Corpus and Text Normalization

This project includes three main tasks that work with text data. The first task extracts information from the NLTK Reuters Corpus, the second task demonstrates text normalization techniques, and the third task (in a Jupyter Notebook) combines various NLP techniques.

## Requirements

Make sure you have the following packages installed:

- `nltk`
- `pandas`
- `jupyter`

You can install these using pip if they are not already installed:

```bash
pip install nltk pandas jupyter
```

## Contents

### File 1: `reuters_data_processing.py`

This script performs the following tasks:
1. **Download Necessary NLTK Data**: Downloads the Reuters corpus and tokenization tools.
2. **Extract Reuters Corpus Data**: Loops through all file IDs in the corpus, extracting each file's categories and raw text.
3. **Create a DataFrame**: Stores the data in a Pandas DataFrame with columns `ids`, `categories`, and `text`.
4. **Data Summary**: Calculates statistics for each file, including the number of characters, words, sentences, and unique vocabulary words.

**Usage**:

```bash
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

**Usage**:

```bash
python text_normalization.py
```

### File 3: `Text_Miner_Toolkit.ipynb`

This Jupyter Notebook demonstrates the integration of text data processing and normalization techniques. It includes:
- **NLP Analysis**: Further exploration of text data.
- **Visualization**: Displays insights from the processed data.
- **Code Execution**: Run the notebook using Jupyter:

```bash
jupyter notebook Text_Miner_Toolkit.ipynb
```

## Running Tasks

1. **Ensure NLTK Resources are Downloaded**: If running for the first time, download the necessary NLTK resources.
2. **Execute Tasks Separately**: Run `reuters_data_processing.py` and `text_normalization.py` scripts individually, and explore the notebook for an integrated analysis.