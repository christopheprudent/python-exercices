# web solution

def cocktail_shaker_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        is_swapped = False
        print(f'i={i}')
        
        for j in range(i, 0, -1):
            print(f'desc: j={j}')
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                is_swapped = True

        for j in range(i):
            print(f'asc: j={j}')
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swapped = True
        
        if not is_swapped:
            return nums
        else:
            print(f'data={nums}')
 
num1 = input('Input comma separated numbers:\n').strip()
nums = [int(item) for item in num1.split(',')]
print(cocktail_shaker_sort(nums))
