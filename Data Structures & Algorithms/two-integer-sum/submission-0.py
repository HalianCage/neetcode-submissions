class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            
            num1 = nums[i]
            complement = target - num1
            if complement in seen:
                return [seen[complement], i]

            seen[num1] = i

        return False
        