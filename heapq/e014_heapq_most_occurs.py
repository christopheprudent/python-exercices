# web solution
import heapq
from collections import Counter
class Solution:
    def top_K_Frequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :return type: List[str]
        """
        ctr = Counter(words)
        print(ctr)
        heap = [(-ctr[word], word) for word in ctr]
        heapq.heapify(heap)
        print(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

    def top_K_occurs(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :return type: List[str]
        """
        ctr = Counter(words)
        print(ctr)
        heap = [(ctr[word], word) for word in ctr]
        heapq.heapify(heap)
        print(heap)
        return heapq.nlargest(k, heap)

if __name__ == '__main__':
    words = ["a", "abc", "abcdef", "a", "abcd", "abcd", "abc", "abcdefg"]
    k = 3
    s = Solution()
    print("3 most frequent elements:")
    print(s.top_K_Frequent(words, k))
    print([x[1] for x in s.top_K_occurs(words, k)])
