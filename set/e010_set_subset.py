def is_subset(s, sub):
    t = s & sub
    #print(t)
    return (t == sub)

def msg(x, y):
    print('Si {} est un sous-ensemble de {}'.format(x, y))

# web solution
print("Test de sous-ensemble, avec opérateur et issubset():\n")
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
print("x: ",setx)
print("y: ",sety)
print("z: ",setz,"\n")
msg('x', 'y')
print(setx <= sety)
print(setx.issubset(sety))
msg('y', 'x')
print(sety <= setx)
print(sety.issubset(setx))
msg('y', 'z')
print(sety <= setz)
print(sety.issubset(setz))
msg('z', 'y')
print(setz <= sety)
print(setz.issubset(sety))
print(is_subset(sety, setz))
