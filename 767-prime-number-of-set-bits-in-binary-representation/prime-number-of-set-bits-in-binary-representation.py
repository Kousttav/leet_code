class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
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
            if is_prime(bin(i).count('1')):
                c+=1
        return c
        