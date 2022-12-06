from collections import OrderedDict
from copy import deepcopy

# input processing
# first - columns (!) of crates
# then 1 line of digits
# then an empty line
# then a list of instructions

with open('day5_input.txt', 'r') as f:
    # first, till we meet the numbers line
    # start building the stacks-crates data
    # a list will represent the stacks from 1 to next
    # each stack is saved as a list, ordered from bottom (0th element)
    # to top (n - 1th elemeht), easier to stack-unstack.
    
    # read the first line only to determine the # of the stacks
    # the length of the line is n * 3 + (n - 1) + 1 = n * 4 elements
    line = f.readline()
    assert len(line) % 4 == 0
    stack_no = len(line) // 4
    stacks = [list() for _ in range(stack_no)]
    f.seek(0)
    
    # now start filling in the stacks
    while not (line := f.readline()).startswith(' 1'):
        # split the string into 4-char chunks
        # that's why we aren't removing the trailing newline char
        # and remove the whitespace immediately
        crates = [line[idx:idx + 4].strip() for idx in range(0, len(line), 4)]
        assert len(crates) == len(stacks)
        for crate, stack in zip(crates, stacks):
            stack.insert(0, crate)
    
    # finally, remove empty crates on top of each stack
    for stack in stacks:
        while stack[-1] == '':
            stack.pop()
    
    # parse the number line and assert length
    assert(int(line.strip()[-1]) == len(stacks))
    
    # skip the empty line
    f.readline()
    
    # now get the instructions till EOF
    instructions = {'n': [], 'from': [], 'to': []}
    while line := f.readline():
        words = line.split(' ')
        instructions['n'].append(int(words[1]))
        instructions['from'].append(int(words[3]))
        instructions['to'].append(int(words[5]))
        
# part 1
stacks_1 = deepcopy(stacks)
for stacks_n, move_from, move_to in zip(instructions['n'],
                                        instructions['from'],
                                        instructions['to']):
    for move in range(stacks_n):
        stacks_1[move_to - 1].append(stacks_1[move_from - 1].pop())
        
print(''.join([stack[-1][1] for stack in stacks_1]))

# part 2
stacks_2 = deepcopy(stacks)
for stacks_n, move_from, move_to in zip(instructions['n'],
                                        instructions['from'],
                                        instructions['to']):
    moved = stacks_2[move_from - 1][-stacks_n:]
    stacks_2[move_from - 1] = stacks_2[move_from - 1][:-stacks_n]
    stacks_2[move_to - 1].extend(moved)
        
print(''.join([stack[-1][1] for stack in stacks_2]))