class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 0: unvisited, 1: visited, 2: safe
        visited = [0] * len(graph)
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 2
            return True
        return [i for i in range(len(graph)) if dfs(i)]