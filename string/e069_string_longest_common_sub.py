def longest_common_sub(s1, s2):
	if len(s1) <= len(s2):
		s, b = s1, s2
	else:
		s, b = s2, s1

	l = i = len(s)
	while i>0:
		subs = [ s[j:j+i] for j in range(l-i+1) ]
		print(f'i={i} subs={subs}')
		for sub in subs:
			if sub in b:
				return sub
		i -= 1

	return None

print(longest_common_sub('abcdefgh', 'xswerabcdwd'))

# web solution
# https://towardsdatascience.com/sequencematcher-in-python-6b1e6f3915fc
# https://docs.python.org/3/library/difflib.html#sequencematcher-objects
from difflib import SequenceMatcher 
  
def longest_Substring(s1,s2): 
  
     seq_match = SequenceMatcher(None,s1,s2) 
  
     match = seq_match.find_longest_match(0, len(s1), 0, len(s2)) 
  
     # return the longest substring 
     if (match.size!=0): 
          return (s1[match.a: match.a + match.size])  
     else: 
          return ('Longest common sub-string not present')  

print()
s1 = 'abcdefgh'
s2 = 'xswerabcdwd'
print("Original Substrings:\n",s1+"\n",s2)
print("\nCommon longest sub_string:")
print(longest_Substring(s1,s2))

