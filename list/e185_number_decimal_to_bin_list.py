def decimal_to_bin_list(n):
    return list(map(int, list(bin(n)[2:])))

# web solution
def decimal_to_binary_list(n):
    # {0:#b}'.format(8) -> '0b1000'
    result = [int(x) for x in list('{0:b}'.format(n))]
    return result

n = 8
print('nombre', n)
print('liste binaire', decimal_to_bin_list(n))
print('liste binaire', decimal_to_binary_list(n))

n = 45
print('nombre', n)
print('liste binaire', decimal_to_bin_list(n))
print('liste binaire', decimal_to_binary_list(n))

n = 100
print('nombre', n)
print('liste binaire', decimal_to_bin_list(n))
print('liste binaire', decimal_to_binary_list(n))
