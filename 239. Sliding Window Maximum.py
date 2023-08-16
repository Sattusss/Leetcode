class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        if not nums:
            return []
        res = []
        queue = collections.deque()
        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
            if i - queue[0] == k - 1:
                queue.popleft()
        return res