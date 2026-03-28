1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        def is_palindrome(i, j):
4            while i < j:
5                if s[i] != s[j]:
6                    return False
7                i += 1
8                j -= 1
9            return True
10
11        l, r = 0, len(s) - 1
12        while l < r:
13            if s[l] != s[r]:
14                rtn=is_palindrome(l +1, r) or is_palindrome(l,r-1)
15                return rtn
16            l+= 1
17            r-= 1
18        return True
19                    