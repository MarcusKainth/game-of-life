import sys

tiles_size = 64


class cell:
    def __init__(self, location, alive=False):
        self.alive = alive
        self.location = location


class Rules:
    def rule(self):  # if alive
        for i in range(tiles_size):
            for j in range(tiles_size):
                c = self.neighbourscounter(tile[i][j])

                if tile[i][j].alive:
                    if c != 2 or c != 3:
                        tile[i][j].alive = False
                    else:
                        tile[i][j].alive = True

                else:
                    if c == 3:
                        tile[i][j].alive = True

    def neighbourscounter(self, cell_):  # Return the number of Neighbours alive#
        c = 0
        cell_loc = cell_.location
        try:
            if tile[abs(cell_loc[0] - 1)][abs(cell_loc[1] - 1)].alive:
                c += 1
        except Exception:
            pass

        try:
            if tile[abs(cell_loc[0] - 1)][abs(cell_loc[1])].alive:
                c += 1
        except Exception:
            pass
        try:
            if tile[abs(cell_loc[0])][abs(cell_loc[1] - 1)].alive:
                c += 1
        except Exception:
            pass
        try:
            if tile[abs(cell_loc[0] + 1)][abs(cell_loc[1] - 1)].alive:
                c += 1
        except Exception:
            pass
        try:
            if tile[abs(cell_loc[0] + 1)][abs(cell_loc[1])].alive:
                c += 1
        except Exception:
            pass
        try:
            if tile[abs(cell_loc[0] - 1)][abs(cell_loc[1] + 1)].alive:
                c += 1
        except Exception:
            pass
        try:
            if tile[abs(cell_loc[0])][abs(cell_loc[1] + 1)].alive:
                c += 1
        except Exception:
            pass
        try:
            if tile[abs(cell_loc[0] + 1)][abs(cell_loc[1] + 1)].alive:
                c += 1
        except Exception:
            pass

        return c


tile = []
for i in range(tiles_size):
    tile.append([])
    for g in range(tiles_size):
        tile[i].insert(g, cell((i, g)))

Rules = Rules()

# Hardcode pattern.
tile [1][1].alive = True
tile [1][2].alive = True
tile [2][1].alive = True
tile [3][1].alive = True
tile [3][2].alive = True
tile [2][2].alive = True

# Print too screen implementing rules.
for a in range(0,3):
    for i in range(tiles_size):
        for g in range(tiles_size):
            if tile[i][g].alive == True:
                sys.stdout.write("X")
            else:
                sys.stdout.write("O")
        print()
    print()
    print()
    Rules.rule()
