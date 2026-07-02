class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        output = [0]*length
        prefix = suffix = 1

        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(-1, -(length+1), -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
        