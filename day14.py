import numpy as np

with open('day14_input.txt', 'r') as f:
    paths = [line.strip() for line in f]

max_x = float('-inf')
min_x = float('inf')
max_y = float('-inf')

paths_coords = []
for path in paths:
    points = path.split(' -> ')
    coords = []
    for point in points:
        x, y = list(map(int, point.split(',')))
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        coords.append((x, y))
    paths_coords.append(coords)

cave = np.full((max_y + 1, (max_x - min_x) + 1), '.')

def set_cave_rocks(cave, start, end, min_x):
    if start[0] == end[0]:
        cave[min(start[1], end[1]):(max(start[1], end[1]) + 1), (start[0] - min_x)] = '#'
    elif start[1] == end[1]:
        cave[start[1], min(start[0] - min_x, end[0] - min_x):(max(start[0] - min_x, end[0] - min_x) + 1)] = '#'

for path in paths_coords:
    # first two
    start, end = path[:2]
    set_cave_rocks(cave, start, end, min_x)
    # other
    if len(path) > 2:
        for next_end in path[2:]:
            set_cave_rocks(cave, end, next_end, min_x)
            end = next_end

# comment out next block for part 1
cave = np.insert(cave, cave.shape[0], np.full(cave.shape[1], '.'), 0)
cave = np.insert(cave, cave.shape[0], np.full(cave.shape[1], '#'), 0)
shape = cave.shape
new_col = np.full(shape[0], '.')
new_col[-1] = '#'
for _ in range(shape[0]):
    cave = np.insert(cave, 0, new_col, 1)
    cave = np.insert(cave, cave.shape[1], new_col, 1)
min_x -= shape[0]

def sand_stayed_in(cave, min_x):
    sand_coords = [0, 500 - min_x]
    while cave[sand_coords[0], sand_coords[1]] != 'o':
        if sand_coords[0] + 1 < cave.shape[0] and cave[sand_coords[0] + 1, sand_coords[1]] == '.':
            # keep falling
            sand_coords[0] += 1
        elif sand_coords[0] + 1 < cave.shape[0] and cave[sand_coords[0] + 1, sand_coords[1]] in ['#', 'o']:
            # try left
            if sand_coords[1] - 1 < 0:
                return False, None
            elif sand_coords[0] + 1 < cave.shape[0] and \
                    cave[sand_coords[0] + 1, sand_coords[1] - 1] == '.':
                sand_coords[0] += 1
                sand_coords[1] -= 1
            else:
                # try right
                if sand_coords[1] + 1 == cave.shape[1]:
                    return False, None
                elif sand_coords[0] + 1 < cave.shape[0] and \
                        cave[sand_coords[0] + 1, sand_coords[1] + 1] == '.':
                    sand_coords[0] += 1
                    sand_coords[1] += 1
                else:
                    # block and stay
                    return True, sand_coords
        else:
            return False, None
    return False, None

units = 0
while True:
    res, sand_coords = sand_stayed_in(cave, min_x)
    if res:
        cave[sand_coords[0], sand_coords[1]] = 'o'
        units += 1
    else:
        break
print(units)
