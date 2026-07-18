class MedianFinder:
    medianList = []
    def __init__(self):
        self.medianList = []
        

    def addNum(self, num: int) -> None:

        self.medianList.append(num)
        
        
    def findMedian(self) -> float:

        length = len(self.medianList)
        self.medianList.sort()

        if length%2 == 0:
            return (self.medianList[length//2] + self.medianList[(length//2)-1])/2
        else:
            return self.medianList[length//2]
        
        