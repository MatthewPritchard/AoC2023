import re


def has_surrounding_symbol(match, fulltext, line_index):
    start, end = match.span()
    for line in fulltext[max(0, line_index - 1): min(len(fulltext), line_index + 2)]:
        for char in line[max(0, start - 1): min(end + 1, len(line))]:
            if char not in ".1234567890":
                return int(match.group())
    return 0


def gears():
    with open("input.txt") as file:
        full_text: list[str] = file.read().split("\n")
        total = 0
        for lineIndex, line in enumerate(full_text):
            numbers = re.finditer(r"\d+", line)
            for match in numbers:
                total += has_surrounding_symbol(match, full_text, lineIndex)
        print(total)


gears()
