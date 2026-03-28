class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for i,j in enumerate(nums):
            d[j].append(i)
        # print(d)
        m=0
        for v in d.values():
            m=max(m,len(v))
        #print(m)

        b = len(nums)
        for v in d.values():
            # print(len(v))
            if len(v) == m:
                b = min(b,v[-1]-v[0]+1)
            # print(b)
        return b