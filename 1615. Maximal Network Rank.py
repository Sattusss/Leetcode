class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, len(graph[i]) + len(graph[j]) - (i in graph[j]))
        return res