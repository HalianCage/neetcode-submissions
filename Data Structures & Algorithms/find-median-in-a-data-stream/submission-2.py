class MedianFinder:
    def __init__(self):
        self.medianList = []
        

    def addNum(self, num: int) -> None:

        self.medianList.append(num)
        self.medianList.sort()
        
        
    def findMedian(self) -> float:

        length = len(self.medianList)

        if length%2 == 0:
            return (self.medianList[length//2] + self.medianList[(length//2)-1])/2
        else:
            return self.medianList[length//2]
        
        