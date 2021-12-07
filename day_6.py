from copy import deepcopy
from utils import read_file

input_data = [int(x) for x in read_file(6)[0].split(',')]


def expand_population(current_generation, iterations):
    for iteration in range(iterations):
        next_generation = {day: 0 for day in range(9)}

        for fish_lifecycle_day in range(9):
            if fish_lifecycle_day == 0:
                next_generation[6] = current_generation[0]
                next_generation[8] = current_generation[0]

            else:
                next_generation[fish_lifecycle_day-1] += current_generation[fish_lifecycle_day]

        current_generation = deepcopy(next_generation)

    return sum(current_generation.values())


initial_fish = {day: 0 for day in range(9)}
for day in input_data:
    initial_fish[day] += 1

print(f'Day 6: {expand_population(initial_fish, 80)}, {expand_population(initial_fish, 256)}')

