class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        one=s.count('1')
        l=[]
        n=len(s)
        i=0
        while i<n:
            if s[i]=="0":
                start=i
                while(i<n and s[i]=='0'):
                    i+=1
                l.append(i-start)
            else:
                i+=1
        print(l)
        mx=0
        for i in range(1,len(l)):
            mx=max(mx,l[i]+l[i-1])
        return mx+one

        