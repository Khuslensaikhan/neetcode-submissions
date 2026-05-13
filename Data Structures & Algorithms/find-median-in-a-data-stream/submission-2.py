import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else: 
            heapq.heappush(self.large, num)
        
        #balancing
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) /2
        else: 
            if len(self.small) > len(self.large):
                return -self.small[0]
            else: 
                return self.large[0]
            
