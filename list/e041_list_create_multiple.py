import collections

# web solution
obj = {}
for i in range(1, 21):
    obj[str(i)] = []

print(obj)
print(sorted(obj.items(), key= lambda x: x[0]))
# hum, missunderstood lambda!
# print(sorted(obj.items(), key= lambda y: int((lambda x: x[0]))(y)))

ordered_obj = collections.OrderedDict(sorted(obj.items()))
print(ordered_obj)
