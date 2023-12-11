import re


def convert_seeds():
    with open("input.txt") as file:
        conversions = []
        for line in file:
            if line.startswith("seeds: "):
                seeds = list(map(int, re.findall(r"\d+", line)))
                seeds = list(zip(seeds[0::2], seeds[1::2]))
                seeds = list(map(lambda x: range(x[0], x[0] + x[1]), seeds))
            elif line.strip().endswith(":"):
                conversions.append([])
            elif not (line.strip() == ""):
                destination, source, length = list(map(int, re.findall(r"\d+", line)))
                conversions[-1].append((range(source, source + length), source - destination))
            else:
                pass

    min_destination = float("inf")
    for seed in seeds:
        min_destination = min(min_destination, min(translation(seed, conversions), key=lambda a: a.start).start)
    print(min_destination)


def translation(seed: range, conversions: list[list[tuple[range, int]]]):
    ranges: list[range] = [seed]
    for c_index, conversion in enumerate(conversions):
        converted = []
        unconverted = []
        for key_range, offset in conversion:
            unconverted = []
            while ranges:
                r = ranges.pop()
                if ranges_intersect(r, key_range):
                    intersection, remaining_ranges = range_intersection2(r, key_range)
                    new_range = range(intersection.start - offset, intersection.stop - offset)
                    converted.append(new_range)
                    unconverted += remaining_ranges
                else:
                    unconverted.append(r)
            ranges = unconverted
        ranges = converted + unconverted

    return ranges


def ranges_intersect(a: range, b: range) -> bool:
    return (a.start < b.stop) and (b.start < a.stop)


# splits ranges into up to 3 parts for values below intersection, inside, and above intersection
def range_intersection(a: range, b: range) -> tuple[range, list[range]]:
    left = range(min(a.start, b.start), max(a.start, b.start))
    intersection = range(max(a.start, b.start), min(a.stop, b.stop))
    right = range(min(a.stop, b.stop), max(a.stop, b.stop))
    return intersection, [i for i in [left, right] if len(i) > 0]


# Same as above, but only returns a's values outside the intersection
def range_intersection2(a: range, b: range):
    left, right = range(0), range(0)
    if a.start < b.start:
        left = range(min(a.start, b.start), max(a.start, b.start))
    intersection = range(max(a.start, b.start), min(a.stop, b.stop))
    if a.stop > b.stop:
        right = range(min(a.stop, b.stop), max(a.stop, b.stop))
    return intersection, [i for i in [left, right] if len(i) > 0]


# prints range less annoyingly (with (1_000) thousand separators) here because you can't override __str__ on range
def repr_range(r: range):
    return "range(" + f'{r.start:_}, ' + f'{r.stop:_})'


convert_seeds()
