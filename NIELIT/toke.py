import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt_tab')
text = "Hello there! How are you doing today? This is a simple sentence tokenization example."

# Tokenize the text into sentences
sentences = sent_tokenize(text)
word = word_tokenize(text)

# Print the list of sentences
for sentence in sentences:
    print(sentence)

print(word)