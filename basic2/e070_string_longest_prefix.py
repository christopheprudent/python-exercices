#def longest_prefix(s1, s2):
#	a1 = list(s1)
#	a2 = list(s2)
#	
#	common = False
#	i = 1
#	while True:
#		t1 = str(a1[:i])
#		t2 = str(a2[:i])
#		if t1 != t2:
#			break
#
#		i += 1
#		common = True
#
#	return (common, ''.join(a1[:i-1]))
#
#rt1 = longest_prefix("abcdefgh", "abcefgh")
#print('les 2 chaînes {} et {} ont un préfixe commun : {} ({})'.format("abcdefgh", "abcefgh", rt1[0], rt1[1]))
#rt2 = longest_prefix("w3r","w3resource")
#print('les 2 chaînes {} et {} ont un préfixe commun : {} ({})'.format("w3r","w3resource", rt2[0], rt2[1]))
#rt3 = longest_prefix("Python","Java")
#print('les 2 chaînes {} et {} ont un préfixe commun : {} ({})'.format("Python","PHP", rt3[0], rt3[1]))

# web solution
def longest_Common_Prefix(str1):
    
    if not str1:
        return ""

    short_str = min(str1,key=len)

    for i, char in enumerate(short_str):
        for other in str1:
            if other[i] != char:
                return short_str[:i]

    return short_str 

print(longest_Common_Prefix(["abcdefgh","abcefgh"]))
print(longest_Common_Prefix(["w3r","w3resource"]))
print(longest_Common_Prefix(["Python","PHP", "Perl"]))
print(longest_Common_Prefix(["Python","PHP", "Java"]))
print(longest_Common_Prefix(["Python"]))
print(longest_Common_Prefix(["Python","Python"]))

