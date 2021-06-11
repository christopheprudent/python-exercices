binseq = input('entrez une séquence de nombres binaires, séparés par une virgule : ')
binval = binseq.split(',')
binint = map(lambda x:int(x, 2), binval)

index_only_mult_5 = [i for i, v in enumerate(binint) if not v % 5]
for idx in index_only_mult_5:
    print(binval[idx], end=',')
print()

# web solution
items = []
num = [x for x in binseq.split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))
