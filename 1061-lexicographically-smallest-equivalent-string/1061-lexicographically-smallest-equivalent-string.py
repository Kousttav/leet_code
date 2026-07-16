from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(list)

        for a, b in zip(s1, s2):
            graph[a].append(b)
            graph[b].append(a)

        visited_global = {}
        
        def dfs(node, visited):
            smallest = node
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    smallest = min(smallest, dfs(nei, visited))
            return smallest

        # Precompute smallest for each char
        for ch in set(s1 + s2):
            if ch not in visited_global:
                visited = set()
                smallest = dfs(ch, visited)
                for v in visited:
                    visited_global[v] = smallest

        # Build result
        res = ""
        for ch in baseStr:
            res += visited_global.get(ch, ch)

        return res