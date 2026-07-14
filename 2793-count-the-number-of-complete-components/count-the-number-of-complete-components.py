from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(idx, source):
            visited[source] = idx
            for nei in graph[source]:
                if visited[nei] == 0:
                    dfs(idx, nei)

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [0] * n

        comp = 1

        for i in range(n):
            if visited[i] == 0:
                dfs(comp, i)
                comp += 1
        ans = 0
        for c in range(1, comp):
            nodes = []
            for i in range(n):
                if visited[i] == c:
                    nodes.append(i)

            k = len(nodes)
            edge = 0
            for node in nodes:
                edge += len(graph[node])

            edge //= 2

            if edge == k * (k - 1) // 2:
                ans += 1

        return ans