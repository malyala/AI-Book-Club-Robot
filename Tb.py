from textblob import TextBlob, Word
import sys
import random

potentialqs= ["What did you think of the main character?", "Do you really feel like they had to follow the arc they did?"]

initialuserq = raw_input("Hi, do you want to here my summary of the main points of the book we are discussing today?")
# virtual book club summarizes book
# builds and trains on these summaries to provide opinions, discussions
if initialuserq == "yes":
	  
	text = '''
	Hello this book is about many things. A girl named Eliza finds a talking squirrel in the forest where she loses her grandmother's apple. "Have you ever lost an apple before?", Eliza asks.
	'''

	blob = TextBlob(text)
	
	#uses textblob documentation
			 
	nouns = list()
	for word, tag in blob.tags:
		if tag == 'NN':
			nouns.append(word.lemmatize())

	print "This text is about..."
	for item in random.sample(nouns, 6):
		word = Word(item)
		print word.pluralize()
	
	if blob.sentiment.polarity < 0.5:
    		negative = ["I didn't like this! It was too sad.", "This book was very dark for me."]
    		print(random.choice(negative))

	else:
    		print("I thought this was a good book!")
		
raw_input(random.choice(potentialqs))


