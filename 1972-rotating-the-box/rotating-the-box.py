class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r=len(box)
        c=len(box[0])
        box2 = [["."] * r for _ in range(c)]
        for i in range(r):
            empty=c-1
            j=c-1
            for j in range(j,-1,-1):
                if box[i][j]=="*":
                    empty=j-1
                if box[i][j]=="#":
                    box[i][j]="."
                    box[i][empty]="#"
                    empty-=1
        for i in range(r):
            j=c-1
            for j in range(j,-1,-1):
                box2[j][r-1-i]=box[i][j]
        return box2


        