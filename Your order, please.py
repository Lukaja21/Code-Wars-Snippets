"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
"""

def order(sentence):
	if len(sentence) > 0:
		words = sentence.split(" ")
		newSentence = []
		count = 1
	
		while len(words) > len(newSentence):
			for word in words:
				if str(count) in word:
					newSentence.append(word)
					break
			count += 1
	
		return " ".join(newSentence)

	else:
		return ""

print(order("4of Fo1r pe6ople g3ood th5e the2"))