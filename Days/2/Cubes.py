from collections import Counter

maxColours = Counter({"red": 12, "green": 13, "blue": 14})
with open("input.txt") as file:
    validGames = 0
    for line in file:
        game, _, entries = line.strip().partition(": ")
        for entry in entries.strip().split("; "):
            for draw in entry.strip().split(", "):
                drawCount = Counter()
                num, _, colour = draw.partition(" ")
                drawCount.update({colour: int(num)})
                drawCount.subtract(maxColours)
                print(drawCount)
                if any((i > 0 for i in drawCount.values())):
                    break
            else:
                continue
            break
        else:
            validGames += int(game.removeprefix("Game "))

print(validGames)
