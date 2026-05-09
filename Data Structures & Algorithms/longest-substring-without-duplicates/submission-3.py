class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0 
        charSet = set()
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[right]) 
            longest = max(longest, right - l + 1)
            
        return longest        