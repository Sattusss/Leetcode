class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        def longestSubarrayWithKOnes(k: int) -> int:
            left = 0
            right = 0
            maxLen = 0
            while right < len(nums):
                if nums[right] == 0:
                    k -= 1
                while k < 0:
                    if nums[left] == 0:
                        k += 1
                    left += 1
                maxLen = max(maxLen, right - left)
                right += 1
            return maxLen

        return longestSubarrayWithKOnes(1)