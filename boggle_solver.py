"""
NAME: Nmachi Igwe
ID: @03112824
DATE: 2025-21-09
"""

class Boggle:
    def __init__(self, grid=None, dictionary=None):
        # Initialize grid and dictionary
        self.grid = grid if grid is not None else []
        self.dictionary = {word.upper() for word in dictionary} if dictionary else set()
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0
        self.solution = []

        # Directions: vertical, horizontal, and diagonal
        self.directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

    # Setter for grid
    def setGrid(self, grid):
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0

    # Setter for dictionary
    def setDictionary(self, dictionary):
        self.dictionary = {word.upper() for word in dictionary}

    # Solve the Boggle board
    def getSolution(self):
        if not self.grid or not self.dictionary:
            return []

        words_found = set()

        def dfs(r, c, path, visited):
            if path in self.dictionary:
                words_found.add(path)

            # Continue DFS only if some dictionary word starts with current path
            if not any(word.startswith(path) for word in self.dictionary):
                return

            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in visited:
                    dfs(nr, nc, path + self.grid[nr][nc], visited | {(nr, nc)})

        for r in range(self.rows):
            for c in range(self.cols):
                dfs(r, c, self.grid[r][c], {(r, c)})

        self.solution = sorted(words_found)
        return self.solution


# Example main function to test interactively
def main():
    grid = [["A","B","C"],
            ["D","E","F"],
            ["G","H","I"]]
    dictionary = ["AB", "ABC", "ABD", "DCA", "EFG", "HI"]
    game = Boggle(grid, dictionary)
    solution = game.getSolution()
    print("Grid:")
    for row in grid:
        print(row)
    print("\nDictionary:", dictionary)
    print("\nSolution:", solution)


if __name__ == "__main__":
    main()
   