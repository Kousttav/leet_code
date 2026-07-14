from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] = rooms[i]
        def dfs(rooms,source, visited): 
            visited[source]=True 
            for i in graph[source]: 
                if not visited[i]: 
                     dfs(rooms,i, visited)
        visited = [False]*len(rooms)
        dfs(rooms,0, visited)
        return False not in visited