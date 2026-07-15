1class Solution:
2    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
3        def dfs(graph,curr,prev):
4            total_time=0
5            for c in graph[curr]:
6                if c==prev:
7                    continue
8                child_time=dfs(graph,c,curr)
9                if child_time>0 or hasApple[c]:
10                    total_time+=child_time+2
11            return total_time
12
13        graph=defaultdict(list)
14        for v,u in edges:
15            graph[v].append(u)
16            graph[u].append(v)
17        t=dfs(graph,0,-1)
18        return t
19