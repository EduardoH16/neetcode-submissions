class Solution:
    def maxDifference(self, s: str) -> int:
        frequencies = defaultdict(int)
        highest_odd = 0
        highest_even = float("inf")

        for c in s:
            frequencies[c] += 1
        
        for val in frequencies.values():
            if val % 2 == 0:
                highest_even = min(highest_even, val)
            else:
                highest_odd = max(highest_odd, val)
        
        return highest_odd - highest_even