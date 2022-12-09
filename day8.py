# input
trees = []
with open('day8_input.txt', 'r') as f:
    while line := f.readline().strip():
        trees.append(list(map(int, list(line))))

DIRECTIONS = ['up', 'down', 'left', 'right']

# part 1
        
def is_visible_from(grid, tree_x, tree_y, direction):
    if direction == 'up':
        for b_tree_y in range(tree_y):
            if grid[b_tree_y][tree_x] >= grid[tree_y][tree_x]:
                return False
        return True
        
    elif direction == 'down':
        for b_tree_y in range(tree_y + 1, len(grid)):
            if grid[b_tree_y][tree_x] >= grid[tree_y][tree_x]:
                return False
        return True
        
    elif direction == 'left':
        for b_tree_x in range(tree_x):
            if grid[tree_y][b_tree_x] >= grid[tree_y][tree_x]:
                return False
        return True
        
    elif direction == 'right':
        for b_tree_x in range(tree_x + 1, len(grid[0])):
            if grid[tree_y][b_tree_x] >= grid[tree_y][tree_x]:
                return False
        return True
        
    else:
        raise ValueError('wrong value for direction')
     
visibles = []

for tree_y, tree_row in enumerate(trees):
    row_visible = []
    for tree_x, tree in enumerate(tree_row):
        tree_visible = any(
            [is_visible_from(trees, tree_x, tree_y, direction) for direction in DIRECTIONS])
        row_visible.append(tree_visible)
    visibles.append(row_visible)
    
print(sum([sum(row) for row in visibles]))

# part 2
def calculate_scenic_score(grid, tree_x, tree_y):
    score = 1

    this_tree = grid[tree_y][tree_x]
        
    # up
    trees_visible = 0
    for s_tree_y in range(tree_y - 1, -1, -1):
        if grid[s_tree_y][tree_x] < this_tree:
            trees_visible += 1
        else:
            trees_visible += 1
            break
    score *= trees_visible
    
    # down
    trees_visible = 0
    for s_tree_y in range(tree_y + 1, len(grid)):
        if grid[s_tree_y][tree_x] < this_tree:
            trees_visible += 1
        else:
            trees_visible += 1
            break
    score *= trees_visible

    # left
    trees_visible = 0
    for s_tree_x in range(tree_x - 1, -1, -1):
        if grid[tree_y][s_tree_x] < this_tree:
            trees_visible += 1
        else:
            trees_visible += 1
            break
    score *= trees_visible
    
    # right
    trees_visible = 0
    for s_tree_x in range(tree_x + 1, len(grid[0])):
        if grid[tree_y][s_tree_x] < this_tree:
            trees_visible += 1
        else:
            trees_visible += 1
            break
    score *= trees_visible
    
    return score
    
scores = []

for tree_y, tree_row in enumerate(trees):
    row_score = []
    for tree_x, tree in enumerate(tree_row):
        row_score.append(calculate_scenic_score(trees, tree_x, tree_y))
    scores.append(row_score)
    
print(max([max(row) for row in scores]))