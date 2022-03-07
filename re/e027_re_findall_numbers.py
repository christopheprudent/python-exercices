# web solution
import re
# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
result = re.split("\D+", text)
print(result)
for element in result:
    print(element)

# dev
print(list(map(int, re.findall(r'(\d+)', text))))
