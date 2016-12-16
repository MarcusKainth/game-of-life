import numpy as np

from patterns import Pattern


class Grid:
    def __init__(self, size, pattern):
        self._grid = []
        self.size = size
        self.set_pattern(pattern)

    def set_pattern(self, pattern):
        self._grid = np.zeros((self.size, self.size), dtype=bool)

        if pattern == Pattern.Gun:
            self.gun()
        elif pattern == Pattern.StillLife:
            self.still_life()
        elif pattern == Pattern.Oscillator:
            self.oscillator()
        elif pattern == Pattern.Glider:
            self.glider()
        elif pattern == Pattern.Spaceship:
            self.spaceship()
        else:
            self._grid = \
                np.random.choice([True, False], self.size * self.size, p=[0.2, 0.8]).reshape(self.size, self.size)

    def gun(self):
        self._grid[1][5] = True
        self._grid[1][6] = True
        self._grid[2][5] = True
        self._grid[2][6] = True
        self._grid[11][5] = True
        self._grid[11][6] = True
        self._grid[11][7] = True
        self._grid[12][4] = True
        self._grid[12][8] = True
        self._grid[13][3] = True
        self._grid[13][9] = True
        self._grid[14][3] = True
        self._grid[14][9] = True
        self._grid[15][6] = True
        self._grid[16][4] = True
        self._grid[16][8] = True
        self._grid[17][5] = True
        self._grid[17][6] = True
        self._grid[17][7] = True
        self._grid[18][6] = True
        self._grid[21][3] = True
        self._grid[21][4] = True
        self._grid[21][5] = True
        self._grid[22][3] = True
        self._grid[22][4] = True
        self._grid[22][5] = True
        self._grid[23][2] = True
        self._grid[23][6] = True
        self._grid[25][1] = True
        self._grid[25][2] = True
        self._grid[25][6] = True
        self._grid[25][7] = True
        self._grid[35][3] = True
        self._grid[35][4] = True
        self._grid[36][3] = True
        self._grid[36][4] = True
        self._grid[35][22] = True
        self._grid[35][23] = True
        self._grid[35][25] = True
        self._grid[36][22] = True
        self._grid[36][23] = True
        self._grid[36][25] = True
        self._grid[36][26] = True
        self._grid[36][27] = True
        self._grid[37][28] = True
        self._grid[38][22] = True
        self._grid[38][23] = True
        self._grid[38][25] = True
        self._grid[38][26] = True
        self._grid[38][27] = True
        self._grid[39][23] = True
        self._grid[39][25] = True
        self._grid[40][23] = True
        self._grid[40][25] = True
        self._grid[41][24] = True

    def still_life(self):
        self._grid[9][9] = True
        self._grid[10][9] = True
        self._grid[9][10] = True
        self._grid[10][10] = True

        # Beehive
        self._grid[15][10] = True
        self._grid[15][9] = True
        self._grid[16][8] = True
        self._grid[16][11] = True
        self._grid[17][10] = True
        self._grid[17][9] = True

        # Loaf
        self._grid[22][9] = True
        self._grid[22][10] = True
        self._grid[23][8] = True
        self._grid[23][11] = True
        self._grid[24][9] = True
        self._grid[24][11] = True
        self._grid[25][10] = True

        # Boat
        self._grid[30][9] = True
        self._grid[31][9] = True
        self._grid[30][10] = True
        self._grid[31][11] = True
        self._grid[32][10] = True

    def oscillator(self):
        # Blinker
        self._grid[9][9] = True
        self._grid[9][11] = True
        self._grid[9][10] = True

        # Toad
        self._grid[15][9] = True
        self._grid[15][10] = True
        self._grid[15][11] = True
        self._grid[16][9] = True
        self._grid[16][10] = True
        self._grid[16][8] = True

        # Beacon
        self._grid[21][9] = True
        self._grid[21][10] = True
        self._grid[22][9] = True
        self._grid[22][10] = True
        self._grid[23][11] = True
        self._grid[23][12] = True
        self._grid[24][11] = True
        self._grid[24][12] = True

    def glider(self):
        # Glider
        self._grid[9][9] = True
        self._grid[9][11] = True
        self._grid[9][10] = True
        self._grid[8][11] = True
        self._grid[7][10] = True

    def spaceship(self):
        # Spaceships
        self._grid[9][9] = True
        self._grid[9][12] = True

        self._grid[10][8] = True
        self._grid[11][8] = True
        self._grid[11][12] = True
        self._grid[12][8] = True

        self._grid[12][9] = True
        self._grid[12][10] = True
        self._grid[12][11] = True

    @property
    def grid(self):
        return self._grid
