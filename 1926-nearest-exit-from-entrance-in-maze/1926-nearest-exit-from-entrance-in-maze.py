from queue import Queue
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r=len(maze)
        c=len(maze[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        q=Queue()
        q.put((entrance[0],entrance[1]))
        maze[entrance[0]][entrance[1]]="+"
        s=0
        while not q.empty():
            size=q.qsize()
            for _ in range(size):
                x,y=q.get()
                if (x, y) != tuple(entrance) and (
                    x == 0 or x == r-1 or y == 0 or y == c-1
                ):
                    return s
                for dx,dy in directions:
                    nx=x+dx
                    ny=y+dy
                    if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != "+":
                        q.put((nx,ny))
                        maze[nx][ny]="+"
            s+=1
        return -1

