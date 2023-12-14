import re


def point_set(start: tuple[int, int], full_text: list[list[str]]):
    (left, right), new_start = connected_neighbours(start, full_text)
    full_text[start[0]][start[1]] = new_start
    loop: set[tuple[int, int]] = {start, left, right}
    pleft, pright, = start, start
    while left != right:
        pleft, left = left, next_point(left, full_text, pleft)
        pright, right = right, next_point(right, full_text, pright)
        loop.add(left)
        loop.add(right)
    return loop


def connected_neighbours(point: tuple[int, int], full_text: list[list[str]], previous=None):
    # This fully just relies on the if statement ordering below to work lol
    joints = {
        ("up", "left"): "J",
        ("up", "down"): "|",
        ("up", "right"): "L",
        ("down", "left"): "7",
        ("down", "right"): "F",
        ("left", "right"): "-"
    }
    x, y = point
    connected = []
    directions = []
    if x > 0 and full_text[x - 1][y] in ("|", "7", "F") and (x - 1, y) != previous:
        directions.append("up")
        connected.append((x - 1, y))
    if x < len(full_text) - 1 and full_text[x + 1][y] in ("|", "J", "L") and (x + 1, y) != previous:
        directions.append("down")
        connected.append((x + 1, y))
    if y > 0 and full_text[x][y - 1] in ("-", "F", "L") and (x, y - 1) != previous:
        directions.append("left")
        connected.append((x, y - 1))
    if y < len(full_text[0]) - 1 and full_text[x][y + 1] in ("-", "J", "7") and (x, y + 1) != previous:
        directions.append("right")
        connected.append((x, y + 1))
    return connected, joints[tuple(directions)]


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
    for pos in adjacent[char]:
        x1, y1 = pos
        if previous != (x + x1, y + y1):
            return x + x1, y + y1


def maze():
    with open("input.txt") as file:
        full_text: list[list[str]] = list(map(list, file.read().split("\n")))
        start = None
        for index, line in enumerate(full_text):
            if "S" in line:
                start = (index, line.index("S"))

    loop = point_set(start, full_text)
    print(len(loop))

    # lazy preprocessing
    binary_map = []
    for i, line in enumerate(full_text):
        new_line = []
        for j, char in enumerate(line):
            new_line.append("." if (i, j) not in loop else char)
        new_line = "".join(new_line).replace("F", "╭").replace("J", "╯").replace("7", "╮").replace("L", "╰")
        binary_map.append(new_line)  # completely unnecessary join for consistency
    # flood fill all "."s touching any edge, count them, and subtract from total number of "."s

    print("original:")
    print("\n".join(map(lambda x: "".join(x), full_text)))
    print("map:")
    print("\n".join(binary_map))

    print("enclosed: E, unenclosed: U")
    # count X's to the left to the left
    enclosed_points = 0
    for i, line in enumerate(binary_map):
        x_count = 0
        for (j, group) in enumerate(re.split(r"(╭-*╯|\||╰-*╮)", line)):
            if ((re.fullmatch(r"╭-*╯", group)) or (re.fullmatch(r"╰-*╮", group)) or (group == "|")):
                x_count += 1
                print(group, end="")
            elif "." in group:
                if x_count % 2 == 1:
                    enclosed_points += group.count(".")
                    print(group.replace(".", "E"), end="")
                else:
                    print(group.replace(".", "U"), end="")
            else:
                print(group, end="")
        print()
        # print(" -> ",  "   ".join(re.split(r"(╭-*╯|\||╰-*╮)", line)))
    return enclosed_points


print(maze())
