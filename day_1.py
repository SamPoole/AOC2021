from utils import read_file


def day_1():
    input_data = [int(x) for x in read_file(1)]

    part_1, part_2 = 0, 0

    for i in range(1, len(input_data)):
        if input_data[i] > input_data[i - 1]:
            part_1 += 1

        if i > 3:
            if sum(input_data[i-2:i+1]) > sum(input_data[i-3:i]):
                part_2 += 1

    return part_1, part_2
