import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
gridSize = 50
pause = False;
cells = [True, False]



def onClick(event):
    global pause
    if pause == False:
        pause = True
    else:
        pause = False

class Rules:
    def rule(self, grid, i, j, newgrid, c):  # if alive

                if grid[i][j]:
                    if c < 2 or c > 3:
                        newgrid[i, j] = False
                else:
                    if c == 3:
                        newgrid[i, j] = True

    def neighbourscounter(self, grid, i, j):  # Return the number of Neighbours alive
        # simplified counting number of neighbours alive
        # also stopped from going out or range
        c = sum([grid[i, (j - 1) % gridSize], grid[i, (j + 1) % gridSize],
                 grid[(i - 1) % gridSize, j], grid[(i + 1) % gridSize, j],
                 grid[(i - 1) % gridSize, (j - 1) % gridSize],
                 grid[(i - 1) % gridSize, (j + 1) % gridSize],
                 grid[(i + 1) % gridSize, (j - 1) % gridSize],
                 grid[(i + 1) % gridSize, (j + 1) % gridSize]])

        return c


rule_ = Rules()

x = raw_input('Set an action or Pattern - Enter or rng for random cells distribution')
if x == '' or x == 'rng':
    # populate grid with random on/off - more off than on
    grid = np.random.choice(cells, gridSize * gridSize, p=[0.2, 0.8]).reshape(gridSize, gridSize)
else:
    print('Not implemented yed!')

def update(data):
    if pause == False:
        global grid
        newGrid = grid.copy()
        for i in range(gridSize):
            for j in range(gridSize):
                total = Rules.neighbourscounter(rule_, grid, i, j)
                Rules.rule(rule_, grid, i, j, newGrid, total)
        mat.set_data(newGrid)
        grid = newGrid
        return [mat]


# set up animation
fig, ax = plt.subplots()

# set up listener method to pause animation on mouse click
fig.canvas.mpl_connect('button_press_event', onClick)

mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, frames=60, interval=150, save_count=50)
plt.show()
