class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        n = len(grid)

        for r in range(n):
            for c in range(n):
                if grid[r][c] in seen:
                    res.append(grid[r][c])
                else:
                    seen.add(grid[r][c])

        for i in range(1, n**2 + 1):
            if i not in seen:
                res.append(i)
                break
        return res