import re
from utils import read_file


def day_10():
    input_data = [line for line in read_file(10)]

    reduction_regex = re.compile(r'(\[])|({})|(<>)|(\(\))')
    incorrect_regex = re.compile(r'[)}>\]]')

    def line_reducer(line):
        if reduction_regex.search(line):
            line = re.sub(r'(\[])|({})|(<>)|(\(\))', '', line)
            return line_reducer(line)
        else:
            return line

    def calculate_scores(data):
        character_scores = {'(': 1, ')': 3,
                            '[': 2, ']': 57,
                            '{': 3, '}': 1197,
                            '<': 4, '>': 25137}
        illegal, legal = [], []
        for line in data:
            line = line_reducer(line)

            # Illegal scores
            if len(re.findall(incorrect_regex, line)) > 0:
                illegal.append(character_scores[re.findall(incorrect_regex, line)[0]])

            # Legal scores
            else:
                line_score = 0
                for character in line[::-1]:
                    line_score = 5 * line_score + character_scores[character]
                legal.append(line_score)

        legal.sort()
        return sum(illegal), legal[int(len(legal) / 2)]

    return calculate_scores(input_data)
