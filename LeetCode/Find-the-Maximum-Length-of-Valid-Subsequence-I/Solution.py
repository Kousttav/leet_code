1class Solution(object):
2    def maximumLength(self, nums):
3        odd = even = 0
4        for num in nums:
5            if num % 2 == 0:
6                even += 1
7            else:
8                odd += 1
9        even_dp= odd_dp=0
10        for num in nums:
11            if num % 2 == 0:
12               even_dp=max(even_dp,odd_dp+1)
13            else:
14               odd_dp=max(odd_dp,even_dp+1) 
15        return max(even, odd,even_dp,odd_dp)
16        