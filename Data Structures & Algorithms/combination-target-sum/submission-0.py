class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        res = []

        tempArr = []

        def fun(idx, target):

            while idx < len(nums):
                tempArr.append(nums[idx])
                cplmt = target - nums[idx]

                if cplmt == 0:
                    res.append(tempArr.copy())

                elif cplmt >= nums[idx]:
                    fun(idx, cplmt)
                
                tempArr.pop()
                idx += 1

        fun(0, target)
        return res