FIRST_WIRE = "R8,U5,L5,D3"

rows, cols = (15, 15)

grid = [ ["." for i in range(cols)] for j in range(rows)]

grid[13][1] = "O"

FIRST_WIRE = FIRST_WIRE.split(",")


curr_y = 13
curr_x = 1

for path in FIRST_WIRE:
    if path[0] == "R":
        i = 0
        right = int(path[1])
        while right > 0:
            curr_x += 1
            grid[curr_y][curr_x] = "-"
            right -= 1
        grid[curr_y][curr_x] = "+"
    if path[0] == "U":
        i = 0
        up = int(path[1])
        while up > 0:
            curr_y -= 1
            grid[curr_y][curr_x] = "|"
            up -= 1
        grid[curr_y][curr_x] = "+"
    #TODO...
            

for row in grid:
    print(row)