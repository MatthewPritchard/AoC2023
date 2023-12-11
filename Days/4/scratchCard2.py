import re


def scratchcards():
    with open("input.txt") as file:
        total = 0
        winnings = []
        for line in file:
            winnings = list(map(lambda x: (x[0] - 1, x[1]), winnings))
            winnings = list(filter(lambda x: x[0] > -1, winnings))
            matches = count_matches(line)
            cards = 1 + sum(i[1] for i in winnings if i[0] >= 0)
            total += cards
            print(winnings, cards)
            winnings.append((matches, cards))
        print(total)


def count_matches(line):
    winners, candidates = re.search(r".*: (.+) \| (.+)", line).groups()
    winners_set = set(re.findall(r"\d+", winners))
    candidates_set = set(re.findall(r"\d+", candidates))
    matches = len(winners_set.intersection(candidates_set))
    return matches


scratchcards()
