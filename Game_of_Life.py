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
elif x== 'gun':
    grid = np.zeros((gridSize, gridSize), dtype=bool)
    grid[1][5]=True
    grid[1][6]=True
    grid[2][5]=True
    grid[2][6]=True
    grid[11][5]=True
    grid[11][6]=True
    grid[11][7]=True
    grid[12][4]=True
    grid[12][8]=True
    grid[13][3]=True
    grid[13][9]=True
    grid[14][3]=True
    grid[14][9]=True
    grid[15][6]=True
    grid[16][4]=True
    grid[16][8]=True
    grid[17][5]=True
    grid[17][6]=True
    grid[17][7]=True
    grid[18][6]=True
    grid[21][3]=True
    grid[21][4]=True
    grid[21][5]=True
    grid[22][3]=True
    grid[22][4]=True
    grid[22][5]=True
    grid[23][2]=True
    grid[23][6]=True
    grid[25][1]=True
    grid[25][2]=True
    grid[25][6]=True
    grid[25][7]=True
    grid[35][3]=True
    grid[35][4]=True
    grid[36][3]=True
    grid[36][4]=True
    grid[35][22]=True
    grid[35][23]=True
    grid[35][25]=True
    grid[36][22]=True
    grid[36][23]=True
    grid[36][25]=True
    grid[36][26]=True
    grid[36][27]=True
    grid[37][28]=True
    grid[38][22]=True
    grid[38][23]=True
    grid[38][25]=True
    grid[38][26]=True
    grid[38][27]=True
    grid[39][23]=True
    grid[39][25]=True
    grid[40][23]=True
    grid[40][25]=True
    grid[41][24]=True

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

