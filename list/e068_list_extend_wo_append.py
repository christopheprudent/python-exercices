x = [10, 20, 30]
y = [40, 50, 60]

print('x= ', x)
print('y= ', y)
x.extend(y)
print('x+y= ', x)

# web solution
x = [10, 20, 30]
x[:0] = y
print('y+x= ', x)
x = [10, 20, 30]
x[len(x):] = y
print('x+y= ', x)
