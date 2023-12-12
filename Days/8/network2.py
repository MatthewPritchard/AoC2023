import re
from functools import reduce
from itertools import cycle
from math import gcd


def network():
    with open("input.txt") as file:
        steps = file.readline().strip().replace("L", "0").replace("R", "1")
        file.readline()

        graph: dict[tuple[str]] = dict()
        start_nodes: list[str] = []
        for line in file:
            node, left, right = re.findall(r"(\w+) = \((\w+), (\w+)\)", line)[0]
            if node.endswith("A"):
                start_nodes.append(node)
            graph[node] = (left, right)

    current_nodes = start_nodes
    results = []
    for index, step in enumerate(cycle(steps)):
        temp = []
        for node in current_nodes:
            if node.endswith("Z"):
                results.append(index)
            else:
                temp.append(node)
        current_nodes = temp
        print(current_nodes, step, list(map(lambda n: graph[n], current_nodes)))
        if not current_nodes:
            return reduce(lambda a, b: abs(a * b) // gcd(a, b), results)

        current_nodes = list(map(lambda n: graph[n][int(step)], current_nodes))


print(network())
