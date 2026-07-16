class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=0
        l=[]
        for n in nums:
            mx=max(mx,n)
            l.append(math.gcd(mx,n))
        l.sort()
        i=0
        j=len(l)-1
        s=0
        while i<j:
            if i==j:
                break
            s+=math.gcd(l[i],l[j])
            i+=1
            j-=1
        return s
        
        