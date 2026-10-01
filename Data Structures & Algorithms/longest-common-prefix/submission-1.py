class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            if s.startswith(res):
                continue
            else:
                new_res = ""
                for j in range(min(len(res), len(s))):
                    if res[j] == s[j]:
                        new_res += res[j]
                    else:
                        break
                res = new_res
        return res