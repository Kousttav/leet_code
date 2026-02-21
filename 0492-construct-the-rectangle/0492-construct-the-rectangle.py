class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l=0
        b=int(area**(1/2))
        while area % b !=0:
            b-=1
        l=area//b
        return [l,b]

        