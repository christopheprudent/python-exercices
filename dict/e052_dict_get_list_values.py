D = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
print('dictionnaire', D)
print('liste de valeurs correspondant à la clé {}'.format('Science'))
print([d['Science'] for d in D])
print('liste de valeurs correspondant à la clé {}'.format('Math'))
print([d['Math'] for d in D])
