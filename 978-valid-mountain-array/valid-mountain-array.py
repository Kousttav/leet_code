class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l,r=0,len(arr)-1
        while l<r:
            if arr[l]<arr[l+1]:
                l+=1
            elif arr[r]<arr[r-1]:
                r-=1
            else:
                break
        return (l==r) and (l>0 and r<len(arr)-1)
        