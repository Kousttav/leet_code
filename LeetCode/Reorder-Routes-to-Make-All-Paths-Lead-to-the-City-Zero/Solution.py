1from collections import defaultdict
2class Solution:
3    def minReorder(self, n: int, connections: List[List[int]]) -> int:
4        graph=defaultdict(list)
5        for v,u in connections:
6            graph[v].append((u,1))
7            graph[u].append((v,0))
8        count=0
9        visited=[False]*(n+1)
10        def dfs(node,prev):
11            nonlocal count
12            for v,c in graph[node]:
13                if prev == v:
14                    continue
15                elif c == 1:
16                    count+=1
17                dfs(v,node)
18        
19        dfs(0,-1)
20        return count
21                
22
23
24        