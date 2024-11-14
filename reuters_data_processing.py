import nltk
import pandas as pd
from nltk.corpus import reuters


nltk.download('reuters')
nltk.download('punkt')


fileids = reuters.fileids()


categories = []
text = []


for file in fileids:
    
    categories.append(reuters.categories(file))
    
  
    raw_text = reuters.raw(file)
    text.append(raw_text)


reutersDf = pd.DataFrame({'ids': fileids, 'categories': categories, 'text': text})


print(reutersDf.head())

for fileid in reuters.fileids():
    num_chars = len(reuters.raw(fileid))
    num_words = len(reuters.words(fileid))
    num_sents = len(reuters.sents(fileid))
    num_vocab = len(set([w.lower() for w in reuters.words(fileid)]))
    print(num_chars, num_words, num_sents, num_vocab, fileid)
