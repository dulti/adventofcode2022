commands = []
with open('day10_input.txt', 'r') as f:
    while line := f.readline().strip():
        if line == 'noop':
            commands.append((0, 0))
        else:
            commands.append((1, int(line.split(' ')[1])))

# part 1

strength_vals = tuple(range(20, 221, 40))
strength = 0
X = 1
cycle = 0

for command, additive in commands:
    if command == 0:
        cycle += 1
        if cycle in strength_vals:
            strength += X * cycle
    else:
        for subcycle in range(2):
            cycle += 1
            if cycle in strength_vals:
                strength += X * cycle
        X += additive
        
print(strength)

# part 2

screen = []
X = 1  # middle of sprite
cycle = 0  # also screen pixel being drawn

def draw(cycle, X, screen):
    if cycle % 40 in (X - 1, X, X + 1):
        screen.append('#')
    else:
        screen.append(' ')

for command, additive in commands:
    if command == 0:
        draw(cycle, X, screen)
        cycle += 1
        
    else:
        for _ in range(2):
            draw(cycle, X, screen)
            cycle += 1
            
        X += additive

for idx in range(0, 201, 40):
    print(''.join(screen[idx:idx + 40]))
