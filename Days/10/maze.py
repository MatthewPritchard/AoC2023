def furthest_point(start: tuple[int, int], full_text: list[str]):
    index = 1
    left, right = connected_neighbours(start, full_text)
    pleft, pright, = start, start
    while left != right:
        print(index, pleft, ">", left, pright, ">", right)
        pleft, left = left, next_point(left, full_text, pleft)
        pright, right = right, next_point(right, full_text, pright)
        index += 1
    return index


def connected_neighbours(point: tuple[int, int], full_text: list[str], previous=None):
    x, y = point
    connected = []
    if (x > 0) and (full_text[x - 1][y] in ("|", "7", "F")) and ((x - 1, y) != previous):
        connected.append((x - 1, y))
    if y > 0 and full_text[x][y - 1] in ("-", "F", "L") and (x, y - 1) != previous:
        connected.append((x, y - 1))
    if x < len(full_text) - 1 and full_text[x + 1][y] in ("|", "J", "L") and (x + 1, y) != previous:
        connected.append((x + 1, y))
    if y < len(full_text[0]) - 1 and full_text[x][y + 1] in ("-", "J", "7") and (x, y + 1) != previous:
        connected.append((x, y + 1))
    return connected


def next_point(point, full_text, previous):
    adjacent = {
        "J": ((-1, 0), (0, -1)),
        "L": ((-1, 0), (0, 1)),
        "|": ((-1, 0), (1, 0)),
        "7": ((1, 0), (0, -1)),
        "F": ((1, 0), (0, 1)),
        "-": ((0, -1), (0, 1))
    }
    x, y = point
    char = full_text[x][y]
    print(char)
    for pos in adjacent[char]:
        x1, y1 = pos
        if previous != (x + x1, y + y1):
            return (x + x1, y + y1)


def maze():
    with open("input.txt") as file:
        full_text = file.read().split("\n")
        start = None
        for index, line in enumerate(full_text):
            if "S" in line:
                start = (index, line.find("S"))

        return furthest_point(start, full_text)


print(maze())
