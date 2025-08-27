class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)
        max=0
        max_ele=0
        for i in s:
            if nums.count(i)>max:
                max=nums.count(i)
                max_ele=i
        return max_ele

        