class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=max_l=0
        char_set= set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[l])
                l +=1
            char_set.add(s[right])
            max_l=max(max_l,right-l+1)
        return max_l
        