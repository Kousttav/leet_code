class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        l=[]
        for i in range(n+1):
            l.append(i)
        list1=l
        list2=nums
        set1 = set(list1)
        set2 = set(list2)
        
        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)

        if len(diff1) == 1:
            return diff1[0]
        elif len(diff2) == 1:
            return diff2[0]

                