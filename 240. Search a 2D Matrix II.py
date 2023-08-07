class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if i<0 or j<0:return 0
            if matrix[i][j] == target:return 1
            if matrix[i][j] < target:return 0
            return dp(i-1, j) + dp(i, j-1)
        return dp(len(matrix)-1, len(matrix[0])-1)
    