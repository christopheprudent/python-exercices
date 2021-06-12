while True:
    s = input('entrez une ligne de texte: ').strip()
    if len(s) == 0:
        break

    if s == s[::-1]:
        print(' ce texte est un palindrome!')
