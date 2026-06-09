1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        l=[]
4        for i in range(n+1):
5            l.append(bin(i).count("1"))
6        return l