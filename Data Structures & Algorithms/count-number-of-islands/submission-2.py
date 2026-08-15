class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.part_of_island = set()
        num_islands = 0
        def find_neighbors(r, c):
            if (r + 1 < len(grid) and grid[r+1][c] == "1"
                and (r+1, c) not in self.part_of_island):
                self.part_of_island.add((r+1, c))
                find_neighbors(r+1, c)
            if (c + 1 < len(grid[r]) and grid[r][c+1] == "1"
                and (r, c+1) not in self.part_of_island):
                self.part_of_island.add((r, c+1))
                find_neighbors(r, c+1)
            if (r != 0 and grid[r-1][c] == "1" 
                and (r-1, c) not in self.part_of_island):
                self.part_of_island.add((r-1, c))
                find_neighbors(r - 1, c)
            if (c != 0 and grid[r][c-1] == "1" 
                and (r, c-1) not in self.part_of_island):
                self.part_of_island.add((r, c-1))
                find_neighbors(r, c - 1)
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r, c) not in self.part_of_island:
                    num_islands += 1
                    self.part_of_island.add((r, c))
                    find_neighbors(r, c)
        return num_islands
                    