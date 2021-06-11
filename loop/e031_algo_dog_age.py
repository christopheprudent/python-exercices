human_age = int(input('Entrez l\'âge de votre chien (en année) : '))

dog_age = min(human_age, 2) * 10.5 + max(human_age -2, 0) * 4
print('votre chien a en réalité {} année(s)'.format(dog_age))
