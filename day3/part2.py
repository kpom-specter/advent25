total = 0

places = 12

with open("data.txt") as f:
    for line in f.read().splitlines():
        jolts = [int(j) for j in line]

        pos = [-1]
        for place in range(1, places+1):
            # start is the last position we saved, plus one
            start = pos[-1]+1

            # end is enough so we don't run out of space
            # length of jolts - (total_places - places_weve_done)
            end = len(jolts) - (places-place)

            # valid_choices is the start to end
            valid_choices = jolts[start:end]

            # highest number in out valid choices
            m = max(valid_choices)

            # the jolt index is the valid_choice offset the last choice
            jolt = start + valid_choices.index(m)

            # Add the jolt position to the pos
            pos.append(jolt)

        # The digits as strings (omitting the starting -1 from the pos list)
        digit_strings = [str(jolts[p]) for p in pos[1:]]

        # Add the total (as an int)
        total += int("".join(digit_strings))

print(total)
