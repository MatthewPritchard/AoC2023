with open("input.txt") as file:
    total = 0
    for line in file:
        digits = [int(i) for i in line if i.isnumeric()]
        total += digits[0] * 10
        total += digits[-1]
    print(total)
