class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if c1 in s_map and s_map[c1] != c2:
                return False
            if c2 in t_map and t_map[c2] != c1:
                return False
            s_map[c1] = c2
            t_map[c2] = c1
        
        return True

