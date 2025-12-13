class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        total_business = ["electronics", "grocery", "pharmacy", "restaurant"]
        storage = {b: [] for b in total_business}

        for i in range(len(code)):
            if (
                businessLine[i] in total_business
                and isActive[i]== True
                and code[i] != ""
                and code[i].replace("_","a").isalnum()
            ):
                storage[businessLine[i]].append(code[i])

        output = []
        for business in total_business:
            storage[business].sort()
            output.extend(storage[business])

        return output
