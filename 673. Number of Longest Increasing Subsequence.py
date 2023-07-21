from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
        max_len = max([x[0] for x in dp])
        return sum([x[1] for x in dp if x[0] == max_len])
    