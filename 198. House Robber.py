from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev = 0
        curr = nums[0]

        for num in nums[1:]:
            prev, curr = curr, max(prev + num, curr)

        return curr