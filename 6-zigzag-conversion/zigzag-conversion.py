class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows >= len(s): return s
        step=1
        row=[""]*numRows
        cur=0
        for c in s:
            row[cur]+=c
            if cur==0:
                step=1
            elif cur == numRows-1:
                step=-1
            cur+=step
        return "".join(row)

        