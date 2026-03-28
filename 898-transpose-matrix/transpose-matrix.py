class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nw=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(n):
            l=[]
            for j in range(m):
                l.append(matrix[j][i])
            nw.append(l)   
        return nw     


        