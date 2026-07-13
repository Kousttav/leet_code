1class Solution:
2    def removeStones(self, stones: List[List[int]]) -> int:
3        def dfs(stones, idx, visited):
4            visited[idx] = True
5
6            r = stones[idx][0]
7            c = stones[idx][1]
8
9            for i in range(len(stones)):
10                if not visited[i] and (stones[i][0] == r or stones[i][1] == c):
11                    dfs(stones, i, visited)
12
13        n = len(stones)
14        components = 0
15        visited = [False] * n
16
17        for i in range(n):
18            if visited[i]:
19                continue
20            dfs(stones, i, visited)
21            components += 1
22
23        return n - components