class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]=d1[i]+1
        print(d1)
        for j in t:
            if j not in d2:
                d2[j]=1
            else:
                d2[j]=d2[j]+1
        print(d2)
        if len(s)>len(t):
            l=d1
            m=d2
        else:
            l=d2
            m=d1
        s=""
        for i in l.keys():
            if i in m.keys() and abs(l[i]-m[i])>0:
                s+=i*abs(l[i]-m[i])
            elif i not in m.keys():
                s+=i*l[i] 
        return s

        