class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not s and not t: return True
        if s and not t or len(s) > len(t): return False

        l = i = count = 0
        while l < len(t) and i < len(s):
            if t[l] == s[i]:
                count += 1
                i += 1
            l += 1
        
        return True if count == len(s) else False
        
