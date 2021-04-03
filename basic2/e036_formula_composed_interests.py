#c0 = 100000
#nmonthes = int(input('nombre de mois: '))
#i = float(input('taux intérêt (%) : '))
#if i>1:
#	i /= 100
#
#def nearest_1000(n):
#	_div = n // 1000
#	_mod = n % 1000
#	_add = 0
#	if _mod > 0:
#		_add = 1
#
#	return (_div+_add)*1000
#
#c = nearest_1000(c0 * (1+i))
#for m in range(1, nmonthes):
#	c = nearest_1000(c * (1+i))
#
#print('au final des %d mois, la dette sera de : %d' %(nmonthes, c))

# web solution
def round_n(n):
    if n%1000:
        return (1+n//1000)*1000
    else:
        return n
     
def compute_debt(n):
    if n==0: return 100000
    return int(round_n(compute_debt(n-1)*1.05))

print("Input number of months:")
result = compute_debt(int(input()))
print("Amount of debt: ","$"+str(result).strip())

