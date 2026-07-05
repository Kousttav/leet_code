1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1:
4            return s
5        
6        rows = [""] * numRows
7        curr_row = 0
8        step = 1 
9
10        for char in s:
11            rows[curr_row] += char
12
13            if curr_row == 0:
14                step = 1
15            elif curr_row == numRows -1:
16                step = -1
17            
18            curr_row += step
19        return "".join(rows)
20