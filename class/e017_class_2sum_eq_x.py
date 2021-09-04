L = [10,20,10,40,50,60,70]
S = [(i, j) for i, x in enumerate(L) for j, y in enumerate(L) if x+y == 50 and i<j]
print('liste', L)
print('indices (i, j) tels que liste(i)+liste(j) == 50 :', S)

# web solution
class py_solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            print(f'i={i} num={num} lookup={lookup}')
            if target - num in lookup:
                # solution: indices (target - num) stocké dans 'lookup', et position courante de 'num'
                return (lookup[target - num], i)
            lookup[num] = i

#i=0 num=10 lookup={}
#i=1 num=20 lookup={10: 0}
#i=2 num=10 lookup={10: 0, 20: 1}
#i=3 num=40 lookup={10: 2, 20: 1}

print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))
#index1=2, index2=3
