numbers = {2, 3, 4, 1, 2 }
target = 5

pairs = set()
for x in numbers:
    y = target - x
    if y in numbers:
        pair = tuple(sorted((x, y)))
        pairs.add(pair)
for p in pairs:
    print(p)