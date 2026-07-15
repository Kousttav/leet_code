1class Solution:
2    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
3        res=[]
4        def dfs(s,path):
5            if s == len(graph)-1:
6                res.append(path[:])
7                return
8            for i in graph[s]:
9                path.append(i)
10                dfs(i,path)
11                path.pop()
12            
13
14        dfs(0,[0])
15        return res
16
17        