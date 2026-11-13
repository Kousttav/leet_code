class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        c=0
        while (max(nums)>0):
            min_value = min(x for x in nums if x > 0)
            for i in range(len(nums)):
                if nums[i]==0:
                    continue
                else:
                    if (nums[i]-min_value)<0:
                        nums[i]=0
                    else:
                        nums[i]=nums[i]-min_value
            c+=1
        return c

        