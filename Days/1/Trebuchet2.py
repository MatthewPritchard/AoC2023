import re

digitMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
digitsExpr = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
with open("input.txt") as file:
    total = 0
    for line in file:
        print(line.strip())
        found: list[str] = re.findall(digitsExpr, line)
        digits = [digitMap[i] if i.isalpha() else int(i) for i in found]
        print(digits[0] * 10, digits[-1])
        total += digits[0] * 10
        total += digits[-1]
    print(total)
