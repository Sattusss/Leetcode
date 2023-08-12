class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0]*len(obstacleGrid[0])
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(len(row)):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]