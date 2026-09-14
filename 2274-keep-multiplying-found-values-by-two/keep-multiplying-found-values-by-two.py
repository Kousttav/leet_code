class Solution:
    def findFinalValue(self, nums: List[int], n: int) -> int:
        while True:
            if n in nums:
                n=n*2
            else:
                return n
        