class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        l=0
        if rungs[0]>dist:
            if dist>1:
                l+=(rungs[0]-1)//dist
            else:
                l+=(rungs[0]-1)
        for i in range(1,len(rungs)):
            if (rungs[i]-rungs[i-1])>dist:
                if dist>1:
                    l+=(rungs[i]-rungs[i-1]-1)//dist
                else:
                    l+=(rungs[i]-rungs[i-1])-1
                    print(l)
        return l



        