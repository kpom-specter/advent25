total = 0

with open("data.txt") as f:
    ranges, items = [b.split() for b in f.read().split("\n\n")]

    for i in map(int, items):
        for r in ranges:
            start, end = map(int, r.split("-"))
            if start <= i <= end:
                total += 1
                print (i, r)
                break

print(total)
