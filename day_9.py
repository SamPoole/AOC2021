from math import prod
from utils import read_file

input_data = [[int(x) for x in line] for line in read_file(9)]
deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited_points = set()


def find_minima(grid):
    minima = set()
    risk_level = 0
    row_max, column_max = len(grid), len(grid[0])
    for x in range(row_max):
        for y in range(column_max):
            adjacent = [grid[x + dx][y+dy] for dx, dy in deltas if 0 <= x + dx < row_max and 0 <= y + dy < column_max]
            if all(height > grid[x][y] for height in adjacent):
                minima.add((x, y))
                risk_level += 1 + grid[x][y]
    return minima, risk_level


def depth_first_search(row, column, grid, visited):
    row_max, column_max = len(grid), len(grid[0])

    if 0 <= row < row_max and 0 <= column < column_max and (row, column) not in visited and grid[row][column] < 9:
        visited.add((row, column))
        return 1 + sum(depth_first_search(row + d_row, column + d_column, grid, visited) for d_row, d_column in deltas)

    else:
        return 0


low_points, part_1 = find_minima(input_data)
basin_sizes = [depth_first_search(row, column, input_data, visited_points) for row, column in low_points]

print(f'Day 9: {part_1}, {prod(sorted(basin_sizes, reverse=True)[:3])}')
