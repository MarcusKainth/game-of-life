import numpy as np

from Patterns import Pattern


class Grid:
    def __init__(self, size, pattern):
        self._grid = []
        self.size = size
        self.set_pattern(pattern)

    def set_pattern(self, pattern):
        if pattern == Pattern.Random:
            self._grid = \
                np.random.choice([True, False], self.size * self.size, p=[0.2, 0.8]).reshape(self.size, self.size)
            return

        self._grid = np.zeros((self.size, self.size), dtype=bool)

    @property
    def grid(self):
        return self._grid
