class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(path)
                path.pop()
        
        res = []
        dfs([])
        return res
