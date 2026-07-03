1class Solution():
2    def longestPalindrome(self, s: str) -> int:
3        n=len(s)
4        l=""
5        for i in range(n):
6            for j in range(i,n):
7                l1=s[i:j+1]
8                if l1[::-1]==l1 and len(l1)>len(l):
9                    l=l1
10        return l