class Solution:
    def findMin(self, nums: List[int]) -> int:

        for r in range(-1, -len(nums), -1):

            if nums[r-1] > nums[r]:
                return nums[r]

        return nums[0]