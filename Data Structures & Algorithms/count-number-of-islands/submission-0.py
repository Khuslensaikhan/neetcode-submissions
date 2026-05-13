class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    # Iterate through every cell in the grid.
    # When a cell with value '1' is found:
    # Increment the island count.
    # Run DFS from that cell.
    # In DFS:
    # If the cell is out of bounds or is '0', return.
    # Mark the current cell as '0' (visited).
    # Recursively explore all 4 directions (up, down, left, right).
    # Continue until all cells are processed.
    # Return the total island count.

        directions  = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] =="0"):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands