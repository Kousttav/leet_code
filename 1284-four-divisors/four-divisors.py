class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        MAX = max(nums)
        divCount = [0] * (MAX + 1)
        divSum = [0] * (MAX + 1)

        for i in range(1, MAX + 1):
            for j in range(i, MAX + 1, i):
                divCount[j] += 1
                divSum[j] += i

        ans = 0
        for n in nums:
            if divCount[n] == 4:
                ans += divSum[n]

        return ans
