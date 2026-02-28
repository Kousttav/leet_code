class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=["Gold Medal","Silver Medal","Bronze Medal"]
        n=len(score)
        if (n>len(l)):
            for i in range(4,n+1):
                l.append(str(i))
        elif(n<len(l)):
            l=l[:n]
        s=sorted(score,reverse=True)
        d={}
        for w in range(len(s)):
            d[s[w]]=l[w]
        print(d)
        res=[]
        for j in score:
            res.append(d[j])
        return res

        
        