total = 0
BLOCKS = [1, 2, 3, 4, 5, 6]
with open("data.txt") as f:
    ranges = f.read().split(",")
    for rng in ranges:

        start, last = [int(x) for x in rng.split("-") if x]

        for x in [str(r) for r in range(start, last+1)]:

            valid_blocks = [b for b in BLOCKS if len(x) % b == 0 and len(x) > b]

            for block in valid_blocks:
                if len(set([x[i:i+block] for i in range(0, len(x), block)])) == 1:
                    total += int(x)
                    print("found a repeater", x, block)
                    break

print("Total: {}".format(total))
