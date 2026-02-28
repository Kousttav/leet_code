class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A")>=2 or ("L"*3) in s:
            return False
        return True


            
        