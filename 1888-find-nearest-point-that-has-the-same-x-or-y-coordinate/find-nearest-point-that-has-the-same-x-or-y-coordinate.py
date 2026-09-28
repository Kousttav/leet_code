class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        d=[]
        for a,b in points:
            if a==x or b==y:
                d.append(abs(a - x) + abs(b - y))
            else:
                d.append(float('inf'))
        
        i=min(d)
        if i == float('inf'):
            return -1
        print(i)
        for j in range(len(d)):
            if d[j]==i:
                return j
                
        