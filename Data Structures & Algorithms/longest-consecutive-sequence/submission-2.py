class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        keyMap = set(nums)
        max_cnt = 0

        for i in keyMap:

            if i-1 in keyMap:
                continue

            cnt = 1
            while i+cnt in keyMap:
                cnt += 1

            max_cnt = max_cnt if max_cnt > cnt else cnt

        return max_cnt