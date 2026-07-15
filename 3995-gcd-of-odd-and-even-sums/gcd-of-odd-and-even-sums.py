class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        so=se=0
        oc=ec=0
        num=0
        while oc<n or ec<n:
            if num%2==0:
                ec+=1
                se+=num
            else:
                oc+=1
                so+=num
            num+=1
        return math.gcd(so,se)
        