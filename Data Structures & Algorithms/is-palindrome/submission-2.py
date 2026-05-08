class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start < end:
            s_start = s[start].lower()
            s_end = s[end].lower()
            while (start < len(s)-1) and (not s_start.isalnum()):
                start+=1
                s_start = s[start].lower()
            while (end >= 0) and (not s_end.isalnum()):
                end -= 1
                s_end = s[end].lower()
            if s_start != s_end:
                return False
            start+=1
            end-=1
        return True