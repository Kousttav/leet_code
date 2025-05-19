class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p=len(digits)
        sum=0
        for i in digits:
            sum+=i*10**(p-1)
            p=p-1
        sum+=1
        l= [int(x) for x in str(sum)]
        return l