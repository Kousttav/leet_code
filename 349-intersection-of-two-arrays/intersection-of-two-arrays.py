class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        if len(nums1)>len(nums2):
            n1=nums1
            n2=nums2
        else:
            n1=nums2
            n2=nums1
        for i in n2:
            if i in n1 and i not in l:
                 l.append(i)
        return l