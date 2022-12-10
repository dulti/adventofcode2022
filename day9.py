# input

moves = []
with open('day9_input.txt', 'r') as f:
    while line := f.readline().strip():
        d, n = line.split(' ')
        moves.append((d, int(n)))

def sign(x):
    if x == 0:
        return 0
    else:
        return x // abs(x)

# part 1
head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

tail_visited = set()  # keeps pairs of (x, y) positions of the tail as tuples

def move_tail(tail_x, tail_y, new_head_x, new_head_y):
    dist_x = abs(new_head_x - tail_x)
    sign_x = sign(new_head_x - tail_x)
    dist_y = abs(new_head_y - tail_y)
    sign_y = sign(new_head_y - tail_y)
    if dist_x < 2 and dist_y < 2:
        # the tail didn't move
        pass
    elif dist_x + dist_y == 2:
        # forward direction, tail follows forward
        if dist_x == 2:
            tail_x += sign_x
        else:
            tail_y += sign_y
    else:
        # big diagonal
        tail_x += sign_x
        tail_y += sign_y
    return tail_x, tail_y

for d, n in moves:
    for _ in range(n):
        if d == 'U':
            head_y += 1
        elif d == 'D':
            head_y -= 1
        elif d == 'R':
            head_x += 1
        elif d == 'L':
            head_x -= 1
        else:
            raise ValueError(f'Wrong direction letter: {d}')
        tail_x, tail_y = move_tail(tail_x, tail_y, head_x, head_y)
        tail_visited.add((tail_x, tail_y))
        
print(len(tail_visited))

# part 2
rope = [[0, 0] for _ in range(10)]
tail_visited = set()

def draw_rope(rope):
    max_dim = max([max(knot) for knot in rope])
    grid = [['.'] * (max_dim + 4) for _ in range(max_dim + 4)]
    for pos, knot in reversed(list(enumerate(rope))):
        if pos == 0:
            pos = 'H'
        grid[knot[1] + 2][knot[0] + 2] = str(pos)
    for row in grid:
        print(' '.join(row))

def tighten_rope(rope, tail_visited):
    for idx_first in range(0, len(rope) - 1):
        new_last_x, new_last_y = move_tail(*rope[idx_first + 1], *rope[idx_first])
        rope[idx_first + 1] = [new_last_x, new_last_y]
        tail_visited.add(tuple(rope[-1]))

for d, n in moves:
    for nth_move in range(n):
    
        if d == 'U':
            rope[0][1] += 1
        elif d == 'D':
            rope[0][1] -= 1
        elif d == 'R':
            rope[0][0] += 1
        elif d == 'L':
            rope[0][0] -= 1
        else:
            raise ValueError(f'Wrong direction letter: {d}')
            
        tighten_rope(rope, tail_visited)

print(len(tail_visited))