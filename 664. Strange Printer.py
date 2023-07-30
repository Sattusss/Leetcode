class Solution:
    def strangePrinter(self, s: str) -> int:
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            if memo[i][j] > 0:
                return memo[i][j]
            res = dfs(i, j - 1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    res = min(res, dfs(i, k) + dfs(k + 1, j - 1))
            memo[i][j] = res
            return res

        memo = [[0] * len(s) for _ in range(len(s))]
        return dfs(0, len(s) - 1)
    