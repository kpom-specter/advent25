zero_count = 0
zero_spins = 0

current_dial = 50

def left(n):
    return 99 if n == 0 else n -1

def right(n):
    return 0 if n == 99 else n + 1

print("The dial starts by pointing at 50.")
with open("data.txt") as f:
    for line in f.read().splitlines():
        num = int(line[1:])
        direction = line[0]

        local_spins = 0
        spin = left if direction == "L" else right
        for x in range(0, abs(num)):
            current_dial = spin(current_dial)
            if current_dial == 0:
                local_spins += 1

        zero_spins += local_spins
        zero_count += (current_dial == 0)
        print("The dial is rotated {} to point at {} (+{} spins)".format(line, current_dial, local_spins, zero_spins))


print("Zero hits", zero_count)
print("Zero spin", zero_spins)
