class Game:
    def __init__(self, grid):
        self._grid = grid.grid
        self.len = len(self._grid)

    def check_rule(self, x, y, new_grid):
        c = self.neighbour_counter(x, y)

        # If this cell is alive
        if self._grid[x][y]:
            # Less than 2 neighbours or greater than 3
            if c < 2 or c > 3:
                # Kill this cell
                new_grid[x][y] = False
        else:
            if c == 3:
                # Resurrect this cell
                new_grid[x][y] = True

    def neighbour_counter(self, x, y):
        # simplified counting number of neighbours alive
        # also stopped from going out or range
        return sum([self._grid[x, (y - 1) % self.len], self._grid[x, (y + 1) % self.len],
                 self._grid[(x - 1) % self.len, y], self._grid[(x + 1) % self.len, y],
                 self._grid[(x - 1) % self.len, (y - 1) % self.len],
                 self._grid[(x - 1) % self.len, (y + 1) % self.len],
                 self._grid[(x + 1) % self.len, (y - 1) % self.len],
                 self._grid[(x + 1) % self.len, (y + 1) % self.len]])

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, value):
        self._grid = value

    @grid.deleter
    def grid(self):
        del self._grid
