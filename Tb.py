from textblob import TextBlob, Word
import sys
import random

text = '''
Hello this book is about many things. A girl named Eliza finds a talking squirrel in the forest where she loses her grandmother's apple. "Have you ever lost an apple before?", Eliza asks.
'''

blob = TextBlob(text)
#blob.tags           

nouns = list()
for word, tag in blob.tags:
    if tag == 'NN':
        nouns.append(word.lemmatize())

print "This text is about..."
for item in random.sample(nouns, 5):
	word = Word(item)
	print word.pluralize()

