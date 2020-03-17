"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
"""

def duplicate_encode(word):
	encodeDict = {}
	newWord = ""

	for char in word:
		if char.lower() in encodeDict:
			encodeDict[char.lower()] += 1
		else:
			encodeDict[char.lower()] = 1

	for char in word:
		if encodeDict[char.lower()] > 1:
			newWord += ")"
		else:
			newWord += "("

	return newWord

print(duplicate_encode("din"))