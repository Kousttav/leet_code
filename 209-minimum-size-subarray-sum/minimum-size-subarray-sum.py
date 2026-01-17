class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=curr = 0
        res = float('inf')

        for right in range(0, len(nums)):
            curr += nums[right]
            while curr >= target:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1

        if res != float('inf'):
            return res
        else:
            return 0