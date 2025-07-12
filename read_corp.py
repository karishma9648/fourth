from nltk.corpus import PlaintextCorpusReader

corpus_root="C:/Users/Dell/OneDrive/Desktop/NIELIT/NLTK"
wordlists=PlaintextCorpusReader(corpus_root,r'.*\.txt')

print(wordlists.fileids()[:1])

print(wordlists.words("C:/Users/Dell/OneDrive/Desktop/NIELIT/NLTK/shelock.txt"))