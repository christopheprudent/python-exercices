def add_Is(s):
	if s[:2] != 'Is':
		return 'Is' + s
	return s


str1='chaîne à modifier'
print('chaîne \'%s\' modifiée si vaut : %s'%(str1, add_Is(str1)))
str1='Is chaîne à modifier'
print('chaîne \'%s\' modifiée si vaut : %s'%(str1, add_Is(str1)))
str1=''
print('chaîne \'%s\' modifiée si vaut : %s'%(str1, add_Is(str1)))
