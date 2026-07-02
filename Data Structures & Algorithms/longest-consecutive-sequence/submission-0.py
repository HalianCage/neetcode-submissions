class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        keyMap = set(nums)

        max_cnt = 0
        for i in nums:
            cnt = 1
            if i-1 in keyMap:
                continue
            
            n=i
            while n+1 in keyMap:
                cnt += 1
                n += 1

            max_cnt = cnt if cnt > max_cnt else max_cnt

        return max_cnt