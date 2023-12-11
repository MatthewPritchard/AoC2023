from collections import Counter


def card_values(card):
    return "J23456789TQKA".find(card)


def lexicographic_to_numeric(hand):
    total = 0
    for index, card in enumerate(reversed(hand)):
        total += (13 ** index) * card_values(card)
    return total


def hand_rank(hand):
    counts = Counter(hand)
    # If there are J's in the hand, treat all of them as the most common card you already have
    if "J" in counts:
        js = counts["J"]
        if js != 5:
            counts.__delitem__("J")
            counts[counts.most_common(1)[0][0]] += js
    sorted_counts = tuple(sorted(counts.values(), reverse=True))
    hands = [(1, 1, 1, 1, 1),  # High Card
             (2, 1, 1, 1),  # .. Pair
             (2, 2, 1),  # ..... Two pair
             (3, 1, 1),  # ..... Three of a kind
             (3, 2),  # ........ Full House
             (4, 1),  # ........ Four of a Kind
             (5,)]  # .......... Five of a kind

    rank = ((10 ** 10) * (hands.index(sorted_counts) + 1)) + lexicographic_to_numeric(hand)
    return rank


def cards():
    with open("input.txt") as file:
        game = []
        for hand, bid in [line.strip().split(" ") for line in file]:
            game.append((hand, bid))
        game.sort(key=lambda h: hand_rank(h[0]))

        total = 0
        for index, (hand, bid) in enumerate(game):
            total += (index + 1) * int(bid)
        print(total)


cards()
