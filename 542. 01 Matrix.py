class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            i, j = q.popleft()
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                if x < 0 or x >= m or y < 0 or y >= n or mat[x][y] != -1:
                    continue
                mat[x][y] = mat[i][j] + 1
                q.append((x, y))
        return mat
        