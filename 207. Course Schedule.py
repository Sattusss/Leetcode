class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0: unvisited, 1: visited, 2: safe
        visited = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
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
        return all(dfs(i) for i in range(numCourses))
    