# creating text objects
import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.tokenize import word_tokenize

raw_text = gutenberg.raw('carroll-alice.txt')
tokens = nltk.word_tokenize(raw_text)

text = Text(tokens)
print(text)
# text.collocations()
text.concordance("Rabbit", width=80)
