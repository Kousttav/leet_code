1class Solution:
2    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
3        setb=set()
4        ans=[]
5        suma=sum(aliceSizes)
6        sumb=0
7        for i in range(len(bobSizes)):
8            sumb+=bobSizes[i]
9            setb.add(bobSizes[i])
10        finalsum=(suma+sumb)/2
11        for c in range(len(aliceSizes)):
12            value=finalsum-suma+aliceSizes[c]
13            if value in setb:
14                ans.append(aliceSizes[c])
15                ans.append(value)
16                return ans
17        return ans