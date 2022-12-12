import math
from copy import deepcopy
from functools import reduce

monkeys = {}

inp = []
with open('day11_input.txt', 'r') as f:
    while line := f.readline():
        if line.strip():
            inp.append(line.strip())

for monkey, starting, operation, test, iftrue, iffalse in zip(*[iter(inp)] * 6):
    monkey_n = int(monkey.split(' ')[1][:-1])
    starting_items = list(map(int, starting.split(': ')[1].split(', ')))
    operation_items = operation.split(': ')[1].split(' ')
    test_num = int(test.split(' ')[-1])
    true_monkey = int(iftrue.split(' ')[-1])
    false_monkey = int(iffalse.split(' ')[-1])

    monkeys[monkey_n] = {'items': starting_items.copy(),
                         'operation': operation_items.copy(),
                         'test': test_num,
                         'true': true_monkey,
                         'false': false_monkey,
                         'activity': 0}

def do_operation(operation):
    assert operation[0] == 'new'
    assert operation[2] == 'old'
    if operation[3] == '+':
        if operation[4] == 'old':
            return lambda x: x * 2
        else:
            return lambda x: x + int(operation[4])
    elif operation[3] == '*':
        if operation[4] == 'old':
            return lambda x: x * x
        else:
            return lambda x: x * int(operation[4])
    else:
        raise ValueError(f'Unknown operator {operation[3]}')

# part 1
monkeys_1 = deepcopy(monkeys)
for _ in range(20):
    for monkey in monkeys_1.keys():
        while len(monkeys_1[monkey]['items']) > 0:
            item = monkeys_1[monkey]['items'].pop(0)
            item = do_operation(monkeys_1[monkey]['operation'])(item)
            item = math.floor(item / 3)
            if item % monkeys_1[monkey]['test'] == 0:
                next_monkey = monkeys_1[monkey]['true']
            else:
                next_monkey = monkeys_1[monkey]['false']
            monkeys_1[next_monkey]['items'].append(item)
            monkeys_1[monkey]['activity'] += 1

activities = [monkeys_1[monkey]['activity'] for monkey in range(len(monkeys_1))]
max_1 = max(activities)
activities.remove(max_1)
max_2 = max(activities)
print(max_1 * max_2)

# part 2
monkeys_2 = deepcopy(monkeys)
gcd = reduce(lambda x, y: x * y, [monkeys_2[monkey]['test'] for monkey in range(len(monkeys_2))])
for cycle in range(10000):
    for monkey in monkeys_2.copy().keys():
        while len(monkeys_2[monkey]['items']) > 0:
            item = monkeys_2[monkey]['items'].pop(0)
            item = do_operation(monkeys_2[monkey]['operation'])(item)
            if item % monkeys_2[monkey]['test'] == 0:
                next_monkey = monkeys_2[monkey]['true']
            else:
                next_monkey = monkeys_2[monkey]['false']
            next_test = monkeys_2[next_monkey]['test']
            item = item % gcd
            monkeys_2[next_monkey]['items'].append(item)
            monkeys_2[monkey]['activity'] += 1

activities = [monkeys_2[monkey]['activity'] for monkey in range(len(monkeys_2))]
max_1 = max(activities)
activities.remove(max_1)
max_2 = max(activities)
print(max_1 * max_2)