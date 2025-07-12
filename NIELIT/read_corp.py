from nltk.corpus import PlaintextCorpusReader

corpus_root="C:\\Users\\Lenovo\\OneDrive\\Desktop\\NIELIT"
wordlists=PlaintextCorpusReader(corpus_root,r'.*\.txt')

print(wordlists.fileids()[:1])

print(wordlists.words("C:\\Users\\Lenovo\\OneDrive\\Desktop\\NIELIT\shelock.txt"))