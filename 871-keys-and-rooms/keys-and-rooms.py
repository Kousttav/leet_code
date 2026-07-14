class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stack = [0]
        count = 1  # Number of rooms visited so far

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    count += 1
                    stack.append(key)

        return count == n