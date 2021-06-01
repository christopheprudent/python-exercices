# web solution
import heapq

class Median_Finder:
    
    def __init__(self):
        #initialize data structure
        self.max_heap = []
        self.min_heap = []
        

    def add_Number(self, num):
        #type num: int, rtype: void
        print('\najout:', num)
        if not self.max_heap and not self.min_heap:
            print(' min,max empty')
            heapq.heappush(self.min_heap, num)
            print(' min', self.min_heap)
            return 
        if not self.max_heap:
            print(' max empty')
            if num > self.min_heap[0]:
                print(f' num={num} >  min(0)={self.min_heap[0]}', self.min_heap)
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
                print(' min', self.min_heap)
            else:
                print(f' num={num} <= min(0)={self.min_heap[0]}', self.min_heap)
                heapq.heappush(self.max_heap, -num)
            print(' max', self.max_heap)
            return
        if len(self.max_heap) == len(self.min_heap):
            print(' len(min) == len(max)')
            if num < -self.max_heap[0]:
                print(f' num={num} <  -max(0)={-self.max_heap[0]}', self.max_heap)
                heapq.heappush(self.max_heap, -num)
                print(' max', self.max_heap)
            else:
                print(f' num={num} >= -max(0)={-self.max_heap[0]}', self.max_heap)
                heapq.heappush(self.min_heap, num)
                print(' min', self.min_heap)
        elif len(self.max_heap) > len(self.min_heap):
            print(' len(min) <= len(max)')
            if num < -self.max_heap[0]:
                print(f' num={num} <  -max(0)={-self.max_heap[0]}', self.max_heap)
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
                print(' max', self.max_heap)
            else:
                print(f' num={num} >= -max(0)={-self.max_heap[0]}', self.max_heap)
                heapq.heappush(self.min_heap, num)
            print(' min', self.min_heap)
        else:
            print(' len(min) >  len(max)')
            if num > self.min_heap[0]:
                print(f' num={num} >  min(0)={self.min_heap[0]}', self.min_heap)
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
                print(' min', self.min_heap)
            else:
                print(f' num={num} <= min(0)={self.min_heap[0]}', self.min_heap)
                heapq.heappush(self.max_heap, -num)
            print(' max', self.max_heap)
        

    def find_Median(self):
        #rtype: float
        print('calcul médiane')
        if len(self.max_heap) == len(self.min_heap):
            print(' len(min) == len(max): (-max(0)+min(0)) /2')
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            print(' len(min) <= len(max): -max(0)')
            return -self.max_heap[0]
        else:
            print(' len(min) >  len(max): min(0)')
            return self.min_heap[0] 

S = Median_Finder()
S.add_Number(1)
S.add_Number(2)
result = S.find_Median()
print(result)
S.add_Number(3)
result = S.find_Median()
print(result)
S.add_Number(4)
S.add_Number(5)
result = S.find_Median()
print(result)

S.add_Number(-4)
result = S.find_Median()
print(result)
