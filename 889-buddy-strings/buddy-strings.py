class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            seen_chars = set ()
            for char in s:
                if char in seen_chars:
                    return True
                seen_chars.add(char)
            return False
        d = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                d.append(i)

        if len(d) == 2:
            i, j = d
            if s[i] == goal[j] and s[j] == goal[i]:
                return True

        return False
        