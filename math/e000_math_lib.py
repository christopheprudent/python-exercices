# https://www.123calculus.com/en/number-divisors-page-1-11-110.html
def divisors (n):
	divisors_list = []
	i=1
	while (i <= n**0.5):
		if (n%i==0):
			divisors_list.append(i)
			divisors_list.append(n//i)
		i=i+1

	divisors_list.sort()
	return(divisors_list)

def proper_divisors(n):
    return divisors(n)[:-1]


