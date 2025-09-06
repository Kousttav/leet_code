class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        m=0
        for i in dimensions:
            l=i[0]
            b=i[1]
            dl=sqrt(l**2+b**2)
            if m<dl:
                area=0
                m=dl
                area=l*b
            elif m==dl:
                if area<=(l*b):
                    area=0
                    area=l*b
        return area
        

        