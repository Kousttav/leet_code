class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        L = []
        for i in range(left, right + 1):
            digits = list(str(i))

            is_self_dividing = True
            for j in range(0, len(digits)):
                if int(digits[j]) == 0 or i % int(digits[j]) != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing:
                L.append(i)

        return L