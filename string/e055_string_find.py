# find the first repeated character of a given string where the index of first occurrence is smallest
def first_repeated_char_nearest_occurence(str1):
  tmp = dict()
  for index,c in enumerate(str1):
    pos = str1[index+1:].find(c)
    if pos > -1:
      if not c in tmp:
        tmp[c] = index+1+pos
        
  if len(tmp) > 0:
    # sort on position, and return first (the smallest)
    return (sorted(tmp.items(), key= lambda x: x[1]))[0]
    
  return "None"


print(first_repeated_char_nearest_occurence("abcdabcd"))
print(first_repeated_char_nearest_occurence("abcd"))
print(first_repeated_char_nearest_occurence("abccbd"))

# web solution (simplier: first occurence)
def first_repeated_char_smallest_distance(str1):
  temp = {}
  for ch in str1:
    if ch in temp:
      return ch, str1.index(ch);
    else:
      temp[ch] = 0
  return 'None'
print(first_repeated_char_smallest_distance("abcabc"))
print(first_repeated_char_smallest_distance("abcb"))
print(first_repeated_char_smallest_distance("abcc"))
print(first_repeated_char_smallest_distance("abcxxy"))
print(first_repeated_char_smallest_distance("abc"))

