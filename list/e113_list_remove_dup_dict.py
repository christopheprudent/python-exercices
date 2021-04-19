def remove_dup_dict(ld):
    uniq_ld = []
    for d in ld:
        if d not in uniq_ld:
            uniq_ld.append(d)

    return uniq_ld

# web solution (w/ set which keep uniqs)
# {tuple(d.items()) for d in L} removes double items
def remove_duplicate_dictionary(list_color):
    result = [dict(e) for e in {tuple(d.items()) for d in list_color}]
    return result

LD = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
print('liste de dict', LD)
print('sans doublon:', remove_dup_dict(LD))
print('sans doublon:', remove_duplicate_dictionary(LD))
