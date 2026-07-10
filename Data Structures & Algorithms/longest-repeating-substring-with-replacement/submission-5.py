class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charMap = defaultdict(int)
        l, maxCnt = 0, 0

        for r in range(len(s)):

            charMap[s[r]] += 1

            while (r-l+1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1

            maxCnt = max(maxCnt, r-l+1)

        return maxCnt