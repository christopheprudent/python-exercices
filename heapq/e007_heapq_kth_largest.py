import heapq

L = [18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1]
print('liste', L)
heapq.heapify(L)
print('déterminer le k-eme élément le plus grand')

while True:
    k  = int(input('entrez k (ctrl-c pour arrêter) : '))
    ll = heapq.nlargest(k, L)
    print('le {}-eme élément le plus grand est : {}'.format(k, ll[-1]))

# web solution
