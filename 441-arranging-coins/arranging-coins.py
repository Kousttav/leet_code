# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         i=0
#         while n>=0:
#             i+=1
#             n=n-i
#         return i-1
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid + 1
            else:
                right = mid - 1
        return right     