from heapq import heappush, heappop
import re


def read_file(day, line_grouping='single', file_type='real'):
    """Reads the file into a list for further processing
    Args:
        day:
            integer value of day.
        line_grouping:
            single for each line to be treated as single object
            multiple for groups of lines separated by an empty line to be treated as a single object
        file_type:
            if 'test' specified, load the test file.
    Returns:
        List of logical groups as individual items.
    """
    test_file = '_test' if file_type == 'test' else ''
    file_path = f'input_files/day_{day}{test_file}.txt'

    # Read file into memory
    with open(file_path) as raw_file:
        file_array = raw_file.read()

    # If single line grouping, read into lines straight away
    if line_grouping == 'multiple':
        file_array = re.sub(r'(?<!\n)\n(?!\n)', ' ', file_array)

    # Clean new line characters from the end
    return [line.strip() for line in file_array.split('\n') if line != '']


def get_neighbours(point, all_points, allow_diagonals=False, ignored_characters=set()):
    """Returns the neighbours of aiven point

    Args:
        point: tuple of (row, column)
        all_points: iterable of points
        allow_diagonals: True to include diagonal neighbours
        ignored_characters: set of characters to ignore if necessary

    Returns:
        list of coordinate neighbour points
    """
    if allow_diagonals:
        deltas = [(d_row, d_column)
                  for d_row in [-1, 0, 1] for d_column in [-1, 0, 1]
                  if not d_row == d_column == 0]
    else:
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    neighbours = [(point[0] + delta[0], point[1] + delta[1]) for delta in deltas]

    return [neighbour
            for neighbour in neighbours
            if neighbour in all_points and all_points[neighbour] not in ignored_characters]


def manhattan(point_from,  point_to):
    return abs(point_from[0] - point_to[0]) + abs(point_from[1] - point_to[1])


def path_find(origin, destination, coordinates_or_weights, weights=False, allow_diagonals=False, ignored_characters=set()):
    """ Finds the shortest path from an origin to a destination

    Args:
        origin:
        destination:
        coordinates_or_weights:
        allow_diagonals:
        weights:
        ignored_characters:

    Returns:
        Cost of the path from origin to destination
    """
    frontier = []
    heappush(frontier, (0, origin))
    came_from = {origin: None}
    cost_so_far = {origin: 0, destination: False}

    while not cost_so_far[destination]:
        current = heappop(frontier)[1]

        for next_point in get_neighbours(current, coordinates_or_weights, allow_diagonals, ignored_characters):
            weight = 1 if not weights else coordinates_or_weights[next_point]
            if next_point not in came_from or cost_so_far[current] + weight < cost_so_far[next_point]:
                came_from[next_point] = current
                cost_so_far[next_point] = cost_so_far[current] + weight
                neighbour_priority = manhattan(next_point, destination)
                frontier.append((neighbour_priority, next_point))

    return cost_so_far[destination]