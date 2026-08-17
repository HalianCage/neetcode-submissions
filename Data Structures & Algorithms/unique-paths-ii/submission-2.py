class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        dp = [1] * n

        for i, row in enumerate(obstacleGrid):
            for j, ele in enumerate(row):

                if ele == 1:
                    dp[j] = 0
                    continue
                
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[j] = dp[j-1]
                    continue
                elif j == 0:
                    continue
                
                dp[j] += dp[j-1]

        return dp[-1]