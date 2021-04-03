#print("Input three integers(a b c): ")
#a,b,c = map(int,input().split(" "))
#
#if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
#	print('Yes')
#else:
#	print('No')

# web solution
print("Input three integers(sides of a triangle)")
int_num = list(map(int,input().split()))
x,y,z = sorted(int_num)
if x**2+y**2==z**2:
    print('Yes')
else:
    print('No')

