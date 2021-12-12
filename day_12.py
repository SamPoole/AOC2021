from utils import read_file

input_data = read_file(12)


def day_12():
    def parse_data(data):
        vertices = set()
        connections = {}

        for line in data:
            start, end = line.split('-')
            if start not in vertices:
                vertices.add(start)
            if end not in vertices:
                vertices.add(end)
            if start not in connections:
                connections[start] = {end}
            else:
                connections[start].add(end)

            if start != 'start':
                if end not in connections:
                    connections[end] = {start}
                else:
                    connections[end].add(start)

        return vertices, connections

    def find_paths(current='start', visited=set(), revisit=True):
        if current == 'end':
            return 1

        if current in visited and current.islower() and not revisit:
            return 0

        else:
            can_still_revisit = revisit and not (current in visited and current.islower())
            visited = visited | {current}
            return sum(find_paths(child, visited, can_still_revisit) for child in all_links[current] if child != 'start')

    all_vertices, all_links = parse_data(input_data)

    return find_paths('start', set(), False), find_paths('start', set(), True)