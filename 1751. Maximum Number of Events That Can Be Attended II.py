from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        dp = [[0] * (k + 1) for _ in range(len(events) + 1)]

        for i in range(1, len(events) + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]
                for l in range(i):
                    if events[l][1] < events[i - 1][0]:
                        dp[i][j] = max(dp[i][j], dp[l][j - 1] + events[i - 1][2])

        return dp[-1][-1]
    