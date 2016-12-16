from Grid import Grid
from Patterns import Pattern
from Game import Game

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Draw:
    def __init__(self, pattern):
        # Minimum size of 50 for other patterns to work correctly
        self.grid = Grid(50, pattern)
        self.game_of_life = Game(self.grid)
        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=60, interval=150, save_count=50)
        self.mat = self.ax.matshow(self.game_of_life.grid)

    def update(self, data):
        grid = self.game_of_life.grid
        size = len(grid)
        new_grid = grid.copy()

        for x in range(size):
            for y in range(size):
                self.game_of_life.check_rule(x, y, new_grid)

        self.mat.set_data(new_grid)
        self.game_of_life.grid = new_grid
        return [self.mat]

    def run(self):
        plt.show()

if __name__ == "__main__":
    draw = Draw(Pattern.Random)
    draw.run()
