1from collections import defaultdict
2class Solution:
3    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
4        graph = defaultdict(list)
5        for i in range(len(rooms)):
6            graph[i] = rooms[i]
7        def dfs(rooms,source, visited): 
8            visited[source]=True 
9            for i in graph[source]: 
10                if not visited[i]: 
11                     dfs(rooms,i, visited)
12        visited = [False]*len(rooms)
13        dfs(rooms,0, visited)
14        return False not in visited