multiple15 = lambda x : x % 15 == 0 and x > 0
a = [10, 15, 20, 30, 60, 0]
print([ x for x in a if multiple15(x) ])
