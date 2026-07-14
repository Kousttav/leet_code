class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        l=[]
        while n>0:
            r=n%10
            if r!=0:
                l.append(r)
                s+=r
            n=n//10
        num=0
        for _ in range(len(l)):
            num=num*10+l.pop()
        return num*s
        