from collections import Counter


def card_values(card):
    return "23456789TJQKA".find(card)


def lexicographic_to_numeric(hand):
    total = 0
    for index, card in enumerate(reversed(hand)):
        total += (13 ** index) * card_values(card)
    return total


def hand_rank(hand):
    counts = tuple(sorted(Counter(hand).values(), reverse=True))
    hands = [(1, 1, 1, 1, 1),  # High Card
             (2, 1, 1, 1),  # .. Pair
             (2, 2, 1),  # ..... Two pair
             (3, 1, 1),  # ..... Three of a kind
             (3, 2),  # ........ Full House
             (4, 1),  # ........ Four of a Kind
             (5,)]  # .......... Five of a kind

    rank = ((10 ** 10) * (hands.index(counts) + 1)) + lexicographic_to_numeric(hand)
    return rank


def cards():
    with open("input.txt") as file:
        game = [(hand, bid) for hand, bid in [line.strip().split(" ") for line in file]]
        game.sort(key=lambda h: hand_rank(h[0]))

        total = sum((index + 1) * int(bid) for index, (hand, bid) in enumerate(game))
        print(total)


cards()
