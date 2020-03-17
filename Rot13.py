"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 

ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 

If there are numbers or special characters included in the string, they should be returned as they are. 

Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
"""

def rot13(message):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	newMessage = ""

	for char in message:
		if char.lower() in alphabet:
			if char.isupper():
				uppercase = True
			else:
				uppercase = False
	
			char = char.lower()
	
			if alphabet.index(char) + 13 > 25:
				newChar = alphabet[alphabet.index(char) - 13]
			else:
				newChar = alphabet[alphabet.index(char) + 13]
	
			if uppercase:
				newMessage += newChar.capitalize()
			else:
				newMessage += newChar
		
		else:
			newMessage += char

	return newMessage

print(rot13("d"))