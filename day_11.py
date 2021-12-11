from utils import read_file

row_max = col_max = 10


def make_grid(input_data):
    grid = {}
    for row in range(row_max):
        for column in range(col_max):
            grid[(row, column)] = int(input_data[row][column])

    return grid


def get_neighbours(coordinate):
    neighbours = []
    deltas = [(d_row, d_column) for d_row in [-1, 0, 1] for d_column in [-1, 0, 1] if not d_row == d_column == 0]
    for d_row, d_column in deltas:
        if 0 <= coordinate[0] + d_row < row_max and 0 <= coordinate[1] + d_column < col_max:
            neighbours.append((coordinate[0] + d_row, coordinate[1] + d_column))

    return neighbours


def flash(coordinate, grid):
    if grid[coordinate] == -1:
        return 0

    grid[coordinate] += 1

    if grid[coordinate] <= 9:
        return 0
    else:
        grid[coordinate] = -1

        return 1 + sum([flash(neighbour, grid) for neighbour in get_neighbours(coordinate)])


def process_grid(grid):
    iteration = 1
    flashes = 0

    while True:
        flashes_this_iteration = 0
        for coordinate in grid:
            flashes_this_iteration += flash(coordinate, grid)

        for coordinate in grid:
            if grid[coordinate] == -1:
                grid[coordinate] = 0

        if iteration <= 100:
            flashes += flashes_this_iteration

        if flashes_this_iteration == row_max * col_max:
            return flashes, iteration

        else:
            iteration += 1


print(process_grid(make_grid(read_file(11))))
