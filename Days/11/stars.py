def stars(expansion: int):
    with open("input.txt") as file:
        text = file.read().split("\n")
        horizontal = []
        vertical = []
        for index, line in enumerate(text):
            h_count = line.count("#")
            if h_count == 0:
                horizontal += [0] * expansion
            else:
                horizontal.append(h_count)

            v_count = sum(1 if c[index] == "#" else 0 for c in text)
            if v_count == 0:
                vertical += [0] * expansion
            else:
                vertical.append(v_count)

        total_distance = 0
        combinations = 0
        for direction in (horizontal, vertical):
            for index, star1 in enumerate(direction):
                if star1 > 0:
                    for index2, star2 in enumerate(direction[index + 1:]):
                        if star2 > 0:
                            combinations += star1 * star2
                            total_distance += (star1 * star2) * (index2 + 1)

        print("combinations", combinations)
        print("total distance", total_distance)


stars(2)
