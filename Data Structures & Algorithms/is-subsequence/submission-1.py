class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = i = 0
        while l < len(t) and i < len(s):
            if t[l] == s[i]:
                i += 1
            l += 1
        
        return True if i == len(s) else False
        
