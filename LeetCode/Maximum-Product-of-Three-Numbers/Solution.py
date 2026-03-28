1class Solution:
2    def maximumProduct(self, nums: List[int]) -> int:
3        nums. sort()
4        r1 = nums[0]*nums[1]*nums[-1]
5        r2=nums[-1]*nums[-2]*nums[-3]
6        return max(r1,r2)