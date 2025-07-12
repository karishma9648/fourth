# corpus - it contains a predefined dataset by which we can train ai models

import nltk
from nltk.corpus import gutenberg
nltk.download('gutenberg')

file_id = 'austen-emma.txt'
text=gutenberg.raw(file_id)
print(text[:150])
print(gutenberg.fileids())