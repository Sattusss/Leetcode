from typing import List
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # return true if x and y are in the same set
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return False
        if self.size[rootx] < self.size[rooty]:
            rootx, rooty = rooty, rootx
        self.parent[rooty] = rootx
        self.size[rootx] += self.size[rooty]
        self.count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Kruskal's algorithm
        # Time complexity: O(ElogE + ElogV)
        # Space complexity: O(E)
        def kruskal(mst, skip, start, end):
            uf = UnionFind(n)
            if start != -1:
                uf.union(edges[start][0], edges[start][1])
                mst += edges[start][2]
            for i in range(len(edges)):
                if i == skip or i == start:
                    continue
                if uf.union(edges[i][0], edges[i][1]):
                    mst += edges[i][2]
            return mst if uf.count == 1 else float('inf')
        
        # sort edges by weight
        edges = sorted([[u, v, w, i] for i, (u, v, w) in enumerate(edges)], key=lambda x: x[2])
        mst = kruskal(0, -1, -1, -1)
        ans = [[], []]
        for i in range(len(edges)):
            if kruskal(0, i, -1, -1) > mst:
                ans[0].append(edges[i][3])
            elif kruskal(0, -1, i, -1) == mst:
                ans[1].append(edges[i][3])
        return ans