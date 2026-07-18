class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # Step 1: add each ele to small
        # Step 2: check if max of small is smaller than min of large; if not not, pop max of small and push into large
        # Step 3: check if len of small is approximately equal to len of large, and vice versa; balance if not

        # Python implements min heap by default; There is not inbuilt max heap implementation, so we multiply by -1
        heapq.heappush(self.small, -num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large)+1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small)+1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        

    def findMedian(self) -> float:

        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
        
        