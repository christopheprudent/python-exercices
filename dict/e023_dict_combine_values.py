# web solution
from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print('liste de dictionnaires', item_list)
result = Counter()
for d in item_list:
    # Counter retourne 0 si la clé n'existe pas déjà
    result[d['item']] += d['amount']
print('combinaisons des mêmes éléments (clé) en additionnant leur montant comme valeur')
print(result) 

