class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_rows = 10
        self.num_rows = 30
        self.grid = [[0 for j in range(self.num_rows)]for i in range(self.num_rows)]
        
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_rows):
                print(self.grid[row][column], end =" ")
                print()    