import re
from collections import defaultdict
from functools import reduce


def has_surrounding_symbol(match, fulltext, lineindex, symbol_map):
    start, end = match.span()
    line = fulltext[lineindex]
    for lineNo in range(max(0, lineindex - 1), min(len(fulltext), lineindex + 2)):
        line = fulltext[lineNo]
        for charNo in range(max(0, start - 1), min(end + 1, len(line))):
            char = line[charNo]
            if char not in ".1234567890":
                symbol_map[(lineNo, charNo)].append(match)


def gears():
    with open("input.txt") as file:
        total: int = 0
        full_text: list[str] = file.read().split("\n")
        gear_map = defaultdict(list)
        for lineIndex, line in enumerate(full_text):
            numbers = re.finditer(r"\d+", line)
            for match in numbers:
                has_surrounding_symbol(match, full_text, lineIndex, gear_map)
        for symbol, gear_list in gear_map.items():
            if len(gear_list) == 2:
                total += reduce(lambda x, y: int(x.group()) * int(y.group()), gear_list)
        print(total)


gears()
