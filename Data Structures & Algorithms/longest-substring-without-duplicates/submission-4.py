class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxCnt, l = 0, 0
        memSet = set()

        for r in range(len(s)):
            while s[r] in memSet:
                memSet.remove(s[l])
                l += 1
            
            memSet.add(s[r])
            maxCnt = max(maxCnt, r-l+1)

        return maxCnt

            
        