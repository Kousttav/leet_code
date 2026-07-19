from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, c in roads:
            graph[u].append((v, c))
            graph[v].append((u, c))

        visited = [False] * (n + 1)
        res = float('inf')

        def dfs(s):
            nonlocal res
            visited[s] = True

            for v, d in graph[s]:
                res = min(res, d)
                if not visited[v]:
                    dfs(v)

        dfs(1)
        return res