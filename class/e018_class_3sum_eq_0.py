class sum3_eq_0_solution:
    def sum3_eq_0(self, among):
        sol = []
        for i, x in enumerate(among):
            j = i+1
            while j < len(among):
                k = j+1
                while k < len(among):
                    if x+among[j]+among[k] == 0:
                        sol.append((x, among[j], among[k]))
                    k += 1
                j += 1
        return sol

# web solution
class py_solution:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])

                    j, k = j + 1, k - 1
                    # optimisation
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            # optimisation
            # si même élément (que le précédent), on a déjà le résultat (le même!), on peut donc passer au suivant
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return result



L = [-25, -10, -7, -3, 2, 4, 8, 10]
print('liste', L)
print('éléments (x,y,z) tels que x+y+z == 0')
print(sum3_eq_0_solution().sum3_eq_0(L))
print(py_solution().threeSum(L))
