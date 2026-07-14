1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        n = len(rooms)
4        visited = [False] * n
5        visited[0] = True
6        stack = [0]
7        count = 1  # Number of rooms visited so far
8
9        while stack:
10            room = stack.pop()
11            for key in rooms[room]:
12                if not visited[key]:
13                    visited[key] = True
14                    count += 1
15                    stack.append(key)
16
17        return count == n