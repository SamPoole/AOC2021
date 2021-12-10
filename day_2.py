from utils import read_file


def day_2():
    input_data = [x for x in read_file(2)]

    position = [0, 0, 0]  # position, depth for part 1, depth for part 2
    aim = 0

    for command in input_data:
        instruction, amount = command.split(' ')
        if instruction == 'forward':
            position[2] += int(amount) * aim
            position[0] += int(amount)
        elif instruction == 'down':
            aim += int(amount)
            position[1] += int(amount)
        elif instruction == 'up':
            aim -= int(amount)
            position[1] -= int(amount)

    return position[0] * position[1], position[0] * position[2]
