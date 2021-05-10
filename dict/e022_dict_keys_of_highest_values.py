# https://stackoverflow.com/questions/12266617/finding-top-k-largest-keys-in-a-dictionary-python

# web solution
from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
print('dictionnaire', my_dict)
print('clés des 3 plus grandes valeurs')
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest) 
print('3 plus grandes clés')
three_largest = nlargest(3, my_dict)
print(three_largest) 
