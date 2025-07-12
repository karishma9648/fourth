import nltk
import urllib.request
from bs4 import BeautifulSoup

# Download tokenizer (only needed once)
nltk.download('punkt')

# Fetch HTML content
url = 'https://news.abplive.com/'
html = urllib.request.urlopen(url).read()

# Parse HTML and extract text
soup = BeautifulSoup(html, 'html.parser')
raw = soup.get_text()

# Tokenize words
tokens = nltk.word_tokenize(raw)

# Print results
print(raw[:60])  # Print the first 60 characters
print(tokens[:15])  # Print the first 15 tokens
