1class Solution:
2    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
3        nw=[]
4        m=len(matrix)
5        n=len(matrix[0])
6        for i in range(n):
7            l=[]
8            for j in range(m):
9                l.append(matrix[j][i])
10            nw.append(l)   
11        return nw     
12
13
14        