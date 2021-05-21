sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}

print('set 1', sn1)
print('set 2', sn2)
inter = sn1 & sn2
print('intersection', inter)
sn1 -= inter
print('set 1 sans les données communes (intersection)')
print(sn1)

# web solution
sn1 = {1,2,3,4,5}
sn1.difference_update(sn2)
print(sn1)
sn1 = {1,2,3,4,5}
print(sn1 - sn2)
