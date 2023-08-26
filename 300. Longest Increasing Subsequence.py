class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = max(dp[j]) + 1, j < i and nums[j] < nums[i]
        # dp[i] = 1 if no such j exists
        # O(n^2) time, O(n) space
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            max_len = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, dp[j])
            dp[i] = max_len + 1
        return max(dp)