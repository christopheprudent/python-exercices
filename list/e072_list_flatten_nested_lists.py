L = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
nl = []

#for i, l in enumerate(L):
    #nl.extend(L[i:i+1])
    #nl[i:] = L[i:i+1]

for x in L:
    if isinstance(x, list):
        for i in x:
            nl.append(i)
    else:
        nl.append(x)
        

print('liste ', L)
print('suite mise à plat: ', nl) 
