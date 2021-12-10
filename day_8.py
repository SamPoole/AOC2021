def day_8():
    with open('input_files/day_8.txt') as f:
        def line_splitter(string_line):
            inp, outp = string_line.replace('\n', '').split(' | ')
            inp, outp = inp.split(' '), outp.split(' ')
            return [inp, outp]

        all_lines = f.readlines()
        inputs, outputs = [line_splitter(line)[0] for line in all_lines], [line_splitter(line)[1] for line in all_lines]

    def part_1(output_data):
        counter = 0
        for output_line in output_data:
            for item in output_line:
                if len(item) in [2, 3, 4, 7]:
                    counter += 1

        return counter

    def decode_inputs(input_lines):
        def intersection_with(consider, against):
            return len(set(consider).intersection(set(encoding_dictionary[against])))

        encoding_dictionary = {i: '' for i in range(9)}

        for line in input_lines:
            # First pass to get instantly identifiable
            for item in line:
                if len(item) == 2:
                    encoding_dictionary[1] = item
                elif len(item) == 3:
                    encoding_dictionary[7] = item
                elif len(item) == 4:
                    encoding_dictionary[4] = item
                elif len(item) == 7:
                    encoding_dictionary[8] = item

            # Second pass to work out the rest by set intersection
            for item in line:
                if len(item) == 5:
                    if intersection_with(item, 1) == 2:
                        encoding_dictionary[3] = item
                    elif intersection_with(item, 4) == 3:
                        encoding_dictionary[5] = item
                    else:
                        encoding_dictionary[2] = item
                elif len(item) == 6:
                    if intersection_with(item, 4) == 4:
                        encoding_dictionary[9] = item
                    elif intersection_with(item, 7) == 3:
                        encoding_dictionary[0] = item
                    else:
                        encoding_dictionary[6] = item

            return {''.join(sorted(value)): key for key, value in encoding_dictionary.items()}

    def decode_outputs(input_lines, output_lines):
        decoded_outputs = []
        for inp, outp in zip(input_lines, output_lines):
            decoder = decode_inputs([inp])
            output_str = ''
            for item in outp:
                output_str += str(decoder[''.join(sorted(item))])

            decoded_outputs.append(int(output_str))

        return decoded_outputs

    return part_1(outputs), sum(decode_outputs(inputs, outputs))
