class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = i = 0
        while l < len(s) and i < len(t):
            if s[l] == t[i]:
                i += 1
            l += 1
        return len(t) - i