class Solution:
    def countEven(self, num: int) -> int:
        c=0
        def check(n):
            n=str(n)
            s=0
            for i in n:
                s+=int(i)
            return s
        for i in range(1,num+1):
            if check(i)%2==0:
                c+=1
        return c

            

        