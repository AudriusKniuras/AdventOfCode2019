import copy

FIRST_WIRE = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
SECOND_WIRE = "U62,R66,U55,R34,D71,R55,D58,R83"

rows, cols = (400, 400)

empty_grid = [ ["." for i in range(cols)] for j in range(rows)]

init_y = 100
init_x = 100
empty_grid[init_y][init_x] = "O"



def find_distance(start_x, start_y, cross_x, cross_y):
    distance = abs(start_x - cross_x) + abs(start_y - cross_y)
    return distance

def path_new(grid, instructions, curr_x = init_x, curr_y = init_y):
    for path in instructions:
        if path[0] == "R":
            right = int(path[1:])
            while right > 0:
                curr_x += 1
                grid[curr_y][curr_x] = "-"
                right -= 1
        if path[0] == "L":
            left = int(path[1:])
            while left > 0:
                curr_x -= 1
                grid[curr_y][curr_x] = "-"
                left -= 1
        if path[0] == "U":
            up = int(path[1:])
            while up > 0:
                curr_y -= 1
                grid[curr_y][curr_x] = "|"
                up -= 1
        if path[0] == "D":
            down = int(path[1:])
            while down > 0:
                curr_y += 1
                grid[curr_y][curr_x] = "|"
                down -= 1
        grid[curr_y][curr_x] = "+"
    return grid

 
first_grid = path_new(copy.deepcopy(empty_grid), FIRST_WIRE.split(","))
second_grid = path_new(copy.deepcopy(empty_grid), SECOND_WIRE.split(","))

shortest_distance = 10000
for i in range(rows):
    for j in range(cols):
        if (first_grid[i][j] != ".") and (second_grid[i][j] != ".") and (first_grid[i][j] != second_grid[i][j]):
            print(f'x: {j}, y: {i}')
            distance = find_distance(init_x, init_y, j, i)
            if shortest_distance > distance:
                shortest_distance = distance
print(shortest_distance)

# for row in second_grid:
#     print(row)
