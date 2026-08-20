class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        N, M = len(grid[0]), len(grid)
        dp = [float('inf')] * N

        for r in range(0, M):
            for c in range(0, N):

                if r == 0:
                    dp[c] = grid[r][c]
                    if c != 0:
                        dp[c] += dp[c-1]
                    continue
                elif c == 0:
                    dp[c] += grid[r][c]
                    continue

                dp[c] = min(dp[c], dp[c-1]) + grid[r][c]

        return dp[-1]