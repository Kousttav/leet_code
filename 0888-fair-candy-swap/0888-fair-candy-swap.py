class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        setb=set()
        ans=[]
        suma=sum(aliceSizes)
        sumb=0
        for i in range(len(bobSizes)):
            sumb+=bobSizes[i]
            setb.add(bobSizes[i])
        finalsum=(suma+sumb)/2
        for c in range(len(aliceSizes)):
            value=finalsum-suma+aliceSizes[c]
            if value in setb:
                ans.append(aliceSizes[c])
                ans.append(value)
                return ans
        return ans