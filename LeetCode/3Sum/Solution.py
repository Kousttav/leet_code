1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        index = 1
5        x = nums[0]
6        counter = 1
7        while index < len(nums):
8            if nums[index] == x:
9                counter = counter + 1
10                if x == 0:
11                    if counter > 3:
12                        nums.pop(index)
13                    else:
14                        index = index + 1
15                elif counter > 2:
16                    nums.pop(index)
17                else:
18                    index = index + 1
19            else:
20                x = nums[index]
21                counter = 1
22                index = index + 1
23        if(not all(n>0 for n in nums)):
24            counts = Counter(nums)
25            result = [[0,0,0]] if counts[0] >= 3 else []
26            nums =[i for i in sorted(counts) if i!=0]
27            if counts[0]>0:
28                for i in nums:
29                    if i>0:
30                        break
31                    if -i in counts:
32                        result.append([-i , 0 , i])
33            for i in nums:
34                if i & 1:
35                    continue
36                remaining = -i >> 1
37                if counts[remaining] >= 2:
38                    result.append([i, remaining, remaining])
39            for i, n in enumerate(nums):
40                kk = -(nums[0] + n)
41                if kk < n:
42                    break
43                j = bisect_right(nums, -n << 1) if n < 0 else i + 1
44                k = bisect_right(nums, kk)
45                for right in nums[j:k]:
46                    left = -(n + right)
47                    if left in counts:
48                        result.append([left, n, right])
49            del counts , nums
50            return result
51        else:
52            return []