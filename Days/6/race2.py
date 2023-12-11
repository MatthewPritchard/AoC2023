import math
import re


def race():
    with open("input.txt") as file:
        times, distances = map(lambda line: re.findall(r"\d+", line.replace(" ", "")), file.readlines())

    races = zip(map(int, times), map(int, distances))

    total = 1
    for time, record in races:
        a, b, c = -1, time, -record
        start = quadratic(a, b, c)
        if int(start) == start:
            options = range(math.ceil(start + 1), time - math.floor(start))
        else:
            options = range(math.ceil(start), time - math.floor(start))

        print(start, options, len(options))
        total *= len(options)
    return total


def quadratic(a, b, c):
    return (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a


print(race())
