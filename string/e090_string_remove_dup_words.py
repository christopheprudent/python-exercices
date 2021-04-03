def remove_dup_words(s):
	words = s.split()
	for i, word in enumerate(words):
		if word in words[:i]:
			del words[i]

	return ' '.join(words)

print(remove_dup_words('Python Exercises Practice Solution Exercises'))
