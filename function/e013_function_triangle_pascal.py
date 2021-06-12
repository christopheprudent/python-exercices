def get_triangle_pascal(n):
    _pascal = [[1] * i for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            _pascal[i][j] = _pascal[i-1][j-1] + _pascal[i-1][j]

    return _pascal

# web solution
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return

print('triangle de Pascal')
while True:
    n = int(input('entrez le nombre de lignes désiré : '))
    if n == 0:
        break

    print(get_triangle_pascal(n))
    print()
    pascal_triangle(n)
