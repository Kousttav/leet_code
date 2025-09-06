class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        m=0
        for i in dimensions:
            l=i[0]
            b=i[1]
            dl=sqrt(l**2+b**2)
            if m<dl:
                m=dl
                area=l*b
            elif m==dl:
                if area<=(l*b):
                    area=l*b
        return area
        

        