class Solution:
    def maxDepth(self, s: str) -> int:
        mx=0
        c=0
        for i in s:
            if i == "(":
                c+=1

            if i==")":
                c-=1
            mx=max(mx,c)
        return mx