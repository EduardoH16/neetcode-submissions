class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            grid[r][c] = 0
            area = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if(nr < 0 or nc < 0 or nr >= ROWS
                        or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(bfs(r, c), max_area)
        return max_area