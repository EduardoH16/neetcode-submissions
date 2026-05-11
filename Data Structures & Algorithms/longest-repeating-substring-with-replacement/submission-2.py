class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        l = maxF = 0
        res = 0

        for r in range(len(s)):
            frequencies[s[r]] = 1 + frequencies.get(s[r], 0)
            maxF = max(maxF, frequencies[s[r]])

            while (r - l + 1) - maxF > k:
                frequencies[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
    
        return res