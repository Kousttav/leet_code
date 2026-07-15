1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.prefix = [0]
5        for n in nums:
6            self.prefix.append(n + self.prefix[-1])
7
8    def sumRange(self, left: int, right: int) -> int:
9        return self.prefix[right + 1] - self.prefix[left]
10
11# Your NumArray object will be instantiated and called as such:
12# obj = NumArray(nums)
13# param_1 = obj.sumRange(left,right)