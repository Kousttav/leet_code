1class Solution:
2    def gcdOfOddEvenSums(self, n: int) -> int:
3        so=se=0
4        oc=ec=0
5        num=0
6        while oc<n or ec<n:
7            if num%2==0:
8                ec+=1
9                se+=num
10            else:
11                oc+=1
12                so+=num
13            num+=1
14        return math.gcd(so,se)
15        