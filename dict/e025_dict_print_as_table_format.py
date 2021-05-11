# web solution
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print('dictionnaire trié')
print(sorted(my_dict.items()))
print('concaténation clé et valeur')
print(*([key] + value for key, value in sorted(my_dict.items())))
print('affichage en colonnes')
for row in zip(*([key] + value for key, value in sorted(my_dict.items()))):
    print(*row)
