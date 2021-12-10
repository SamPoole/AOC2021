import math
from utils import read_file


def day_7():
    input_data = [int(x) for x in read_file(7)[0].split(',')]

    def sum_fuel_part_1(data):
        def get_median(input_list):
            list_length = len(input_list)
            index = (list_length - 1) // 2

            sorted_list = sorted(input_list)

            if list_length % 2 == 0:
                return sorted_list[index]
            else:
                return int((sorted_list[index] + sorted_list[index + 1]) / 2)

        median = get_median(data)
        total = 0
        for datum in data:
            total += abs(datum - median)

        return total

    def sum_fuel_part_2(data):
        def geometric_sum_from_1(value):
            # int() not needed, but it's tidier given (n^2 + n)/2 is always even
            return int((value ** 2 + value) / 2)

        list_mean = math.floor(sum(data) / len(data))

        total = sum([geometric_sum_from_1(abs(list_mean - position)) for position in data])

        return total

    return sum_fuel_part_1(input_data), sum_fuel_part_2(input_data)
