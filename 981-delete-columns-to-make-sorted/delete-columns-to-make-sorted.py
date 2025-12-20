class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l = []
        for idx in range(len(strs[0])):
            t = []
            for wd in strs: 
                t.append(wd[idx])
            l.append(t)
        c = 0
        for val in l:
            if val != sorted(val):
                c += 1
        return c
