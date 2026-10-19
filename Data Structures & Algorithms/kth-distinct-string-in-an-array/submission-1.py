class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequencies = defaultdict(int)

        for s in arr:
            frequencies[s] += 1
    
        for s in arr:
            if frequencies[s] == 1:
                k -= 1
                if k == 0: return s

        return ""