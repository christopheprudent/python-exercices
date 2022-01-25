def sum_of_first_numbers(n):
    return (n*(n+1))/2

# https://www.math-only-math.com/sum-of-the-squares-of-first-n-natural-numbers.html
def sum_of_squares_of_first_numbers(n):
    return (n*(n+1)*(2*n+1))/6

if __name__ == '__main__':
    s1 = sum_of_first_numbers(12)
    print('dev) somme des premiers nombres, n=', 12, 'égale à', s1)
    s2 = sum_of_squares_of_first_numbers(12)
    print('dev) somme des carrés des premiers nombres, n=', 12, 'égale à', s2)

