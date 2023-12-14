import re
from itertools import tee


def sand():
    with open("input.txt") as file:
        total = 0
        for line in file:
            numbers = list(map(int, re.findall(r"-?\d+", line)))
            print(numbers)
            total += extrapolate(numbers)
        return total


def extrapolate(numbers: list[int]):
    rows = [numbers]
    while not all([i == 0 for i in rows[-1]]):
        rows.append(list(map(lambda x: x[1] - x[0], pairwise(rows[-1]))))

    rows.append([0])
    for index, row in enumerate(reversed(rows)):
        if index != 0:
            row.insert(0, row[0] - rows[-index][0])
    return rows[0][0]


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


print(">>>", sand())
