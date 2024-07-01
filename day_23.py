from utils import path_find


def initial_setup(raw_data):
    _spaces = {}
    _targets = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
    _scores = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

    for row in range(len(raw_data)):
        for column in range(len(raw_data[row])):
            if raw_data[row][column] not in (' ', '#'):
                _spaces[(row, column)] = raw_data[row][column]
    return _spaces, _targets, _scores


def manhattan(point_from, point_to):
    return abs(point_from[0] - point_to[0]) + abs(point_from[1] - point_to[1])


def find_destination(_location, _spaces):
    left_corridor = sorted(_spaces, key=lambda x: x[1])[0]
    right_corridor = sorted(_spaces, key=lambda x: x[1])[-1]
    amphipod_type = _spaces[_location]
    target_room = targets[amphipod_type]
    target_room_locations = [location for location in _spaces if location[0] > 1 and location[1] == target_room]

    # if room doesn't contain other elements, return max empty spot in the room
    if not any([True for location in target_room_locations if _spaces[location] not in ['.', amphipod_type]]):
        return 0, sorted([space for space in target_room_locations if _spaces[space] == '.'], reverse=True)[0]

    # if we're currently in a room, find the nearest empty corridor end
    elif _location[0] > 1:
        if _spaces[left_corridor] == '.':
            dist_to_left = manhattan(_location, left_corridor)
        else:
            dist_to_left = 100
        if _spaces[right_corridor] == '.':
            dist_to_right = manhattan(_location, right_corridor)
        else:
            dist_to_right = 100
        if dist_to_left < dist_to_right:
            return dist_to_left, left_corridor
        elif dist_to_left > dist_to_right:
            return dist_to_right, right_corridor
        else:
            return False

    # Ineligible to move
    else:
        return False


def move(_point, _spaces, debug_move=True, debug_grid=False):
    def debug_spaces():
        for row in range(1, len(input_data) - 1):
            string_to_print = ''
            for column in range(len(input_data[0])):
                string_to_print += _spaces.get((row, column), ' ')
            print(string_to_print)

    origin = _point
    destination = find_destination(_point, _spaces)
    ignored = {'A', 'B', 'C', 'D'}
    path_length = path_find(origin, destination, _spaces, False, False, ignored)
    _spaces[destination] = _spaces[origin]
    _spaces[origin] = '.'
    if debug_move:
        print(f'Moved {_spaces[destination]} from {origin} to {destination} in {path_length} steps')
    if debug_grid:
        debug_spaces()


input_data = ['#############', '#...........#', '###B#C#B#D###', '  #A#D#C#A#', '  #########']
very_easy_data = [
    '#############',
    '#...........#',
    '###.#C#.#A###',
    '  #.#B#.#.#',
    '  #########']
spaces, targets, scores = initial_setup(very_easy_data)



