import math
from utils import read_file

input_data = read_file(17)


# target area: x=20..30, y=-10..-5
def get_possible_steps(min_x, max_x):
    def x_value_check(initial_velocity, possible_steps, x_min, x_max, step=1):
        if initial_velocity * step - (step - 1) < x_min:
            return x_value_check(initial_velocity, possible_steps, x_min, x_max, step + 1)
        elif x_min <= initial_velocity * step - (step - 1) <= x_max:
            possible_steps.add(step)
            return x_value_check(initial_velocity, possible_steps, x_min, x_max, step + 1)
        else:
            return possible_steps

    starting_x = math.ceil(math.sqrt(2 * min_x + 0.25) - 0.5)

    all_steps = set()
    for velocity in range(starting_x, max_x + 1):
        all_steps = all_steps | x_value_check(velocity, set(), min_x, max_x)
    return all_steps


potential_steps = get_possible_steps(20, 30)


def get_y_values(possible_steps, y_min, y_max):
    def geometric_sum(n_to, n_from):
        return int(-0.5 * (n_from - n_to - 1) * (n_from + n_to))


for step in list(potential_steps):
    print(step, 2, geometric_sum(2, 2-(step - 1)))


