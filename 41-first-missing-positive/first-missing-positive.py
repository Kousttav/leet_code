class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Ignore numbers <= 0 or > n
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0

        # Step 2: Place each number in its correct index
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        # Step 3: Find the first index where nums[i] != i+1
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1
