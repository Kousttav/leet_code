class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        rigth_sum = {}
        rigth_counter = {}
        left_sum = {}
        left_counter = {}

        for i, n in enumerate(nums):
            rigth_sum[n] = rigth_sum.get(n, 0) + i
            rigth_counter[n] = rigth_counter.get(n, 0) + 1
        res = []
        for i, n in enumerate(nums):
            rigth_sum[n] -= i
            rigth_counter[n] -= 1
            val = rigth_sum[n] - rigth_counter[n] * i
            val += left_counter.get(n, 0) * i - left_sum.get(n, 0)
            res.append(val)
            left_sum[n] = left_sum.get(n, 0) + i
            left_counter[n] = left_counter.get(n, 0) + 1
        return res