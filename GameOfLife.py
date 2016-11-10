tiles_size = 64

class cell:
    def __init__(self, location, alive=False):
        self.alive = alive
        self.location = location


class Rules:
    def rule(self, cell_):  # if alive
        for i in xrange(tiles_size):
            for j in xrange(tiles_size):
                c = self.neighbourscounter(self, tile[i][j])

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
        cell_loc = cell.location
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
for i in xrange(tiles_size):
    tile.append([])
    for g in xrange(tiles_size):
        tile[i].insert(g, cell((i, g)))
