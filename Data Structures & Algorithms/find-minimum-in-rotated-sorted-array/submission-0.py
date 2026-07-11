class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minEle = nums[0]

        for ele in nums:
            minEle = min(minEle, ele)

        return minEle