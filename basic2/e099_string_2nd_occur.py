def all_occurrences(string, search):
	ls = len(search)
	occur = []
	for i in range(len(string) - ls +1):
		if string[i:i + ls] == search:
			occur.append(i)

	return occur

def second_occurrence(string, search):
	ao = all_occurrences(string, search)
	if len(ao) > 1:
		return ao[1]
	else:
		return -1

# web solution
def find_string(txt, str1):
	return txt.find(str1, txt.find(str1)+1)

print(second_occurrence("The quick brown fox jumps over the lazy dog", "the"))
print(second_occurrence("the quick brown fox jumps over the lazy dog", "the"))
