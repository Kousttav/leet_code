class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest_string = min(strs, key=len)
        for i in range(len(shortest_string), 0, -1):
            prefix = shortest_string[:i]
            valid = True
            for s in strs:
                if not s.startswith(prefix):
                    valid = False
                    break
            if valid:
                return prefix

        return ""
