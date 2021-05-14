D = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
print('dictionnaire', D)
print('longueur totale des chaînes')
print(sum(len(x) for x in D.values() if isinstance(x, str)))
