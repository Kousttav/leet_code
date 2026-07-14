from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(source):
            for nei in graph[source]:
                if visited[nei] == -1:
                    visited[nei] = 1 - visited[source]
                    if not dfs(nei):
                        return False
                elif visited[nei] == visited[source]:
                    return False
            return True

        visited = [-1] * (n + 1)

        for i in range(1, n + 1):
            if visited[i] == -1:
                visited[i] = 0
                if not dfs(i):
                    return False

        return True