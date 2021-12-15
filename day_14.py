from utils import read_file


input_data = read_file(14)
initial_string = input_data[0]
replacements = dict([line.split(' -> ') for line in input_data[1:]])


def get_initial_state(current_string):
    pair_counts = dict()
    letter_counts = dict()

    for index in range(len(current_string) - 1):
        if current_string[index] + current_string[index + 1] in pair_counts:
            pair_counts[current_string[index] + current_string[index + 1]] += 1
        else:
            pair_counts[current_string[index] + current_string[index + 1]] = 1

    for index in range(len(current_string)):
        if current_string[index] in letter_counts:
            letter_counts[current_string[index]] += 1
        else:
            letter_counts[current_string[index]] = 1

    return pair_counts, letter_counts


def replace_pairs(current_state):
    current_pairs, current_letters = current_state

    new_pairs = {key: 0 for key in replacements}

    for key in current_pairs:
        new_pairs[key[0] + replacements[key]] += current_pairs[key]
        new_pairs[replacements[key] + key[1]] += current_pairs[key]
        if replacements[key] in current_letters:
            current_letters[replacements[key]] += current_pairs[key]
        else:
            current_letters[replacements[key]] = current_pairs[key]

    return new_pairs, current_letters


def iterate(iterations, current_state):
    for _ in range(iterations):
        current_state = replace_pairs(current_state)
    return current_state


part_1 = iterate(10, get_initial_state(initial_string))
part_2 = iterate(40, get_initial_state(initial_string))
print(f'Day 14: {max(part_1[1].values()) - min(part_1[1].values())},',
      f'{max(part_2[1].values()) - min(part_2[1].values())}')

