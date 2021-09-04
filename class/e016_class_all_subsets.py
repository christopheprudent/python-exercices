# web solution

class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))

# itérations
# ([] [4,5,6])
# ([] [5,6] + [4] [5,6])
# ([] [6] + [5] [6]) + ([4] [6] + [4, 5] [6])
# ([] [] + [6] []) + ([5] [] + [5, 6] []) + ([4] [] + [4, 6] []) + ([4, 5] [] + [4, 5, 6][])
#
# soit: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
