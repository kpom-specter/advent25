total = 0

with open("data.txt") as f:
    for line in f.read().splitlines():
        jolts = [int(j) for j in line]
        tens_pos = jolts.index(max(jolts[:-1]))
        ones_pos = jolts.index(max(jolts[tens_pos+1:]))
        total += int("{}{}".format(jolts[tens_pos], jolts[ones_pos]))

print(total)
