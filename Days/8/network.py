import re
from itertools import cycle


def network():
    with open("input.txt") as file:
        steps = file.readline().strip().replace("L", "0").replace("R", "1")
        file.readline()
        graph: dict[tuple[str]] = dict()
        for line in file:
            node, left, right = re.findall(r"(\w+) = \((\w+), (\w+)\)", line)[0]
            graph[node] = (left, right)

        current_node = "AAA"
        for index, step in enumerate(cycle(steps)):
            print(current_node, step, graph[current_node])
            if current_node == "ZZZ":
                return index
            current_node = graph[current_node][int(step)]


print(network())
