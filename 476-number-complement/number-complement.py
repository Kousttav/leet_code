class Solution:
    def findComplement(self, x: int) -> int:
        if x == 0: 
            bi = '0' 
        else: 
            bi=""
            while x > 0:
                r = x % 2
                bi = str(r) + bi
                x //= 2
        r=""
        for i in range(len(bi)):
            if bi[i]=="1":
                r+="0"
            else:
                r+="1"
        d=0
        power = 0
        for i in range(len(r)-1, -1, -1):
            d += int(r[i]) * (2 ** power)
            power += 1
        
        return d

