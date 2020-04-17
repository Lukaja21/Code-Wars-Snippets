def anagrams(word, words):
	word = list(word)
	word.sort()
	anagrams = []


	for listWord in words:
		listListWord = list(listWord.replace(" ", ""))
		listListWord.sort()
		print(listListWord)
		if listListWord == word:
			anagrams.append(listWord.replace(" ", ""))

	return anagrams

print(anagrams('abba', ['a    abb', 'abcd', 'bbaa', 'dada']))