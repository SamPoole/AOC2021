import re
from utils import read_file

input_data = [x for x in read_file(5, 'single')]


def line_from_endpoints(endpoints_string):
    endpoints = [int(x) for x in re.findall(r'\d+', endpoints_string)]

    if endpoints[2] > endpoints[0]:
        x_direction = 1
    elif endpoints[2] == endpoints[0]:
        x_direction = 0
    else:
        x_direction = -1

    if endpoints[3] > endpoints[1]:
        y_direction = 1
    elif endpoints[3] == endpoints[1]:
        y_direction = 0
    else:
        y_direction = -1

    # Horizontal
    if y_direction == 0:
        orthogonal = True
        points = [(x, endpoints[1]) for x in range(endpoints[0], endpoints[2] + x_direction, x_direction)]
    # Vertical
    elif x_direction == 0:
        orthogonal = True
        points = [(endpoints[0], x) for x in range(endpoints[1], endpoints[3] + y_direction, y_direction)]
    # Diagonal
    else:
        orthogonal = False
        points = [(x, y) for x, y in zip(range(endpoints[0], endpoints[2] + x_direction, x_direction), range(endpoints[1], endpoints[3] + y_direction, y_direction))]

    if x_direction != 0 and y_direction != 0:
        return orthogonal, points
    else:
        return orthogonal, points


def generate_point_visits(data):
    points_visited = set()
    points_visited_more_than_once = set()
    points_visited_with_diagonals = set()
    points_visited_more_than_once_with_diagonals = set()

    for line in data:
        orthogonal, generated_points = line_from_endpoints(line)
        for point in generated_points:
            # Orthogonal
            if orthogonal and point not in points_visited:
                points_visited.add(point)
            elif orthogonal and point not in points_visited_more_than_once:
                points_visited_more_than_once.add(point)
            # Diagonal
            if point not in points_visited_with_diagonals:
                points_visited_with_diagonals.add(point)
            elif point not in points_visited_more_than_once_with_diagonals:
                points_visited_more_than_once_with_diagonals.add(point)

    return len(points_visited_more_than_once), len(points_visited_more_than_once_with_diagonals)


results = generate_point_visits(input_data)

print(f'Day 5: {results[0]}, {results[1]}')


