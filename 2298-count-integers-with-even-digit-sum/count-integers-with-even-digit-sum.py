class Solution:
    def countEven(self, num: int) -> int:
        total = 0
        n = num

        while n > 0:
            total += n % 10
            n //= 10

        if total % 2 == 0:
            return num // 2
        else:
            return (num - 1) // 2