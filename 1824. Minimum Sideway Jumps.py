class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]
        for i in range(1, len(obstacles)):
            if obstacles[i] != 0:
                dp[obstacles[i] - 1] = float('inf')
            for j in range(3):
                if j != obstacles[i] - 1:
                    dp[j] = min(dp[j], dp[(j + 1) % 3] + 1, dp[(j + 2) % 3] + 1)
        return min(dp)