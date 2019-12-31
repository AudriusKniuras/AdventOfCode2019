FIRST_WIRE = "R8,U5,L5,D3"

rows, cols = (15, 15)

grid = [ ["." for i in range(cols)] for j in range(rows)]

grid[13][1] = "O"

FIRST_WIRE = FIRST_WIRE.split(",")

for path in FIRST_WIRE:
    curr_y = 13
    curr_x = 1

    

for row in grid:
    print(row)