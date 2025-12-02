mirror_total = 0

with open("data.txt") as f:
    ranges = f.read().split(",")
    for rng in ranges:

        start, last = [int(x) for x in rng.split("-") if x]

        for x in [str(r) for r in range(start, last+1)]:
            if len(x) % 2 != 0:
                continue
            half = int(len(x) / 2)

            left, right = x[:half], x[half:]
            if left != right:
                continue

            mirror_total += int("{}{}".format(left, right))

print("Total: {}".format(total))
