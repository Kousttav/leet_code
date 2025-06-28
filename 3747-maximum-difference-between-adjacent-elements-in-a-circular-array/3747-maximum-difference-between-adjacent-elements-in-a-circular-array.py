class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        mx = abs(nums[-1] - nums[0])
        for i in range(len(nums)-1):
            diff = nums[i] - nums[i+1]
            if abs(diff) > mx:
                mx = abs(diff)
        return mx