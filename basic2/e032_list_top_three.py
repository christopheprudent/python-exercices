#print("Input the heights of eight buildings:")
#l = [int(input()) for i in range(8)]
l = [25,35,15,16,30,45,37,39]
print("Heights of the top three buildings:")
l = sorted(l)
#print(*l[:4:-1], sep='\n')
print(*l[-3:][::-1], sep='\n')

