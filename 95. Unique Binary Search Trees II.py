# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def dfs(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            res = []
            for i in range(start, end + 1):
                lefts = dfs(start, i - 1)
                rights = dfs(i + 1, end)
                for left in lefts:
                    for right in rights:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            
            memo[(start, end)] = res
            return res
        
        return dfs(1, n) if n else []
    