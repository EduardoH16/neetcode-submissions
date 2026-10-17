class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(list)
        t_map = defaultdict(list)

        for i in range(len(s)):
            c = s[i]
            s_map[c].append(i)
        
        for i in range(len(t)):
            c = t[i]
            t_map[c].append(i)

        for key, val in s_map.items():
            found = False
            for key1, val1 in t_map.items():
                if val == val1:
                    found = True
                    val = []
                    val1 = []
                    break
            if not found: return False

        return True

