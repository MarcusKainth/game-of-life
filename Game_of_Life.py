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
while True:
    x = raw_input('Set a Pattern - help  ')
    if x == '' or x == 'rng':
        # populate grid with random on/off - more off than on
        grid = np.random.choice(cells, gridSize * gridSize, p=[0.2, 0.8]).reshape(gridSize, gridSize)
        break
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
        break
    elif x == 'help':
        print('gun, rng, still lifes, oscillators, glider, spaceships ')
    elif x== 'still lifes':
        grid = np.zeros((gridSize, gridSize), dtype=bool)
        #Block
        grid[9][9] = True
        grid[10][9] = True
        grid[9][10] = True
        grid[10][10] = True

        #Beehive
        grid[15][10] = True
        grid[15][9] = True
        grid[16][8] = True
        grid[16][11] = True
        grid[17][10] = True
        grid[17][9] = True

        #Loaf
        grid[22][9] = True
        grid[22][10] = True
        grid[23][8] = True
        grid[23][11] = True
        grid[24][9] = True
        grid[24][11] = True
        grid[25][10] = True

        #Boat
        grid[30][9] = True
        grid[31][9] = True
        grid[30][10] = True
        grid[31][11] = True
        grid[32][10] = True

        pau=True
        break
    elif x == 'oscillators':
        grid = np.zeros((gridSize, gridSize), dtype=bool)

        #Blinker
        grid[9][9] = True
        grid[9][11] = True
        grid[9][10] = True

        #Toad
        grid[15][9] = True
        grid[15][10] = True
        grid[15][11] = True
        grid[16][9] = True
        grid[16][10] = True
        grid[16][8] = True

        #Beacon
        grid[21][9] = True
        grid[21][10] = True
        grid[22][9] = True
        grid[22][10] = True
        grid[23][11] = True
        grid[23][12] = True
        grid[24][11] = True
        grid[24][12] = True

        pause=True
        break
    elif x== 'glider':
        grid = np.zeros((gridSize, gridSize), dtype=bool)

        #Glider
        grid[9][9] = True
        grid[9][11] = True
        grid[9][10] = True
        grid[8][11]=True
        grid[7][10]=True

        pause = True
        break

    elif x=='spaceships':
        grid = np.zeros((gridSize, gridSize), dtype=bool)

        # Spaceships
        grid[9][9] = True
        grid[9][12] = True

        grid[10][8] = True
        grid[11][8] = True
        grid[11][12] = True
        grid[12][8] = True

        grid[12][9] = True
        grid[12][10] = True
        grid[12][11] = True

        pause = True
        break

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
