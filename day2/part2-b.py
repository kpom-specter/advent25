import re

pattern = re.compile(r'^(.+)\1+$')  # "some digits" repeated at least twice

total = 0

with open("data.txt") as f:
    text = f.read().strip()

for rng in text.split(","):

    start, last = [int(x) for x in rng.split("-") if x]

    for n in range(start, last + 1):
        s = str(n)
        if pattern.fullmatch(s):     # same as ^...$ with re.match
            print("invalid:", n)
            total += n

print("total:", total)
