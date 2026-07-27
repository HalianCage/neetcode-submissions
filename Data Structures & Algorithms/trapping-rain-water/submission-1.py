class Solution:
    def trap(self, height: List[int]) -> int:

        # builing prefix array
        prefix = []
        maxi = 0

        for n in height:
            prefix.append(maxi)
            maxi = maxi if maxi > n else n

        # building suffix array
        rev = height.copy()
        rev.reverse()
        suffix = []
        maxi = 0
        for n in rev:
            suffix.append(maxi)
            maxi = maxi if maxi > n else n

        suffix.reverse()

        ar = 0

        for i in range(0, len(height)):
            temp = min(prefix[i], suffix[i]) - height[i]

            if temp > 0:
                ar += temp

        return ar



        