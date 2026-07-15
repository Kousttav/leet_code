class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(graph,curr,prev):
            total_time=0
            for c in graph[curr]:
                if c==prev:
                    continue
                child_time=dfs(graph,c,curr)
                if child_time>0 or hasApple[c]:
                    total_time+=child_time+2
            return total_time

        graph=defaultdict(list)
        for v,u in edges:
            graph[v].append(u)
            graph[u].append(v)
        t=dfs(graph,0,-1)
        return t
