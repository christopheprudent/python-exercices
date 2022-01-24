import math

def deg2rad(x):
    return x * (math.pi / 180)

def rad2deg(x):
    return x * (180 / math.pi)

if __name__ == '__main__':
    print('dev) conversion degré en radian', 15, 'égal à', deg2rad(15))
    print('dev) conversion radian en degré', .52, 'égal à', rad2deg(.52))

