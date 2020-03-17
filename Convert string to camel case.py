"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 

The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
"""

def to_camel_case(text):
	text.replace("-", "_")

	words = text.split("_")

	for word in words[1:]:
		words[words.index(word)] = word.capitalize()

	words = "".join(words)
	return words

print(to_camel_case("The_stealth_warrior"))