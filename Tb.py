from textblob import TextBlob, Word
import sys
import random

initialuserq = raw_input("Hi, do you want to here my summary of the main points of the book we are discussing today?)"
# virtual book club summarizes book
# builds and trains on these summaries to provide opinions, discussions
if initialuserq == "yes":
	  
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

