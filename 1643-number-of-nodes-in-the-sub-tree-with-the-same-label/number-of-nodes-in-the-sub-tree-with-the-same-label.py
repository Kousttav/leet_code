class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph=defaultdict(list)
        for v,u in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(graph,curr,prev,res,labels,count):
            lb=labels[curr]
            count_before_visiting_child=count[ord(lb)-ord('a')]
            count[ord(lb)-ord('a')]+=1
            for c in graph[curr]:
                if c==prev:
                    continue
                dfs(graph,c,curr,res,labels,count)
            count_after_visiting_child=count[ord(lb)-ord('a')]
            res[curr]=count_after_visiting_child-count_before_visiting_child

        res=[0]*n
        count=[0]*26
        dfs(graph,0,-1,res,labels,count)
        return res