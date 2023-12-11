import re


def convert_seeds():
    with open("input.txt") as file:
        conversions = []
        for line in file:
            if line.startswith("seeds: "):
                seeds = list(map(int, re.findall(r"\d+", line)))
            elif line.strip().endswith(":"):
                conversions.append([])
            elif not (line.strip() == ""):
                destination, source, length = list(map(int, re.findall(r"\d+", line)))
                conversions[-1].append((range(source, source + length), source - destination))
            else:
                pass

        print(min(map(lambda seed: translation(seed, conversions), seeds)))


def translation(seed, conversions):
    value = seed
    for conversion in conversions:
        for source_range, offset in conversion:
            if value in source_range:
                value -= offset
                break
    return value


convert_seeds()
