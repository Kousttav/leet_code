1class Solution:
2    def reverseWords(self, s: str) -> str:
3        s=s.split()
4        l=""
5        for i in range(len(s)-1,-1,-1):
6            l+=s[i]+" "
7        return l.strip()
8        