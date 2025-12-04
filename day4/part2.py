map = []
surrounding_area = [-1, 0, 1]

with open("data.txt") as f:
    for line in f.read().splitlines():
        map.append([c for c in line])

height = len(map)
width = len(map[0])

def get_eight_neighbors(x, y, current_map):
    ns = []
    for nx in surrounding_area:
        for ny in surrounding_area:
            if nx == 0 and ny == 0:
                continue

            if 0 > (neighbor_x := nx + x) or neighbor_x > width - 1:
                continue

            if 0 > (neighbor_y := ny + y) or neighbor_y > height - 1:
                continue

            ns.append(current_map[neighbor_y][neighbor_x])

    return ns


def forklift(current_map):

    total = 0
    new_map = []

    for y, row in enumerate(current_map):
        new_map.append([])
        for x, c in enumerate(row):
            if c != "@":
                new_map[y].append(c)
                continue

            neighbors = get_eight_neighbors(x, y, current_map)

            if len([p for p in neighbors if p == '@']) < 4:
                total += 1
                new_map[y].append('x')
            else:
                new_map[y].append('@')

    if total > 0:
        total += forklift(new_map)

    return total

print(forklift(map))
