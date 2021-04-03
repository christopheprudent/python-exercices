import collections
text = input('Entrez une ligne de texte : ')

def compute_text(text):
	words = text.split()
	compute = dict()
	for word in words:
		if not word in compute:
			compute[word] = {'occurence' : 1, 'length' : len(word) }
		else:
			compute[word]['occurence'] += 1

	return compute

ctext = compute_text(text)
print('-' * 30)
print(ctext)
print(ctext.keys())
print(ctext.values())
print(ctext.items())
counter = collections.Counter(text.split())
print(counter)
print(counter.most_common())
print(counter.most_common()[0][0])

print('-' * 30)
ctext_occur = sorted(ctext.items(), key=lambda item: item[1]['occurence'])
print(ctext_occur)
most_freq = (list(ctext_occur)[-1])[0]
print('The most frequently word is %s' % str(most_freq))
#print('The most frequently word is %s' % next(iter(ctext_occur)))

print('-' * 30)
ctext_len = sorted(ctext.items(), key=lambda item: item[1]['length'], reverse=True)
print(ctext_len)
print('The longer word is %s' % (next(iter(ctext_len)))[0])
