import re
from utils import read_file


input_data = read_file(22)


def parse_line(_line):
    matches = re.findall(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', _line)[0]
    return matches[0], [int(match) for match in matches[1:]]


steps = [parse_line(line) for line in input_data]
cubes = set()

for step_type, area in steps:
    for x in range(max(area[0], -50), min(area[1], 50) + 1):
        for y in range(max(area[2], -50), min(area[3], 50) + 1):
            for z in range(max(area[4], -50), min(area[5], 50) + 1):
                if step_type == 'on':
                    cubes.add((x, y, z))
                else:
                    cubes.discard((x, y, z))

print(len(cubes))
