class MedianFinder:

    #maxHeap? 
    #we neeed array, heapsize, i 
    def __init__(self):
        #initializes median finder object
        self.data = []

    def addNum(self, num: int) -> None:
        #adds integer num from the data stream to the data structure
        self.data.append(num)
    def findMedian(self) -> float:
        #returns the median of all elements so far.
        #returns double
        self.data.sort()
        n = len(self.data)
        return (self.data[n // 2] if (n & 1) else
                (self.data[n // 2] + self.data[n // 2 - 1]) / 2)
