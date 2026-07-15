1class Solution:
2    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
3        graph=defaultdict(list)
4        for v,u in edges:
5            graph[u].append(v)
6            graph[v].append(u)
7
8        def dfs(graph,curr,prev,res,labels,count):
9            lb=labels[curr]
10            count_before_visiting_child=count[ord(lb)-ord('a')]
11            count[ord(lb)-ord('a')]+=1
12            for c in graph[curr]:
13                if c==prev:
14                    continue
15                dfs(graph,c,curr,res,labels,count)
16            count_after_visiting_child=count[ord(lb)-ord('a')]
17            res[curr]=count_after_visiting_child-count_before_visiting_child
18
19        res=[0]*n
20        count=[0]*26
21        dfs(graph,0,-1,res,labels,count)
22        return res