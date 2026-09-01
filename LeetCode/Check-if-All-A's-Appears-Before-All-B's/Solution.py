1class Solution:
2    def checkString(self, s: str) -> bool:
3        p=len(s)
4        for i,wd in enumerate(s):
5            if wd=="b":
6                p=i
7                break
8        print(p)
9        st=s[p:]
10        return "a" not in st
11
12        