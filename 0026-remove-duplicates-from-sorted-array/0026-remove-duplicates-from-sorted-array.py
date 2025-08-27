class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        b=[]
        for n in nums:
            if n not in b:
                b.append(n)
        b.sort()
        for i in range(len(nums)):
            if i<len(b):
                nums[i]=b[i]
        nums=nums[:len(b)]
        return len(nums)