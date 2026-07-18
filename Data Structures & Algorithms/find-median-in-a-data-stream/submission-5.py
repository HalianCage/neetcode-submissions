class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        
        # push into the correct heap
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # rebalance
        if len(self.small) > len(self.large)+1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small)+1 < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:

        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
        
        