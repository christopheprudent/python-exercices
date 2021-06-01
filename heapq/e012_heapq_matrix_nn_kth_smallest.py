import heapq
import pprint

M = [
    [0, 2, 4]
  , [1, 2, 5]
  , [7, 8, 9]
]

print('matrice')
pprint.pprint(M)

H = heapq.merge(*M)
k = 3
kmin = heapq.nsmallest(k, list(H))
print('{}-eme élément le plus petit est {}'.format(k, kmin[-1]))

# web solution
class Solution():
    def find_Kth_Smallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        temp = [[False] * n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        temp[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            print(f'(ans,i,j)=({ans},{i},{j})')
            if i + 1 < m and not temp[i + 1][j]:
                temp[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not temp[i][j + 1]:
                temp[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans

s = Solution()
result = s.find_Kth_Smallest(M, k)
print('{}-eme élément le plus petit est {}'.format(k, result))
