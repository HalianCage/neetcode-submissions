class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxAr, l, r, dist = 0, 0, len(heights)-1, len(heights)-1

        while l < r:
            Ar = dist * min(heights[l], heights[r])
            maxAr = maxAr if maxAr > Ar else Ar

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            dist -= 1

        return maxAr
        