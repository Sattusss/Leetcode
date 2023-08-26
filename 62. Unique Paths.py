class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # O(mn) time, O(mn) space
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(m)[1:]:
            for j in range(n)[1:]:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]