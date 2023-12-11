from functools import reduce

with open("input.txt") as file:
    totalPower = 0
    for line in file:
        game, _, entries = line.strip().partition(": ")
        minColours = {"red": 0, "blue": 0, "green": 0}
        for entry in entries.strip().split("; "):
            for draw in entry.strip().split(", "):
                num, _, colour = draw.partition(" ")
                num = int(num)
                minColours[colour] = max(num, minColours[colour])
        totalPower += reduce(lambda x, y: x * y, minColours.values())
    print(totalPower)
