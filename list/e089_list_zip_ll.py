L1=[[1, 3], [5, 7], [9, 11]]
L2=[[2, 4], [6, 8], [10, 12, 14]]
L=[x+y for x, y in zip(L1, L2)]

print(f'l1={L1} l2={L2}')
print('liste "zippée:', L)

# web solution
zL = list(map(list.__add__, L1, L2))
print('liste "zippée:', zL)
