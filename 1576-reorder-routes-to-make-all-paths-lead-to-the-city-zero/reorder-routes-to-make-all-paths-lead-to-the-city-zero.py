from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=defaultdict(list)
        for v,u in connections:
            graph[v].append((u,1))
            graph[u].append((v,0))
        count=0
        def dfs(node,prev):
            nonlocal count
            for v,c in graph[node]:
                if prev == v:
                    continue
                elif c == 1:
                    count+=1
                dfs(v,node)
        dfs(0,-1)
        return count
                


        