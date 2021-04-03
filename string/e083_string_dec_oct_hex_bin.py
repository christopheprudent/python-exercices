i = int(input('Entrez un nombre entier : '))
print('i= {0:d} {0:o} {0:x} {0:b}'.format(i))

# web solution
o = str(oct(i))[2:]
h = str(hex(i))[2:]
h = h.upper()
b = str(bin(i))[2:]
d = str(i)
print("Decimal Octal Hexadecimal (capitalized), Binary")
print(d,' '*(7-len(d)-1),o,' '*(5-len(o)-1),h,' '*(26-len(h)-1),b)
