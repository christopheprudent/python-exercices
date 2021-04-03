str1='hello world!'

for c in str1:
	if c in 'aeiouy':
		print('lettre %s est une voyelle'%(c))
	else:
		print('lettre %s est une consonne'%(c))
