"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.
"""

def alphabet_position(text):
	newStr = ""
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	for char in text:
		try: 
			newStr += str(alphabet.index(char.lower()) + 1) + " "
		except:
			pass

	return newStr[:-1]

print(alphabet_position("The sunset sets at twelve o' clock."))