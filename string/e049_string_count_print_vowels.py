def count_print_vowels(s):
	t = [ (i, v) for i, v in enumerate(s) if v.lower() in "aeiou" ]
	for i, v in t:
		print(f'vowel {v} at index {i}')

count_print_vowels('Hello World!')
count_print_vowels('PARIS!')
