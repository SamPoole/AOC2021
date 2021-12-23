from heapq import heappush, heappop
from time import time
from utils import read_file, path_find

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


def find_paths(data, scale_up=1):
    origin = (0, 0)
    destination = (scale_up * len(data) - 1, scale_up * len(data[0]) - 1)
    weights = set_up(data, scale_up)

    return path_find(origin, destination, weights, True, False)


start_time_1 = time()
result_1 = find_paths(input_data, 1)
print(f'Part 1: {result_1} in {time() - start_time_1:0.5f} seconds')
start_time_2 = time()
result_2 = find_paths(input_data, 5)
print(f'Part 2: {result_2} in {time() - start_time_2:0.5f} seconds')
print(f'Total duration: {time() - start_time_1:0.5f} seconds')
