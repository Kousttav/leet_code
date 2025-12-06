class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        l=sorted(nums, reverse=True)
        for i in range(2,len(l)):
            if (l[i]+l[i-1])>l[i-2]:
                return l[i-2]+l[i-1]+l[i]
        return 0