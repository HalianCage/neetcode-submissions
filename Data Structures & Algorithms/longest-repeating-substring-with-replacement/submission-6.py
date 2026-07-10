class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charMap = defaultdict(int)
        l, maxCnt = 0, 0
        maxf = 0

        for r in range(len(s)):

            charMap[s[r]] += 1
            maxf = max(maxf, charMap[s[r]])

            while (r-l+1) - maxf > k:
                charMap[s[l]] -= 1
                l += 1

            maxCnt = max(maxCnt, r-l+1)

        return maxCnt