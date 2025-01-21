class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=0
        t=x
        while x>0:
            r=x%10
            s=s*10+r
            x=x//10
        return s == t
x=121
sol=Solution()
print(sol.isPalindrome(x))
