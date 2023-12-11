import re

with open("input.txt") as file:
    total = 0
    for line in file:
        _, _, line2 = line.strip().partition(":")
        winners, _, candidates = line2.strip().partition("|")
        winner_set = set(re.findall(r"\d+", winners))
        candidate_set = set(re.findall(r"\d+", candidates))
        if len(winner_set.intersection(candidate_set)) > 0:
            total += 2 ** (len(winner_set.intersection(candidate_set)) - 1)
    print(total)
