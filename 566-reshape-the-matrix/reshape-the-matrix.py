class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        f=[]
        for row in mat:
            for num in row:
                f.append(num)                
        if r * c != len(f): 
            return mat
        else:
            new_mat = []
            idx = 0
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(f[idx])
                    idx += 1
                new_mat.append(row)
        return new_mat

        