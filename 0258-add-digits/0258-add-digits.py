class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        while num >= 10:
            l = []

            while num > 0:
                l.append(num % 10)
                num //= 10

            num = sum(l)

        return num