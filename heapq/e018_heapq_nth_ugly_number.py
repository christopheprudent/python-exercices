# https://www.geeksforgeeks.org/ugly-numbers/

# Function to get the nth ugly number
def getNthUglyNo(n):

	ugly = [0] * n # To store ugly numbers

	# 1 is the first ugly number
	ugly[0] = 1

	# i2, i3, i5 will indicate indices for
	# 2,3,5 respectively
	i2 = i3 = i5 = 0

	# Set initial multiple value
	next_multiple_of_2 = 2
	next_multiple_of_3 = 3
	next_multiple_of_5 = 5

	# Start loop to find value from
	# ugly[1] to ugly[n]
	for l in range(1, n):

		# Choose the min value of all available multiples
		ugly[l] = min(next_multiple_of_2,
					next_multiple_of_3,
					next_multiple_of_5)

		# Increment the value of index accordingly
		if ugly[l] == next_multiple_of_2:
			i2 += 1
			next_multiple_of_2 = ugly[i2] * 2

		if ugly[l] == next_multiple_of_3:
			i3 += 1
			next_multiple_of_3 = ugly[i3] * 3

		if ugly[l] == next_multiple_of_5:
			i5 += 1
			next_multiple_of_5 = ugly[i5] * 5

	# Return ugly[n] value
	return ugly[-1]

# web solution
import heapq
class Solution(object):      
    #:type n: integer
    #:return type: integer      
    def nth_Ugly_Number(self, n):
        ugly_num = 0
        heap = []
        heapq.heappush(heap, 1)
        for _ in range(n):
            print(" heapq", heap) 
            ugly_num = heapq.heappop(heap)
            if ugly_num % 2 == 0:
                heapq.heappush(heap, ugly_num * 2)
            elif ugly_num % 3 == 0:
                heapq.heappush(heap, ugly_num * 2)
                heapq.heappush(heap, ugly_num * 3)
            else:
                heapq.heappush(heap, ugly_num * 2)
                heapq.heappush(heap, ugly_num * 3)
                heapq.heappush(heap, ugly_num * 5)

        return ugly_num

# Driver Code
def main():

    S = Solution()
    n = 7
    print('{}-eme ugly-nombre est'.format(n))
    print(getNthUglyNo(n))
    result = S.nth_Ugly_Number(n)
    print(result)

    n = 10
    print('{}-eme ugly-nombre est:'.format(n))
    print(getNthUglyNo(n))
    result = S.nth_Ugly_Number(n)
    print(result)

if __name__ == '__main__':
	main()

# This code is contributed by Neelam Yadav
