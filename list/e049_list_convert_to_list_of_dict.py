def convert_to_list_of_dict(l1, l2):
    ld = []
    for i in range(len(l1)):
        d = dict()
        d['color_name'] = l1[i] 
        d['color_code'] = l2[i] 
        ld.append(d)

    return ld

cn = ["Black", "Red", "Maroon", "Yellow"]
cc = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print('listes {} {}'.format(cn, cc))
print(convert_to_list_of_dict(cn, cc))

# web solution
print([{'color_name': n, 'color_code': c} for n, c in zip(cn, cc)])
