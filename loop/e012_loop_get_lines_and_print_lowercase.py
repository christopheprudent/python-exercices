text = []
while True:
    s = input('entrez une ligne de texte : ')
    if len(s) == 0:
        break

    text.append(s.lower())

print('voici le texte que vous venez de saisir, en minuscules')
for s in text:
    print(s)
