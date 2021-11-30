import re


def read_file(day, line_grouping='single', file_type='real'):
    """Reads the file into a list for further processing
    Args:
        day:
            integer value of day.
        line_grouping:
            single for each line to be treated as single object
            multiple for groups of lines separated by an empty line to be treated as a single object
        file_type:
            if 'test' specified, load the test file.
    Returns:
        List of logical groups as individual items.
    """
    test_file = '_test' if file_type == 'test' else ''
    file_path = f'input_files/day_{day}{test_file}.txt'

    # Read file into memory
    with open(file_path) as raw_file:
        file_array = raw_file.read()

    # If single line grouping, read into lines straight away
    if line_grouping == 'multiple':
        file_array = re.sub(r'(?<!\n)\n(?!\n)', ' ', file_array)

    # Clean new line characters from the end
    return [line.strip() for line in file_array.split('\n') if line != '']