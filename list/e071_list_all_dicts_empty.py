def all_dicts_empty(ld):
    return all(len(d) == 0 for d in ld)

ld1 = [{},{},{}]
print(all_dicts_empty(ld1))
ld2 =  [{1,2},{},{}]
print(all_dicts_empty(ld2))

# web solution
print(all(not d for d in ld1))
print(all(not d for d in ld2))
