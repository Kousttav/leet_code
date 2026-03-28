class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return max(d,key=d.get)
        