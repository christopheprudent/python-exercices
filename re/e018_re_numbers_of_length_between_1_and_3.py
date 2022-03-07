# web solution
import re
to_search = 'Exercises number 1, 12, 13, and 345, 1234 are important'

# avec \b sinon 1234 est retourné 2 fois: 123 et 4
results = re.finditer(r"(\b[0-9]{1,3}\b)", to_search)

print("Number of length 1 to 3 in '%s'" % to_search)
for n in results:
     print(n.group(0))
