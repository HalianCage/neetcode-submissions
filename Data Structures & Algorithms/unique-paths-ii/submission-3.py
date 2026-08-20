class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (M+1)
        dp[M-1] = 1

        for r in range(N-1, -1, -1):
            for c in range(M-1, -1, -1):

                if obstacleGrid[r][c]:
                    dp[c] = 0
                else:
                    dp[c] += dp[c+1]

        return dp[0]
        