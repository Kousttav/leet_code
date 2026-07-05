1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows==1: return s
4        step=1
5        row=[""]*numRows
6        cur=0
7        for c in s:
8            row[cur]+=c
9            if cur==0:
10                step=1
11            elif cur == numRows-1:
12                step=-1
13            cur+=step
14        return "".join(row)
15
16        