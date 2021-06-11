print('veuillez saisir la longueur de chacun des trois côtés d\'un triangle')
x = int(input('x= '))
y = int(input('y= '))
z = int(input('z= '))

if x==y==z:
    print('il s\'agit d\'un triangle equilatéral')
elif x==y or x==z or y==z:
    print('il s\'agit d\'un triangle isocèle')
elif x!=y and x!=z and y!=z:
    print('il s\'agit d\'un triangle scalène')
else:
    print('ben, un triangle quoi!')
