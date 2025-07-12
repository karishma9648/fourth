# using wordnet
import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')

wn.synsets('motorcar')
print(wn.synset('car.n.01').lemma_names())
for synset in wn.synsets('car')[1:3]:
    print(synset.lemma_names())
    
# checking sunset for walk
walk_synset = wn.synset('walk.v.01')
print("Entailments of 'walk':", walk_synset.entailments())

step_synset = wn.synset('step.v.01')
print("Synset for 'step.v.01':", step_synset)
    