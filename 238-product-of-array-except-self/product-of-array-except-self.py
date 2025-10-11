class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>=2:
            return [0]*len(nums)
        total=1
        for k in range(len(nums)):
            total*=nums[k]
        print(total)
        other=1
        for i in range(len(nums)):
            if nums[i]!=0:
                other*=nums[i]
        print(other)
        l=[] 
        for j in range(len(nums)):
            if nums[j]!=0:
                l.append(int(total/nums[j]))
            else:
                l.append(int(other))
        return l
        