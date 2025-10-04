class Solution(object):
    def findMaxAverage(self, nums, k):
        s = sum(nums[:k])
        mx = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            if s > mx:
                mx= s
        return float(mx/k)