class Solution:
    def minChanges(self, s: str) -> int:
        c=0
        for i in range(1,len(s),2):
            print(s[i-1:i+1])
            if s[i-1:i+1].count('1')==1:
                c+=1
        return c
        