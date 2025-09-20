class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=[]
        if nums==[] or target not in nums:
            return [-1,-1]
        for val in nums:
            if val not in d:
                d[val]=nums.count(val)
        if target in d:
            if d[target]==1:
               return [nums.index(target),nums.index(target)]
            else:
                for i in range(len(nums)):
                    if nums[i]==target:
                        l.append(i)
                        break
                for j in range(len(nums)-1,0,-1):
                    if nums[j]==target:
                        l.append(j)
                        break
                return l
                    
