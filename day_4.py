from utils import read_file


def day_4():
    input_data = [x for x in read_file(4)]

    class BingoBoard:
        def __init__(self, _id, _values):
            self.id = _id
            self.rows = [[int(x) for x in _values[i].split(' ') if x != ''] for i in range(5)]
            self.columns = [[] for i in range(5)]
            for column in range(5):
                for row in range(5):
                    self.columns[column] += [self.rows[row][column]]
            self.picked_rows = [[] for i in self.rows]
            self.picked_columns = [[] for i in self.columns]
            self.won = False

        def check_win(self):
            for index in range(5):
                if len(self.picked_rows[index]) == 5 or len(self.picked_columns[index]) == 5:
                    self.won = True
            return self.id, self.won

        def call_number(self, _number):
            for index in range(5):
                if _number in self.rows[index]:
                    self.picked_rows[index] += [_number]
                if _number in self.columns[index]:
                    self.picked_columns[index] += [_number]

            return self.check_win()

        def final_score(self, _winning_number):
            all_numbers = {value for row in self.rows for value in row}
            all_picked = {value for row in self.picked_rows for value in row}
            unpicked_numbers = all_numbers - all_picked

            return _winning_number * sum(unpicked_numbers)

    def play_bingo(data):
        numbers = [int(x) for x in data[0].split(',')]
        initial_values = data[1:]

        all_boards = {}
        for i in range(int(len(initial_values) / 5)):
            all_boards[i] = BingoBoard(i, initial_values[5 * i: 5 * i + 5])

        part_1 = None
        winning_boards = set()
        for number in numbers:
            for board in all_boards:
                win_check = all_boards[board].call_number(number)
                if win_check[1] and len(winning_boards) == 0:
                    part_1 = all_boards[win_check[0]].final_score(number)
                if win_check[1] and board not in winning_boards:
                    winning_boards.add(board)
                if len(winning_boards) == len(all_boards):
                    return part_1, all_boards[win_check[0]].final_score(number)

        return 'Error!', 'We have reached the end without a winner!'

    results = play_bingo(input_data)
    return results[0], results[1]
