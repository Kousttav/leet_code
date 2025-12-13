from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        total_business = ["electronics", "grocery", "pharmacy", "restaurant"]
        storage = {b: [] for b in total_business}

        for i in range(len(code)):
            if (
                businessLine[i] in total_business
                and isActive[i]
                and code[i] != ""
                and re.fullmatch(r'[\w]+', code[i])
            ):
                storage[businessLine[i]].append(code[i])

        output = []
        for business in total_business:
            storage[business].sort()     # 🔑 sort within business
            output.extend(storage[business])

        return output
