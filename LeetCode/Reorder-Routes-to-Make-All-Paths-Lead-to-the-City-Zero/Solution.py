1from collections import defaultdict
2class Solution:
3    def minReorder(self, n: int, connections: List[List[int]]) -> int:
4        graph=defaultdict(list)
5        for v,u in connections:
6            graph[v].append((u,1))
7            graph[u].append((v,0))
8        count=0
9        def dfs(node,prev):
10            nonlocal count
11            for v,c in graph[node]:
12                if prev == v:
13                    continue
14                elif c == 1:
15                    count+=1
16                dfs(v,node)
17        dfs(0,-1)
18        return count
19                
20
21
22        