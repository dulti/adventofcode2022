class Elevations:

    def __init__(self, file_name):
        self.grid = []
        self.start = []
        self.end = []

        with open(file_name, 'r') as f:
            while line := f.readline().strip():
                self.grid.append(list(line))

        self.steps = [[0] * len(self.grid[0]) for _ in range(len(self.grid))]
        self.visited = [[False] * len(self.grid[0]) for _ in range(len(self.grid))]
        self.neighbors = []

    def mark_poi(self):
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if cell == 'S':
                    self.start = [row_idx, col_idx]
                    self.grid[row_idx][col_idx] = 'a'
                elif cell == 'E':
                    self.end = [row_idx, col_idx]
                    self.grid[row_idx][col_idx] = chr(ord('z') + 1)

    def get_grid(self, row, col):
        return self.grid[row][col]

    def get_steps(self, row, col):
        return self.steps[row][col]

    def set_steps(self, row, col, val):
        self.steps[row][col] = val

    def is_visited(self, row, col):
        return self.visited[row][col]

    def visit(self, row, col):
        self.visited[row][col] = True

    def get_neighbors(self, row, col):
        if (row != 0 and [row - 1, col] not in self.neighbors and
                not self.is_visited(row - 1, col) and
                ord(self.get_grid(row, col)) + 1 >= ord(self.get_grid(row - 1, col))):
            # upper
            self.neighbors.append([row - 1, col, self.get_steps(row, col)])

        if (row != len(self.grid) - 1 and [row + 1, col] not in self.neighbors and
                not self.is_visited(row + 1, col) and
                ord(self.get_grid(row, col)) + 1 >= ord(self.get_grid(row + 1, col))):
            # lower
            self.neighbors.append([row + 1, col, self.get_steps(row, col)])

        if (col != 0 and [row, col - 1] not in self.neighbors and
                not self.is_visited(row, col - 1) and
                ord(self.get_grid(row, col)) + 1 >= ord(self.get_grid(row, col - 1))):
            # left
            self.neighbors.append([row, col - 1, self.get_steps(row, col)])

        if (col != len(self.grid[0]) - 1 and [row, col + 1] not in self.neighbors and
                not self.is_visited(row, col + 1) and
                ord(self.get_grid(row, col)) + 1 >= ord(self.get_grid(row, col + 1))):
            # right
            self.neighbors.append([row, col + 1, self.get_steps(row, col)])

    def fill_steps(self):
        self.mark_poi()

        self.visit(*self.start)
        self.get_neighbors(*self.start)  # initial

        while self.neighbors:
            row, col, steps = self.neighbors.pop(0)
            if not self.is_visited(row, col):  # hasn't been filled at an earlier cycle
                self.visit(row, col)
                self.set_steps(row, col, steps + 1)
                self.get_neighbors(row, col)

# part 1
elevations = Elevations('day12_input.txt')
elevations.fill_steps()
print(elevations.get_steps(*(elevations.end)))

# part 2
class ElevationsAll(Elevations):

    def __init__(self, file_name):
        super().__init__(file_name)

    def mark_poi(self):
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if cell in ['S', 'a']:
                    self.start.append([row_idx, col_idx])
                    self.grid[row_idx][col_idx] = 'a'
                elif cell == 'E':
                    self.end = [row_idx, col_idx]
                    self.grid[row_idx][col_idx] = chr(ord('z') + 1)

    def fill_steps(self):

        self.mark_poi()

        for start_point in self.start:
            self.visit(*start_point)
            self.get_neighbors(*start_point)  # initial

        while self.neighbors:
            row, col, steps = self.neighbors.pop(0)
            if not self.is_visited(row, col):  # hasn't been filled at an earlier cycle
                self.visit(row, col)
                self.set_steps(row, col, steps + 1)
                self.get_neighbors(row, col)

elevations_all = ElevationsAll('day12_input.txt')
elevations_all.fill_steps()
print(elevations_all.get_steps(*elevations_all.end))