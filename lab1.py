import math
import matplotlib
import numpy
import random




#Qusetion 4
def move(grid):
    rand_x1=random.randrange(0,latticeSize-1)
    rand_y1=random.randrange(0,latticeSize-1)

    while grid[rand_x1][rand_y1]=='0':
        rand_x1=random.randrange(0,latticeSize-1)
        rand_y1=random.randrange(0,latticeSize-1)

    rand_x2=random.randrange(0,latticeSize-1)
    rand_y2=random.randrange(0,latticeSize-2)

    while rand_x1==rand_x2 and rand_y1==rand_y2:
        rand_x2=random.randrange(0,lattice-1)
        rand_y2=random.randrange(0,lattice-1)

    #switch
    temp=grid[rand_x1][rand_y1]
    grid[rand_x1][rand_y1]=grid[rand_x2][rand_y2]
    grid[rand_x2][rand_y2]=temp

    return grid

#Qusetion 5
def metropolisMove(inputGrid, intialEnergy):
    grid = move(inputGrid)
    stepEnergy = calcEnergy(grid)
    print(f"Energy{intialEnergy}")
    print(f"Energy{stepEnergy}")
    diffEnergy = stepEnergy-intialEnergy
    if diffEnergy<0:
        return(True,grid,stepEnergy)
    else:
        R = random.uniform(0,1)
        if math.exp(-diffEnergy/T*1.380649e-23)>R:
            return(True, grid, stepEnergy)
        else:
            return(False, inputGrid, intialEnergy)

acceptance="Rejected"
acceptdMoves =0
rejectedMoves =0

for i in range(0, steps):
    (success, graph, Total_Energy=metropolisMove(graph, Total_Energy)
    if success:

#Question3

     