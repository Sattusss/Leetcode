class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        dp = {}
        for i in stones:
            dp[i] = set()
        dp[1].add(1)
        for i in range(1, len(stones)):
            for j in dp[stones[i]]:
                for k in range(j-1, j+2):
                    if k > 0 and stones[i]+k in dp:
                        dp[stones[i]+k].add(k)
        return len(dp[stones[-1]]) > 0