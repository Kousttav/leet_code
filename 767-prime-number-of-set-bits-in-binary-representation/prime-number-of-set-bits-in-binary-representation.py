class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def binary(x):
            if x==0:
                bi="0"
            else:
                bi=""
                while x>0:
                    r=x%2
                    bi=str(r)+bi
                    x//=2
            return bi
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**(1/2)) + 1, 2):
                if n % i == 0:
                    return False
            return True
        c=0
        for i in range(left,right+1):
            if is_prime(binary(i).count('1')):
                c+=1
        return c
        