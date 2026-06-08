class Solution:
    def convertToBase7(self, num: int) -> str:
        if num ==0:
            return "0"
        l=[]
        t=True
        if num<0:
            t=False
            num=num*-1
        while num>0:
            l.append(str(num%7))
            num//=7
        if t==False:
            l.append("-")
        return "".join(l[::-1])
        