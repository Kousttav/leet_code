1class Solution:
2    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
3        L = []
4        for i in range(left, right + 1):
5            digits = list(str(i))
6
7            is_self_dividing = True
8            for j in range(0, len(digits)):
9                if int(digits[j]) == 0 or i % int(digits[j]) != 0:
10                    is_self_dividing = False
11                    break
12
13            if is_self_dividing:
14                L.append(i)
15
16        return L