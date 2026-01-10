class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ts=0
        for i in range(len(nums)):
            if nums[i]<=4:
                continue
            else:
                p=nums[i]
                c=0
                s=0
                for j in range(1,int(math.sqrt(p))+1):
                    if p%j==0:
                        if p//j==j:
                            s+=j
                            c+=1
                        else:
                            s+=j
                            s+=p//j
                            c+=2
                        if c>4:
                            break
                if c==4:
                    ts+=s
        if ts>0:
            return ts
        else:
            return 0