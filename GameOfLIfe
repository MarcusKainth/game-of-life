map_size = 64


class cell:
    def __init__(self, location, alive=False):
        self.alive = alive
        self.location = location


class Rules:
    def rule(self, cell_):  # if alive
        for i in xrange(map_size):
            for j in xrange(map_size):
                c = self.neighbourscounter(self, map[i][j])

                if map[i][j].alive:
                    if c != 2 or c != 3:
                        map[i][j].alive = False
                    else:
                        map[i][j].alive = True

                else:
                    if c == 3:
                        map[i][j].alive = True

    def neighbourscounter(self, cell_):  # Return the number of Neighbours alive#
        c = 0
        cell_loc = cell.location
        try:
            if map[abs(cell_loc[0] - 1)][abs(cell_loc[1] - 1)].alive:
                c += 1
        except Exception:
            pass

        try:
            if map[abs(cell_loc[0] - 1)][abs(cell_loc[1])].alive:
                c += 1
        except Exception:
            pass
        try:
            if map[abs(cell_loc[0])][abs(cell_loc[1] - 1)].alive:
                c += 1
        except Exception:
            pass
        try:
            if map[abs(cell_loc[0] + 1)][abs(cell_loc[1] - 1)].alive:
                c += 1
        except Exception:
            pass
        try:
            if map[abs(cell_loc[0] + 1)][abs(cell_loc[1])].alive:
                c += 1
        except Exception:
            pass
        try:
            if map[abs(cell_loc[0] - 1)][abs(cell_loc[1] + 1)].alive:
                c += 1
        except Exception:
            pass
        try:
            if map[abs(cell_loc[0])][abs(cell_loc[1] + 1)].alive:
                c += 1
        except Exception:
            pass
        try:
            if map[abs(cell_loc[0] + 1)][abs(cell_loc[1] + 1)].alive:
                c += 1
        except Exception:
            pass

        return c


Map = []
for i in xrange(map_size):
    map.append([])
    for g in xrange(map_size):
        map[i].insert(g, cell((i, g)))
