text = 'Python is popular than Java'
#new_text = text.replace('Python', 'Java', 1)
#print(new_text)
words = text.split()
for i, word in enumerate(words):
	if word == 'Python':
		words[i] = 'Java'
	elif word == 'Java':
		words[i] = 'Python'

print(*words)
