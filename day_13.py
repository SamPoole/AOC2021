import re
from utils import read_file

input_data = read_file(13)


def origami(data, print_after_each_fold=False):
    dots = {}
    folds = []
    col_max, row_max = 0, 0
    for line in data:
        if line.find(',') >= 0:
            x, y = line.split(',')
            col_max = int(x) if int(x) > col_max else col_max
            row_max = int(y) if int(y) > row_max else row_max
            dots[(int(x), int(y))] = '#'

        else:
            fold_match = re.findall(r'fold along ([xy])=(\d+)', line)[0]
            folds.append((fold_match[0], int(fold_match[1])))

    def print_dots():
        print('-' * col_max)
        for row in range(row_max):
            print(('.'.join([dots.get((col, row), ' ') for col in range(col_max)])).replace('.', ''))
        print('-' * col_max)

    for iteration, fold in enumerate(folds):
        new_dots = {}

        if print_after_each_fold:
            print_dots()

        if fold[0] == 'y':
            for dot in dots:
                if dot[1] < fold[1]:
                    new_dots[dot] = dots[dot]
                else:
                    new_dots[(dot[0], fold[1] - (dot[1] - fold[1]))] = dots[dot]
            row_max = fold[1]
        if fold[0] == 'x':
            for dot in dots:
                if dot[0] < fold[1]:
                    new_dots[dot] = dots[dot]
                else:
                    new_dots[(fold[1] - (dot[0] - fold[1]), dot[1])] = dots[dot]
            col_max = fold[1]
        dots = new_dots

        if iteration == 0:
            print(f'Part 1: {len(dots)}')

    print('Part 2:')
    print_dots()


origami(input_data)
