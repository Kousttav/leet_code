class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = len(str(low))
        h = len(str(high))
        res = []

        for length in range(l, h + 1):
            num = 0
            for i in range(1, length + 1):
                num = num * 10 + i

            add = int("1" * length)   
            while num % 10 != 0 and num % 10 <= 9:
                if low <= num <= high:
                    res.append(num)

                if num % 10 == 9:
                    break

                num += add

        return res