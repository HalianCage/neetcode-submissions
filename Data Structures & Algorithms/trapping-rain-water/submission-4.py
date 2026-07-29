class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        prefix = [0]*n

        mx = height[0]

        for i in range(1, n):
            prefix[i] = mx
            mx = max(height[i], mx)

        suffix = [0]*n
        mx = height[-1]

        for i in range(n-2, -1, -1):
            suffix[i] = mx
            mx = max(mx, height[i])

        ar = 0
        
        for i in range(n):

            temp = min(prefix[i], suffix[i])-height[i]

            if temp < 0:
                continue
            ar += temp

        return ar


        