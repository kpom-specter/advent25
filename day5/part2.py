from collections import deque

total = 0
with open("data.txt") as f:
    raw_ranges, _ = [b.split() for b in f.read().split("\n\n")]

    # Turn the ranges into a list of tuples (start, end) of ints
    ranges = [tuple(map(int, r.split("-"))) for r in raw_ranges]

    # Sort this by the starting value
    ranges.sort(key=lambda x: x[0])

    # Create a queue of the ranges so we can safely iterate and skip
    q = deque(ranges)
    while q :
        current = q.popleft()
        print(f"range {current[0]:,} - {current[1]:,}")

        # If the next element (zero, after we popped above) start > current's end
        # and keep poppin until we our next element is not in our current end
        while q and current[1] >= q[0][0]:
            next = q.popleft()
            print(f"\t squishes ({next[0]:_} – {next[1]:_})")

            # The new current range end is whichever is higher, merging the ranges
            current = (current[0], max(next[1], current[1]))


        print(f"\t resulting in ({current[0]:_} – {current[1]:_})")

        # The range 3-3 is one item. Hence the trailing +1
        freshies = (current[1] - current[0]) + 1
        print(f"\t totals to {freshies}")
        total += freshies

print(total)
