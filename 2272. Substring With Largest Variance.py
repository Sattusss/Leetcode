class Solution:
    def largestVariance(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                res = max(res, self.variance(s[i:j + 1]))
        return res