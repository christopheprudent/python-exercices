#def divisors_parity(n):
#	_divs=[1]
#	k = n // 2
#	for i in range(2, k+1):
#		if n % i == 0:
#			_divs += [i]
#
#	_divs += [n]
#	return _divs
#
#n = int(input('Entrez un nombre entier positif : '))
#divs = divisors_parity(n)
#ndivs = len(divs)
#if ndivs % 2 == 0: parity='paire'
#else: parity='impaire'
#
#print('%d possède %d diviseurs(%s), soit de parité %s' %(n, ndivs, str(divs), parity)) 

# web solution
def divisor(n):
  print('n=%d %s' %(n, str([i for i in range(1,n+1) if not n % i])))
  x = len([i for i in range(1,n+1) if not n % i])
  return x

#  for i in range(n):
#    print('i=%d %s' %(i, str([i for i in range(1,n+1) if not n % i])))
#    x = len([i for i in range(1,n+1) if not n % i])
#  return x

print(divisor(15))
print(divisor(12))
print(divisor(9))
print(divisor(6))
print(divisor(3))

