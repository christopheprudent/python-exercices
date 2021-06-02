# web solution
import array
x = array.array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
print(x)
s = x.tobytes()
print(s)

for c in s:
    print('{0:3d} {1}'.format(c, chr(c)))
