1class Solution:
2    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
3        root_distance=0
4        N=0  
5        def dfsRoot(graph,curr,prev,curr_depth):
6            nonlocal root_distance
7            total_count=1
8            root_distance+=curr_depth
9            for child in graph[curr]:
10                if child==prev:
11                    continue
12                total_count+=dfsRoot(graph, child, curr, curr_depth+1) 
13            count[curr]=total_count
14            return total_count
15
16        def DFS(graph,curr,prev,res):
17            for child in graph[curr]:
18                if child==prev:
19                    continue
20                res[child]=res[curr]-count[child]+(N-count[child])
21                DFS(graph,child,curr,res)
22
23             
24        graph=defaultdict(list)
25        for v,u in edges:
26            graph[v].append(u)
27            graph[u].append(v)
28        print(graph)
29        N=n
30        count=[0]*n
31        dfsRoot(graph,0,-1,0)
32        res=[0]*n
33        res[0]=root_distance
34        DFS(graph,0,-1,res)
35        return res
36
37
38        