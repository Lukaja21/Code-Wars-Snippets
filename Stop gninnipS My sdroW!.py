"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 

Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
"""

def spin_words(sentence):
	newSentence = ""

	for word in sentence.split(" "):
		if len(word) >= 5:
			newSentence += word[::-1] + " "

		else:
			newSentence += word + " "

	return newSentence[:-1]

print(spin_words("Welcome"))