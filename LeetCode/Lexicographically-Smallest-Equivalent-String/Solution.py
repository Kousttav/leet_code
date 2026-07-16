1from collections import defaultdict
2
3class Solution:
4    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
5        graph = defaultdict(list)
6
7        for a, b in zip(s1, s2):
8            graph[a].append(b)
9            graph[b].append(a)
10
11        visited_global = {}
12        
13        def dfs(node, visited):
14            smallest = node
15            visited.add(node)
16
17            for nei in graph[node]:
18                if nei not in visited:
19                    smallest = min(smallest, dfs(nei, visited))
20            return smallest
21
22        # Precompute smallest for each char
23        for ch in set(s1 + s2):
24            if ch not in visited_global:
25                visited = set()
26                smallest = dfs(ch, visited)
27                for v in visited:
28                    visited_global[v] = smallest
29
30        # Build result
31        res = ""
32        for ch in baseStr:
33            res += visited_global.get(ch, ch)
34
35        return res