class Solution():
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        l=""
        for i in range(n):
            for j in range(i,n):
                l1=s[i:j+1]
                if l1[::-1]==l1 and len(l1)>len(l):
                    l=l1
        return l
