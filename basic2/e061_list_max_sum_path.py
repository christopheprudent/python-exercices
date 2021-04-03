import sys
print("Input the numbers (ctrl+d to exit):")
nums = [list(map(int, l.split(","))) for l in sys.stdin]
mvv = nums[0]
print('diamond len: %d' % len(nums))
print(f'mvv=${mvv}')

for i in range(1, (len(nums)+1)//2):
    print(f'i={i}')
    rvv = [0]*(i+1)
    print(f'rvv=${rvv}')
    for j in range(i):
        print(f'j={j}')
        rvv[j] = max(rvv[j], mvv[j]+nums[i][j])
        print(f'rvv=${rvv}')
        rvv[j+1] = max(rvv[j+1], mvv[j]+nums[i][j+1])
        print(f'rvv=${rvv}')
    mvv = rvv
    print(f'mvv=${mvv}')

print()
for i in range((len(nums)+1)//2, len(nums)):
    print(f'i={i}')
    rvv = [0]*(len(mvv)-1)
    print(f'rvv=${rvv}')
    for j in range(len(rvv)):
        print(f'j={j}')
        rvv[j] = max(mvv[j], mvv[j+1]) + nums[i][j]
        print(f'rvv=${rvv}')
    mvv = rvv
    print(f'mvv=${mvv}')

print("Maximum value of the sum of integers passing according to the rule on one line.") 
print(mvv[0])

