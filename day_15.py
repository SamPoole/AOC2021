from heapq import heappush, heappop
from time import time
from utils import read_file

input_data = read_file(15)


def set_up(data, scale_up=1):
    max_row, max_col = len(data), len(data[0])
    weight_map = {}
    for row in range(max_row):
        for col in range(max_col):
            weight_map[(row, col)] = int(data[row][col])

    if scale_up == 1:
        return weight_map

    else:
        weight_map_2 = {}
        for tile_row in range(scale_up):
            for tile_col in range(scale_up):
                for point in weight_map:
                    new_point = (point[0] + max_row * tile_row, point[1] + max_col * tile_col)
                    new_weight = (weight_map[point] + tile_col + tile_row - 1) % 9 + 1
                    weight_map_2[new_point] = new_weight

        return weight_map_2


def manhattan(point_from, point_to):
    return abs(point_from[0] - point_to[0]) + abs(point_from[1] - point_to[1])


def get_neighbours(point, point_grid):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = [(point[0] + delta[0], point[1] + delta[1]) for delta in deltas]
    return [neighbour for neighbour in neighbours if neighbour in point_grid]


def path_find(data, scale_up=1):
    weights = set_up(data, scale_up)
    destination = (scale_up * len(data) - 1, scale_up * len(data[0]) - 1)
    # return destination
    came_from = {(0, 0): None}
    cost_so_far = {(0, 0): 0, destination: False}
    frontier = []
    heappush(frontier, (0, (0, 0)))

    while not cost_so_far[destination]:
        current = heappop(frontier)[1]

        for next_point in get_neighbours(current, weights):
            if next_point not in came_from or cost_so_far[current] + weights[next_point] < cost_so_far[next_point]:
                came_from[next_point] = current
                cost_so_far[next_point] = cost_so_far[current] + weights[next_point]
                neighbour_priority = manhattan(next_point, destination)
                frontier.append((neighbour_priority, next_point))

    return cost_so_far[destination]


start_time_1 = time()
result_1 = path_find(input_data, 1)
end_time_1 = time() - start_time_1
print(f'Part 1: {result_1} in {end_time_1:0.5f} seconds')
start_time_2 = time()
result_2 = path_find(input_data, 5)
end_time_2 = time() - start_time_2
print(f'Part 2: {result_2} in {end_time_2:0.5f} seconds')

