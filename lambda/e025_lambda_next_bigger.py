# web solution
def rearrange_bigger(n):
    global DEBUG
    #Break the number into digits and store in a list
    nums = list(str(n))
    if DEBUG:
        print(f'nums={nums}')
    for i in range(len(nums)-2, -1, -1):
        if DEBUG:
            print(f'i={i} [{i}]={nums[i]} [{i+1}]={nums[i+1]}')
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0],  z))
            if DEBUG:
                print(f'z=nums[{i}:]={z} y=min(x,x>{z[0]})={y}')
            z.remove(y)
            if DEBUG:
                print(f'après effacement y : z={z}')
            z.sort()
            if DEBUG:
                print(f'après tri : z={z}')
            nums[i:] = [y] + z
            if DEBUG:
                print(f'nums[{i}:]={nums[i:]}')
            return int("".join(nums))
    return False

DEBUG=False
n = 12
print("Nombre:", n)
print("Prochain nombre supérieur:", rearrange_bigger(n))

n = 10
print("\nNombre:", n)
print("Prochain nombre supérieur:", rearrange_bigger(n))
      
n = 201
print("\nNombre:", n)
print("Prochain nombre supérieur:", rearrange_bigger(n))

n = 102
print("\nNombre:", n)
print("Prochain nombre supérieur:", rearrange_bigger(n))

n = 445
print("\nNombre:", n)
print("Prochain nombre supérieur:", rearrange_bigger(n))

n = 10010
print("\nNombre:", n)
print("Prochain nombre supérieur:", rearrange_bigger(n))

DEBUG=True
n = 13410
print("\nNombre:", n)
print("Prochain nombre supérieur:", rearrange_bigger(n))
