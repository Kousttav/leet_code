1from collections import defaultdict
2
3class Solution:
4    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
5        graph = defaultdict(list)
6
7        for u, v in dislikes:
8            graph[u].append(v)
9            graph[v].append(u)
10
11        def dfs(source):
12            for nei in graph[source]:
13                if visited[nei] == -1:
14                    visited[nei] = 1 - visited[source]
15                    if not dfs(nei):
16                        return False
17                elif visited[nei] == visited[source]:
18                    return False
19            return True
20
21        visited = [-1] * (n + 1)
22
23        for i in range(1, n + 1):
24            if visited[i] == -1:
25                visited[i] = 0
26                if not dfs(i):
27                    return False
28
29        return True