from utils import read_file


def day_3():
    input_data = [x for x in read_file(3)]

    def sum_bits_at_index(binary_list, index):
        index_count = 0

        for instruction in binary_list:
            index_count += int(instruction[index])

        return index_count

    def part_1(data):
        gamma, epsilon = '', ''
        number_of_instructions = len(data)

        positional_counts = [sum_bits_at_index(data, i) for i in range(len(data[0]))]

        for value in positional_counts:
            if value >= number_of_instructions / 2:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'

        return int(gamma, 2) * int(epsilon, 2)

    def part_2(data):
        def bit_reduce(binary_list, mode, index=0):

            if mode == 'oxygen':
                value_to_keep = '1' if sum_bits_at_index(binary_list, index) >= len(binary_list) / 2 else '0'
            else:
                value_to_keep = '0' if sum_bits_at_index(binary_list, index) >= len(binary_list) / 2 else '1'

            binary_list = [x for x in binary_list if x[index] == value_to_keep]

            if len(binary_list) == 1:
                return int(binary_list[0], 2)

            else:
                return bit_reduce(binary_list, mode, index + 1)

        return bit_reduce(data, 'oxygen') * bit_reduce(data, 'co2')

    return part_1(input_data), part_2(input_data)
