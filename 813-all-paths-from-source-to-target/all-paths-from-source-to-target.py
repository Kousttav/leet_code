class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        def dfs(s,path):
            if s == len(graph)-1:
                res.append(path[:])
                return
            for i in graph[s]:
                path.append(i)
                dfs(i,path)
                path.pop()
            

        dfs(0,[0])
        return res

        