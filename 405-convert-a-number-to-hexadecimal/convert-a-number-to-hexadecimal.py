class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        s = ""
        d = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        while num >= 1:
            r = num % 16
            if r > 9:
                s = d[r] + s
            else:
                s = str(r) + s
            num //= 16
        return s
