1class Solution:
2    def gcdSum(self, nums: list[int]) -> int:
3        mx=0
4        l=[]
5        for n in nums:
6            mx=max(mx,n)
7            l.append(math.gcd(mx,n))
8        l.sort()
9        i=0
10        j=len(l)-1
11        s=0
12        while i<j:
13            if i==j:
14                break
15            s+=math.gcd(l[i],l[j])
16            i+=1
17            j-=1
18        return s
19        
20        