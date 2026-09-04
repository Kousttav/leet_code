1class Solution:
2    def minChanges(self, s: str) -> int:
3        c=0
4        for i in range(1,len(s),2):
5            print(s[i-1:i+1])
6            if s[i-1:i+1].count('1')==1:
7                c+=1
8        return c
9        