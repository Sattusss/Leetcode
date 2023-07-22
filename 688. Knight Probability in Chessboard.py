class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1

        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for i in range(1, k + 1):
            for j in range(n):
                for l in range(n):
                    for dx, dy in moves:
                        x, y = j + dx, l + dy
                        if 0 <= x < n and 0 <= y < n:
                            dp[i][j][l] += dp[i - 1][x][y] / 8

        return sum(dp[k][j][l] for j in range(n) for l in range(n))
