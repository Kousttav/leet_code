class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        arr2.sort()
        for i in range(len(arr1)):
            low = 0
            high = len(arr2)-1
            while(low <= high):
                mid = (low+high)//2
                if(abs(arr1[i] - arr2[mid]) <= d):
                    count += 1
                    break
                elif(arr1[i] < arr2[mid]):
                    high = mid-1
                else:
                    low = mid+1
        return len(arr1)-count
        